

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "safecall.h"

int main()
{
    char a[9] = "1234567";
    char b[10] = "123456789";
    SAFE_MEMCPY (a, b, sizeof(a), sizeof(b));
    SAFE_STRING_TAIL_0 (a, sizeof(a));
    printf ("a=%s,b=%s\n", a, b);
    return 0;
}