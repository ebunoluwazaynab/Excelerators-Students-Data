import pandas as pd
import numpy as np

# Set the current year
current_year = 2024
np.random.seed(42)

# Define age ranges for each sub-level
age_ranges = {
    'JSS1': (9, 11),
    'JSS2': (10, 12),
    'JSS3': (11, 13),
    'SS1': (14, 15),
    'SS2': (15, 16),
    'SS3': (16, 17)
}

# Define extracurricular activities with assigned Activity IDs (including all 14 activities)
activities = {
    'Male': {
        1: 'Football',
        2: 'Basketball',
        3: 'Chess',
        4: 'Robotics',
        5: 'Athletics'
    },
    'Female': {
        6: 'Dance',
        7: 'Debate',
        8: 'Drama',
        9: 'Volleyball',
        10: 'Arts & Crafts'
    },
    'Academic': {
        11: 'Math Club',
        12: 'Science Club',
        13: 'Debate Club',
        14: 'Literary Society'
    }
}

# Function to generate a random Nigerian phone number
def generate_phone_number():
    prefix = np.random.choice(['080', '081', '070', '090'])
    suffix = ''.join([str(np.random.randint(0, 10)) for _ in range(8)])
    return prefix + suffix

# Assign specific class levels based on general level (Junior, Art, Science, Commercial)
def assign_specific_class_level(class_level):
    if class_level == 'Junior':
        return np.random.choice(['JSS1', 'JSS2', 'JSS3'])
    else:
        return np.random.choice(['SS1', 'SS2', 'SS3'])

# Generate birth year and enrollment date based on specific class level
def generate_student_info(specific_class_level):
    min_age, max_age = age_ranges[specific_class_level]
    age = np.random.randint(min_age, max_age + 1)
    birth_year = current_year - age

    # Enrollment date based on class level and age progression
    if 'JSS' in specific_class_level:
        enrollment_year = current_year - (13 - age)  # Junior
    else:
        enrollment_year = current_year - (17 - age)  # Senior

    return birth_year, enrollment_year

# Split full name into first and last names
def split_name(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1] if len(names) > 1 else ""
    return first_name, last_name

# Assign an activity ID based on gender, with some outliers
def assign_activity_id(gender):
    # 5% chance to assign a non-typical activity for gender (e.g., males doing Dance or females doing Football)
    if np.random.rand() < 0.05:
        # Outliers: assign an activity from the opposite gender's activities
        if gender == 'Male':
            return np.random.choice(list(activities['Female'].keys()))  # Male does female activity
        else:
            return np.random.choice(list(activities['Male'].keys()))  # Female does male activity
    else:
        # Otherwise, assign an activity typical for the gender
        if gender == 'Male':
            return np.random.choice(list(activities['Male'].keys()))  # Male activity
        else:
            return np.random.choice(list(activities['Female'].keys()))  # Female activity

# Generate the student table with specific class levels and Activity IDs
def create_student_table(academic_df, personal_df):
    # Deduplicate the academic_df to get unique students
    unique_students_df = academic_df.drop_duplicates(subset=['Student ID'])

    student_table = []

    for index, row in unique_students_df.iterrows():
        student_id = row['Student ID']
        general_class_level = row['Class Level']  # General class level (Junior, Art, Science, Commercial)

        # Assign specific class level
        specific_class_level = assign_specific_class_level(general_class_level)

        # Extract full name and split
        full_name = personal_df.loc[personal_df['Student ID'] == student_id, 'Full Name'].values[0]
        first_name, last_name = split_name(full_name)

        # Extract gender
        gender = personal_df.loc[personal_df['Student ID'] == student_id, 'Gender'].values[0]

        # Generate birth year and enrollment date based on specific class level
        birth_year, enrollment_year = generate_student_info(specific_class_level)

        # Extract guardian details
        guardian_type = personal_df.loc[personal_df['Student ID'] == student_id, 'Guardian Type'].values[0]
        guardian_occupation = personal_df.loc[personal_df['Student ID'] == student_id, 'Guardian Occupation'].values[0]
        guardian_checkin = personal_df.loc[personal_df['Student ID'] == student_id, 'Guardian Check-In Frequency'].values[0]

        # Generate a random guardian phone number
        guardian_contact = generate_phone_number()

        # Assign Activity ID based on gender (with potential for outliers)
        activity_id = assign_activity_id(gender)

        # Create a dictionary for each student
        student_dict = {
            'Student ID': student_id,
            'First Name': first_name,
            'Last Name': last_name,
            'Full Name': full_name,
            'Gender': gender,
            'General Class Level': general_class_level,  # Junior, Art, Science, Commercial
            'Specific Class Level': specific_class_level,  # JSS1, JSS2, JSS3, SS1, SS2, SS3
            'Birth Year': birth_year,
            'Enrollment Year': enrollment_year,
            'Guardian Type': guardian_type,
            'Guardian Occupation': guardian_occupation,
            'Guardian Check-in Frequency': guardian_checkin,
            'Guardian Contact': guardian_contact,
            'Activity ID': activity_id  # Store Activity ID, with possibility for outliers
        }

        # Append the student data to the student_table list
        student_table.append(student_dict)

    return pd.DataFrame(student_table)

# Create the student table
student_table_df = create_student_table(academic_performance_fixed_df, personal_data_df)

# Save the student table to CSV file if needed
student_table_df.to_csv('student_table.csv', index=False)

