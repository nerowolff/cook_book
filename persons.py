from pprint import pprint
cook_book = {}
def setting(key,_list):
    cook_book[key]=[]
    for items in _list:
        ingr={}
        items=items.split(' | ')
        ingr.setdefault('ingredient_name', items[0])
        ingr.setdefault('quantity', int(items[1]))
        ingr.setdefault('measure', items[2])

        
        cook_book[key]+=[ingr]
with open('cook_book.txt',encoding='UTF-8') as f:
    dish=f.read()
    dish_list=dish.split("\n")
    dish_list_=[]
    for element in dish_list:
        if element =="":
            setting(dish_list_[0],dish_list_[2:])
            dish_list_=[]
        elif element==dish_list[-1]:
            dish_list_.append(element)
            cook_book.setdefault(dish_list_[0])
            setting(dish_list_[0],dish_list_[2:])
        else:
            dish_list_.append(element)


def get_shop_list_by_dishes(list,dishes, person_count):
    ingredient_list={}
    for dish in dishes:
        for item in list[dish]:
            if item['ingredient_name'] not in ingredient_list:
                ingredient_list[item['ingredient_name']]={'miasure':(item['measure']),'quantity':item['quantity']*person_count}
            else:
    #Исправил логику подсчета ингредиентов
                ingredient_list[item['ingredient_name']]['quantity']+=(item['quantity']*person_count)
    # Исправил работу с глобальной переменной.теперь функция принимает ее в качестве параметра и возврашает локальную переменную,
    # не ищет cook_book снаружи и не изменяет ее напрямую.
    return ingredient_list

pprint(get_shop_list_by_dishes(cook_book,['Фахитос', 'Омлет'], 2))