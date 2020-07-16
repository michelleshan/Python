#4 Iterate Through a Dictionary with List Values
#  Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
#  prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
#  For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for entry in some_dict:
        print(len(some_dict[entry]),entry.upper())
        for value in some_dict[entry]:
            print(value)
printInfo(dojo)