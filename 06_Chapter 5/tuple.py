t1 = (1,) # single element tuple
print(t1)
# (1,)
#concatenation
t1 = t1 + (4,2,2,264,123,"hello","world")
print(t1)
# (1, 4, 2, 2, 264, 123, 'hello', 'world')

#slicing
print(t1[0:6]) #(1, 4, 2, 2, 264, 123)
print(t1[-4:-1]) #(264, 123, 'hello')

#repetition
print(t1*4)
#(1, 4, 2, 2, 264, 123, 'hello', 'world', 1, 4, 2, 2, 264, 123, 'hello', 'world', 1, 4, 2, 2, 264, 123, 'hello', 'world', 1, 4, 2, 2, 264, 123, 'hello', 'world')  

#count and Index
print(t1.count(2))
# 2


#The is immutable so we can change the value of it's


