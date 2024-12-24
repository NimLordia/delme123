import os
import platform
from enum import Enum
import json
import pandas as pd

class Actions(Enum):
    EXIT = 1 
    ADD = 2
    DISPLAY = 3
    DELETE = 4
    FIND = 5
    DEL_ALL = 6

cars = []
FILE_NAME = 'cars.json'

def save_cars_to_file():
    """
    Save the `cars` list to a JSON file, adding an index to each car.
    """
    for i, car in enumerate(cars):
        car["index"] = i  # Add or update the index field
    
    with open(FILE_NAME, 'w') as f:
        json.dump(cars, f, indent=4)  # Save to file in JSON format
        print("File written successfully")

def read_cars_from_file():
    """
    Read the `cars` list from a JSON file.
    """
    global cars
    try:
        with open(FILE_NAME, 'r') as f:
            cars = json.load(f)  # Load JSON data from file into the `cars` list
            
    except FileNotFoundError:
        print("The file does not exist.")
    except json.JSONDecodeError:
        print("The file is not in a valid JSON format.")

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

def print_all_cars():
    """
    Print all cars in the `cars` list, including their index.
    """
    for car in cars:
        print(f"{car['index']}: Make: {car['make']}, Brand: {car['brand']}, Model: {car['model']}, Color: {car['color']}")

def add_car():
    """
    Add a new car to the `cars` list and save it to the file.
    """
    cars.append({
        "make": input("Car make? "),
        "brand": input("Car brand? "),
        "model": input("Car model? "),
        "color": input("Car color? ")
    })
    save_cars_to_file()

def delete_car():
    """
    Delete a car by its index from the `cars` list.
    """
    try:
        print_all_cars()
        index_to_delete = int(input("Enter the index of the car to delete: "))
        global cars
        cars = [car for car in cars if car["index"] != index_to_delete]
        save_cars_to_file()
        print(f"Car at index {index_to_delete} deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def find_car():
    print("Which make are you looking for?")
    cars_make = set()
    for car in cars:
        cars_make.add(car["make"])
    print(f"These are the makes available: {cars_make}")
    car_make = input("Enter your make ")
    for car in cars:
        if car["make"] == car_make:
            print (car)
    car_index = input("Choose specific car index: ")
    for car in cars:
        if car["index"] == int(car_index):
            print(car)                

if __name__ == "__main__":
    read_cars_from_file()
    while True:
        try:
            user_selection = Actions(int(menu()))
            clear_terminal()
            
            if user_selection == Actions.EXIT:
                print("Exiting")
                exit()
            elif user_selection == Actions.ADD:
                add_car()
            elif user_selection == Actions.DISPLAY:
                print_all_cars()
            elif user_selection == Actions.DELETE:
                delete_car()
            elif user_selection == Actions.FIND:
                find_car()                    
            elif user_selection == Actions.DEL_ALL:
                cars.clear()
                save_cars_to_file()
                print("All cars deleted.")
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Please enter a valid number.")
