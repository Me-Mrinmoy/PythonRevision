import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files and directories in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

def create_file(directory, filename):
    try:
        with open(os.path.join(directory, filename), 'w') as file:
            file.write('')
        print(f"File '{filename}' created successfully.")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

def create_directory(directory, dirname):
    try:
        os.makedirs(os.path.join(directory, dirname))
        print(f"Directory '{dirname}' created successfully.")
    except FileExistsError:
        print("Directory already exists.")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

def delete_file(directory, filename):
    try:
        os.remove(os.path.join(directory, filename))
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def delete_directory(directory, dirname):
    try:
        os.rmdir(os.path.join(directory, dirname))
        print(f"Directory '{dirname}' deleted successfully.")
    except FileNotFoundError:
        print("Directory not found.")
    except OSError:
        print("Directory is not empty.")
    except PermissionError:
        print("Permission denied.")

def rename_file_or_directory(directory, old_name, new_name):
    try:
        os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
        print(f"'{old_name}' renamed to '{new_name}'.")
    except FileNotFoundError:
        print("File or directory not found.")
    except PermissionError:
        print("Permission denied.")

def main():
    while True:
        print("\nFile Manager")
        print("1. List files and directories")
        print("2. Create file")
        print("3. Create directory")
        print("4. Delete file")
        print("5. Delete directory")
        print("6. Rename file or directory")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '7':
            break
        
        directory = input("Enter the directory path: ")
        
        if choice == '1':
            list_files(directory)
        elif choice == '2':
            filename = input("Enter the filename to create: ")
            create_file(directory, filename)
        elif choice == '3':
            dirname = input("Enter the directory name to create: ")
            create_directory(directory, dirname)
        elif choice == '4':
            filename = input("Enter the filename to delete: ")
            delete_file(directory, filename)
        elif choice == '5':
            dirname = input("Enter the directory name to delete: ")
            delete_directory(directory, dirname)
        elif choice == '6':
            old_name = input("Enter the old name: ")
            new_name = input("Enter the new name: ")
            rename_file_or_directory(directory, old_name, new_name)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
