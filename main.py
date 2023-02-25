from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        dish_name = line.strip()
        number = int(f.readline())
        ingridients_list = []
        for _ in range(number):
            ingridients = f.readline().strip()
            ingridient_name, quantity, measure = ingridients.split(' | ')
            ingridients_list.append({'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = ingridients_list
        f.readline()

# pprint(cook_book, sort_dicts=False) #Вывод результата Задания № 1

menu = "Меню:\nОмлет\nУтка по-пекински\nЗапеченный картофель\nФахитос"
print(menu)
dishes = list(input('Выберите название блюда: ').split(','))
person_count = int(input('Введите количество персон: '))
def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = {}
    for dish in dishes:
        if dish in cook_book:
            dish_lists = cook_book[dish]
            for dish_list in dish_lists:
                q = dish_list.pop('ingridient_name')
                dish_list['quantity'] = int(dish_list['quantity'])
                dish_list['quantity'] *= person_count
                if q in dishes_list:
                    dishes_list[q]['quantity'] += dish_list['quantity']
                else:
                    dishes_list[q] = dish_list
    pprint(dishes_list)
get_shop_list_by_dishes(dishes, person_count)



