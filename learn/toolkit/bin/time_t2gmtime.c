/**
 * 转换time_t 为 0 时区时间
 */

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, const char **argv)
{
        if (argc != 2)
        {
                printf ("argc != 2\n");
                return 0;
        }

        long lnTime = atol (argv[1]);

        struct tm stm = {};
        gmtime_r ( (time_t*)&lnTime, &stm);

        char strTime[64] = {};
        strftime (strTime, sizeof(strTime), "%F %T", & stm);

        printf ("%ld --> %s\n", lnTime, strTime);

        return 0;
}