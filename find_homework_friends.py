import json

common_person = []

if __name__ == '__main__':
    files_list = json.load(open("./classes_list.json", "r"))

    list_size = len(files_list)

    for num in range(0, list_size - 1):
        class_one = json.load(open(files_list[num] + '.json', "r"))
        for person in class_one:
            for num1 in range(num + 1, list_size):
                class_x = json.load(open(files_list[num1] + '.json', "r"))
                if person in class_x:
                    print(person, files_list[num], files_list[num1])
