#LEVEL 1
#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies2 = {'Sophos','Instagram','Snapchat','Tiktok'}
it_companies.update(it_companies2)
print(it_companies)
#4
it_companies.remove('Twitter')
print(it_companies)
#5
it_companies.discard('Twitter')  #this method doesn't raise an error if value is not present
# it_companies.remove('Twitter')  #this method raises an error if value is mot present


#LEVEL 2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
A.update(B)
print(A)

#2 items in both sets
print(A.intersection(B))
#3 subset
print(A.issubset(B))

#4 disjoint
print(A.isdisjoint(B))
#5 joining
print(A.union(B))
print(B.union(A))
#6symmentric difference   (**clarify which should start b2n A & B)
print(A.symmetric_difference(B))
#7 delete
del A
del B

#LEVEL 3 
#1 convert ages to set (removes duplicates)
age = [22, 19, 24, 25, 26, 24, 25, 24]
agest = set(age)
print(agest)
print(len(age) > len(agest))
#2 
"""String(ordered sequence of characters which may be repeated.)
List(ordered but changeable, also allows duplicate members)
Tuple(data types that are ordered and unchangeable,written in())
Set(collection of unordered items- can find union,difference,disjoint of elements,duplicate items are not allowed)"""

#3 (sentence to list), (find unique words using set)
sentence = "I am a teacher and I love to inspire and teach people"
lissst = sentence.split()
print(lissst)

print(set(lissst))



