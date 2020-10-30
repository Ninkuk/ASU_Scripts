def print_menu():
    selected_option = -1
    print("\nWelcome to the ASU scripts!\n___________________________")
    print("\n[1] Use class to check availability"
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


if __name__ == '__main__':
    option = print_menu()
