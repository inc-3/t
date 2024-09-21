import re

def filter_uids(file_path, names_to_filter):
    # Read input data from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        uid_data = file.read()

    # Split the input data into lines
    uid_list = uid_data.strip().split('\n')

    # Compile a regular expression pattern for matching names
    name_pattern = r'\b(' + '|'.join(re.escape(name) for name in names_to_filter) + r')\b'

    # Filter UIDs that match the exact name pattern
    filtered_uids = [uid for uid in uid_list if re.search(name_pattern, uid)]

    # Return the filtered UIDs
    return filtered_uids

# Specify the file path and names to filter
file_path = '/sdcard/2.txt'  # Replace with the path to your input file
names_to_filter = ["Md", "Md.", "Abdul", "Akhtar", "Ali", "Amin", "Anis", "Asif", "Aziz", "Bashir", "Bilal",
        "Faisal", "Farhan", "Habib", "Hassan", "Hossain", "Imran", "Iqbal", "Jamil", "Kamal", "Karim", 
    "Khan", "Mahmud", "Moin", "Monir", "Nasir", "Nawaz", "Rahim", "Rashid", "Rehman", "Salim", 
    "Sami", "Shahid", "Sharif", "Tariq", "Yasin", "Zaman", "Salman", "Wajid", "Sk", "Rahman", 
    "Hasan", "Jahan", "Parvez", "Shakil", "Shahin", "Sohel", "Tarek", "Sajjad", "Raju", "Shamim", 
    "Sumon", "Shahed", "Shakib", "Arif", "Sabbir", "Noman", "Shafi", "Shah", "Shahriar", "Tanvir", 
    "Rafi", "Masud", "Rafiq", "Rakib", "Sobuj", "Shuvo", "Faruk", "Nayeem", "Mehedi", "Munna", 
    "Anwar", "Kabir", "Shuvo", "Rajib", "Sohag", "Sajib", "Rony", "Sakib", "Shahjalal", "Nasim", 
    "Sakil", "Shuvojit", "Sujon", "Ashik", "Shafiq", "Mahfuz", "Habibullah", "Rasel", "Mizan", 
    "Monir", "Mithun", "Mamun", "Shanto", "Mehrab", "Rubel", "Sumon", "Sabbir", "Razib", "Khairul", 
    "Rafat", "Arafat", "Mahbub", "Nizam", "Biplab", "Pavel", "Arman", "Bijoy", "Shanto", "Hasib", 
    "Ranjan", "Masum", "Liton", "Shamim", "Nazim", "Tuhin", "Arman", "Forhad", "Sakif", "Jabed", 
    "Shakir", "Rifat", "Rakib", "Muntasir", "Biplob", "Tuhin", "Rabbi", "Rab", "Sourav", "Jony", 
    "Partha", "Pavel", "Sohan", "Ratul", "Rabiul", "Rifat", "Mizanur", "Jahid", "Alamin", "Tanjim", 
    "Mahir", "Sajal", "Rifat", "Ratul", "Sarwar", "Shihab", "Rajon", "Jamil", "Rasel", "Ahsan", 
    "Maruf", "Tanveer", "Sajjad", "Rifat", "Saiful", "Shohel", "Tuhin", "Anik", "Shuvo", "Ridoy", 
    "Arafat", "Saif", "Hasib", "Bipul", "Jewel", "Sakib", "Sahed", "Sujon", "Mehedi", "Rafat", 
    "Sakib", "Shihab", "Shamim", "Siam", "Munim", "Sharif", "Rana", "Shamim", "Rana", "Kawsar", 
    "Mahmud", "Akash", "Rafi", "Mahbub", "Munna", "Rasel", "Mehedi", "Shohel", "Rakib", "Nayeem", 
    "Rakib", "Mehedi", "Arafat", "Kawsar", "Tahsin", "Rasel", "Arif", "Biplob", "Rakib", "Sajjad", 
    "Tanzim", "Tuhin", "Mehedi", "Mehedi", "Hasan", "Rasel", "Rakib", "Shamim", "Munna", "Rony", 
    "Fahim", "Mehedi", "Jewel", "Rafsan", "Munna", "Shamim", "Najim", "Rakib", "Najim", "Sabbir", 
    "Shanto", "Biplob", "Mithun", "Shamim", "Nazim", "Mukul", "Tahsin", "Anisur", "Abdus", 
    "Mohammad", "Kazi", "Abul", "Nur", "Nazmul", "Sohel", "Monjur", "Arifur", "Mostafizur", 
    "Kamrul", "Sazzad", "Aminul", "Rashed", "Mahfuzur", "Monirul", "Shafiqul", "Imtiaz", "Enamul", 
    "Fakrul", "Mahmudul", "Samsul", "Abdur", "Farid", "Mizanur", "Jahirul", "Helal", "Shahidul", 
    "Liton", "Rezaul", "Jashim", "Selim", "Anwar", "Motiur", "Azizul", "Golam", "Habiba", "Hanif", 
    "Ibrahim", "Jamal", "Kabir", "Harun", "Masud", "Mahim", "Jisan", "Jibon", "Shofik", "Mustakim", 
    "Irfan", "Rahmatullah", "Fazlul", "Shamsul", "Afsar", "Mahbubul", "Shafayat", "Shariful", 
    "Iqra", "Anan", "Ishtiaq", "Ahad", "Ehsanul", "Abdullah", "Shabbir", "Liton", "Masum", 
    "Aklas", "Ashraful", "Atiq", "Mohiuddin", "Najmul", "Feroze", "Jaber", "Ashrafuzzaman", 
    "Mahbubur", "Nazib", "Sadiq", "Shahedul", "Imranul", "Muntashir", "Naushad", "Rashidur", "Touhid", 
    "Wali", "Mahfuzul", "Saad", "Azhar", "Naeem", "Shahiduzzaman", "Tazul", "Helaluddin", "Masudul", 
    "Murshed", "Nure Alam", "Nasrul", "Khalid", "Sayeed", "Maswood", "Shamsuzzaman", "Tanzir", 
    "Nahid", "Shaikh", "Rubayet", "Shadman", "Hasnain", "Shams", "Ibadur", "Arafatul", "Humaun", 
    "Akash", "Tarik", "Shuvo", "Arshad", "Bashar", "Junaid", "Khaled", "Mahin", "Nadir", "Wasim", 
    "Zubair", "Nazrul", "Rashedul", "Zakir", "Aftab", "Anwarul", "Asad", "Fazle", "Khorshed", 
    "Lokman", "Ishraq", "Touhidur", "Hassanuzzaman", "Nusratullah", "Tayef", "Tawfiq", "Zahedul", 
    "Shojib", "Abdulahi", "Shawkat", "Sadat", "Zahidur", "Hossainul", "Adnan", "Tarek", "Saeed",
    "Sk", "Amin", "Emran", "Rana", "Riad", "Shagor", "Kawsar", "Anis", "Ashraf", "Akbar", "Alim", 
    "Arif", "Azim", "Bashir", "Babar", "Badrul", "Baki", "Belal", "Bodi", "Bulbul", "Chowdhury", "Daud", "Dulal", 
    "Emon", "Enamul", "Fahim", "Farhad", "Faisal", "Ferdous", "Gafur", "Gazi", "Habib", "Hasib", "Hasan", "Helal", 
    "Hossain", "Ibrahim", "Imran", "Iqbal", "Ismail", "Jahid", "Jalal", "Jamil", "Jasim", "Kabir", "Kamal", "Karim", 
    "Khaled", "Liton", "Mahi", "Mahfuz", "Mamun", "Manik", "Masud", "Mizan", "Mokbul", "Moin", "Monir", "Mostafa", 
    "Mujib", "Murad", "Nafis", "Naim", "Nasim", "Nazmul", "Niaz", "Noman", "Nur", "Parvez", "Rafiqul", "Rakib", 
    "Rashed", "Razib", "Rezaul", "Sohel", "Riaz", "Ripon", "Rubel", "Sabbir", "Sadiq", "Sajid", "Salam", "Sami", 
    "Sanjib", "Shahid", "Shakib", "Shamsul", "Sharif", "Sohag", "Sumon", "Tariq", "Taufiq", "Touhid", "Wahid", 
    "Yasin", "Zahid", "Zahir", "Zakir", "Zaman", "Zia", "Zubair", "Abdul", "Abid", "Adnan", "Afif", "Ahad", "Ahmad", 
    "Ahsan", "Akash", "Ali", "Alim", "Aminul", "Amzad", "Anik", "Anwar", "Arifur", "Asad", "Ashfaq", "Atiq", "Azhar", 
    "Aziz", "Babu", "Badal", "Basir", "Bijoy", "Bilal", "Chanchal", "Delwar", "Dipu", "Ehsan", "Ershad", "Eshan", 
    "Fakhrul", "Faruq", "Fazle", "Golam", "Hafiz", "Hamid", "Haris", "Hasnat", "Hedayet", "Humayun", "Ilias", 
    "Ishtiaq", "Jabed", "Jafor", "Jamshed", "Johirul", "Junaid", "Kamrul", "Kawsar", "Khalil", "Khorshed", "Lalon", 
    "Latif", "Mahmud", "Majid", "Maksud", "Manjur", "Maruf", "Mazhar", "Mehedi", "Milton", "Minhaj", "Miraz", 
    "Mobarak", "Mohsin", "Morshed", "Muazzam", "Mubin", "Mujibur", "Mustafa", "Nadim", "Nahid", "Nasir", "Nazim", 
    "Niloy", "Nizam", "Noor", "Nure", "Obaid", "Omar", "Pavel", "Rahim", "Rakhat", "Rana", "Rasel", "Rifat", "Riyad", 
    "Rokon", "Ruhul", "Sabit", "Saiful", "Sajjad", "Salim", "Sarwar", "Shafiq", "Shahin", "Shakil", "Shamim", 
    "Shanto", "Sheikh", "Sohail", "Subho", "Tanjil", "Tanvir", "Tipu", "Tuhin", "Uzzal", "Wasim", "Younus", "Zafor", 
    "Zahidul", "Zakaria", "Zamal", "Zulfiqar", "Afsar", "Afzal", "Alam", "Amirul", "Ananta", "Anindya", "Ashik", 
    "Ashim", "Ashraful", "Atikur", "Aynal", "Azad", "Babul", "Bahauddin", "Barkat", "Bashar", "Bokul", "Danish", 
    "Ekram", "Fahad", "Faisal", "Farhan", "Farid", "Fayez", "Ferdous", "Gaziul", "Giyas", "Golam", "Harun", 
    "Hasanuzzaman", "Helal", "Himel", "Hiron", "Hossainul", "Hridoy", "Ibrahim", "Iftekhar", "Imtiaz", "Iqbal", 
    "Ishtiaque", "Jalil", "Jewel", "Jibon", "Kamal", "Kamrul", "Kawser", "Kazi", "Khaledur", "Latifur", "Liton", 
    "Lutfar", "Mahadi", "Mahbub", "Mahdi", "Majed", "Manik", "Maruf", "Masraf", "Masum", "Mazharul", "Mehdi", 
    "Milon", "Mizanur", "Mohammad", "Mohibur", "Moinul", "Mokhlesur", "Monowar", "Morsalin", "Mubarak", "Muhaimin", 
    "Mujahid", "Mustafizur", "Nadim", "Nahiyan", "Najmul", "Nayeem", "Nazir", "Nezam", "Nishat", "Niyaz", "Noorul", 
    "Oli", "Omar", "Parvez", "Rabbani", "Rabbi", "Rafique", "Raihan", "Rakibul", "Rashedul", "Reza", "Riazul", 
    "Rokonuzzaman", "Ruhul", "Rumana", "Saad", "Sabbir", "Sabir", "Sadi", "Saiful", "Sajeeb", "Sajidur", "Sajjadur", 
    "Salman", "Samad", "Samir", "Sanjoy", "Sarwar", "Saud", "Sazzad", "Shahidul", "Shahed", "Shahedul", "Shahriar", 
    "Shakibul", "Shamimul", "Shariful", "Shaukat", "Sohail", "Sujan", "Sumon", "Suruj", "Syed", "Tajul", "Tamal", 
    "Tanveer", "Tariqul", "Taufiqur", "Tipu", "Toufique", "Touhidul", "Uzzal", "Wasim", "Yasinul", "Yunus", 
    "Zahirul", "Zakariah", "Zayed", "Ziaul", "Zillur", "Zubayer", "Zulfiqar"]

# Call the function to filter UIDs
filtered_uids = filter_uids(file_path, names_to_filter)

# Print the filtered UIDs
for uid in filtered_uids:
    print(uid)
