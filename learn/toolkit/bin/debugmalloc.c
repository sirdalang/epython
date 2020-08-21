#include <stdio.h>
#include <stdlib.h>


void* MALLOC_DEBUG (int size, const char *szFile, int line, const char *szFunction)
{
    void *p = malloc (size);
    
    printf ("MLOC_DEBUG p=%p size=%d at [%s %d %s]\n", p, size, szFile, line, szFunction);
    return p;
}

void FREE_DEBUG (void *p, const char *szFile, int line, const char *szFunction)
{
    free (p);
    printf ("FREE_DEBUG p=%p at [%s %d %s]\n", p, szFile, line, szFunction);
    return ;
}