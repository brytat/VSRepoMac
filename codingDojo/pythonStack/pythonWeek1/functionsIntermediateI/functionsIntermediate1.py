
#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)

sports_directory = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
    }
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

#Iterate Through a List of Dictionaries
students2 = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for x in some_list:
        print("first_name - " + x['first_name'] + ", last_name - " + x['last_name'])
iterateDictionary(students2)

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])
iterateDictionary2("first_name",students2)
iterateDictionary2("last_name",students2)

#Iterate Through a Dictionary with List Values
dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
def printInfo(element):
    for x in element:
        print(len(element[x]),x)
        for y in element[x]:
            print(y)

printInfo(dojo)