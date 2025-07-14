"""
Hospital Management System

This module provides a console-based Hospital Management System
that supports CRUD operations for managing doctors, staff, patients,
and test records. It uses SQLAlchemy for database interactions
and ConsoleMenu for the user interface.

Features:
- Manage Doctors
- Manage Staff
- Manage Staff Shifts
- Manage Patients
- Manage Test Records
- Manage Appointments
- Manage Medical History
- Manage Beds
- Manage Prescriptions
- Manage Notifications
- Interactive Menu System for CRUD operations
- Help 

Modules Required:
- database: Defines the database connection.
- sqlalchemy: For ORM operations.
- prettytable: To format query results as tables.
- consolemenu: For the menu interface.
- schemas: Contains data models.
- db_operator: Contains CRUD operation functions for database interactions.

Usage:
Run the script, and interact with the menu to perform the required operations.

"""

import pwinput
import json
import time
from sqlalchemy.orm import Session
from sqlalchemy import text 
from prettytable import PrettyTable
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem, ExitItem

from datetime import datetime
from database import get_db_cli
from schemas import DoctorBase, StaffBase, StaffShiftBase, PatientBase, TestRecordBase, AppointmentBase, MedicalHistoryBase, BedBase, PrescriptionBase, PrescriptionDetailBase

from database import Base

from login.loginclass import LoginSystem
import db_operator as db_ops


def print_table(results, stop=True):
    """
    Display query results in a tabular format using PrettyTable.

    Args:
        results: List of SQLAlchemy objects or a single object.
    """
    table = PrettyTable()

    if results:
        if isinstance(results, list):
            if isinstance(results[0], Base):
                table.field_names = [column.name for column in results[0].__table__.columns]
                for row in results:
                    table.add_row([getattr(row, column) for column in table.field_names])
            else:
                table.field_names = dict(results[0]._mapping).keys()
                for item in results:
                    table.add_row(dict(item._mapping).values())
        else:
            if isinstance(results, Base):
                table.field_names = [column.name for column in results.__table__.columns]
                table.add_row([getattr(results, column) for column in table.field_names])
            else:
                results_dict = dict(results._mapping)
                table.field_names = results_dict.keys()
                table.add_row(results_dict.values())

        print(table)

    if stop:
        input("Press Enter to return to the menu...")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False
    
# Define actions for Doctor management
def create_doctor(db_session):
    """
    Create a new doctor record in the database.
    """
    name = input('Enter the Doctor\'s Name: ')
    speciality = input('Enter the Doctor\'s Speciality: ')
    phone = input('Enter the Phone Number: ')
    email = input('Enter the Email: ')

    external_data = {'Doc_Name': name, 'Speciality': speciality, 'Phone_Num': phone, 'Email': email}

    result = db_ops.create_doctor(db_session, DoctorBase(**external_data))
    print_table(result)


def get_doctors(db_session):
    """
    Display all doctors from the database.
    """
    print_table(db_ops.get_doctors(db_session))


def get_doctor(db_session):
    """
    Retrieve and display a specific doctor by ID.
    """
    doctor_id = int(input('Please Enter doctor id:'))
    print_table(db_ops.get_doctor(db_session, doctor_id))


def update_doctor(db_session):
    """
    Update a doctor's record.
    """
    doctor_id = int(input('Please Enter doctor id:'))
    doctor = db_ops.get_doctor(db_session, doctor_id)
    print_table(doctor, False)

    name = input('Please Enter Name: ')
    name = doctor.Doc_Name if name == '' else name

    phone = input('Please Enter Phone Number: ')
    phone = doctor.Phone_Num if phone == '' else phone

    speciality = input('Please Enter doctor\'s Speciality: ')
    speciality = doctor.Speciality if speciality == '' else speciality

    email = input('Please Enter Email: ')
    email = doctor.Email if email == '' else email

    external_data = {'Doc_Name': name, 'Speciality': speciality, 'Phone_Num': phone, 'Email': email}
    db_doctor = db_ops.update_doctor(db_session, doctor_id, DoctorBase(**external_data))
    print_table(db_doctor)


def delete_doctor(db_session):
    """
    Delete a doctor's record by ID.
    """
    print_table(db_ops.get_doctors(db_session), False)
    doctor_id = int(input('Please Enter doctor id:'))
    db_doctor = db_ops.delete_doctor(db_session, doctor_id)
    print_table(db_doctor)


# Define actions for Staff management
def create_staff(db_session):
    """
    Create a new Staff record in the database.
    """
    name = input('Enter the Staff\'s Name: ')
    department = input('Enter the Staff\'s Department: ')
    shift = input('Enter the shift: ')

    external_data = {'Name': name, 'Department': department, 'Upcoming_Shifts': shift}

    result = db_ops.create_staff(db_session, StaffBase(**external_data))
    print_table(result)


