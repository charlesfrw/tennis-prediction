import os
from termcolor import colored

def print_menu():
    print(colored("----------------------------------------------------------------------", 'green'))
    print(colored("                TENNIS PYTHON PROGRAMS (by Charlesfrw on GitHub)             ", 'green'))
    print(colored("----------------------------------------------------------------------", 'green'))
    print(colored("Explore tennis data with these Python programs.", 'yellow'))
    print("")
    print(colored("1. Data Finder", 'yellow'))
    print(colored("2. ATP Rankings", 'yellow'))
    print(colored("3. ATP Players Statistics", 'yellow'))
    print(colored("4. Data Extractor for Machine Learning", 'yellow'))
    print(colored("5. Data Preprocessing for Machine Learning", 'yellow'))
    print(colored("6. Prediction by Machine Learning", 'yellow'))
    print(colored("7. Exit", 'red'))
    print("")

def run_program(program_name):
    program_path = os.path.join('/Users/charles/Desktop/TENNIS/Python', program_name)
    os.system(f'python3 {program_path}')
    input(colored("\nPress Enter to return to the menu...", 'cyan'))

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input(colored("Enter the program number to launch (1-7): ", 'cyan'))

        if choice == '1':
            run_program('Tennis_Data_Finder.py')
        elif choice == '2':
            run_program('Tennis_ATP_Rankings.py')
        elif choice == '3':
            run_program('Tennis_ATP_Player_Statistics.py')
        elif choice == '4':
            run_program('Tennis_Data_Extractor.py')
        elif choice == '5':
            run_program('Preprocessing.py')
        elif choice == '6':
            run_program('Machine_Learning.py')
        elif choice == '7':
            print(colored("Exiting the menu. Goodbye!", 'red'))
            break
        else:
            print(colored("Invalid choice. Please enter a number between 1 and 7"))
                          
