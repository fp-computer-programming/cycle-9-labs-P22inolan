# Author: IBN (AMDG) 1/10/2022

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = (v * 2)
    return lst

print(double_stuff([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10])
print(double_stuff([1, 2.5, 3, 4.6, 5]) == [2, 5.0, 6, 9.2, 10])
print(double_stuff([1, "egg", 7.5, 6, "soup"]) == [2, 'eggegg', 15.0, 12, 'soupsoup'])