def get_staff(db_session):
    """
    Display all Staff from the database.
    """
    print_table(db_ops.get_staff(db_session))


def get_staff_member(db_session):
    """
    Retrieve and display a specific Staff by ID.
    """
    staff_id = int(input('Please Enter staff id:'))
    print_table(db_ops.get_staff_member(db_session, staff_id))


def update_staff(db_session):
    """
    Update a Staff's record.
    """
    staff_id = int(input('Please Enter staff id:'))
    staff = db_ops.get_staff_member(db_session, staff_id)
    print_table(staff, False)

    name = input('Please Enter Name: ')
    name = staff.Doc_Name if name == '' else name

    dept = input('Please Enter Department: ')
    dept = staff.Department if dept == '' else dept

    shift = input('Please Enter shift: ')
    shift = staff.shift if shift == '' else shift

    external_data = {'Name': name, 'Department': dept, 'Upcoming_Shifts': shift}
    db_staff = db_ops.update_staff(db_session, staff_id, StaffBase(**external_data))
    print_table(db_staff)


def delete_staff(db_session):
    """
    Delete a Staff's record by ID.
    """
    print_table(db_ops.get_doctors(db_session), False)
    staff_id = int(input('Please Enter doctor id:'))
    db_staff = db_ops.delete_staff(db_session, staff_id)
    print_table(db_staff)


# Define actions for Staff Shift management
def create_staff_shift(db_session):
    """
    Create a new Staff Shift record in the database.
    """

    staff = db_ops.get_staff(db_session)
    print_table(staff, False)

    while True:
        staff_id = input('Enter the Staff ID: ')
        if db_ops.get_staff_member(db_session, staff_id) is None:
            print('Invaild Staff ID')
        else:
            break

    while True:
        shift_start = input('Enter the Shift Start Date (YYYY-MM-DD HH:MM:SS): ')
        if is_valid_date(shift_start):
            break
        else:
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.')
    
    while True:
        shift_end = input('Enter the Shift End Date (YYYY-MM-DD HH:MM:SS): ')
        if is_valid_date(shift_end):
            break
        else:
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.')

    external_data = {'Staff_ID': staff_id, 'Shift_Start': shift_start, 'Shift_End': shift_end}

    result = db_ops.create_staff_shift(db_session, StaffShiftBase(**external_data))
    print_table(result)

def get_staff_shifts(db_session):
    """
    Display all Staff Shifts from the database.
    """
    print_table(db_ops.get_staff_shifts(db_session))

def get_staff_shift(db_session):
    """
    Retrieve and display a specific Staff Shift by ID.
    """
    shift_id = int(input('Please Enter shift id:'))
    print_table(db_ops.get_staff_shift(db_session, shift_id))

def get_staff_shift_by_staff_id(db_session):
    """
    Retrieve and display a specific Staff Shift by Staff ID.
    """
    staff_id = int(input('Please Enter Staff ID:'))
    print_table(db_ops.get_staff_shift_by_staff_id(db_session, staff_id))

def update_staff_shift(db_session):
    """
    Update a Staff Shift record.
    """
    shift_id = int(input('Please Enter shift id:'))
    shift = db_ops.get_staff_shift(db_session, shift_id)
    print_table(shift, False)

    staff_id = input('Please Enter Staff ID: ')
    staff_id = shift.Staff_ID if staff_id == '' else staff_id

    shift_start = input('Please Enter Shift Start Date: ')
    shift_start = shift.Shift_Start if shift_start == '' else shift_start

    shift_end = input('Please Enter Shift End Date: ')
    shift_end = shift.Shift_End if shift_end == '' else shift_end

    external_data = {'Staff_ID': staff_id, 'Shift_Start': shift_start, 'Shift_End': shift_end}
    db_shift = db_ops.update_staff_shift(db_session, shift_id, StaffShiftBase(**external_data))
    print_table(db_shift)

def delete_staff_shift(db_session):
    """
    Delete a Staff Shift record by ID.
    """
    print_table(db_ops.get_staff_shifts(db_session), False)
    shift_id = int(input('Please Enter shift id:'))
    db_shift = db_ops.delete_staff_shift(db_session, shift_id)
    print_table(db_shift)


# Define actions for Patient management
def create_patient(db_session):
    """
    Create a new Patient record in the database.
    """
    name = input('Enter the Patient\'s Name: ')
    email = input('Enter the Patient\'s Email: ')
    record = input('Enter the Patient\'s Records: ')
    phone = input('Enter the Phone Number: ')
    doc_id = input('Enter the Doctor ID: ')
    staff_id = input('Enter the Staff ID: ')

    external_data = {'Patient_Name': name, 'Patient_Records': record,
         'Phone_Num': phone, 'Email':email, 'Doc_ID':doc_id, 'Staff_ID':staff_id}

    result = db_ops.create_patient(db_session, PatientBase(**external_data))
    print_table(result)


