import pandas as pd
import numpy as np
import random

# Set the random seed for reproducibility
np.random.seed(42)

# Expanded list of Nigerian first names
male_names = ['Ayodeji', 'Adeola', 'Tunde', 'Musa', 'Ibrahim', 'Babatunde', "Abdullahi", "Femi", "Tobi", "Emmanuel", "David", "Isreal", "Moses",
              "Donald", "Solomon", "Ridwan", "Clinton", "Daniel", "Joseph", "Divine", "Yusuf", 'Daniel', 'Divine', "Fawaz", 'Michael', 'Samson']
female_names = ['Aminat', 'Oluwaseyi', 'Kemi',  'Halima', 'Fatima', 'Bukola', "Zainab", "Oluchi", "Deborah", "Faith", "Goodness",
               "Charity", "Toyibat", "Boluwatife", "Comfort", "Cleopatra", "Dara", "Cyllia", 'Oreoluwa']

# List of Nigerian surnames
surnames = [
    "Abadaki", "Abagun", "Abaribe", "Abdullahi", "Adarabioyo", "Adebutu", "Adedeji", "Adedibu", "Adefope", "Adefuye", "Adegbenro",
    "Adejuyigbe", "Adekugbe", "Adeniran", "Aderemi", "Adesokan", "Adetiba", "Adewumi", "Adewusi", "Agbetu", "Ajudua", "Akanbi",
    "Akinde", "Akindele", "Akinjo", "Akinkugbe", "Akpabio", "Akraka", "Aladefa", "Aladesanmi", "Alagbe", "Aliyu", "Ameobi", 
    "Anjorin", "Anyiam", "Aremu", "Atanda", "Ayanbadejo", "Ayorinde", "Babayaro", "Bakare", "Balarabe", "Bamigboye", "Buraimoh",
    "Chukwumerije", "Daramola", "Deniran", "Dosunmu", "Durosinmi", "Eniola", "Enyinnaya", "Fakeye", "Fatai", "Folayan", "Fuwape", 
    "Gwacham", "Gwarzo", "Ibekwe", "Idahor", "Idahosa", "Idiata", "Idonije", "Igbinoghene", "Ihemeje", "Imeh", "Kolade", "Madueke", 
    "Maikori", "Makinde", "Monye", "Odita", "Odunbaku", "Odutola", "Ofoedu", "Ogbodo", "Ogunkoya", "Ogunsola", "Ojulari", 
    "Okoduwa", "Okojie", "Okoronkwo", "Okposo", "Olaoye", "Olatunji", "Olukoya", "Olusola", "Omolade", "Onyeama", "Onyegbule", 
    "Oseni", "Otedola", "Oteh", "Owoh", "Oyeleye", "Shoyinka", "Tanimowo", "Ubosi", "Udechukwu", "Udoka", "Ujah", "Ukeje", 
    "Uloko", "Uwazuruike", "Yesufu"
]

# Guardian relationship types
guardian_types = ['Parent', 'Grandparent', 'Aunt/Uncle', 'Sibling']

# Occupations lists based on student performance categories
high_performance_occupations = ['Doctor', 'Engineer', 'Lawyer', 'Lecturer', 'Banker']
medium_performance_occupations = ['Teacher', 'Civil Servant', 'Small Business Owner', 'Technician']
low_performance_occupations = ['Farmer', 'Trader', 'Unemployed', 'Artisan']

# Load the academic performance data (to get performance summary)
academic_performance_df = pd.read_csv('academic_performance.csv')

# Classify students by performance category
academic_performance_df['Performance Category'] = pd.cut(
    academic_performance_df['Average Grade (100%)'],
    bins=[0, 50, 70, 100],
    labels=['Low Performer', 'Medium Performer', 'High Performer']
)

# Group by Student ID to summarize performance category (most common performance category)
student_performance_summary = academic_performance_df.groupby('Student ID')['Performance Category'].apply(lambda x: x.mode()[0])

# Function to generate personalized student data
def generate_personal_data(student_performance_summary):
    personal_data = []

    for student_id, performance_category in student_performance_summary.items():
        # Assign names based on gender
        gender = np.random.choice(['Male', 'Female'])
        first_name = random.choice(male_names) if gender == 'Male' else random.choice(female_names)
        surname = random.choice(surnames)
        full_name = f"{first_name} {surname}"

        # Guardian involvement based on performance category
        if performance_category == 'High Performer':
            guardian_involvement = 'Daily'
            guardian_type = np.random.choice(guardian_types[:2])  # More likely to have parents/grandparents
            occupation = np.random.choice(high_performance_occupations)
        elif performance_category == 'Medium Performer':
            guardian_involvement = np.random.choice(['Daily', 'Weekly', 'Bi-Weekly'])
            guardian_type = np.random.choice(guardian_types)
            occupation = np.random.choice(medium_performance_occupations)
        else:  # Low Performer
            guardian_involvement = np.random.choice(['Weekly', 'Bi-Weekly', 'Rarely'])
            guardian_type = np.random.choice(guardian_types)
            occupation = np.random.choice(low_performance_occupations)

        # Append the generated data
        personal_data.append({
            'Student ID': student_id,
            'Full Name': full_name,
            'Gender': gender,
            'Guardian Type': guardian_type,
            'Guardian Check-In Frequency': guardian_involvement,
            'Guardian Occupation': occupation
        })

    return pd.DataFrame(personal_data)

# Generate the personal data
personal_data_df = generate_personal_data(student_performance_summary)

# Save the personal data to a CSV file
personal_data_df.to_csv('personal_data.csv', index=False)

