def generate_markdown(patient_info, assessment, treatment_plan, progress):
    markdown_text = "## Rehabilitation Progress Note\n\n"
    markdown_text += "### Patient Information\n"
    markdown_text += "Name: {}\n".format(patient_info["Name"])
    markdown_text += "Date of Birth: {}\n".format(patient_info["DOB"])
    markdown_text += "Contact Information: {}\n".format(patient_info["Contact"])
    markdown_text += "Diagnosis: {}\n\n".format(patient_info["Diagnosis"])
    markdown_text += "### Assessment\n{}\n\n".format(assessment)
    markdown_text += "### Treatment Plan\n{}\n\n".format(treatment_plan)
    markdown_text += "### Progress\n{}\n\n".format(progress)
    return markdown_text

patient_info = {
    "Name": "Jane Doe",
    "DOB": "01/01/2000",
    "Contact": "555-555-5555",
    "Diagnosis": "Strained ankle"
}
assessment = "Patient presents with pain and swelling in the ankle. Limited range of motion observed."
treatment_plan = "Prescribe physical therapy exercises to improve range of motion and reduce pain."
progress = "Patient has shown improvement in range of motion and reports decreased pain."

print(generate_markdown(patient_info, assessment, treatment_plan, progress))
