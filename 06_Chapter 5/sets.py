# The sets is an unordered, unindexed and mutable collection that stores unique elements only.

#The set are creat using two way:
#1

my_set = {1,2,3,4,5}
print(my_set)
#2

my_set = set({2,45,62,"hello","world"})
print(my_set)

for item in my_set:
    print(item)
    
my_set.add('Vs code')
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(232) # This will not throw error if element not present
print(my_set)

my_set.pop() # This will remove random element
print(my_set)

my_set.clear() # remove all element from sets
print(my_set)


a={1,2,3}
b={3,4,5}

#set Operation

print(a.union(b))

print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


#Output:

# {1, 2, 3, 4, 5}
# {2, 'world', 'hello', 45, 62}
# 2
# world
# hello
# 45
# 62
# {'Vs code', 2, 'world', 'hello', 45, 62}
# {'Vs code', 'world', 'hello', 45, 62}
# {'Vs code', 'world', 'hello', 45, 62}
# {'world', 'hello', 45, 62}
# set()
# {1, 2, 3, 4, 5}
# {3}
# {1, 2}
# {1, 2, 4, 5}