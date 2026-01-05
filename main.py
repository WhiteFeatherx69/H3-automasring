import ctypes
from ctypes import wintypes
from datetime import datetime
from pathlib import Path

# -------------------------
# Windows: Known Folder API
# -------------------------
class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8),
    ]


# FOLDERIDs (Microsoft Known Folders)
FOLDERID_Desktop = GUID(
    0xB4BFCC3A, 0xDB2C, 0x424C,
    (wintypes.BYTE * 8)(0xB0, 0x29, 0x7F, 0xE9, 0x9A, 0x87, 0xC6, 0x41)
)

FOLDERID_Documents = GUID(
    0xFDD39AD0, 0x238F, 0x46AF,
    (wintypes.BYTE * 8)(0xAD, 0xB4, 0x6C, 0x85, 0x48, 0x03, 0x69, 0xC7)
)

FOLDERID_Downloads = GUID(
    0x374DE290, 0x123F, 0x4565,
    (wintypes.BYTE * 8)(0x91, 0x64, 0x39, 0xC4, 0x92, 0x5E, 0x46, 0x7B)
)

shell32 = ctypes.WinDLL("shell32", use_last_error=True)
ole32 = ctypes.WinDLL("ole32", use_last_error=True)

shell32.SHGetKnownFolderPath.argtypes = [
    ctypes.POINTER(GUID),
    wintypes.DWORD,
    wintypes.HANDLE,
    ctypes.POINTER(wintypes.LPWSTR)
]
shell32.SHGetKnownFolderPath.restype = wintypes.HRESULT


def get_known_folder_path(folder_id: GUID) -> Path:
    ppszPath = wintypes.LPWSTR()
    hr = shell32.SHGetKnownFolderPath(ctypes.byref(folder_id), 0, None, ctypes.byref(ppszPath))
    if hr != 0:
        raise OSError(f"SHGetKnownFolderPath fejlede (HRESULT={hr})")
    try:
        return Path(ppszPath.value)
    finally:
        ole32.CoTaskMemFree(ppszPath)


# -------------
# App logic
# -------------
def ask_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            v = int(s)
            if min_val <= v <= max_val:
                return v
        print(f"Ugyldigt valg. Skriv et tal mellem {min_val} og {max_val}.")


def ask_yes_no(prompt: str) -> bool:
    while True:
        s = input(prompt + " (j/n): ").strip().lower()
        if s in ("j", "ja"):
            return True
        if s in ("n", "nej"):
            return False
        print("Skriv j eller n.")


def main():
    print("=== Python Automatisering (Menu) ===")

    print("\nVælg placering:")
    print("1) Desktop")
    print("2) Dokumenter")
    print("3) Downloads")

    choice = ask_int("Dit valg (1-3): ", 1, 3)

    if choice == 1:
        base_path = get_known_folder_path(FOLDERID_Desktop)
        base_name = "Desktop"
    elif choice == 2:
        base_path = get_known_folder_path(FOLDERID_Documents)
        base_name = "Dokumenter"
    else:
        base_path = get_known_folder_path(FOLDERID_Downloads)
        base_name = "Downloads"

    print(f"\nPlacering fundet ({base_name}): {base_path}")

    folder_base = input("\nSkriv mappenavn (fx Projekt): ").strip()
    if not folder_base:
        print("Du skrev intet. Stopper.")
        raise SystemExit(1)

    make_many = ask_yes_no("Vil du lave flere mapper?")
    count = 1
    if make_many:
        count = ask_int("Hvor mange mapper? (1-50): ", 1, 50)

    add_timestamp = ask_yes_no("Vil du tilføje dato/tid til mappenavn?")

    created = []

    for i in range(1, count + 1):
        name = folder_base
        if count > 1:
            name = f"{name}_{i:02d}"
        if add_timestamp:
            name = f"{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

        folder_path = base_path / name
        folder_path.mkdir(parents=True, exist_ok=True)

        log_file = folder_path / "log.txt"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"Oprettet: {datetime.now()}\n")

        created.append(folder_path)

    print("\n✅ Færdig!")
    print(f"Oprettet {len(created)} mappe(r):")
    for p in created:
        print(" -", p)


if __name__ == "__main__":
    main()
