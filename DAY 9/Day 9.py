#LEVEL 1
#1

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
        print('You need more ', 18-age , 'years to learn to drive')

#2
#2
your_age = int(input('Enter your age: '))
my_age = 40
difference = (your_age - my_age)
if your_age > my_age and difference == 1 :
    print('You are ', difference,' year older than me')
elif difference > 1:
    print('You are ', difference, ' years older than me')
elif my_age == your_age:
    print('We are agemates')
elif your_age < my_age and difference == 1 :
    print('Iam ', abs(difference), ' year older than you')

else :

    print('Iam', abs(difference) ,' years older than you')


#3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a>b:
    print("a is greater than b")
elif a<b:
        print("a is smaller than b")
else:
    print("a is equal to b")

#exercise level 2
#1
score = int(input('Enter your grade: '))
if score > 0:
    if score >=80 and score <= 100:
        print('GRADE A')
    elif score >=70 and score <= 79:
        print('GRADE B')
    elif score >=60 and score <= 69:
        print('GRADE C')
    elif score >=50 and score <= 59:
        print('GRADE D')
    elif score >=0 and score <= 49:
        print('GRADE F')
else:
        print("Invalid entry")
#2
month = str(input('Enter the month: '))
month = month.upper()
if month == 'SEPTEMBER'or month == 'OCTOBER' or month =='NOVEMBER':
    print('The season is Autumn')
elif month == 'DECEMBER' or month== 'JANUARY' or month == 'FEBRUARY':
    print('The season is winter')
elif month == 'MARCH' or month =='APRIL' or month == 'MAY':
    print('season is spring')
elif month == 'JUNE' or month == 'AUGUST' or month== 'JULY':
    print('season is summer')
else:
    print('Invalid month entry')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
enteredvalue = str(input('enter fruit: '))
enteredvalue = enteredvalue.lower()
if enteredvalue in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(enteredvalue)
    print(fruits)
    

#LEVEL 3
#4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print(person['skills'][(len(person['skills']))//2])
if 'python' in person['skills']:
    print('python exists')
else:
   print('python does not exist')

if ['Javascript','React'] == person['skills']:
    print('He is a front end developer')
elif ['Node','Python' ,'MongoDB'] == person['skills']:
    print('He is a backend developer')
elif ['React','Node' ,'MongoDB'] == person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person ['is_marred'] and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'] , 'lives in', person['country'] +'.'' He is married.')