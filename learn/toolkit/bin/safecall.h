#pragma once

#define SAFE_MEMCPY(pDst,pSrc,nSizeDst,nSizeSrc)\
    do {\
        memcpy (pDst, pSrc, nSizeDst < nSizeSrc ? nSizeDst : nSizeSrc);\
    } while (0);

#define SAFE_STRING_TAIL_0(pStr,size)\
    do {\
        pStr[size-1]='\0';\
    } while (0);