
#include "ds.h"
#include "debugprint.h"

/********************** MACROS **********************/

/* int（32） 支持纳秒形式达 2s */
static inline int sec2nsec(double f) {return f * 1000 * 1000 * 1000;}

/********************** CLASS IMPLEMENTATION **********************/

SWriteJob::SWriteJob() : 
    d({
        0,
        0,
        {0},
        {0},
        0,
        0,
        4,
        0,
        STATE_INITIALIZED,
    }),
    m_mutex_this (PTHREAD_MUTEX_INITIALIZER),
    m_cond (PTHREAD_COND_INITIALIZER),
    m_mutex_cond (PTHREAD_MUTEX_INITIALIZER)
{
}

SWriteJob::~SWriteJob() 
{
}

void SWriteJob::lock()
{
    pthread_mutex_lock (& m_mutex_this);
}

void SWriteJob::unlock()
{
    pthread_mutex_unlock (& m_mutex_this);
}

void SWriteJob::update()
{
    pthread_cond_signal (& m_cond);
}

void SWriteJob::waitupdate()
{
    pthread_cond_wait (& m_cond, & m_mutex_cond);
}

void SWriteJob::waitupdate(double fSeconds)
{
    if (fSeconds <= 0) 
    {
        _error ("unexpected value: duration=%f\n", fSeconds);
        return ;
    }
    struct timespec ts = {};
    clock_gettime (CLOCK_REALTIME, & ts);
    
    ts.tv_sec += (int)fSeconds;
    ts.tv_nsec += sec2nsec(fSeconds - (int)fSeconds);

    // 处理进位
    if (ts.tv_nsec >= sec2nsec(1)) 
    {
        ts.tv_sec += 1;
        ts.tv_nsec -= sec2nsec(1);
    }

    _debug ("wait %ld.%ld\n", ts.tv_sec, ts.tv_nsec);

    pthread_cond_timedwait(& m_cond, & m_mutex_cond, &ts);
}

void SWriteJob::mkcopy(const SWriteJob &jobref)
{
    d = jobref.d;
}