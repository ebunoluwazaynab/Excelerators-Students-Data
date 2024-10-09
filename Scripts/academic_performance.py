import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Define function to generate academic performance data
def generate_academic_performance_data_fixed(num_junior=400, num_senior=600, num_subjects=9):
    # Subject lists
    junior_subjects = [
        'Mathematics', 'English Language', 'Basic Science', 'Social Studies', 
        'Fine Arts', 'Agricultural Science', 'Civic Education', 'Health Education', 
        'Business Studies', 'French', 'Computer Studies', 'Home Economics', 
        'Music', 'Basic Technology'
    ]
    
    science_subjects = [
        'Physics', 'Chemistry', 'Biology', 'Mathematics', 'English Language', 
        'Animal Husbandry', 'Data Processing', 'Computer Science', 
        'Agricultural Science', 'Civic Education', 'Geography', 'Economics', 
        'Further Mathematics'
    ]
    
    commercial_subjects = [
        'Accounting', 'Commerce', 'Economics', 'Geography', 'Government', 
        'Agricultural Science', 'Biology', 'English Language', 'Mathematics', 
        'Further Mathematics', 'Civic Education'
    ]
    
    art_subjects = [
        'Literature-in-English', 'Government', 'Biology', 'French', 'Economics', 
        'Mathematics', 'English Language', 'Further Mathematics', 
        'Civic Education', 'Data Processing', 'Animal Husbandry'
    ]

    # Generate zero-padded student IDs
    junior_student_ids = [f"{i:04d}" for i in range(1, num_junior + 1)]
    senior_student_ids = [f"{i:04d}" for i in range(num_junior + 1, num_junior + num_senior + 1)]
    student_ids = np.concatenate([junior_student_ids, senior_student_ids])

    class_levels = []
    genders = []
    subjects = []
    first_test_scores = []
    second_test_scores = []
    final_exam_scores = []
    average_scores = []

    # Helper function to generate gender-specific scores based on subject
    math_courses = ['Mathematics', 'Physics', 'Further Mathematics', 'Chemistry', 'Economics']
    english_courses = ['Literature-in-English', 'Government', 'Biology', 'French', 'English Language']

    def generate_gender_specific_scores(subject, gender):
        if subject in math_courses:
            if gender == 'Male':
                first_test = np.random.choice([np.random.randint(10, 18), np.random.randint(5, 10)], p=[0.6, 0.4])
                second_test = np.random.choice([np.random.randint(10, 18), np.random.randint(5, 10)], p=[0.6, 0.4])
                final_exam = np.random.choice([np.random.randint(40, 50), np.random.randint(30, 40)], p=[0.6, 0.4])
            else:  # Female
                first_test = np.random.choice([np.random.randint(5, 10), np.random.randint(10, 18)], p=[0.55, 0.45])
                second_test = np.random.choice([np.random.randint(5, 10), np.random.randint(10, 18)], p=[0.55, 0.45])
                final_exam = np.random.choice([np.random.randint(30, 40), np.random.randint(40, 50)], p=[0.55, 0.45])
        elif subject in english_courses:
            if gender == 'Female':
                first_test = np.random.randint(10, 18)
                second_test = np.random.randint(10, 18)
                final_exam = np.random.randint(40, 50)
            else:  # Male
                first_test = np.random.randint(5, 15)
                second_test = np.random.randint(5, 15)
                final_exam = np.random.randint(30, 50)
        else:
            first_test = np.random.randint(5, 16)
            second_test = np.random.randint(7, 18)
            final_exam = np.random.randint(20, 50)

        return first_test, second_test, final_exam

    # Generate data for Junior students
    for student_id in junior_student_ids:
        class_levels.extend(['Junior'] * num_subjects)
        gender = np.random.choice(['Male', 'Female'])
        genders.extend([gender] * num_subjects)

        # Select 9 distinct subjects for junior students
        student_subjects = np.random.choice(junior_subjects, num_subjects, replace=False)

        for subject in student_subjects:
            subjects.append(subject)
            first_test, second_test, final_exam = generate_gender_specific_scores(subject, gender)
            average_score = first_test + second_test + final_exam

            first_test_scores.append(first_test)
            second_test_scores.append(second_test)
            final_exam_scores.append(final_exam)
            average_scores.append(average_score)

    # Repeat the process for Senior students (Science, Art, and Commercial)
    for student_id in senior_student_ids:
        class_type = np.random.choice(['Science', 'Art', 'Commercial'])
        class_levels.extend([class_type] * num_subjects)
        gender = np.random.choice(['Male', 'Female'])
        genders.extend([gender] * num_subjects)

        if class_type == 'Science':
            student_subjects = np.random.choice(science_subjects, num_subjects, replace=False)
        elif class_type == 'Art':
            student_subjects = np.random.choice(art_subjects, num_subjects, replace=False)
        else:
            student_subjects = np.random.choice(commercial_subjects, num_subjects, replace=False)

        for subject in student_subjects:
            subjects.append(subject)
            first_test, second_test, final_exam = generate_gender_specific_scores(subject, gender)
            average_score = first_test + second_test + final_exam

            first_test_scores.append(first_test)
            second_test_scores.append(second_test)
            final_exam_scores.append(final_exam)
            average_scores.append(average_score)

    # Create the DataFrame from the collected data
    data = {
        'Student ID': np.repeat(student_ids, num_subjects),
        'Gender': genders,
        'Class Level': class_levels,
        'Subject': subjects,
        'First Test (20%)': first_test_scores,
        'Second Test (20%)': second_test_scores,
        'Final Exam (60%)': final_exam_scores,
        'Average Grade (100%)': average_scores
    }

    return pd.DataFrame(data)

# Generate the academic performance dataset
academic_performance_fixed_df = generate_academic_performance_data_fixed()

# Save the dataset to a CSV file
academic_performance_fixed_df.to_csv('academic_performance.csv', index=False)
