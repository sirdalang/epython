#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>

static void bitprint(const void *pData, int nSize)
{
    char bitmap[8] = {0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80};

    for (int i = 0; i < nSize; ++i)
    {
        if ((i) % 4 == 0)
            printf ("0x%04x: ", i);
        for (int j = sizeof(bitmap) - 1; j >= 0; --j)
        {
            if (((char*)pData)[i] & bitmap[j])
            {
                printf ("1");
            }
            else 
            {
                printf ("0");
            }
        }
        printf (" ");
        
        if ((i+1) % 4 == 0)
            printf ("\n");
    }

    printf ("\n");
}

int main(int argc, const char **argv)
{
    int ret = -1;
    int fd = -1;
    void *pBuf = NULL;

    do 
    {
        if (argc != 2)
        {
            printf ("usage: %s [file]\n", argv[0]);
            break;
        }
        const char *szFile = argv[1];

        fd = open (argv[1], O_RDONLY);
        if (fd < 0)
        {
            printf ("open %s failed\n", szFile);
            break;
        }

        struct stat sStat = {};
        ret = fstat (fd, & sStat);
        if (ret < 0)
        {
            printf ("stat %s failed\n", szFile);
            break;
        }

        if (sStat.st_size > 64 * 1024)
        {
            printf ("size over\n");
            break;
        }

        pBuf = malloc (sStat.st_size);
        if (pBuf == NULL)
        {
            printf ("malloc failed\n");
            break;
        }

        read (fd, pBuf, sStat.st_size);
        bitprint (pBuf, sStat.st_size);

        ret = 0;
    }
    while (0);

    if (fd > 0)
    {
        close (fd);
        fd = -1;
    }

    return ret;
}