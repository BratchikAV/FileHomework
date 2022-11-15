import os.path

with open("КулинарнаяКнига.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for x in file:
        dish = x.strip()
        ingredient_num = file.readline()
        ingredients = []
        for _ in range(int(ingredient_num)):
            ingredient = file.readline().strip().split(" | ")
            ingredient_name, quantity, measure = ingredient
            ingredients.append({"ingredient_name": ingredient_name,
                                "quantity": quantity,
                                "measure": measure})
        file.readline()
        cook_book[dish] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    wishlist = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                name = ingredient["ingredient_name"]
                if name not in wishlist.keys():
                    wishlist[name] = {'measure': ingredient["measure"],
                                               'quantity': int(ingredient["quantity"]) * person_count}
                    continue
                else:
                    wishlist[name]["quantity"] += int(ingredient["quantity"]) * person_count

    print(wishlist)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

import os

current = os.getcwd()
file_name_1 = "firstFile.txt"
file_name_2 = "secondFile.txt"

with open(file_name_1, "rt", encoding="utf-8") as file_1:
    lines1 = 0
    for _ in file_1:
        lines1 += 1

with open(file_name_2, "rt", encoding="utf-8") as file_2:
    lines2 = 0
    for _ in file_2:
        lines2 += 1
print(lines2)

with open("thirdFile.txt", "wt", encoding="utf-8") as file_3:
    file_3.write(f"{os.path.basename(file_name_2)} \n")
    file_3.write(f"{str(lines2)} \n")
    lines_2 = open(file_name_2, "rt", encoding="utf-8").readlines()
    for line in lines_2:
        file_3.write(f"{line.strip()} \n")
    file_3.write(f"{os.path.basename(file_name_1)} \n")
    file_3.write(f"{str(lines1)} \n")
    lines_1 = open(file_name_1, "rt", encoding="utf-8").readlines()
    for line in lines_1:
        file_3.write(f"{line.strip()} \n")