def get_patients(db_session):
    """
    Display all Patients from the database.
    """
    print_table(db_ops.get_patients(db_session))
    print("Listing all patients...")


def get_patient(db_session):
    """
    Retrieve and display a specific patient by ID.
    """
    patient_id = int(input('Please Enter patient id:'))
    print_table(db_ops.get_doctor(db_session, patient_id))


def update_patient(db_session):
    """
    Update a patient's record.
    """
    patient_id = int(input('Please Enter patient id:'))
    patient = db_ops.get_patient(db_session, patient_id)
    print_table(patient, False)

    name = input('Please Enter Name: ')
    name = patient.Patient_Name if name == '' else name

    record = input('Please Enter Patient Records: ')
    record = patient.Patient_Records if record == '' else record

    phone = input('Please Enter Phone Number: ')
    phone = patient.Phone_Num if phone == '' else phone

    email = input('Please Enter Email: ')
    email = patient.Email if email == '' else email

    doc_id = input('Please Enter Doctor ID: ')
    doc_id = patient.Doc_ID if doc_id == '' else doc_id

    staff_id = input('Please Enter Staff ID: ')
    staff_id = patient.Staff_ID if staff_id == '' else staff_id

    external_data = {'Patient_Name': name, 'Patient_Records': record,
        'Phone_Num': phone, 'Email': email, 'Doc_ID': doc_id, 'Staff_ID': staff_id}

    db_staff = db_ops.update_staff(db_session, staff_id, PatientBase(**external_data))
    print_table(db_staff)


def delete_patient(db_session):
    """
    Delete a patient record by ID.
    """
    print_table(db_ops.get_patients(db_session), False)
    patient_id = int(input('Please Enter patient id:'))
    db_patient = db_ops.delete_patient(db_session, patient_id)
    print_table(db_patient)


# Define actions for Test Record management
def create_test_record(db_session):
    """
    Create a new test record in the database.
    """
    patient_id = input('Enter the Patient ID: ')
    name = input('Enter the Record Name: ')
    date = input('Enter Date: ')
    remark = input('Enter Remark: ')

    external_data = {'Patient_ID': patient_id, 'Record_Name': name,
            'Test_Date': date, 'Remarks':remark}

    result = db_ops.create_test_record(db_session, TestRecordBase(**external_data))
    print_table(result)


def get_test_records(db_session):
    """
    Display all Test Records from the database.
    """
    print_table(db_ops.get_test_records(db_session))


def get_test_record(db_session):
    """
    Retrieve and display a specific Test Record by ID.
    """
    records_id = int(input('Please Enter test record id:'))
    print_table(db_ops.get_test_record(db_session, records_id))


def update_test_record(db_session):
    """
    Update a Test record.
    """
    record_id = int(input('Please Enter Record id:'))
    record = db_ops.get_test_record(db_session, record_id)
    print_table(record, False)

    patient_id = input('Please Patient ID: ')
    patient_id = record.Patient_ID if patient_id == '' else patient_id

    name = input('Please Enter Record Name: ')
    name = record.Record_Name if name == '' else name

    date = input('Please Enter Test Date: ')
    date = record.Test_Date if date == '' else date

    remarks = input('Please Enter Remarks: ')
    remarks = record.Remarks if remarks == '' else remarks

    external_data = {'Patient_ID': patient_id, 'Record_Name': name, 'Test_Date': date, 'Remarks': remarks}
    db_staff = db_ops.update_staff(db_session, record, TestRecordBase(**external_data))
    print_table(db_staff)


def delete_test_record(db_session):
    """
    Delete a Test record by ID.
    """
    print_table(db_ops.get_test_records(db_session), False)
    record_id = int(input('Please Enter Test Record ID:'))
    db_record = db_ops.delete_test_record(db_session, record_id)
    print_table(db_record)


