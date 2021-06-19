#Day 2:30 Days of python programming

#Declaration of variables 

first_name=('Mag')
last_name= ('Anonymous')
full_name=first_name + last_name
country = ('Egypt')
city=('Cairo')
age=78
year=2050
is_married=True
is_True=('Yes')
is_light_on=False
chair,contactx,address = 'seated',4,5.6

#check datatypes of variables declared


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))
print(type([chair,contactx,address]))

#length and compare
print(len(first_name))
print(len(last_name))

#num 4 operations
num_one=5
num_two=4
_total=num_one + num_two
variable_diff=num_two-num_one
_product=num_two*num_one
_division= num_one/num_two
variable_remainder=num_one%num_two
variable_exp=num_one**num_two
variable_floor_division=num_one//num_two
print([num_one,num_two,_total,variable_diff,_product,_division,variable_remainder,variable_exp,variable_floor_division])

# circle problem(area,circumference)
radius=30.0
pi=3.142
area_of_circle=pi*radius*radius
print(int(area_of_circle))

circum_of_circle=2*pi*radius
print(int(circum_of_circle))

#radius as user input
radius=float(input("Enter the radius of your circle: "))
area=pi*radius*radius
print("Your area is: ", int(area))

#built in input function
 
first_name= input("Enter your first name: ")
last_name= input("Enter your last name: ")
country= input("Enter your country: ")
age=int(input("Enter your age: "))

print("Your name is: ", first_name)
print("Your last name is: ", last_name )
print("your country is: ", country)
print("You are", age, "years old")











