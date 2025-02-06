#include <windows.h>

DWORD WINAPI MessageThread(LPVOID lpParam) {
    MessageBoxA(NULL, "Hello from injected DLL!", "Injected", MB_OK | MB_ICONINFORMATION);
    return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved) {
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        CreateThread(NULL, 0, MessageThread, NULL, 0, NULL);
    }
    return TRUE;
}
