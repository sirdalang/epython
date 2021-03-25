
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

/**
 * 写任务
 */
static start_write_test(int nKB, int nCount)
{

}

/********************** PUBLIC INTERFACE **********************/

int write_test(int nKb, int nCount)
{
    start_write_test(nKB, nCount);
    while (true) {
        sleep (60);
    }
}