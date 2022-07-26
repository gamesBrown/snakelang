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



x[1][0]=15

print(x)



students[0]['last_name'] ="Bryant"
print(students)

sports_directory['soccer'][0] ='Andres'
print(sports_directory)

z[0]['y']=30
print(z)

def iterateDictionary(some_list):
    
    for i in range(len(students)):
        result = ""
        for key in students[i]:
            if students[i][key] != students[i]['last_name']:
                result += f'First Name {students[i][key]} '
                
            else:
                result+= f'Last Name - {students[i][key]}'
                print(result)
                    
                

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])



iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict_list):
    for key in dict_list:
        print("-------------------")
        print(f"{key}: {len(dict_list[key])}")
        for i in range(len(dict_list[key])):
            print(dict_list[key][i])

printInfo(dojo)






