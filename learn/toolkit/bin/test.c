

#include <stdlib.h>

#include "debugmalloc.h"

int main()
{
    void *p = malloc (100);
    free (p);
    return 0;
}