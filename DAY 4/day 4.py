#DAY 4 30 DAYS CHALLENGE
#1
first ='Thirty'
second = 'days'
third = 'of' 
fourth = 'python'
one_string = first + ' ' + second + ' ' + third + ' ' + fourth
print(one_string)
#2
one = 'Coding'
two = 'For'
three = 'All'
single_string = one + ' ' + two + ' ' + three
print(single_string)
#3
company = "Coding For All"
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
slice_first = company[6:]
print(slice_first)
#10
print(company.find('Coding'))
#11
print(company.replace('Coding' ,'Python'))
#12
sentence = 'Python For Everyone'
print(sentence.replace('Everyone' , 'All'))
#13
print(company.split(' '))
#14
mystring = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(mystring.split(','))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
string1 ='Python For Everyone'
acronym1 =string1[0] + string1[7] + string1[11]
print(acronym1)
#19
acronym2 =company[0] + company[7] + company[11]
print(acronym2)
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rfind('l'))
#23
sentence1 = 'You cannot end a sentence with because because because is a conjuction'
print(sentence1.find('because'))
#24
print(sentence1.rindex('because'))
#25
print(sentence1.replace('because',""))
#26 
print(sentence1.find('because'))
#27 repeated @ 23
#28
print(company.startswith('Coding'))
#29
print(company.endswith('coding'))
#30
string2 = ' Coding For All '
print(string2.strip(' '))
#31
srrr = '30DaysOfPython'
print(srrr.isidentifier())
srt = 'thirty_days_of_python'
print(srt.isidentifier())
#32
lissst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(lissst))
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print('Name\t\tAge\tCountry\t\tCity \nAsabeneh\t250\tFinland\t\tHelsinki')
#35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f meters square'%(radius,area))
#36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

