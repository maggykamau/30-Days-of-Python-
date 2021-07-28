#LEVEL 1 EXERCISE
#1
lssst = [] #this is an empty list

#2 list, more than 5 items
lisst = ['goat', 'hen','cow' ,56, 34, 67]
#3 len of list
print(len(lisst))
#4
print(lisst[0])
print(lisst[2:4])
print(lisst[-1])
#5  change this
mixed_data_types = ['maria' , '14', '150cm' , 'single','988']
print(mixed_data_types)
print(len(mixed_data_types))
#6
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
#10 
it_companies_copy = it_companies.copy()
it_companies[0] = "Macafee"
print(it_companies) #the answer for this is most probably wrong, repeat.
#11
it_companies.append('Samsung')
print(it_companies)
#12
it_companies.insert(3,'Sophos')
print(it_companies)
#13
it_companies[1] = it_companies[1].upper()
print(it_companies)
#14
print(("#;").join(it_companies))
#15
does_exist = 'Twitter' in it_companies
print(does_exist)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
slice_three = it_companies[3:]
print(slice_three)
#19
slice_last = it_companies[0:-3]
print(slice_last)
#20
middle = it_companies[((len(it_companies))//2)]
print(middle)
#21
it_companies.pop(0)
print(it_companies)
#22
it_companies.pop(((len(it_companies))//2))
print(it_companies)
#23
it_companies.pop(-1)
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
#27 (you can use append)
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#LEVEL 2 EXERCISE
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
maximum = max(ages)
print(maximum)
minimum = min(ages)
print(minimum)
ages.append(maximum)
ages.append(minimum)
print(ages)
#median
ages.sort()
print(ages)
mmedian = len(ages)//2
median = (ages[mmedian] + ages[~mmedian])/2
print(median)
#average age
average = sum(ages)/len(ages)
print(average)
#Range
rangee = range(maximum,minimum)
print(rangee)
rangee = maximum - minimum
print(rangee)
#compare values
print(abs(maximum)< abs(minimum))

#1 middle country
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
countries.sort
middle_country = len(countries)//2
print(countries[middle_country])

#2 adding and division (please review again)
first  = countries[0:middle_country +1]
second = countries[middle_country + 1:]
print(len(first), len(second))

#3
countriess = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third, *scandic_countries = countriess
print(countriess)

