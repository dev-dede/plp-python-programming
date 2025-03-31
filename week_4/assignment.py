try:
    filename = input("Please input the name of the file you want to open and read, remember to add the extension ")

    with open(filename, "r") as file:
        data = file.read()
        modified_data = data.upper() # Modify content (e.g., convert to uppercase)

    new_filename = "modified_" + filename #Create a varible that stores the filename

    with open(new_filename, "w") as new_file:
        new_file.write(modified_data) #Write modified version of original file into another file created
    print(f"Modified file saved as '{new_filename}'")


except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
        print("Error: Permission denied. You may not have access to this file.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")