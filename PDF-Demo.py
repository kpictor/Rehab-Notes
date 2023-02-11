from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style='U', size=14)
        self.cell(0, 10, "Rehabilitation Progress Notes", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, "Page %s" % self.page_no(), 0, 0, "C")

def create_pdf(patient_name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Patient Name: %s" % patient_name, 0, 1)
    pdf.output("rehab_notes_%s_%s.pdf" % (patient_name, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), "F")

patient_name = input("Enter patient name: ")
create_pdf(patient_name)
