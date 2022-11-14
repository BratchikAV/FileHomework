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

print(cook_book)