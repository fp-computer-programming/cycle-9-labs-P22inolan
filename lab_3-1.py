# Author: IBN (AMDG) 1/11/2022

def add_foods(lst):
    sixth_letter = []
    short_foods = []
    not_foods = []
    try:
        for i, v in enumerate(lst):
            try:
                if len(v) >= 6:
                    sixth_letter.append(v[5])
                elif len(v) < 6:
                    short_foods.append(v)
            except TypeError:
                not_foods.append(v)
    finally:
        print('sixth_letter:', sixth_letter)
        print('short_foods:', short_foods)
        print("not_foods:", not_foods)


(add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple']))
(add_foods(['naan', 'celery', 'buckwheat', 7, 'clementine']))
(add_foods(['cheeseburger', True, 'chicken', 'rice', 'radish']))
