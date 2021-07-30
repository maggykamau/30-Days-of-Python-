#LEVEL 1
#1
empty_tuple = tuple()
print(empty_tuple)
#2
brothers = ('Sam','Martin','John','James')
sisters = ('Rose','Mary','Elsa','Suzy')
print(brothers)
print(sisters)
#3
siblings = brothers + sisters
print(siblings)
#4
print('I have ' + str(len(siblings))+ ' siblings')
#5
family_members = list(siblings)
family_members.append('Richard')
family_members.append('Esther')
print(family_members)
family_members = tuple(family_members)

#LEVEL 2
#1 unpacking
brother,sister,parent1,parent2,*siblings = family_members
print(brother)


#2
fruits = ('mango','orange','banana','grape')
vegetables = ('cabbage','kales','capcicum','carrot')
animal_products = ('milk','eggs','wool','honey')
food_stuff_tp = fruits + vegetables + animal_products

#3
food_stuff_It = list(food_stuff_tp)
print(food_stuff_It)

#4
print(food_stuff_It[5:7])

#5
firrst = food_stuff_It[:4]

secoond = food_stuff_It[:3]
print(firrst + secoond)


#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)







