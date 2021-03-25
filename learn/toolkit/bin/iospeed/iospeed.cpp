
#include "iospeed.h"

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#include "ds.h"
#include "debugprint.h"

/********************** TPYES **********************/


/********************** CLASS IMPLEMENTATION **********************/


/********************** PRIVATE FUNCTION **********************/

/**
 * 计算两个时间的间隔
 */
static double DurationOf(const struct timeval *tvBegin, const struct timeval *tvEnd)
{
	int nSecsDif = tvEnd->tv_sec - tvBegin->tv_sec;
	int nMSecsDif = (tvEnd->tv_usec - tvBegin->tv_usec) / 1000;

	return (nSecsDif * 1000 + nMSecsDif) / (double)1000;
}

static void *thread_write(void *param)
{
    pthread_detach(pthread_self());
    SWriteJob *job = (SWriteJob*)param;

    job->lock();
    gettimeofday (& job->tvJobStart, NULL);
    job->unlock();

    void *pMem = malloc (job->nWriteBufKB * 1000);
    for (int i = 0; i < job->nCount; ++i) {
        char szFilename[64] = {};
        snprintf (szFilename, sizeof(szFilename)-1, "file_%d.dat");
        if (access (szFilename, F_OK) == 0) {
            _info ("file %s exist, continue with next file\n");
            continue ;
        }

        int fd = open (szFilename, O_CREAT | O_RDWR, 0664);
        if (fd < 0) {
            _error ("create file %s failed\n");
            break;
        }

        int ret = write (fd, pMem, job->nWriteBufKB * 1000);
        if (ret != job->nWriteBufKB * 1000) {
            _error ("write ret=%d\n", ret);
            close (fd);
            fd = -1;
            break;
        }
        close (fd);

        job->lock();
        job->nTotalKB += job->nWriteBufKB;
        job->unlock();
        job->update();
    }

    job->lock();
    gettimeofday (& job->tvJobEnd, NULL);
    job->unlock();
    job->update();
}

static void *thread_status(void *param)
{
    pthread_detach (pthread_self());
}

/**
 * 写任务
 */
static void start_write_test(SWriteJob *job)
{
    pthread_t tid_write = {};
    pthread_t tid_status = {};

    if (0 != pthread_create (&tid_write, NULL, thread_write, job))
    {
        _error ("pthread_create failed\n");
    }
    if (0 != pthread_create (&tid_status, NULL, thread_status, job))
    {
        _error ("pthread_create failed\n");
    }

    return ;
}

/********************** PUBLIC INTERFACE **********************/

int write_test(int nKB, int nCount)
{
    SWriteJob job;
    job.nKB = nKB;
    job.nCount = nCount;

    start_write_test(&job);
    while (true) {
        sleep (60);
    }
    return 0;
}