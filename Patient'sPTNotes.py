import datetime
import os

# define a function that generates a physical therapy record for a patient
def generate_pt_notes():
    # prompt the user to input patient information
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender (Male/Female): ")
    #date_of_examination = datetime.datetime.now().strftime("%Y-%m-%d")
    date_of_examination = input("Enter the date of examination (YYYY-MM-DD): ")
    # prompt the user to input examination information
    chief_complaint = input("Enter patient's chief complaint: ")
    history_of_present_illness = input("Enter patient's history of present illness: ")
    past_medical_history = input("Enter patient's past medical history: ")
    medication = input("Enter patient's current medication: ")
    patient_posture = input("Enter patient's posture: ")
    patient_gait = input("Enter patient's gait: ")
    visual_inspection = input("Enter visual inspection of the affected area was performed:")
    palpation = input("Enter palpation of the affected area was performed:")
    patient_AROM = input("Enter patient's Active Range of Motion (AROM): ")
    patient_strength = input("Enter patient's strength: ")
    patient_sensory = input("Enter patient's sensory: ")
    patient_reflexes = input("Enter patient's reflexes: ")
    patient_special_tests = input("Enter patient's special tests: ")
    icf = input("Enter patient's ICF information: ") # prompt the user to input ICF information
    treatment_plan = input("Enter patient's treatment plan: ")
    expected_outcome = input("Enter patient's expected outcome: ")
    follow_up = input("Enter the date for follow-up appointment (YYYY-MM-DD): ")
    
    # format the data as a markdown text
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

### Visual Inspection
{visual_inspection}

### Palpation
{palpation}

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

### ICF
{icf} 

## Treatment Plan

{treatment_plan}

## Expected Outcome

{expected_outcome}

## Follow-Up

A follow-up appointment is scheduled for {follow_up}.
    """.format(name=name, age=age, gender=gender, date_of_examination=date_of_examination,
               chief_complaint=chief_complaint, history_of_present_illness=history_of_present_illness,
               past_medical_history=past_medical_history, medication=medication, patient_posture=patient_posture,
               patient_gait=patient_gait, visual_inspection=visual_inspection, palpation=palpation, patient_AROM=patient_AROM, patient_strength=patient_strength,
               patient_sensory=patient_sensory, patient_reflexes=patient_reflexes, patient_special_tests=patient_special_tests,
               icf=icf, treatment_plan=treatment_plan, expected_outcome=expected_outcome, follow_up=follow_up)

    # save the markdown text to a file on the desktop
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    file_name = "{date}-Hu.-{name}PTNotes".format(date=date_str, name=name)
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    file_path = os.path.join(desktop_path, file_name + ".md")
  
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(markdown_text)


    print("Markdown document generated as", file_name + ".md on Desktop")  

# Example usage:
generate_pt_notes()