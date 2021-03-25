
#include "ds.h"

SWriteJob::SWriteJob() : 
    mutex_this (PTHREAD_MUTEX_INITIALIZER),
    nKB(0),
    nCount(0),
    tvJobStart({0}),
    tvJobEnd({0}),
    nTotalKB(0),
    nPrintKB(1000),
    nWriteBufKB(1)
{
    sem_init (& m_sem_update, 0, 0);
}

SWriteJob::~SWriteJob() 
{
    sem_destroy (& m_sem_update);
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
    sem_post (& m_sem_update);
}

void SWriteJob::waitupdate()
{
    sem_wait (& m_sem_update);
}