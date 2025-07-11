cook_book = {}
def setting(key,_list):
    cook_book[key]=[]
    for items in _list:
        ingr={}
        items=items.split(' | ')
        ingr.setdefault('ingredient_name', items[0])
        ingr.setdefault('quantity', int(items[1]))
        ingr.setdefault('measure', items[2])
        # print(ingr)
        
        cook_book[key]+=[ingr]
    # print(lists_1)
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
# print(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    result={}
    for x in dishes:
        for item in cook_book[x]:
            result.setdefault(item['ingredient_name'],{'measure':item['measure'],'quantity':item['quantity']*person_count})
    print(result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)