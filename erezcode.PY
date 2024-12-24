import pandas as pd
from enum import Enum


class Options(Enum):
    NAMES = 1
    AGES = 2
    IDS = 3
    STATUSES = 4
    EXIT = 5


def printMenu():
    for option in Options:
        print(f"{option.value} - {option.name}")


def searchItem(list_to_search, item_to_search, collumName):
   try:
    if item_to_search.isdigit():
           
            item_to_search = int(item_to_search)
            print(f"Searching {list_to_search[item_to_search]}...")
            count = df[df[collumName] == list_to_search[item_to_search]].shape[0]
            print(f"Found: {count}")


            filtered = df[df[collumName] == list_to_search[item_to_search]]
            print(filtered)
    else:
        print("Invalid input")
   except ValueError:
      print("Invalid input")
   except IndexError:
      print("Out of range!")
     
df = pd.read_json('people_data.txt')




if __name__ == "__main__":
    ids = list(df['id'].unique())
    names = list(df['name'].unique())
    ages = list(df['age'].unique())
    statuses = list(df['status'].unique())


    while True:
        printMenu()
        user_selection = input("select an option: ")
        if user_selection.isdigit():


            user_selection = Options(int(user_selection))
            if user_selection == Options.NAMES:
                for index, i in enumerate(names):
                    print(f"{index}:  Name - {i}")


                nameToFind = (input("Select a name to find (by index): "))
                searchItem(names, nameToFind, 'name')


            elif user_selection == Options.AGES:
                    for index, i in enumerate(ages):
                     print(f"{index}: Age - {i}")


                    ageToFind = int(input("Select an Age to find (by index): "))
                    searchItem(ages, ageToFind, 'age')
                    ageToFind = (ages[ageToFind])
                    filteredAges = df[df['age'] == ageToFind]
                    print(filteredAges)
           
            elif user_selection == Options.IDS:
                    for index, i in enumerate(ids):
                     print(f"{index}: ID - {i}")


                    idToFind = int(input("Select an ID to find (by index): "))
                    searchItem(ids, idToFind, 'id')


            elif user_selection == Options.STATUSES:
                    for index, i in enumerate(statuses):
                     print(f"{index}: Status - {i}")


                    statusToFind = (input("Select a status to find (by index): "))
                    searchItem(statuses, statusToFind, 'status')


            elif user_selection == Options.EXIT:
                    exit()
           
        else:
            print("Invalid")





