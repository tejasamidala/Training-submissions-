import os

def list_files_recursive(path, indent=0):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            print("  " * indent + "- " + item)
            if os.path.isdir(full_path):
                list_files_recursive(full_path, indent + 1)
    except Exception as e:
        print("Error:", e)

folder_path = input("📂 Enter the folder path to scan: ")
print(f"\nScanning contents of: {folder_path}\n")
list_files_recursive(folder_path)