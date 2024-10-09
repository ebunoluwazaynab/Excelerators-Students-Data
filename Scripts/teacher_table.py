import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Nigerian surnames list provided
nigerian_surnames = [
    "Abara", "Abdullah", "Abiola", "Abimbola", "Abubakar", "Adebayo", "Abdullahi",
    "Adesina", "Aguta", "Aku", "Bolaji", "Balogun", "Babangida", "Bello",
    "Bankole", "Baba", "Bennet", "Bassey", "Chris", "Chukwu", "Dambe", "Danjuma",
    "Dauda", "Ejiofor", "Etienam", "Eesuola", "Egbe", "Emem", "Eze", "Falade",
    "Folorunsho", "Gbadamosi", "Guh", "Hassan", "Ibeh", "Igwe", "Igbinedion",
    "Ihejirika", "Ikande", "Ibrahim", "Iwuchukwu", "Jacob", "Jimoh", "Konkwo",
    "Kalu", "Kikelomo", "Kazah", "Kanye", "Kporaro", "Kolawole", "Lawal",
    "Musa", "Mohammed", "Mmeremikwu", "Mustapha", "Matins", "Manuel", "Njoku",
    "Nnadi", "Nwadike", "Nwaeze", "Nwaigbo", "Nnachi", "Nwabili", "Okoro",
    "Onyema", "Obianagha", "Okpara", "Okusanya", "Oladoyinbo", "Okon", "Ojo",
    "Okeke", "Owayale", "Odoemene", "Popoola", "Peter", "Prest", "Rabiu",
    "Rafiu", "Razzaq", "Raheem", "Sanusi", "Sami", "Sulaimom", "Samuel",
    "Tyjani", "Tersoo", "Taiwo", "Ugochukwu", "Uba", "Uthman", "Unigwe",
    "Ukpabi", "Uche", "Umaru", "Umunna", "Uchenna", "Yakubu", "Yusuf",
    "Adeoye", "Adeyemi", "Agbani", "Akerele", "Akpabio", "Alana", "Alaneme",
    "Ali", "Amaechi", "Anenih", "Asaju", "Attah", "Chidubem", "Nwaike",
    "Obi", "Obiaka", "Obiakaeze", "Obiakpani", "Okoturo", "Olanrewaju",
    "Olowe", "Oni", "Onyilogwu", "Osondu", "Oyinlola", "Shehu", "Uchce",
    "Umeh", "Uzoegbu", "Zabu", "Agrinya", "Akinjide", "Bosede", "Orelias",
    "Otueome"
]

# List of subjects (flattening all categories)
junior_subjects = [
    'Mathematics', 'English Language', 'Basic Science', 'Social Studies', 'Fine Arts',
    'Agricultural Science', 'Civic Education', 'Health Education', 'Business Studies',
    'French', 'Computer Studies', 'Home Economics', 'Music', 'Basic Technology']

science_subjects = [
    'Physics', 'Chemistry', 'Biology', 'Mathematics', 'English Language',
    'Animal Husbandry', 'Data Processing', 'Computer Science',
    'Agricultural Science', 'Civic Education', 'Geography', 'Economics',
    'Further Mathematics']

commercial_subjects = [
    'Accounting', 'Commerce', 'Economics', 'Geography', 'Government',
    'Agricultural Science', 'Biology',
    'English Language', 'Mathematics', 'Further Mathematics', 'Civic Education']

art_subjects = [
    'Literature-in-English', 'Government',
    'Biology', 'French', 'Economics',
    'Mathematics', 'English Language', 'Further Mathematics',
    'Civic Education', 'Data Processing', 'Animal Husbandry']

all_subjects = junior_subjects + science_subjects + commercial_subjects + art_subjects

# Function to generate a random phone number
def generate_teacher_phone():
    prefix = np.random.choice(['080', '081', '070', '090'])
    suffix = ''.join([str(np.random.randint(0, 10)) for _ in range(8)])
    return prefix + suffix

# Function to generate a random hire date within the last 10 years
def generate_hire_date():
    start_date = datetime.now() - timedelta(days=365*10)  # 10 years ago
    random_days = np.random.randint(0, 365*10)
    hire_date = start_date + timedelta(days=random_days)
    return hire_date.date()

# Function to assign gender and format name based on Mr./Mrs. convention
def assign_teacher_name():
    surname = np.random.choice(nigerian_surnames)
    gender = np.random.choice(['Male', 'Female'])

    if gender == 'Male':
        name = f"Mr. {surname}"
    else:
        name = f"Mrs. {surname}"

    return name, gender

# Create the Teacher Table
def create_teacher_table(num_teachers, subject_list, teacher_ids):
    teacher_table = []

    for i in range(num_teachers):
        teacher_id = teacher_ids[i]  # Ensure consistency with the existing teacher_id

        # Randomly assign a subject
        subject = np.random.choice(subject_list)

        # Assign teacher name and gender
        name, gender = assign_teacher_name()

        # Generate random contact info and hire date
        contact_info = generate_teacher_phone()
        hire_date = generate_hire_date()

        # Create a dictionary for the teacher
        teacher_dict = {
            'teacher_id': teacher_id,
            'full_name': name,
            'gender': gender,
            'subject_name': subject,  # In the actual system, subject_id would be FK, but we use subject names here
            'contact_info': contact_info,
            'hire_date': hire_date
        }

        # Append the teacher data to the teacher_table list
        teacher_table.append(teacher_dict)

    return pd.DataFrame(teacher_table)

# Assuming you have teacher IDs already existing
existing_teacher_ids = np.arange(1, 15)  # Replace this with actual teacher IDs

# Generate teacher data for the subjects
teacher_table_df = create_teacher_table(len(existing_teacher_ids), all_subjects, existing_teacher_ids)

# Save the teacher table to CSV file if needed
teacher_table_df.to_csv('teacher_table.csv', index=False)

