
/**
 * 打印写速度
 */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

/**
 * 返回秒
 */
float DurationOf(const struct timeval *tvBegin, const struct timeval *tvEnd)
{
	int nSecsDif = tvEnd->tv_sec - tvBegin->tv_sec;
	int nMSecsDif = (tvEnd->tv_usec - tvBegin->tv_usec) / 1000;

	return (nSecsDif * 1000 + nMSecsDif) / (float)1000;
}

int main(int argc, const char **argv)
{
	if (argc < 3)
	{
		printf ("usage: %s [number] [size](KB)\n", argv[0]);
		return -1;
	}

	int num = atoi (argv[1]);
	int nsize = atoi (argv[2]);

	num = abs(num);
	nsize = abs(nsize);

	printf ("creating %d files of size %d KB...\n", num, nsize);

	struct timeval tvStart = {};
	gettimeofday (& tvStart, NULL);

	int nKbTotal = 0;
	int nKbPerRound = 0;

	int i = 0;
	struct timeval tvLastRound = tvStart;
	for (i = 0; i < num; ++i)
	{
		char szFileName[64];
		snprintf (szFileName, sizeof(szFileName), "file_%d", i);

		if (access(szFileName, R_OK) == 0)
		{
			printf ("file [%s] exists, ignored\n", szFileName);
			continue ;
		}

		int fd = open (szFileName, O_WRONLY | O_CREAT, 0664);
		if (fd < 0)
		{
			printf ("open file [%s] failed, break\n", szFileName);
			break;
		}

		char buf[1000] = {};

		int nKbWritten = 0;
		while (nKbWritten < nsize)
		{
			int ret_write = write (fd, buf, sizeof(buf));
			if (ret_write != sizeof(buf))
			{
				printf ("write to file [%s] failed, break\n", szFileName);
				close (fd);
				break;
			}
			++nKbWritten;
		}

		nKbPerRound += nKbWritten;
		nKbTotal += nKbWritten;

		struct timeval tvNow;
		gettimeofday (& tvNow, NULL);
		if (DurationOf(&tvLastRound, &tvNow) > 1.0f)
		{
			printf ("%d KB written, totaltime=%.1f s, %d KB cur written, cur: %.1f KB/s, total: %1.f KB/s\n", 
				nKbTotal, 
				DurationOf(&tvStart, &tvNow),
				nKbPerRound,
				(nKbPerRound) / DurationOf(&tvLastRound, &tvNow), 
				nKbTotal / DurationOf(&tvStart, &tvNow));
			tvLastRound = tvNow;
			nKbPerRound = 0;
		}

		close (fd);
	}

	printf ("circles number = %d\n", i);

	return 0;
}