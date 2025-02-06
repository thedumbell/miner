#include <windows.h>

void ShowMessageBox() {
    MessageBoxA(NULL, "Hello from injected DLL!", "Injected", MB_OK | MB_ICONINFORMATION);
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved) {
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hModule); // Gereksiz thread çağrılarını kapat
        ShowMessageBox();  // Doğrudan çağır (CreateThread kullanmadan)
    }
    return TRUE;
}
