import os

# Menü definiálása
programs = {
    "1": ("Restarter (Keeps your wi-fi alive)", "bash restarter.sh"),
    "2": ("Telegram bot (Telegram bot host)", "python bot1.py"),
    "3": ("Process kill (All process from the list) - összes", "tmux kill-server"),
    "5": ("Running processes (Shows backround running tasks)", ""),
   "..": ("", ""),
    "0": ("Exit", "exit"),
}
os.system("clear")
def show_menu():
    os.system('toilet -F metal "Toolbox"')
    print("\nChoose an item:\n")
    for key, value in programs.items():
        print(f"{key}. {value[0]}")

print("\n")  # Üres sor beszúrása

def start_program(choice):
    if choice in programs:
        command = programs[choice][1]

        if command == "exit":
            print("Exit...")
            os.system("clear")
            exit()

        program_name = command.replace(" ", "_")  # Szóköz helyett aláhúzás

        # **Most pontos grep keresést végzünk a tmux session listában**
        session_check = os.popen(f"tmux list-sessions | grep -w {program_name}").read().strip()

        if session_check:
            os.system("clear")
        else:
            os.system("clear")
            os.system(f"tmux new-session -d -s {program_name} '{command}'")
    else:
        os.system("clear")
        print("Invalid number!")

while True:
    show_menu()
    user_input = input("\n-> ")
    if user_input == "5":
        os.system("clear")
        os.system("python menu1.py")
        exit()
    else:
        start_program(user_input)
