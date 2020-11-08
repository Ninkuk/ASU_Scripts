from datetime import datetime


# simply prints the menu
def print_menu():
    print("\n-------------------------------")
    print("| Welcome to the ASU scripts! |")
    print("-------------------------------")

    print("\n[1] Use class code to check availability"
          "\n[2] Check all available classes for a course"
          "\n[3] View your set alerts\n")


# handles the user input and validation of the menu
def get_menu_option():
    selected_option = -1
    print_menu()
    while True:
        selected_input = input("Please select an option: ")
        try:
            if int(selected_input) in [1, 2]:
                selected_option = int(selected_input)
                break
            else:
                print("\nSorry, please enter a valid number.")
        except:
            print("\nSorry, please enter a valid number.")
            continue

    print(f"Selected option[{selected_option}]")
    return selected_option


def get_class_code():
    pass


# handles the user input for getting the search semester
def get_semester(current_month, current_year):
    print("Registrations are open for the following semesters:")
    selected_option = -1

    # print available semesters
    if current_month in range(2, 4):  # Feb - Mar
        print(f"[1] Spring {current_year}")  # show current year
        print(f"[2] Summer {current_year}")
        print(f"[3] Fall {current_year}")
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) in range(1, 4):
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue
    elif current_month in range(4, 6):  # Apr - May
        print(f"[1] Summer {current_year}")
        print(f"[2] Fall {current_year}")
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) in range(1, 3):
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue
    elif current_month in range(9, 11):  # Sep - Oct
        print(f"[1] Fall {current_year}")
        print(f"[2] Spring {current_year + 1}")  # show next year
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) in range(1, 3):
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue
    elif current_month in range(11, 13):  # Nov - Dec
        print(f"[1] Spring {current_year + 1}")  # show next year
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) is 1:
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue
    elif current_month == 1:  # Jan
        print(f"[1] Spring {current_year}")  # show current year
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) is 1:
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue
    else:  # rest of the months: Jun - Aug
        print(f"[1] Fall {current_year}")
        print()

        while True:
            selected_input = input("Please select a semester: ")
            try:
                if int(selected_input) is 1:
                    selected_option = int(selected_input)
                    break
                else:
                    print("\nSorry, please enter a valid number.")
            except:
                print("\nSorry, please enter a valid number.")
                continue

    return selected_option


# handles the user input for getting the search subject
def get_subject():
    print()
    while True:
        subject_input = input("Enter a subject to search (like CSE or MAT): ")
        if len(subject_input) is 3:
            return subject_input.upper()
        else:
            print("\nSorry, please enter a valid subject code.")


# handles the user input for getting the course number
def get_course_number():
    print()
    while True:
        number_input = input("Enter the course number to search (like 101 or 360): ")
        try:
            if len(number_input) is 3 and int(number_input) > 0:
                return int(number_input)
            else:
                print("\nSorry, please enter a valid course number.")
        except:
            print("\nSorry, please enter a valid course number.")
            continue


def get_course_info():
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nSelect a semester to search")
    semester = get_semester(current_month, current_year)
    print(f"Selected semester")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    subject = get_subject()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    course_number = get_course_number()

    return [semester, subject, course_number]


if __name__ == '__main__':
    option = get_menu_option()

    if option is 1:
        get_class_code()
    elif option is 2:
        get_course_info()
    elif option is 3:
        pass
    else:
        print("Sorry, it seems you entered an invalid command.")
