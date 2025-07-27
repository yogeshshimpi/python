my_dict = {
    'a':1,
    'b':4,
    'c':234,
    'text':"Hello world"
}

print(my_dict)

print(my_dict["a"])

print(my_dict.get("text","Not Found"))  # Avoid error if key not present

print(my_dict.get("tex","Not Found"))  


# Add, update, remove method

my_dict['b'] = "Yogesh"
print(my_dict)

my_dict.update({'str':"hello world"})
print(my_dict)

my_dict.pop('c')
print(my_dict)


del my_dict['a']
print(my_dict)

my_dict.clear()
print(my_dict)