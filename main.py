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

