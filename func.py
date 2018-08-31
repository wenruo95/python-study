# encoding: utf-8

def print_info(name, age = 18) :
    print(name, ", age = ", age)

def print_list(arg1, *list) :
    print(arg1)
    for var in list:
        print(var)

def print_dict(arg1, **dict) :
    print(arg1, dict)


print_info("xiaoming")
print_info("xiaoming",22)


print_list(55, 1, 2, 3)
print_dict(66, a = 1, b = 2, c = 3)
