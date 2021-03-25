
/**
 * 数据对象
 */

#pragma once

// 写入任务：数据对象
class SWriteJob 
{
public:
    int nKB;        // 每个文件的大小，单位：KB
    int nCount;     // 写文件的个数
    struct timeval tvJobStart;      // 任务启动时间
    struct timeval tvJobEnd;        // 任务结束时间
    int nTotalKB;       // 当前已写入的总大小，单位：KB
    int nPrintKB;       // 打印周期对应写入大小，单位：KB
    int nWriteBufKB;    // 写入块大小，单位：KB
public:
    SWriteJob();
    ~SWriteJob();
    void lock();
    void unlock();
    void update();
    void waitupdate();
private:
    sem_t m_sem_update;
    pthread_mutex_t m_mutex_this;
private:
    SWriteJob& operator=(SWriteJob const &) {};
    SWriteJob(SWriteJob const &) {};
};