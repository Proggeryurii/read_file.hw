cook_book = {}
with open('text.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    x = True
    i = 0
    tpr = lines[-1] + "\n"
    lines[-1] = tpr
    for line in lines:
        try:
            int(line)
            x = True
        except ValueError: 
            x = False
        if x:
            cook_book[lines[i - 1].strip()] = []
            ingredients = 0
            for ingredient in range(0, int(line)):
                cook_book[lines[i - 1].strip()].append({})
                count_symbols = 0
                last_count_symbols = 0
                count_pipeline = 3
                while count_pipeline != 0:
                    for symbol in lines[i+ingredient + 1]:
                        symbol = str(symbol)
                        if count_pipeline != 1:
                            while symbol != '|':
                                count_symbols += 1
                                break
                            else:
                                word = " "
                                for bukva in range(last_count_symbols , count_symbols):
                                    word = word + lines[i+ingredient + 1][bukva]
                                last_count_symbols = count_symbols + 1
                                if count_pipeline == 3:
                                    cook_book[lines[i - 1].strip()][ingredient]['ingredient_name'] = word.strip()
                                if count_pipeline == 2:
                                    cook_book[lines[i - 1].strip()][ingredient]['quantity'] = int(word.strip())
                                if count_symbols == 1:
                                    cook_book[lines[i - 1].strip()][ingredient]['measure'] = word.strip()
                                count_pipeline -= 1
                        else:
                            while symbol != "\n":
                                count_symbols += 1
                                break
                            else:
                                word = " "
                                for bukva in range(last_count_symbols + 2, count_symbols + 2):
                                    word = word + lines[i+ingredient + 1][bukva]
                                last_count_symbols = count_symbols
                                if count_pipeline == 3:
                                    cook_book[lines[i - 1].strip()][ingredient]['ingredient_name'] = word.strip()
                                if count_pipeline == 2:
                                    cook_book[lines[i - 1].strip()][ingredient]['quantity'] = word.strip()
                                if count_pipeline == 1:
                                    cook_book[lines[i - 1].strip()][ingredient]['measure'] = word.strip()
                                count_pipeline -= 1
                    
                ingredients += 1

        i += 1

def get_shop_list_by_dishes(dishes: list, person_count):
    get_shop_list_by_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            get_shop_list_by_dishes[ingredient['ingredient_name']] = {}
            get_shop_list_by_dishes[ingredient['ingredient_name']]['measure'] = ingredient['measure']
            get_shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] = ingredient['quantity'] * person_count
    return get_shop_list_by_dishes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))