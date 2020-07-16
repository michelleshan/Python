#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# a Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changex(list):
    list[1][0]=15
    return list
print(changex(x))

# b Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_students(list):
    list[0]['last_name'] = 'Bryant'
    return list
print(change_students(students))

# c In the sports_directory, change 'Messi' to 'Andres'
def sportsfans(dictionary):
    dictionary['soccer'][0] = 'Andres'
    return dictionary
print(sportsfans(sports_directory))

# d Change the value 20 in z to 30
def change_z(dictionary):
    dictionary[0]['y'] = 30
    return dictionary
print(change_z(z))

#2 Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for i in range (0,len(some_list)):
        for k in some_list[i]:
            print(k,"-",some_list[i][k])
iterateDictionary(students)

#3 Get Values From a List of Dictionaries
#  Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name,some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name]')
iterateDictionary2('last_name',students)

#4 Iterate Through a Dictionary with List Values
#  Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
#  For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo(some_dict):
    for entry in some_dict:
        print(len(some_dict[entry]),entry.upper())
        for value in some_dict[entry]:
            print(value)
printInfo(dojo)