# Define actions for Appointment management
def create_appointment(db_session):
    """
    Create a new appointment in the database.
    """
    while True:
        doc_id = int(input('Enter the Doctor ID: '))
        if db_ops.get_doctor(db_session, doc_id) is None:
            print('Invaild Doctor ID')
        else:
            break

    doctor = db_ops.get_doctor(db_session, doc_id)
    print_table(doctor, False)

    while True:
        patient_id = input('Enter the Patient ID: ')
        if db_ops.get_patient(db_session, patient_id) is None:
            print('Invaild Patient ID')
        else:
            break

    while True:
        app_date = input('Enter the Appointment Date (YYYY-MM-DD HH:MM:SS): ')
        if is_valid_date(app_date):
            break
        else:
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.')

    while True:
        status = input('Enter the Status (0-4 0-Open, 1-Scheduled, 2-Completed, 3-Cancelled, 4-Expired): ')
        if status.isdigit() and int(status) >= 0 and int(status) <= 4:
            status = int(status)
            break
        else:
            print('Invaild Status Number')

    while True:
        typeof = input('enter the type of appointment (Online or Inperson): ')
        if typeof in ['Online', 'Inperson']:
            break
        else:
            print('Invaild type of appointment')

    speciality = doctor.Speciality

    note = input('Please Enter the Notes: ')

    external_data = {'Patient_ID': patient_id, 'Doc_ID': doc_id, 'Appointment_Date': app_date,
            'Statusof': status,'Typeof': typeof,'Speciality': speciality, 'Notes':note}

    result = db_ops.create_appointment(db_session, AppointmentBase(**external_data))
    print_table(result)


def create_open_appointment(db_session):
    """
    Create a new open appointment in the database.
    """
    while True:
        doc_id = int(input('Enter the Doctor ID: '))
        if db_ops.get_doctor(db_session, doc_id) is None:
            print('Invaild Doctor ID')
        else:
            break

    doctor = db_ops.get_doctor(db_session, doc_id)
    print_table(doctor, False)

    speciality = doctor.Speciality
    while True:
        appo_date = input('Enter the Appointment Date (YYYY-MM-DD HH:MM:SS): ')
        if is_valid_date(appo_date):
            break
        else:
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.')

    status = 0
    external_data = { 'Doc_ID': doc_id, 'Appointment_Date': appo_date, 'Speciality': speciality, 'Statusof': status}

    result = db_ops.create_appointment(db_session, AppointmentBase(**external_data))
    print_table(result)


def get_appointments_by_speciality(db_session):
    """
    Retrieve and display appointments by Doctor Speciality.
    """
    doctors = db_ops.get_doctors(db_session)
    print_table(doctors, False)
    speciality = input('Please Enter Doctor Speciality: ')
    print_table(db_ops.get_appointments_by_speciality(db_session, speciality))


def get_appointment_by_doc_id(db_session):
    """
    Retrieve and display a specific Appointment by Doctor ID.
    """
    doc_id = int(input('Please Enter Doctor ID: '))
    print_table(db_ops.get_appointments_by_doctor_id(db_session, doc_id))


def get_appointment_by_patient_id(db_session):
    """
    Retrieve and display a specific Appointment by Patient ID.
    """
    patient_id = int(input('Please Enter Patient ID: '))
    print_table(db_ops.get_appointments_by_patient_id(db_session, patient_id))


def update_appointment(db_session):
    """
    Update a Appointment.
    """
    appointment_id = int(input('Please Enter Appointment id:'))
    appointment = db_ops.get_appointment(db_session, appointment_id)
    print_table(appointment, False)

    doc_id = input('Please Enter Doctor ID: ')
    doc_id = appointment.Doc_ID if doc_id == '' else doc_id

    patient_id = input('Please Enter Patient ID: ')
    patient_id = appointment.Patient_ID if patient_id == '' else patient_id

    app_date = input('Please Enter Appointment Date: ')
    app_date = appointment.Appointment_Date if app_date == '' else app_date

    while True:
        status = input('Please Enter Status (0-4 0-Open, 1-Scheduled, 2-Completed, 3-Cancelled, 4-Expired): ')
        if status.isdigit() and int(status) >= 0 and int(status) <= 4:
            status = int(status)
            break
        else:
            print('Invaild Input!')
        
    while True:
        typeof = input('enter the type of appointment (Online or Inperson): ')
        if typeof in ['Online', 'Inperson']:
            break
        else:
            print('Invaild type of appointment')

    speciality = appointment.Speciality

    note = input('Please Enter Note: ')
    note = appointment.Notes if note == '' else note

    external_data = {'Doc_ID':doc_id, 'Patient_ID': patient_id, 'Statusof': status, 'Typeof': typeof, 'Speciality': speciality, 'Appointment_Date': app_date, 'Notes': note}
    db_ops.update_appointment(db_session, appointment_id, AppointmentBase(**external_data))
    print_table(db_ops.get_appointment(db_session, appointment_id))


def delete_appointment(db_session):
    """
    Delete a Appointment by ID.
    """
    appointment_id = int(input('Please Enter Appointment id:'))
    appointment = db_ops.get_appointment(db_session, appointment_id)
    print_table(appointment)
    db_ops.delete_appointment(db_session, appointment_id)


