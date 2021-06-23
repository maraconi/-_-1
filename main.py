from pprint import pprint

cook_book = {}

with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
    # while True:
    #     dishes = f.readline().strip()
    #     if not dishes:
    #         break
    #     count = int(f.readline().strip())
    #     cook_book[dishes] = []
    #     line = f.readline().strip()
    #     while line:
    #         ingredient = line.split(" | ")
    #         ingredients_dict = {"ingredient_name": ingredient[0], "quantity": int(ingredient[1]), "measure": ingredient[2]}
    #         cook_book[dishes].append(ingredients_dict)
    #         line = f.readline().strip()
    #     #     print(ingredients_dict)
    #     # print(cook_book[dishes])
    # pprint (cook_book)

    for line in f:
        dish_name = line.strip()
        counter = f.readline().strip()
        list_of_ingredient = []
        for i in range(int(counter)):
            ingredient = f.readline().strip().split(" | ")
            ingredients_dict = {"ingredient_name": ingredient[0], "quantity": ingredient[1],
                                "measure": ingredient[2]}
            list_of_ingredient.append(ingredients_dict)
            cook_book[dish_name] = {dish_name: list_of_ingredient}
            cook_book.update(cook_book[dish_name])
        f.readline().strip()
    pprint(cook_book)
