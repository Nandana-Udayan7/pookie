
file_name = input("Enter the file name: ")

# Find the extension
if '.' in file_name:
    extension = file_name.split('.')[-1]
    print("The file extension is:", extension)
else:
    print("No extension found in the file name.")
