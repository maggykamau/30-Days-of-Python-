#DAY 3 OF 30 DAY CHALLENGE
#declaration of variables
age = 10
height = 5.46
complex_number = 9+ 7j

 #script to calculate area
base_of_triangle = float(input("Enter the base of the triangle: "))
height_of_triangle = float(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
print("The area of the triangle is: " , area_of_triangle)

#script to calculate perimeter
side_a = float(input("Enter side a of your triangle: "))
side_b = float(input("Enter side b of your triangle: "))
side_c = float(input("Enter side c of your triangle: "))
perimeter = side_a + side_b + side_c
print("Perimeter of your triangle is: " , perimeter)

#area & perimeter of rectangle script

length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width 
perimeter_of_rectangle = 2 * (length + width)
print("Area of the rectangle is: ",area_of_rectangle)
print("Perimeter of rectangle is: ", perimeter_of_rectangle)

#area and circumference of circle
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area_of_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area of the circle is: ",area_of_circle)
print("Circumference of the circle is: ", circumference)

#8  script for slope y=2x-2
y1, x2 = 0, 0
x1= (y1 +2)/2
y2= 2 * x2-2
m1= (y2 -y1) /(x2-x1)
print("The X intercept is: ", x1, "And the y intercept is: ", y2)
# 9 script for slope 2
x1,x2=2,6
y1,y2=2,10
m=y2-y1/x2-x1
print("The gradient is: ", m ,"Between points 8 & 9")
#10 comparison statement 
print(m1 == m)
#11 value of y
x = -3
y=(x**2) + (6*x)+9
print("The value of y= ", y ,"when x is -3")
# 12 length of python and jargon\
print('Length of python is: ', len('python'))
print('Length of jargon is: ', len('jargon'))
if len('python')>=len('jargon'):
	print("True")
else:
	print("False")

 #13 and operator
print('on' in 'python' and 'on' in 'jargon')

#14 in operator
print('jargon' in 'I hope this course is not full of jargon' )
#15 no 'on'
print('on'  not in 'dragon' and 'on' not in 'python')
#16 
len('python')
print(float(len('python')))
print(str(len('python')))

#17 check if numbr is even 
number = int(input("Enter a number: "))
if (number % 2 ==0):
	print("number is even")
else:
	print("number is not even")

#18 floor division
print(7//3 == int(2.7))
#19 equal to
print('10' == 10)

#20 equal to 2
print(int(9.8) == 10)

#21 script for user input

hours =float(input("Enter hours: "))
rate_per_hour=float(input("Enter rate per hour: "))
pay_per_person= hours * rate_per_hour
print("Your weekly earning is: ", pay_per_person)

#22 enter number of years
number_of_years=int(input("Enter number of years you have lived: "))
seconds=3153600
total_seconds_lived=number_of_years*seconds
print("You have lived for: ", total_seconds_lived , "seconds")

#23 python script to display table 

print("A program to display the following table")
a=1
b=2
c=3
d=4
e=5
print(a,  a,  a,  a ** 2,       a * a * a)
print(b,  a,  b,  b ** 2,       b * b * b)
print(c,  a,  c,  c ** 2,       c * c * c)
print(d,  a,  d,  d ** 2,       d * d * d)
print(e,  a,  e,  e ** 2,       e * e * e )

#different formula for 23
for i in range(1,6):
	print(i**1,i**0,i**1,i**2,i**3)