import datetime

def generate_pt_record():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender (Male/Female): ")
    date_of_examination = datetime.datetime.now().strftime("%Y-%m-%d")
#date_of_examination = input("Enter the date of examination (YYYY-MM-DD): ")
    chief_complaint = input("Enter patient's chief complaint: ")
    history_of_present_illness = input("Enter patient's history of present illness: ")
    past_medical_history = input("Enter patient's past medical history: ")
    medication = input("Enter patient's current medication: ")
    patient_posture = input("Enter patient's posture: ")
    patient_gait = input("Enter patient's gait: ")
    patient_AROM = input("Enter patient's Active Range of Motion (AROM): ")
    patient_strength = input("Enter patient's strength: ")
    patient_sensory = input("Enter patient's sensory: ")
    patient_reflexes = input("Enter patient's reflexes: ")
    patient_special_tests = input("Enter patient's special tests: ")
    treatment_plan = input("Enter patient's treatment plan: ")
    expected_outcome = input("Enter patient's expected outcome: ")
    follow_up = input("Enter the date for follow-up appointment (YYYY-MM-DD): ")

    date_str = datetime.datetime.now().strftime("%Y%m%d")
    file_name = "{date}-Hu.-{name}PTRecord".format(date=date_str, name=name)

    markdown_text = """
# Physical Therapy Record for {name}

## Patient Information

### Name
{name}

### Age
{age}

### Gender
{gender}

## Examination Information

### Date of Examination
{date_of_examination}

### Chief Complaint
{chief_complaint}

### History of Present Illness
{history_of_present_illness}

### Past Medical History
{past_medical_history}

### Current Medication
{medication}

## Physical Exam

### Posture
{patient_posture}

### Gait
{patient_gait}

### Active Range of Motion (AROM)
{patient_AROM}

### Strength
{patient_strength}

### Sensory
{patient_sensory}

### Reflexes
{patient_reflexes}

### Special Tests
{patient_special_tests}

## Treatment Plan

{treatment_plan}

## Expected Outcome

{expected_outcome}

## Follow-Up

A follow-up appointment is scheduled for {follow_up}.
    """.format(name=name, age=age, gender=gender, date_of_examination=date_of_examination,
               chief_complaint=chief_complaint, history_of_present_illness=history_of_present_illness,
               past_medical_history=past_medical_history, medication=medication, patient_posture=patient_posture,
               patient_gait=patient_gait, patient_AROM=patient_AROM, patient_strength=patient_strength,
               patient_sensory=patient_sensory, patient_reflexes=patient_reflexes, patient_special_tests=patient_special_tests,
               treatment_plan=treatment_plan, expected_outcome=expected_outcome, follow_up=follow_up)

    with open(file_name + ".md", 'w') as file:
        file.write(markdown_text)

    print("Markdown document generated as", file_name + ".md")

# Example usage:
generate_pt_record()

