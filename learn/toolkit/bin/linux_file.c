
/**
 * 针对 linux 下文件的读写进行试验
 */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/time.h>
#include <time.h>

#include <stdio.h>



#define _debug(x...) do {printf("[debug][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _info(x...) do {printf("[info][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _error(x...) do {printf("[error][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)

#define _debug_timeprint() \
	do { \
		struct timeval tvTmp = {}; \
        struct tm stmTmp = {}; \
        char szDTime[64] = {}; \
        char szResult[64] = {}; \
        \
		gettimeofday (& tvTmp, NULL); \
        gmtime_r (& tvTmp.tv_sec, & stmTmp); \
		strftime (szDTime, sizeof(szDTime), "%F %T", &stmTmp); \
        snprintf (szResult, sizeof(szResult), "%s.%03d", szDTime, (int)(tvTmp.tv_usec / 1000)); \
        \
        printf ("timestamp[%s %d %s] %s\n", __FILE__,__LINE__,__FUNCTION__, szResult); \
	} while (0)


/**
 * 两个文件描述符 指向同一个文件
 * 结论：
 * 
 * 不同文件描述符具有不同的偏移值。
 */
static int test_1()
{
    char strFileName[] = "temp.file";

    unlink (strFileName);

    int fd_a = open (strFileName, O_CREAT | O_WRONLY, 0664);
    int fd_b = open (strFileName, O_CREAT | O_WRONLY, 0664);

    char strA[] = "AAAA";
    char strB[] = "BBBB";

    write (fd_a, strA, sizeof(strA) - 1);
    write (fd_b, strB, sizeof(strB) - 1);

    close (fd_a);
    close (fd_b);

    return 0;
}

/**
 * lseek 
 * 
 * 结论，lseek越过末尾会产生空白区域
 */
static int test_2()
{
    char strFileName[] = "temp.file";
    unlink (strFileName);

    int fd = open (strFileName, O_CREAT | O_WRONLY, 0664);

    int nCurSeek = lseek (fd, 0, SEEK_CUR);
    _debug ("curseek = %d\n", nCurSeek);

    lseek (fd, 10, SEEK_SET);
    
    char strA[] = "AAAA";
    write (fd, strA, sizeof(strA) - 1);

    close (fd);

    return 0;
}

/**
 * lseek 
 * 
 * lseek 产生空白文件的时候，性能如何？
 */
static int test_3()
{
    char strFileName[] = "temp.file";
    unlink (strFileName);

    char buffer[8] = "abcdef";

    int fd = open (strFileName, O_CREAT | O_WRONLY, 0664);

    int nCurSeek = lseek (fd, 0, SEEK_CUR);
    _debug ("curseek = %d\n", nCurSeek);

    write (fd, buffer, sizeof(buffer));

    struct timeval tvStart = {}, tvEnd = {};

    _debug_timeprint();

    nCurSeek = lseek (fd, 14 * 1024 * 1024, SEEK_SET);
    _debug_timeprint();

    write (fd, buffer, sizeof(buffer));
    _debug_timeprint();

    return 0;
}

int main()
{
    // test_1 ();
    // test_2 ();
    test_3 ();
    return 0;
}