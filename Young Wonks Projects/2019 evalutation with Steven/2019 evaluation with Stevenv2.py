"""Random Age function (a)
-------------------------------------------------------------------------------
 * creates a list of random numbers between a and b
 * returns the list of random numbers
"""

"""Addition to Random Age function (f)
------------------------------------------------------------------------------
 * pops index 5 and replaces it with a new random age between -10 and 10
 * pops all ages from 30 to 40 and replaces it with a random age between 60 and 100
"""

import random
import sys

def randomAges():
    ages = []
    for i in range(1,16,1):
        ages.append(str(random.randint(-100,100)))
    #f
    ages[5] = str(random.randint(-10,10))
    for age in range(len(ages)):
        if int(ages[age]) <= 40 and int(ages[age]) >=30:
            ages[age]=str(random.randint(60,100))
    
    return ages

"""Option to add or remove animals (d)
-------------------------------------------------------------------------------
 * adds an option to add animals after inputting 3 animal names
 * adds an option to remove animals after inputting 3 animal names
 * prints the keys and values next to each other after each step
"""
moreanimals=[]
def addORremoveAnimal(animals):
    choice = input('would you like to add or remove animals(add/remove/continue/exit): ')
    if choice == 'add':
        addanimal = input('enter animal name: ')
        animals[addanimal]=randomAges()
        print('added: ',addanimal)
        print(animals)
        addORremoveAnimal(animals)
    elif choice =='remove':
        removeanimal = input('enter animal name: ')
        if removeanimal in animals:
            del animals[removeanimal]
            print('removed: ',removeanimal)
            print(animals)
            addORremoveAnimal(animals)
    elif choice == 'continue':
        print('continuing')
    elif choice =='exit':
        print('exiting')
        sys.exit()
    else:
        print('invalid response: type add, remove, continue, or exit')
        addORremoveAnimal(animals)

"""Sort animal age function (e)
-------------------------------------------------------------------------------
 * takes in a dictionary argument and returns the oldest age from each animal list
 * returns the list index from each animal list
 * all positive ages are moved into an empty list and sorted from youngest to oldest
 * returns a dictionary with the biggest age and index for each animal
"""

def sortanimalAge(animals):
    format_1={}
    agelist=[]
    positiveage=[]
    for animal in animals:
        format_1[animal]={'biggest_age':None,'num':None}
        for age in animals[animal]:
            agelist.append(int(age))
        for i in agelist:
            if i > 0:
                positiveage.append(i)
        positiveage.sort()
        format_1[animal]['biggest_age'] = positiveage[-1]
        format_1[animal]['num'] = len(positiveage)
        agelist=[]
        positiveage=[]
    return format_1

"""Sort and print function (h)
-------------------------------------------------------------------------------
 * sorts and prints all the animal names (keys) and animal age lists (values) separately
"""

def sortandprint(animals):
    for i in animals:
        print('animal name: ',i)
        print('animal ages: ',animals[i])
        print()

"""Function that resets the animal age of one animal list (g)
-------------------------------------------------------------------------------
 * a feature where the user is able to reset the animal age list for one animal
"""

def resetanimalage(animals):
    c = input('would you like to reset animal age for one animal(yes/no): ')
    if c == 'yes':
        name = input('enter animal name: ')
        for animal in animals:
           if name == animal:
               print('reseting the ages of: ',animal)
               animals[animal]=randomAges()
               print(animals)
               
    elif c == 'no':
        print('animal ages kept the same')
    else:
        print('type yes or no')
        resetanimalage(animals)
        
"""Two functions (returnSum and returnMean) to get the sum of each animal list and the mean/average of the sums (b)
------------------------------------------------------------------------------
  * returnSum takes in a dictionary argument and returns the sum of each animal age list in a dictionary
  * returnSum removes all negate ages first and uses a for loop to add the sum of each positive integer
  * returnMean takes in a dictionary (animalSum) from the returnSum function and uses it to return to mean for each animal
"""
def returnSum(animals):
    temp=[]
    animalSum={}

    for animal in animals:
        animalSum[animal] = {'sum':None,'num':None}
        for age in animals[animal]:
            if int(age) > 0:
                temp.append(int(age))
        animalSum[animal]['sum'] = sum(temp)
        animalSum[animal]['num'] = len(temp)
        temp=[]
    return animalSum

def returnMean(animalSum,format_1):
    animalMean = {}
    for animal in animalSum:
        animalMean[animal] = {'mean': animalSum[animal]['sum']/animalSum[animal]['num']}

    for animal in animalMean:
        print(animal,'sum:',animalSum[animal]['sum'],'mean:',round(animalMean[animal]['mean'],1))

    #e printing in format
    for animal in format_1:
        print(animal,'age: ',format_1[animal]['biggest_age'], 'index: ',format_1[animal]['num'])
"""function that runs the program
-------------------------------------------------------------------------------
 * calls the other functions in order
"""
def run():
    animalOne = input('enter animal name: ')
    animalTwo = input('enter animal name: ')
    animalThree = input('enter animal name: ')
    animals = {animalOne: randomAges(),animalTwo: randomAges(),animalThree: randomAges()}

    sortandprint(animals)
    
    returnMean(returnSum(animals),sortanimalAge(animals))

    print(addORremoveAnimal(animals))

    sortandprint(animals)  

    resetanimalage(animals)

    sortandprint(animals)

    returnMean(returnSum(animals),sortanimalAge(animals))

"""function that reruns the program
-------------------------------------------------------------------------------
 * calls the run function if the user enters yes
"""
def rerun():
    global animals
    a = input('would you like to rerun the program?(yes/no): ')
    if a == 'yes':
        run()
    elif a == 'no':
        print('exiting')
        sys.exit()
    else:
        print('type yes or no')
        rerun()
run()
rerun()