# Define actions for Medical History management
def create_medical_history(db_session):
    """
    Create a new Medical History in the database.
    """
    while True:
        doc_id = int(input('Enter the Doctor ID: '))
        if db_ops.get_doctor(db_session, doc_id) is None:
            print('Invaild Doctor ID')
        else:
            break

    while True:
        patient_id = input('Enter the Patient ID: ')
        if db_ops.get_patient(db_session, patient_id) is None:
            print('Invaild Patient ID')
        else:
            break

    record_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    diagnosis = input('Please Enter the Diagnosis: ')
    treatment = input('Please Enter the Treatment: ')

    external_data = {'Patient_ID': patient_id, 'Doc_ID': doc_id, 'Record_Date': record_date,
            'Diagnosis': diagnosis, 'Treatment': treatment}

    result = db_ops.create_medical_history(db_session, MedicalHistoryBase(**external_data))
    print_table(result)


def get_medical_history_by_doc_id(db_session):
    """
    Retrieve and display a specific Medical History by Doctor ID.
    """
    doc_id = int(input('Please Enter Doctor ID: '))
    print_table(db_ops.get_medical_history_by_doctor_id(db_session, doc_id))


def get_medical_history_by_patient_id(db_session):
    """
    Retrieve and display a specific Appointment by Patient ID.
    """
    patient_id = int(input('Please Enter Patient ID: '))
    print_table(db_ops.get_medical_history_by_patient_id(db_session, patient_id))


def update_medical_history(db_session):
    """
    Update a Medical History.
    """
    history_id = int(input('Please Enter History id:'))
    history = db_ops.get_medical_history(db_session, history_id)
    print_table(history, False)

    doc_id = input('Please Enter Doctor ID: ')
    doc_id = history.Doc_ID if doc_id == '' else doc_id

    patient_id = input('Please Enter Patient ID: ')
    patient_id = history.Patient_ID if patient_id == '' else patient_id

    record_date = input('Please Enter Appointment Date: ')
    record_date = history.Record_Date if record_date == '' else record_date 

    diagnosis = input('Please Enter the Diagnosis: ')
    diagnosis = history.Diagnosis if diagnosis == '' else diagnosis

    treatment = input('Please Enter the Treatment: ')
    treatment = history.Treatment if treatment == '' else treatment

    external_data = {'Doc_ID':doc_id, 'Patient_ID': patient_id, 'Record_Date': record_date, 'Diagnosis': diagnosis, 'Treatment': treatment}
    db_ops.update_medical_history(db_session, history_id, MedicalHistoryBase(**external_data))
    print_table(db_ops.get_medical_history(db_session, history_id))


def delete_medical_history(db_session):
    """
    Delete a Medical History by ID.
    """
    history_id = int(input('Please Enter Medical History ID:'))
    history = db_ops.get_medical_history(db_session, history_id)
    print_table(history)
    db_ops.delete_medical_history(db_session, history_id)


# Define actions for Bed management
def get_available_bed(db_session):
    '''
    Retrieve and display available bed.
    '''
    print_table(db_ops.get_available_bed(db_session))


