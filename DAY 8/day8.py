#DAY 8
#1 empty dict
dog = {}
print(dog)
#2 add values
dog['name'] = 'Goldie'
dog['color'] = 'grey'
dog['breed'] = 'huskie'
dog['legs'] = '4'
dog['age'] = 5
print(dog)

#3 
student_dict = {'first_name':'Joy','last_name':'James','gender':'female', 'age':16,
'marital_status':'single','skills':['java','nessus','c','wireshark'],'country':'Eritrea',
'City':'Johnston','address':{'street':'James_street','Zipcode':'86859'}}
print(student_dict)

#4 length of student_dict
print(len(student_dict))
#5

print(type(student_dict['skills']))
""""
print(student_dict(type(['skills'))) """
#6
student_dict['skills'].append('json')
print(student_dict)
#7
keys = student_dict.keys()
print(keys)
#8
values = student_dict.values()
print(values)

#9
print(student_dict.items())
#10delete

del student_dict['City']
print(student_dict)

#11

del student_dict
