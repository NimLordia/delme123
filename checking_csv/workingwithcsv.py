import pandas as pd

FILE_NAME = 'carslist.csv'

df = pd.read_csv(FILE_NAME)

print(df.head(0))
user_selection = input("Choose column to work on ")
column_to_check = df[user_selection]
column_to_check = column_to_check.sort_values().tolist()
# print(column_to_check)
target = input("Choose your required value ")
left = 0
right = len(column_to_check) -1 
ind = (left + right) // 2
count = 0

# 

while True:
    if int(column_to_check[ind]) == int(target):
        count += 1 
        print(f"Found the target at {ind} after {count} iterations")
        break
    elif int(column_to_check[ind]) > int(target):
        right = ind
        ind = (left+right) //2
        count += 1 
    elif int(column_to_check[ind]) < int(target):
        left = ind
        ind = (left+right) //2
        count += 1
