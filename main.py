import ctypes
from ctypes import wintypes
from datetime import datetime
from pathlib import Path

# --- Windows GUID type ---
class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8),
    ]

# FOLDERID_Desktop = {B4BFCC3A-DB2C-424C-B029-7FE99A87C641}
FOLDERID_Desktop = GUID(
    0xB4BFCC3A,
    0xDB2C,
    0x424C,
    (wintypes.BYTE * 8)(0xB0, 0x29, 0x7F, 0xE9, 0x9A, 0x87, 0xC6, 0x41)
)

shell32 = ctypes.WinDLL("shell32", use_last_error=True)
ole32 = ctypes.WinDLL("ole32", use_last_error=True)

shell32.SHGetKnownFolderPath.argtypes = [
    ctypes.POINTER(GUID),          # rfid
    wintypes.DWORD,                # dwFlags
    wintypes.HANDLE,               # hToken
    ctypes.POINTER(wintypes.LPWSTR) # ppszPath
]
shell32.SHGetKnownFolderPath.restype = wintypes.HRESULT

def get_desktop_path() -> Path:
    ppszPath = wintypes.LPWSTR()
    hr = shell32.SHGetKnownFolderPath(ctypes.byref(FOLDERID_Desktop), 0, None, ctypes.byref(ppszPath))
    if hr != 0:
        raise OSError(f"SHGetKnownFolderPath fejlede (HRESULT={hr})")
    try:
        return Path(ppszPath.value)
    finally:
        ole32.CoTaskMemFree(ppszPath)

# --- Program ---
print("=== Python Automatisering ===")

folder_name = input("Hvad skal mappen hedde? ").strip()
if not folder_name:
    print("Du skrev intet. Stopper.")
    raise SystemExit(1)

desktop = get_desktop_path()
new_folder = desktop / folder_name
new_folder.mkdir(parents=True, exist_ok=True)

log_file = new_folder / "log.txt"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"Oprettet: {datetime.now()}\n")

print(f"Desktop fundet: {desktop}")
print(f"Mappe klar: {new_folder}")
print("Log skrevet")
print("Færdig ✔️")
