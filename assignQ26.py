my_string = input("Enter a string: ")
prefix = input("Enter prefix to check (press Enter to skip): ")
suffix = input("Enter suffix to check (press Enter to skip): ")
if prefix and my_string.startswith(prefix):
    print(f"The string '{my_string}' starts with '{prefix}'")
if suffix and my_string.endswith(suffix):
    print(f"The string '{my_string}' ends with '{suffix}'")
