l1 = ['Apple','Ball','Doll','Cat']
print(l1)
# ['Apple', 'Ball', 'Doll', 'Cat']

print(l1[0:4])
# ['Apple', 'Ball', 'Doll', 'Cat']

print(l1[2:])
# ['Doll', 'Cat']

print(l1[:3])
# ['Apple', 'Ball', 'Doll']


l1.append('VS code')
print(l1)
# ['Apple', 'Ball', 'Doll', 'Cat', 'VS code']

l1.sort()
print(l1)
# ['Apple', 'Ball', 'Cat', 'Doll', 'VS code']

l1.remove('Apple')
# ['Ball', 'Cat', 'Doll', 'VS code']
print(l1)

l1.insert(0,'Coding')
print(l1)
# ['Coding', 'Ball', 'Cat', 'Doll', 'VS code']

l1.extend(['Python','Java','C','C++'])
print(l1)
# ['Coding', 'Ball', 'Cat', 'Doll', 'VS code', 'Python', 'Java', 'C', 'C++']

l1.pop()
print(l1)
# ['Coding', 'Ball', 'Cat', 'Doll', 'VS code', 'Python', 'Java', 'C']

l1.pop(-2)
print(l1)
# ['Coding', 'Ball', 'Cat', 'Doll', 'VS code', 'Python', 'C']




#Comment line is output of above print()