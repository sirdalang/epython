/**
 * sem_post.c
 * 
 * Éú³ÉÐÅºÅ
 */

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <fcntl.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <unistd.h>

int main(int argc, const char **argv)
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

    int nvalue = 0;
    sem_getvalue (pSem, &nvalue);
    if (nvalue != 0)
    {
        printf ("sem not zero, reset --> 0\n");
        
        while (1)
        {
            sem_getvalue (pSem, &nvalue);
            if (nvalue != 0)
            {
                sem_trywait (pSem);
                usleep (1000);
                printf ("sem decrease to %d\n", nvalue);
            }
            else 
            {
                printf ("sem to zero\n");
                break;
            }
        }
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

        sem_post(pSem);
        printf("post sem\n");
    }
}