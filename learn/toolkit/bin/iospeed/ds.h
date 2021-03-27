
/**
 * 数据对象
 */

#pragma once

#include <sys/time.h>
#include <semaphore.h>
#include <pthread.h>

// 写入任务：数据对象
class SWriteJob 
{
public:
    enum STATE 
    {
        STATE_INITIALIZED,
        STATE_WRITING,
        STATE_FINISH,
        STATE_ERROR
    };
    struct Data
    {
        int nKB;        // 每个文件的大小，单位：KB
        int nCount;     // 写文件的个数
        struct timeval tvJobStart;      // 任务启动时间
        struct timeval tvJobEnd;        // 最后写入时间
        int nTotalKB;       // 当前已写入的总大小，单位：KB
        int nPrintKB;       // 打印周期对应写入大小，单位：KB
        int nWriteBufKB;    // 写入块大小，单位：KB
        int nBps;           // 当前写入速度
        STATE eState;
    };
    Data d;
public:
    SWriteJob();
    ~SWriteJob();
    void lock();
    void unlock();
    void update();
    void waitupdate();
    void waitupdate(double fSeconds);
    void mkcopy(const SWriteJob &);
private:
    pthread_mutex_t m_mutex_this;
    pthread_cond_t m_cond;
    pthread_mutex_t m_mutex_cond;
private:
    SWriteJob& operator=(SWriteJob const &);
    SWriteJob(SWriteJob const &);
};