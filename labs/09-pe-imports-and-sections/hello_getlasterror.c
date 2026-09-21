#include <stdio.h>
#include <windows.h>

int main(void)
{
    DWORD err = GetLastError();
    printf("GetLastError=%lu\n", (unsigned long)err);
    return 0;
}
