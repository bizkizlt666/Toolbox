import os

# Menü definiálása
programs = {
    "1": ("Restarter", "bash restarter.sh"),
    "2": ("Telegram Music bot", "python bot1.py"),
    "3": ("HTOP rendszerfigyelő", "htop"),
    "4": ("Process kill - összes", "tmux kill-server"),
   "..": ("", ""),
    "0": ("Kilépés", "exit"),
}
os.system("clear")
def show_menu():
    os.system('toilet -F metal "Toolbox"')
    print("\nVálassz egy programot az indításhoz:\n")
    for key, value in programs.items():
        print(f"{key}. {value[0]}")

print("\n")  # Üres sor beszúrása

def start_program(choice):
    if choice in programs:
        command = programs[choice][1]

        if command == "exit":
            print("Kilépés...")
            os.system("clear")
            exit()

        program_name = command.replace(" ", "_")  # Szóköz helyett aláhúzás

        # **Most pontos grep keresést végzünk a tmux session listában**
        session_check = os.popen(f"tmux list-sessions | grep -w {program_name}").read().strip()

        if session_check:
            os.system("clear")
            print(f"{program_name} már fut egy tmux sessionben!")
        else:
            os.system("clear")
            os.system(f"tmux new-session -d -s {program_name} '{command}'")
            print(f"{program_name} elindítva egy új tmux sessionben.")
    else:
        print("Érvénytelen választás, próbáld újra!")

while True:
    show_menu()
    user_input = input("\nAdd meg a számot: ")
    start_program(user_input)
