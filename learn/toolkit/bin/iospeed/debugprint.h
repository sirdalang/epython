
#pragma once

#define DEBUG

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

/* 打印精确到毫秒的时间 */
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

#ifdef DEBUG
#define _debug(x...) do {printf("[debug][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _info(x...) do {printf("[info][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _error(x...) do {printf("[error][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#else 
#define _debug(x...) do {;} while (0)
#define _info(x...) do {printf("[info][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _error(x...) do {printf("[error][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#endif 


#ifndef PTHREAD_MUTEX_DEBUG__
#define PTHREAD_MUTEX_DEBUG__

static int DEBUG_PTHREAD_MUTEX_LOCK(pthread_mutex_t *mutex, const char *szMutexName, 
                const char *szFile, int line, const char *szFunction)
{
    _debug_timeprint();
    printf ("[MUTEX][%s %d %s] pre lock on %s\n", szFile, line, szFunction, szMutexName);
    int ret = pthread_mutex_lock (mutex);
    _debug_timeprint();
    printf ("[MUTEX][%s %d %s] aft lock on %s\n",szFile, line, szFunction, szMutexName);
    return ret;
}

static int DEBUG_PTHREAD_MUTEX_UNLOCK(pthread_mutex_t *mutex, const char *szMutexName, 
                const char *szFile, int line, const char *szFunction)
{
    _debug_timeprint();
    printf ("[MUTEX][%s %d %s] pre unlock on %s\n", szFile, line, szFunction, szMutexName);
    int ret = pthread_mutex_unlock (mutex);
    _debug_timeprint();
    printf ("[MUTEX][%s %d %s] aft unlock on %s\n",szFile, line, szFunction, szMutexName);
    return ret;
}

#ifdef pthread_mutex_lock
#undef pthread_mutex_lock
#endif 

#ifdef pthread_mutex_unlock
#undef pthread_mutex_unlock
#endif 

#define pthread_mutex_lock(mutex) DEBUG_PTHREAD_MUTEX_LOCK(mutex, #mutex, __FILE__,__LINE__,__FUNCTION__)
#define pthread_mutex_unlock(mutex) DEBUG_PTHREAD_MUTEX_UNLOCK(mutex, #mutex, __FILE__,__LINE__,__FUNCTION__)

#endif // PTHREAD_MUTEX_DEBUG__
