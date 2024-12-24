import os
import platform
from enum import Enum
import json
import pandas as pd
import json


class Actions(Enum):
    EXIT = 1 
    ADD = 2
    DISPLAY = 3
    DELETE = 4
    FIND = 5
    DEL_ALL = 6
    REACTIVATE = 7

people = []    
file_name = 'people_data.txt'

def add_person():
    global people
    people.append({
        "name":input("Enter the name "),
        "age":input("Enter the age "),    
        "status":"active"})
    enumerate(people)
    save_people_to_file()

def display():
    for pep in people:
        if pep["status"] == "active":
            print(f"Name: {pep['name']}, Age: {pep['age']}, ID: {pep['id']}, Status {pep['status']}")


def delete_person():
    display()
    pep_to_delete = int(input('Choose the ID of the person to delete: '))
    global people
    for pep in people:
        if pep["id"] == pep_to_delete:
            pep["status"] = "inactive"
    save_people_to_file()

def find_person():
    pass

def delete_all():
    people = []
    save_people_to_file()

def save_people_to_file():
    global people
    for i, pep in enumerate(people):
        pep["id"] = i
    with open(file_name, 'w') as f:
        json.dump(people, f, indent= 4)
        print("File saved")

def load_people_from_file():
    global people
    try:
        with open(file_name, 'r') as f:
            people = json.load(f)
    except json.JSONDecodeError:
        print("The file does not exist")

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("These are the actions available, choose the number: ")
    for act in Actions:
        print(f"{act.value} - {act.name}")
    return input("Your selection? ")

def reactivate_person():
    global people
    for pep in people:
        if pep['status'] == 'inactive':
            print(pep)
    pep_to_reactivate = int(input("Choose the ID of the person to reactivate "))
    for pep in people:
        if pep['id'] == pep_to_reactivate:
            pep['status'] = 'active'
            print(f'Reactivated {pep}')


if __name__ == "__main__":
    load_people_from_file()
    while True:
        try:
            user_selection =  Actions (int(menu()))
            clear_terminal()

            if user_selection == Actions.EXIT:
                exit()
            elif user_selection ==Actions.ADD:
                add_person()
            elif user_selection == Actions.DEL_ALL:
                delete_all()
            elif user_selection == Actions.DELETE:
                delete_person()
            elif user_selection == Actions.DISPLAY:
                display()
            elif user_selection == Actions.FIND:
                find_person()
            elif user_selection == Actions.REACTIVATE:
                reactivate_person()
            else:
                clear_terminal()
                print("Enter a valid number ")
        except ValueError:
            print("Please enter a valid number ")