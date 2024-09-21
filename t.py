import re

def filter_uids(file_path, names_to_filter):
    # Read input data from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        uid_data = file.read()

    # Split the input data into lines (assuming each UID is on a new line)
    uid_list = uid_data.strip().split('\n')

    # Compile a regular expression pattern for exact name matching
    name_pattern = r'\b(?:' + '|'.join(re.escape(name) for name in names_to_filter) + r')\b'

    # Filter UIDs that match the exact names from the provided list
    filtered_uids = [uid for uid in uid_list if re.search(name_pattern, uid)]

    # Return the filtered UIDs
    return filtered_uids

# Specify the file path and names to filter
file_path = '/sdcard/2.txt'  # Replace with the actual path to your file
names_to_filter = ["Md", "Md.", "Abdul", "Akhtar", "Ali", "Amin", "Anis", "Asif", "Aziz", "Bashir", 
                   "Bilal", "Faisal", "Farhan", "Habib", "Hassan", "Hossain", "Imran", "Iqbal", 
                   "Jamil", "Kamal", "Karim", "Khan", "Mahmud", "Moin", "Monir", "Nasir", 
                   "Nawaz", "Rahim", "Rashid", "Rehman"]

# Get the filtered UIDs
filtered_uids = filter_uids(file_path, names_to_filter)

# Print the filtered UIDs (or save them to a file as needed)
for uid in filtered_uids:
    print(uid)
