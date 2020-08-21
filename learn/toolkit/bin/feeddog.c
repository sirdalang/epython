

#include <sys/types.h>
#include <sys/fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <signal.h>

#include <stdio.h>


#define DEBUG

#ifdef DEBUG
#define _debug(x...) do {printf("[debug][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _info(x...) do {printf("[info][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _error(x...) do {printf("[error][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#else 
#define _debug(x...) do {;} while (0)
#define _info(x...) do {printf("[info][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#define _error(x...) do {printf("[error][%s %d %s]", \
	__FILE__,__LINE__,__FUNCTION__);printf(x);} while (0)
#endif 

// #define  __HI3518EV300__
#define __HI3516EV200__

#define	WATCHDOG_IOCTL_BASE	'W'

#if defined (__HI3518EV300__)
#define WDIOC_SETOPTIONS     _IOWR(WATCHDOG_IOCTL_BASE, 4, int)
#define WDIOC_KEEPALIVE      _IO(WATCHDOG_IOCTL_BASE, 5)                                                                 
#define WDIOC_SETTIMEOUT     _IOWR(WATCHDOG_IOCTL_BASE, 6, int)
#define WDIOC_GETTIMEOUT     _IOR(WATCHDOG_IOCTL_BASE, 7, int)
#elif defined (__HI3516EV100__) || defined (__HI3516EV200__)
#define WDIOC_SETOPTIONS     _IOWR(WATCHDOG_IOCTL_BASE, 4, int)
#define WDIOC_KEEPALIVE      _IO(WATCHDOG_IOCTL_BASE, 5)                                                                 
#define WDIOC_SETTIMEOUT     _IOWR(WATCHDOG_IOCTL_BASE, 6, int)
#define WDIOC_GETTIMEOUT     _IOR(WATCHDOG_IOCTL_BASE, 7, int)
#endif


int main()
{
    signal (SIGHUP, SIG_IGN);

    int fd_wdt = open("/dev/watchdog", O_RDWR, 0);

    if (fd_wdt < 0) 
    {
        perror("/dev/watchdog");
        return -1;
    }

    int nTimeOut = 0;
    int ret = ioctl(fd_wdt, WDIOC_GETTIMEOUT, &nTimeOut);
    if (ret < 0)
    {
        perror("WDIOC_GETTIMEOUT");
        return -1;
    }

    _info ("timeout = %d\n", nTimeOut);

    while (1)
    {
        ret = ioctl(fd_wdt, WDIOC_KEEPALIVE);
        if (ret < 0)
        {
            perror("WDIOC_KEEPALIVE");
            return -1;
        }
        sleep (1);
    }
    
    return 0;
}