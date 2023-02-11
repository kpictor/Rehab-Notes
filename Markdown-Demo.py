import datetime

def main():
    patient_name = input("Enter patient name: ")
    patient_age = input("Enter patient age: ")
    patient_diagnosis = input("Enter patient diagnosis: ")
    patient_symptoms = input("Enter patient symptoms: ")
    patient_treatment = input("Enter patient treatment plan: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    markdown_file = open("Rehabilitation_Progress_Note_" + patient_name + ".md", "w")
    markdown_file.write("# Rehabilitation Progress Note\n\n")
    markdown_file.write("Patient Name: " + patient_name + "\n\n")
    markdown_file.write("Patient Age: " + patient_age + "\n\n")
    markdown_file.write("Diagnosis: " + patient_diagnosis + "\n\n")
    markdown_file.write("Symptoms: " + patient_symptoms + "\n\n")
    markdown_file.write("Treatment Plan: " + patient_treatment + "\n\n")
    markdown_file.write("Date: " + note_date + "\n\n")
    markdown_file.write("Progress notes go here\n")
    markdown_file.close()

if __name__ == "__main__":
    main()