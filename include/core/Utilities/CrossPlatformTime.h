#pragma once

#ifdef _WIN32
    #include <winsock2.h>
    #include <windows.h>

    inline int gettimeofday(timeval* tv, void*) {
        FILETIME ft;

        GetSystemTimeAsFileTime(&ft);

        unsigned long long t = ((unsigned long long)ft.dwHighDateTime << 32) | ft.dwLowDateTime;

        // Convert from 100ns intervals sinc Jan 1 1601
        t -= 116444736000000000ULL;

        tv->tv_sec = (long)(t / 10000000ULL);
        tv->tv_usec = (long)((t % 10000000ULL) / 10);

        return 0;
    }
#else
    #include <sys/time.h>
#endif