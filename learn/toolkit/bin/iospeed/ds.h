
/**
 * ���ݶ���
 */

#pragma once

// д���������ݶ���
class SWriteJob 
{
public:
    int nKB;        // ÿ���ļ��Ĵ�С����λ��KB
    int nCount;     // д�ļ��ĸ���
    struct timeval tvJobStart;      // ��������ʱ��
    struct timeval tvJobEnd;        // �������ʱ��
    int nTotalKB;       // ��ǰ��д����ܴ�С����λ��KB
    int nPrintKB;       // ��ӡ���ڶ�Ӧд���С����λ��KB
    int nWriteBufKB;    // д����С����λ��KB
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