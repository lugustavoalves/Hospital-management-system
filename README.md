# Hospital-management-system

 This project was created in a group with the following people: [@onlyxool](https://github.com/onlyxool), [@AbinayaKalaiarasan](https://github.com/AbinayaKalaiarasan) and [@dornalaspandana](https://github.com/dornalaspandana). 

## Getting Started

### Installation

**Clone the repository**

```bash
git clone https://github.com/lugustavoalves/Hospital-management-system.git

cd Hospital-management-system
```



### Installation of dependent libraries

```bash
pip install -r requirements.txt
```



### Create Database

Run https://github.com/lugustavoalves/Hospital-management-system/blob/main/Hospital_Management_System.sql



Use [Conda](https://docs.anaconda.com/miniconda/) or [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) create a virtual environment



### Run the project (console)

```bash
python main_cli.py
```

<img width="900" alt="Screenshot 2024-12-08 at 21 04 29" src="https://github.com/user-attachments/assets/5cf9d612-5018-42e6-beca-b26c20a44f51">


Login with User Name: `admin` Password `admin`. OR login as patient without password

<img width="900" alt="Screenshot 2024-12-08 at 21 06 04" src="https://github.com/user-attachments/assets/cf66ff39-9de4-4993-b098-9c7baff5ba31">





### Run the project (Web)

```bash
uvicorn main:app --reload
# or
python main_web.py
```
<img width="803" alt="web" src="https://github.com/user-attachments/assets/42bf9e76-d1b2-4206-bcf0-ffe83090b3db">



### Test

Use your browser to visit http://127.0.0.1:8000/doctors/









### ER Diagram

```mermaid
erDiagram
    Doctors {
        INT Doc_ID PK "Primary Key"
        VARCHAR Doc_Name "Doctor Name"
        VARCHAR Speciality "Speciality"
        VARCHAR Phone_Num "Phone Number"
        VARCHAR Email "Email"
    }

    Staff {
        INT Staff_ID PK "Primary Key"
        VARCHAR Name "Staff Name"
        VARCHAR Department "Department"
        VARCHAR Email "Email (Unique)"
        DATE Hire_Date "Hire Date"
    }

    StaffShifts {
        INT Shift_ID PK "Primary Key"
        INT Staff_ID FK "Foreign Key to Staff"
        DATETIME Shift_Start "Shift Start Time"
        DATETIME Shift_End "Shift End Time"
    }

    Patients {
        INT Patient_ID PK "Primary Key"
        VARCHAR Patient_Name "Patient Name"
        VARCHAR Patient_Records "Patient Records"
        VARCHAR Phone_Num "Phone Number"
        VARCHAR Email "Email"
        INT Doc_ID FK "Foreign Key to Doctors"
        INT Staff_ID FK "Foreign Key to Staff"
    }

    Test_Records {
        INT Record_ID PK "Primary Key"
        INT Patient_ID FK "Foreign Key to Patients"
        VARCHAR Record_Name "Record Name"
        DATETIME Test_Date "Test Date"
        VARCHAR Remarks "Remarks"
    }

    Appointments {
        INT Appointment_ID PK "Primary Key"
        INT Patient_ID FK "Foreign Key to Patients"
        INT Doc_ID FK "Foreign Key to Doctors"
        DATETIME Appointment_Date "Appointment Date"
        TINYINT Statusof "Appointment Status"
        VARCHAR Typeof "Appointment Type"
        VARCHAR Speciality "Speciality"
        VARCHAR Notes "Additional Notes"
    }

    MedicalHistory {
        INT History_ID PK "Primary Key"
        INT Patient_ID FK "Foreign Key to Patients"
        INT Doc_ID FK "Foreign Key to Doctors"
        VARCHAR Diagnosis "Diagnosis"
        VARCHAR Treatment "Treatment"
        DATETIME Record_Date "Record Date"
    }

    Wards {
        INT Ward_ID PK "Primary Key"
        VARCHAR Ward_Name "Ward Name"
        INT Capacity "Ward Capacity"
    }

    Beds {
        INT Bed_ID PK "Primary Key"
        INT Ward_ID FK "Foreign Key to Wards"
        INT Patient_ID FK "Foreign Key to Patients"
        VARCHAR Status "Bed Status"
        DATETIME Assigned_Date "Assigned Date"
    }

    Prescriptions {
        INT Prescription_ID PK "Primary Key"
        INT Patient_ID FK "Foreign Key to Patients"
        INT Doctor_ID FK "Foreign Key to Doctors"
        DATETIME Date_Issued "Date Issued"
        VARCHAR Notes "Prescription Notes"
    }

    Prescription_Details {
        INT Detail_ID PK "Primary Key"
        INT Prescription_ID FK "Foreign Key to Prescriptions"
        VARCHAR Medication_Name "Medication Name"
        VARCHAR Dosage "Dosage"
        VARCHAR Frequency "Frequency"
        VARCHAR Duration "Duration"
    }

    Notifications {
        INT Notification_ID PK "Primary Key"
        VARCHAR Recipient_Type "Recipient Type"
        INT Recipient_ID "Recipient ID"
        TEXT Message "Notification Message"
        VARCHAR Status "Notification Status"
        DATETIME Created_At "Created At"
        DATETIME Read_At "Read At"
    }

    Doctors ||--o{ Patients : "Assigned"
    Doctors ||--o{ Appointments : "Has"
    Doctors ||--o{ MedicalHistory : "Records"
    Doctors ||--o{ Prescriptions : "Issues"

    Staff ||--o{ StaffShifts : "Works"
    Staff ||--o{ Patients : "Cares"

    Patients ||--o{ Test_Records : "Has"
    Patients ||--o{ Appointments : "Schedules"
    Patients ||--o{ MedicalHistory : "Maintains"
    Patients ||--o{ Prescriptions : "Prescribed"
    Patients ||--o{ Beds : "Assigned"

    Wards ||--o{ Beds : "Contains"

    Prescriptions ||--o{ Prescription_Details : "Includes"

```





