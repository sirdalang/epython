
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

/********************** MACROS **********************/

static inline int KB2B(int n) {return n * 1024;}
static inline double B2KB(int n) {return n / 1024.0;}

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
    SWriteJob *job = (SWriteJob*)param;

    job->lock();
    gettimeofday (& job->d.tvJobStart, NULL);
    job->d.eState = SWriteJob::STATE_WRITING;
    job->unlock();

    void *pMem = malloc (KB2B(job->d.nWriteBufKB));
    for (int i = 0; i < job->d.nCount; ++i) 
    {
        char szFilename[64] = {};
        snprintf (szFilename, sizeof(szFilename)-1, "file_%d.dat", i);
        if (access (szFilename, F_OK) == 0) 
        {
            _info ("file %s exist, continue with next file\n", szFilename);
            continue ;
        }

        int fd = open (szFilename, O_CREAT | O_RDWR, 0664);
        if (fd < 0) 
        {
            _error ("create file %s failed\n", szFilename);
            break;
        }

        int nBlocks = (job->d.nKB / job->d.nWriteBufKB);
        nBlocks = (nBlocks <= 0 ? 1 : nBlocks);

        for (int j = 0; j < nBlocks; ++j) 
        {
            struct timeval tvBlockStart = {}, tvBlockEnd = {};

            gettimeofday (& tvBlockStart, NULL);
            int ret = write (fd, pMem, KB2B(job->d.nWriteBufKB));
            // usleep (100000);
            gettimeofday (& tvBlockEnd, NULL);

            if (ret != KB2B(job->d.nWriteBufKB)) 
            {
                _error ("write ret=%d\n", ret);
                close (fd);
                fd = -1;
                break;
            }
            
            job->lock();
            job->d.nTotalKB += job->d.nWriteBufKB;
            job->d.tvJobEnd = tvBlockEnd;
            job->unlock();
        }
        close (fd);
        fd = -1;
    }

    job->lock();
    job->d.eState = SWriteJob::STATE_FINISH;
    job->unlock();
    job->update();

    _debug ("write thread fin\n");

    return NULL;
}

static void *thread_status(void *param)
{
    SWriteJob *job = (SWriteJob*)param;

    int nKBRec = 0;
    struct timeval tvStepBegin = {};
    struct timeval tvStepEnd = {};

    bool bFin = false;
    while (true) 
    {
        SWriteJob tmpJob;
        job->lock();
        tmpJob.mkcopy (*job);
        job->unlock();

        switch (tmpJob.d.eState)
        {
            case SWriteJob::STATE_INITIALIZED:
            {
                break;
            }
            case SWriteJob::STATE_WRITING:
            {
                break;
            }
            case SWriteJob::STATE_FINISH:
            {
                bFin = true;
                break;
            }
            default:
            {
                _error("unexpected value=%d\n", tmpJob.d.eState);
                break;
            }
        }

        if (bFin) 
        {
            printf ("finnish\n");
            break;
        }

        double fCurSpeed = 0.0;
        double fDuration = DurationOf (& tvStepBegin, & tvStepEnd);
        if (fDuration > 0.05) 
        {
            fCurSpeed = (tmpJob.d.nTotalKB - nKBRec) / fDuration;
        }

        double fAvgSpeed = 0.0;
        double fTotalDuration = DurationOf(& tmpJob.d.tvJobStart, & tmpJob.d.tvJobEnd);
        if (fTotalDuration > 0.05) 
        {
            fAvgSpeed = tmpJob.d.nTotalKB / fTotalDuration;
        }
        
        printf ("timer: %.2f s, bytes: %d/%d KB, cur: %.2f KB/s, avg: %.2f KB/s\n",
                DurationOf(& tmpJob.d.tvJobStart, & tmpJob.d.tvJobEnd),
                tmpJob.d.nTotalKB,
                tmpJob.d.nKB * tmpJob.d.nCount,
                fCurSpeed,
                fAvgSpeed);

        nKBRec = tmpJob.d.nTotalKB;
        gettimeofday (& tvStepBegin, NULL);

        job->waitupdate(0.25); // interval

        gettimeofday (& tvStepEnd, NULL);
    }

    _debug ("status thread fin\n");

    return NULL;
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

    pthread_join (tid_write, NULL);
    pthread_join (tid_status, NULL);

    return ;
}

/********************** PUBLIC INTERFACE **********************/

int write_test(int nKB, int nCount)
{
    SWriteJob job;
    job.d.nKB = nKB;
    job.d.nCount = nCount;

    start_write_test(&job);
    return 0;
}