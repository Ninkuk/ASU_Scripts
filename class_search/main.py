from datetime import datetime


def print_menu():
    selected_option = -1
    print("\nWelcome to the ASU scripts!\n___________________________")
    print("\n[1] Use class code to check availability"
          "\n[2] Check for all available classes for a course\n")
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

    return selected_option


def get_class_code():
    pass


def get_course_info():
    print("Select a semester to search")

    today = datetime.today()
    current_month = today.month
    current_year = today.year

    print("Registrations are open for the following semesters:")
    # print available semesters
    if current_month in range(2, 4):  # Feb - Mar
        print(f"[1] Spring {current_year}")  # show current year
        print(f"[2] Summer {current_year}")
        print(f"[3] Fall {current_year}")

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


if __name__ == '__main__':
    option = print_menu()
    if option is 1:
        get_class_code()
    else:
        get_course_info()
