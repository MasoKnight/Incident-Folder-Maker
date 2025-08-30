import os

def clean_path(input_path):
    """
    Removes any surrounding quotation marks from the input path.

    :param input_path: The file path as entered by the user.
    :return: The cleaned file path.
    """
    return input_path.strip().strip("'").strip('"')

def create_labeled_folders(base_path, folder_names):
    """
    Creates labeled folders in the specified base path.

    :param base_path: The path where folders should be created.
    :param folder_names: A list of folder names to create.
    """
    try:
        if not os.path.exists(base_path):
            print(f"Base path '{base_path}' does not exist. Creating it.")
            os.makedirs(base_path)
        
        for folder_name in folder_names:
            folder_path = os.path.join(base_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created folder: {folder_path}")
            else:
                print(f"Folder already exists: {folder_path}")

        print("All folders created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    raw_base_path = input("Enter the base path where folders should be created: ")
    base_path = clean_path(raw_base_path)

    folder_names = [
        "Screenshots",
        "Message Trace",
        "Sign In Logs",
        "Audit Logs"
    ]
    create_labeled_folders(base_path, folder_names)
