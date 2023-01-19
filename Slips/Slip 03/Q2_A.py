
dict = {'a': 1, 'b': 2, 'c': 3}

user_key = input("Enter key: ")

if user_key in dict.keys():
    dict[user_key] = 'new value'

print(dict)