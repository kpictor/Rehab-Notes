# Physical Therapy Record Generator

This repository contains a Python script that generates a professional and comprehensive physical therapy (PT) record based on user input. The generated document is in Markdown format and includes information about the patient, examination information, physical exam, treatment plan, expected outcome, and follow-up appointment. The document is organized into sections with headings, making it easy to read and navigate.

## Features

- Prompts user to input patient information, examination information, physical exam, treatment plan, expected outcome, and follow-up appointment.
- Generates a Markdown document with the information organized into sections with headings.
- Saves the generated document in the same directory with the name `yyyymmdd-Hu.-{name}PTRecord.md`, where `yyyymmdd` is the current date and `{name}` is the name of the patient.
- The physical exam section includes specific and professional assessment fields, such as posture, gait, Active Range of Motion (AROM), strength, sensory, reflexes, and special tests.

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the repository directory.
3. Run the following command to execute the script:
python generate_pt_record.py
4. Follow the prompts to enter the information for the PT record.
5. The generated Markdown document will be saved in the same directory with the name `yyyymmdd-Hu.-{name}PTRecord.md`, where `yyyymmdd` is the current date and `{name}` is the name of the patient.

## Contributing

Contributions are welcome! If you have any suggestions or bug reports, please open an issue or create a pull request.

## License

None
