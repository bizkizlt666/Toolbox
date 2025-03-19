import psutil
import os
import time
# **A programok listája, amelyeket ellenőrizni akarunk**
progs = {
    "python bot1.py": "Telegram bot",
    "bash restarter.sh": "Restarter",
}

def is_process_running(program):
    """Megnézi, hogy az adott program fut-e."""
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        cmdline = " ".join(process.info['cmdline']) if process.info['cmdline'] else ""

        if program in cmdline:
            return True  # Ha megtaláltuk, fut

    return False  # Ha nem találtuk meg, nem fut

def check_programs():
    """Kiírja az összes program állapotát."""
    #print("Futó programok ellenőrzése:\n")
    os.system('toilet -F metal "Toolbox"')
    for cmd, name in progs.items():
        status = "\U0001F7E2" if is_process_running(cmd) else "\U0001F534"
        print(f"{name}: {status}")


def main():
    if __name__ == "__main__":
        os.system("clear")
        check_programs()

while True:
    main()
    user_input = input("\n0 - back\n\n-> ")
    if user_input == "0":
        os.system("clear")
        os.system("python menu.py")
        exit()
    else:
        main()
