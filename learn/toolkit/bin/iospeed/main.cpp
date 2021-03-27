
#include "iospeed.h"

#include <stdio.h>
#include <stdlib.h>

#include "debugprint.h"

static void wrong_input_handler(int argc, char *argv[])
{
    printf ("Usage: %s [size KB] [count]\n", argv[0]);
    exit (0);
    return ;
}

int main(int argc, char *argv[])
{
    if (argc != 3) 
    {
        wrong_input_handler(argc, argv);
    }

    int nKB = atoi(argv[1]);
    int nCount = atoi (argv[2]);

    if (nKB <= 1 || nCount <= 1) 
    {
        wrong_input_handler(argc, argv);
    }

    _debug ("start\n");
    write_test (nKB, nCount);

    return 0;
}