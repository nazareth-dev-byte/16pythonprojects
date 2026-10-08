
"""import os

file_path = "C:/Users/DELL/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The location '{file_path}' does not exist")
import csv

How to write an output files using python

import JSON

employees = ["Eugene", "SquidWard", "SpongeBob","Patrick"]
employees = {"name":"SpongeBob",
             "age": "30",
             "job": "cook"}

employees = [["Name", "Age", "Job"],
             ["SpongeBob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"],
             ]

try:
    txt_data = "I like orange "
    file_path = "C:/Users/DELL/Desktop/NewOutput.csv"

    with open(file=file_path, mode="w", newline = "")as file:
        a is for append,x is to write the file when the file doesn't exist, r is to read the file
        file.write("\n" + txt_data)
        for employee in employees:
            file.write(employee + " ")
        json.dump(employees, file, indent=4)
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        The dump method, will convert our dictionary to json string to output it
        print(f"csv file '{file_path}' was written/created'")
except PermissionError:
    print("You are not permitted to create a file here.")
except FileExistsError:
    print("The file already exists.")
except AttributeError:
    print("The file doesn't exist.")

    #Here, we'll be outputting a JSON file. A JSON file consists of key value pairs.

values = employees.values()
for value in employees.values():
    print(value)

so that is all about writing files using python."""


#Now we're gonna abe reading files using python

import csv

file_path = "C:/Users/DELL/Desktop/NewOutput.csv"

try:
    with open(file = file_path, mode="r", ) as file:
        #content = file.read()
        #content = json.load(file)
        content = csv.reader(file)
        #In our json file, to access our value data given a key,
        #print(content["job"])
        for row in content:
            print(row)
        #print(content)

except FileNotFoundError:
    print("The file doesn't exist.")
except PermissionError:
    print("You are not permitted to read this file.")