def assigne_bed(db_session):
    """
    Assign a Bed to a Patient.
    """
    bed_id = int(input('Please Enter Bed ID: '))
    bed = db_ops.get_bed(db_session, bed_id)
    print_table(bed, False)
    patient_id = int(input('Please Enter Patient ID: '))
    external_data = {'Bed_ID': bed.Bed_ID, 'Ward_ID':bed.Ward_ID, 'Patient_ID': patient_id, 'Status': 'Occupied', 'Assigned_Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    db_ops.update_bed(db_session, bed_id, BedBase(**external_data))
    print_table(db_ops.get_bed(db_session, bed_id))


def get_occupied_bed(db_session):
    '''
    Retrieve and display Occupied bed.
    '''
    print_table(db_ops.get_occupied_bed(db_session))


def release_bed(db_session):
    '''
    Release Bed
    '''
    bed_id = int(input('Please Enter Bed ID: '))
    bed = db_ops.get_bed(db_session, bed_id)
    print_table(bed)
    print('Released.....')
    external_data = {'Bed_ID': bed.Bed_ID, 'Ward_ID':bed.Ward_ID, 'Patient_ID': None, 'Status': 'Available', 'Assigned_Date': None}
    db_ops.update_bed(db_session, bed_id, BedBase(**external_data))
    print_table(db_ops.get_bed(db_session, bed_id))

# Define actions for Prescription
def create_prescriptions(db_session):
    """
    Create a new Prescription in the database.
    """
    patient_id = int(input('Please Enter Patient ID: '))
    doc_id = int(input('Please Enter Doctor ID: '))
    note = input('Please Enter Note: ')

    external_data = {'Patient_ID': patient_id, 'Doctor_ID': doc_id, 'Date_Issued': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Notes':note}
    prescription = db_ops.create_prescription(db_session, PrescriptionBase(**external_data))

    medication = input('Please Enter Medication: ')
    dosage = input('Please Enter Dosage: ')
    frequency = input('Please Enter Frequuency: ')
    duration = input('Please Enter Duration: ')

    external_data2 = {'Prescription_ID': prescription.Prescription_ID, 'Medication_Name': medication, 'Dosage': dosage, 'Frequency': frequency, 'Duration': duration}
    db_ops.create_prescription_detail(db_session, PrescriptionDetailBase(**external_data2))

    print_table(db_ops.get_prescriptions_by(db_session, 'Prescription.Prescription_ID == value', prescription.Prescription_ID))


def get_prescription(db_session):
    """
    Lists prescriptions associated with a specific prescription id.
    """
    prescription_id = int(input('Please Enter Prescription ID: '))
    print_table(db_ops.get_prescriptions_by(db_session, 'Prescription.Prescription_ID == value', prescription_id))


def list_prescription_by_doc_id(db_session):
    """
    Lists prescriptions associated with a specific doctor.
    """
    doc_id = int(input('Please Enter Doctor ID: '))
    print_table(db_ops.get_prescriptions_by(db_session, 'Prescription.Doctor_ID == value', doc_id))


def list_prescription_by_patient_id(db_session):
    """
    Lists prescriptions associated with a specific patient.
    """
    patient_id = int(input('Please Enter Patient ID: '))
    print_table(db_ops.get_prescriptions_by(db_session, 'Prescription.Doctor_ID == value', patient_id))


def list_notification_doctor(db_session):
    """
    Lists Notification associated with a specific Doctor.
    """
    doc_id = int(input('Please Enter Doctor ID: '))
    print_table(db_ops.get_notifications_for_recipient(db_session, 'Doctor', doc_id))


def list_notification_staff(db_session):
    """
    Lists Notification associated with a specific Staff.
    """
    staff_id = int(input('Please Enter Staff ID: '))
    print_table(db_ops.get_notifications_for_recipient(db_session, 'Staff', staff_id))


def list_notification_patient(db_session):
    """
    Lists Notification associated with a specific patient.
    """
    patient_id = int(input('Please Enter Patient ID: '))
    print_table(db_ops.get_notifications_for_recipient(db_session, 'Patient', patient_id))



# Function to create a submenu with CRUD operations for each category
def create_crud_menu(menu_title, create_func, get_all_func, get_func, update_func, delete_func, db_session):
    """
    Create a submenu for managing a specific entity with CRUD options.

    Args:
        menu_title: Title of the submenu.
        create_func: Function for creating an entity.
        get_all_func: Function for retrieving all entities.
        get_func: Function for retrieving a specific entity.
        update_func: Function for updating an entity.
        delete_func: Function for deleting an entity.
        db: Database session.
    """
    submenu = ConsoleMenu(menu_title)
    submenu.append_item(FunctionItem('Create', create_func, [db_session]))
    submenu.append_item(FunctionItem('Get All', get_all_func, [db_session]))
    submenu.append_item(FunctionItem('Get', get_func, [db_session]))
    submenu.append_item(FunctionItem('Update', update_func, [db_session]))
    submenu.append_item(FunctionItem('Delete', delete_func, [db_session]))
    return submenu


# Main function to create the main menu
def create_main_menu(db_session: Session, help_data):
    """
    Create the main menu for the Hospital Management System.

    Args:
        db_session: Database session.
    """
    main_menu = ConsoleMenu('Hospital Management System', 'Please select an option')

    # Doctor submenu
    doctor_menu = create_crud_menu(
        'Doctor Management',
        create_doctor,
        get_doctors,
        get_doctor,
        update_doctor,
        delete_doctor,
        db_session
    )
    doctor_menu.append_item(FunctionItem('Create Prescriptions', create_prescriptions, [db_session]))
    doctor_menu.append_item(FunctionItem('Get Prescriptions by ID', get_prescription, [db_session]))
    doctor_menu.append_item(FunctionItem('List Prescriptions by Doc_ID', list_prescription_by_doc_id, [db_session]))
    doctor_menu.append_item(FunctionItem('List Prescriptions by Patient_ID', list_prescription_by_patient_id, [db_session]))
    doctor_menu.append_item(FunctionItem('Notification', list_notification_doctor, [db_session]))
    doctor_menu_item = SubmenuItem('Doctor', doctor_menu, main_menu)

    # Staff submenu
    staff_menu = create_crud_menu(
        'Staff Management',
        create_staff,
        get_staff,
        get_staff_member,
        update_staff,
        delete_staff,
        db_session
    )
    staff_menu.append_item(FunctionItem('Notification', list_notification_staff, [db_session]))
    staff_menu_item = SubmenuItem('Staff', staff_menu, main_menu)

    # Staff Shift submenu
    staff_shift_menu = create_crud_menu(
        'Staff Shift Management',
        create_staff_shift,
        get_staff_shifts,
        get_staff_shift,
        update_staff_shift,
        delete_staff_shift,
        db_session
    )
    staff_shift_menu.append_item(FunctionItem('Get Staff Shift by Staff ID', get_staff_shift_by_staff_id, [db_session]))
    staff_shift_menu_item = SubmenuItem('Staff Shift', staff_shift_menu, main_menu)

    # Patient submenu
    patient_menu = create_crud_menu(
        'Patient Management',
        create_patient,
        get_patients,
        get_patient,
        update_patient,
        delete_patient,
        db_session
    )
    patient_menu.append_item(FunctionItem('Notification', list_notification_patient, [db_session]))
    patient_menu_item = SubmenuItem('Patient', patient_menu, main_menu)

    # Test Record submenu
    test_record_menu = create_crud_menu(
        'Test Record Management',
        create_test_record,
        get_test_records,
        get_test_record,
        update_test_record,
        delete_test_record,
        db_session
    )
    test_record_menu_item = SubmenuItem('Test Record', test_record_menu, main_menu)

    # Appointments submenu
    appointments_menu = ConsoleMenu('Appointments Management')
    appointments_menu.append_item(FunctionItem('Create', create_appointment, [db_session]))
    appointments_menu.append_item(FunctionItem('Create open Appointment', create_open_appointment, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by DoctorID', get_appointment_by_doc_id, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by Speciality', get_appointments_by_speciality, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by PatientID', get_appointment_by_patient_id, [db_session]))
    appointments_menu.append_item(FunctionItem('Update Appointment', update_appointment, [db_session]))
    appointments_menu.append_item(FunctionItem('Delete Appointment', delete_appointment, [db_session]))
    appointments_menu_item = SubmenuItem('Appointment', appointments_menu, main_menu)

    # Medical Histroy submenu
    history_menu = ConsoleMenu('Medical History Management')
    history_menu.append_item(FunctionItem('Create', create_medical_history, [db_session]))
    history_menu.append_item(FunctionItem('Get Medical History by DoctorID', get_medical_history_by_doc_id, [db_session]))
    history_menu.append_item(FunctionItem('Get Medical History by PatientID', get_medical_history_by_patient_id, [db_session]))
    history_menu.append_item(FunctionItem('Update', update_medical_history, [db_session]))
    history_menu.append_item(FunctionItem('Delete', delete_medical_history, [db_session]))
    history_menu_item = SubmenuItem('Medical History', history_menu, main_menu)

    bed_menu = ConsoleMenu('Bed Management')
    bed_menu.append_item(FunctionItem('list available Bed', get_available_bed, [db_session]))
    bed_menu.append_item(FunctionItem('list occupied Bed', get_occupied_bed, [db_session]))
    bed_menu.append_item(FunctionItem('Assign bed to patient', assigne_bed, [db_session]))
    bed_menu.append_item(FunctionItem('Release bed', release_bed, [db_session]))
    bed_menu_item = SubmenuItem('Bed Management', bed_menu, main_menu)

    # Add submenus to main menu
    main_menu.append_item(doctor_menu_item)
    main_menu.append_item(staff_menu_item)
    main_menu.append_item(staff_shift_menu_item)
    main_menu.append_item(patient_menu_item)
    main_menu.append_item(test_record_menu_item)
    main_menu.append_item(appointments_menu_item)
    main_menu.append_item(history_menu_item)
    main_menu.append_item(bed_menu_item)

    # Help menu item
    main_menu.append_item(FunctionItem("Help", display_help, [db_session, help_data]))

    # Show the menu
    main_menu.show()

def create_patient_menu(db_session: Session, help_data):
    """
    Create the patient menu for the Hospital Management System.

    Args:
        db_session: Database session.
    """
    main_menu = ConsoleMenu('patient menu', 'Please select an option')

    # Test Record submenu
    test_record_menu = create_crud_menu(
        'Test Record Management',
        create_test_record,
        get_test_records,
        get_test_record,
        update_test_record,
        delete_test_record,
        db_session
    )
    test_record_menu_item = SubmenuItem('Test Record', test_record_menu, main_menu)

    # Appointments submenu
    appointments_menu = ConsoleMenu('Appointments Management')
    appointments_menu.append_item(FunctionItem('Create', create_appointment, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by Speciality', get_appointments_by_speciality, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by DoctorID', get_appointment_by_doc_id, [db_session]))
    appointments_menu.append_item(FunctionItem('Get Appointment by PatientID', get_appointment_by_patient_id, [db_session]))
    appointments_menu.append_item(FunctionItem('Update Appointment', update_appointment, [db_session]))
    appointments_menu.append_item(FunctionItem('Delete Appointment', delete_appointment, [db_session]))
    appointments_menu_item = SubmenuItem('Appointment', appointments_menu, main_menu)

    # Medical Histroy submenu
    history_menu = ConsoleMenu('Medical History Management')
    history_menu.append_item(FunctionItem('Create', create_medical_history, [db_session]))
    history_menu.append_item(FunctionItem('Get Medical History by DoctorID', get_medical_history_by_doc_id, [db_session]))
    history_menu.append_item(FunctionItem('Get Medical History by PatientID', get_medical_history_by_patient_id, [db_session]))
    history_menu.append_item(FunctionItem('Update', update_medical_history, [db_session]))
    history_menu.append_item(FunctionItem('Delete', delete_medical_history, [db_session]))
    history_menu_item = SubmenuItem('Medical History', history_menu, main_menu)

    # Add submenus to main menu
    main_menu.append_item(test_record_menu_item)
    main_menu.append_item(appointments_menu_item)
    main_menu.append_item(history_menu_item)

    # Help menu item
    main_menu.append_item(FunctionItem("Help", display_help, [db_session, help_data]))

    # Show the menu
    main_menu.show()

def login():
    """Handles user login"""
    print("\n=== User Login ===")
    username = input("Enter UserName: ")
    password = pwinput.pwinput(prompt='Enter Password: ', mask='*')

    login_system = LoginSystem(db_path='login/login.db')
    _, role = login_system.login_user(username, password)

    if role is not None:
        help_data = load_help_data("help_qa.json")
        with get_db_cli() as db:
            create_main_menu(db, help_data)


def patient_login():
    """Handles patient login"""
    print("\n=== Patient Login by patientid ===")
    userid = input("Enter patientid: ")

    # check if the patient id exists
    with get_db_cli() as db:
        patient = db_ops.get_patient(db, userid)
        if patient is None:
            print("Error: Invalid Patient ID")
            time.sleep(1)
            return
        else:
            print("Welcome, ", patient.Patient_Name)
            time.sleep(1)
            help_data = load_help_data("help_qa.json")
            create_patient_menu(db, help_data)


def load_help_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            #print("Loaded help data:", data)  # Debug print
            return data
    except FileNotFoundError:
        print("Error: Help data file not found.")
        return {"questions": []}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {"questions": []}
    
def execute_query(db_session, query):
    try:
        # Execute the query
        result_proxy = db_session.execute(text(query))
        results = result_proxy.fetchall()  # Fetch all results

        if results:
            # Get column names from the result (this works dynamically based on the query)
            column_names = result_proxy.keys()

            # Create a PrettyTable instance and set field names to column names dynamically
            table = PrettyTable()
            table.field_names = column_names  # Set table headers dynamically based on query result

            # Add rows to the table
            for row in results:
                table.add_row(row)

            print(table)
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error executing query: {e}")

    input("Press Enter to return to the menu...")

def display_help(db_session, help_data):
    """
    Display the help menu and execute queries based on user selection.
    
    Args:
        db_session: Database session for executing queries.
        help_data: JSON data containing categories, questions, and queries.
    """
    while True:
        print("\n=== Help Menu ===")
        categories = help_data.get("questions", [])
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category['category']}")

        print("0. Return to Main Menu")
        try:
            category_idx = int(input("\nSelect a category by index (0 to 4): ")) - 1
            if category_idx == -1:
                return  # Exit to the main menu

            if 0 <= category_idx < len(categories):
                category = categories[category_idx]
                questions = category.get("questions", [])
                print(f"\nCategory: {category['category']}")
                for q_idx, question in enumerate(questions, start=1):
                    print(f"  {q_idx}. {question['question']}")

                print("  0. Return to Category Selection")
                question_idx = int(input("\nSelect a question by index: ")) - 1
                if question_idx == -1:
                    continue  # Return to category selection
                
                if 0 <= question_idx < len(questions):
                    query = questions[question_idx].get("query")
                    execute_query(db_session, query)
                else:
                    print("Invalid question index. Please try again.")
            else:
                print("Invalid category index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    '''
    Main Method
    '''
    menu = ConsoleMenu("Login Interface", "Please select an option")

    # Login menu item
    login_item = FunctionItem("Login", login)
    patient_login_item = FunctionItem("Patient Login", patient_login)

    # Add menu items
    menu.append_item(login_item)
    menu.append_item(patient_login_item)

    # Show the menu
    menu.show()


# Run the main menu
if __name__ == '__main__':
    main()
