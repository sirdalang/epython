/**
 * sem_post.c
 * 
 * ÏûºÄÐÅºÅ
 */

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <fcntl.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <unistd.h>

int main()
{
    sem_t *pSem = sem_open("sem_test", O_CREAT, 0660, 0);

    if (pSem != SEM_FAILED)
    {
        printf("open sem successful!\n");
    }
    else
    {
        printf("open sem failed\n");
        return 0;
    }

    while (1)
    {
        while (1)
        {
            char c = getchar();
            if (c == EOF || c == '\n')
            {
                break;
            }
        }

        printf ("before wait sem\n");
        sem_wait(pSem);
        printf("after wait sem\n");
    }
}