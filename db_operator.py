"""
Database Operations for Hospital Management System

This module defines CRUD operations for managing doctors, staff, patients, 
and test records in a hospital management system. It uses SQLAlchemy for ORM 
interactions and defines functions to perform operations on the database.

Features:
- Create, Read, Update, Delete operations for:
    - Doctors
    - Staff
    - Patients
    - Test Records
    - Appoinments
    - Medical History
    - Beds
    - Prescriptions
    - Notifications

Modules Required:
- sqlalchemy: For ORM operations.
- models: Contains database table models.
- schemas: Contains data validation and creation schemas.
- typing: Provides type hints for better code clarity.

"""
from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Doctor, Staff, StaffShift, Patient, TestRecord, Appointment, MedicalHistory, Bed, Prescription, PrescriptionDetail, Notification

from schemas import DoctorCreate, StaffCreate, StaffShiftCreate, PatientCreate, TestRecordCreate, AppointmentCreate, MedicalHistoryCreate, BedCreate, PrescriptionCreate, PrescriptionDetailCreate, NotificationCreate


# Doctor API 
def create_doctor(db: Session, doctor: DoctorCreate) -> Doctor:
    """
    Create a new doctor in the database.

    Args:
        db (Session): Database session.
        doctor (DoctorCreate): Data for creating a new doctor.

    Returns:
        Doctor: The newly created doctor record.
    """
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctors(db: Session) -> List[Doctor]:
    """
    Retrieve all doctors from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Doctor]: A list of all doctors.
    """
    return db.query(Doctor).all()


def get_doctor(db: Session, doctor_id: int) -> Optional[Doctor]:
    """
    Retrieve a specific doctor by ID.

    Args:
        db (Session): Database session.
        doctor_id (int): ID of the doctor to retrieve.

    Returns:
        Optional[Doctor]: The doctor record, if found; otherwise, None.
    """
    return db.query(Doctor).filter(Doctor.Doc_ID == doctor_id).first()


def update_doctor(db: Session, doctor_id: int, doctor: DoctorCreate) -> Optional[Doctor]:
    """
    Update an existing doctor's details.

    Args:
        db (Session): Database session.
        doctor_id (int): ID of the doctor to update.
        doctor (DoctorCreate): Updated doctor data.

    Returns:
        Optional[Doctor]: The updated doctor record, if found; otherwise, None.
    """
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        for key, value in doctor.dict().items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor


def delete_doctor(db: Session, doctor_id: int) -> Optional[Doctor]:
    """
    Delete a doctor from the database.

    Args:
        db (Session): Database session.
        doctor_id (int): ID of the doctor to delete.

    Returns:
        Optional[Doctor]: The deleted doctor record, if found; otherwise, None.
    """
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor


# Staff API
def create_staff(db: Session, staff: StaffCreate) -> Staff:
    """
    Create a new staff member in the database.

    Args:
        db (Session): Database session.
        staff (StaffCreate): Data for creating a new staff member.

    Returns:
        Staff: The newly created staff record.
    """
    db_staff = Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def get_staff(db: Session) -> List[Staff]:
    """
    Retrieve all staff members from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Staff]: A list of all staff members.
    """
    return db.query(Staff).all()


def get_staff_member(db: Session, staff_id: int) -> Optional[Staff]:
    """
    Retrieve a specific staff member by ID.

    Args:
        db (Session): Database session.
        staff_id (int): ID of the staff member to retrieve.

    Returns:
        Optional[Staff]: The staff record, if found; otherwise, None.
    """
    return db.query(Staff).filter(Staff.Staff_ID == staff_id).first()


def update_staff(db: Session, staff_id: int, staff: StaffCreate) -> Optional[Staff]:
    """
    Update an existing staff member's details.

    Args:
        db (Session): Database session.
        staff_id (int): ID of the staff member to update.
        staff (StaffCreate): Updated staff data.

    Returns:
        Optional[Staff]: The updated staff record, if found; otherwise, None.
    """
    db_staff = get_staff_member(db, staff_id)
    if db_staff:
        for key, value in staff.dict().items():
            setattr(db_staff, key, value)
        db.commit()
        db.refresh(db_staff)
    return db_staff


def delete_staff(db: Session, staff_id: int) -> Optional[Staff]:

    db_staff = get_staff_member(db, staff_id)
    if db_staff:
        db.delete(db_staff)
        db.commit()
    return db_staff


#StaffShift API
def create_staff_shift(db: Session, staff_shift: StaffShiftCreate) -> StaffShift:
    """
    Create a new staff shift in the database.

    Args:
        db (Session): Database session.
        staff_shift (StaffShiftCreate): Data for creating a new staff shift.

    Returns:
        StaffShift: The newly created staff shift record.
    """
    db_staff_shift = StaffShift(**staff_shift.dict())
    db.add(db_staff_shift)
    db.commit()
    db.refresh(db_staff_shift)
    return db_staff_shift

def get_staff_shifts(db: Session) -> List[StaffShift]:
    """
    Retrieve all staff shifts from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[StaffShift]: A list of all staff shifts.
    """
    return db.query(StaffShift).all()

def get_staff_shift(db: Session, shift_id: int) -> Optional[StaffShift]:
    """
    Retrieve a specific staff shift by ID.

    Args:
        db (Session): Database session.
        shift_id (int): ID of the staff shift to retrieve.

    Returns:
        Optional[StaffShift]: The staff shift record, if found; otherwise, None.
    """
    return db.query(StaffShift).filter(StaffShift.Shift_ID == shift_id).first()

def get_staff_shift_by_staff_id(db: Session, staff_id: int) -> Optional[StaffShift]:
    """
    Retrieve a specific staff shift by staff ID.

    Args:
        db (Session): Database session.
        staff_id (int): ID of the staff to retrieve.

    Returns:
        Optional[StaffShift]: The staff shift record, if found; otherwise, None.
    """
    return db.query(StaffShift).filter(StaffShift.Staff_ID == staff_id).all()

def update_staff_shift(db: Session, shift_id: int, staff_shift: StaffShiftCreate) -> Optional[StaffShift]:
    """
    Update an existing staff shift's details.

    Args:
        db (Session): Database session.
        shift_id (int): ID of the staff shift to update.
        staff_shift (StaffShiftCreate): Updated staff shift data.

    Returns:
        Optional[StaffShift]: The updated staff shift record, if found; otherwise, None.
    """
    db_staff_shift = get_staff_shift(db, shift_id)
    if db_staff_shift:
        for key, value in staff_shift.dict().items():
            setattr(db_staff_shift, key, value)
        db.commit()
        db.refresh(db_staff_shift)
    return db_staff_shift

def delete_staff_shift(db: Session, shift_id: int) -> Optional[StaffShift]:
    """
    Delete a staff shift from the database.

    Args:
        db (Session): Database session.
        shift_id (int): ID of the staff shift to delete.

    Returns:
        Optional[StaffShift]: The deleted staff shift record, if found; otherwise, None.
    """
    db_staff_shift = get_staff_shift(db, shift_id)
    if db_staff_shift:
        db.delete(db_staff_shift)
        db.commit()
    return db_staff_shift


# Patient API
def create_patient(db: Session, patient: PatientCreate) -> Patient:
    """
    Create a new patient in the database.

    Args:
        db (Session): Database session.
        patient (PatientCreate): Data for creating a new patient.

    Returns:
        Patient: The newly created patient record.
    """
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patients(db: Session) -> List[Patient]:
    """
    Retrieve all patients from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Patient]: A list of all patients.
    """
    return db.query(Patient).all()


def get_patient(db: Session, patient_id: int) -> Optional[Patient]:
    """
    Retrieve a specific patient by ID.

    Args:
        db (Session): Database session.
        patient_id (int): ID of the patient to retrieve.

    Returns:
        Optional[Patient]: The patient record, if found; otherwise, None.
    """
    return db.query(Patient).filter(Patient.Patient_ID == patient_id).first()


def update_patient(db: Session, patient_id: int, patient: PatientCreate) -> Optional[Patient]:
    """
    Update an existing patient's details.

    Args:
        db (Session): Database session.
        patient_id (int): ID of the patient to update.
        patient (PatientCreate): Updated patient data.

    Returns:
        Optional[Patient]: The updated patient record, if found; otherwise, None.
    """
    db_patient = get_patient(db, patient_id)
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int) -> Optional[Patient]:
    """
    Delete a patient from the database.

    Args:
        db (Session): Database session.
        patient_id (int): ID of the patient to delete.

    Returns:
        Optional[Patient]: The deleted patient record, if found; otherwise, None.
    """
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient


# TestRecord API
def create_test_record(db: Session, test_record: TestRecordCreate) -> TestRecord:
    """
    Create a new test record in the database.

    Args:
        db (Session): Database session.
        test_record (TestRecordCreate): Data for creating a new test record.

    Returns:
        TestRecord: The newly created test record.
    """
    db_test_record = TestRecord(**test_record.dict())
    db.add(db_test_record)
    db.commit()
    db.refresh(db_test_record)
    return db_test_record


def get_test_records(db: Session) -> List[TestRecord]:
    """
    Retrieve all test records from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[TestRecord]: A list of all test records.
    """
    return db.query(TestRecord).all()


def get_test_record(db: Session, record_id: int) -> Optional[TestRecord]:
    """
    Retrieve a specific test record by ID.

    Args:
        db (Session): Database session.
        record_id (int): ID of the test record to retrieve.

    Returns:
        Optional[TestRecord]: The test record, if found; otherwise, None.
    """
    return db.query(TestRecord).filter(TestRecord.Record_ID == record_id).first()


def update_test_record(db: Session, record_id: int, test_record: TestRecordCreate) -> Optional[TestRecord]:
    """
    Update an existing test record's details.

    Args:
        db (Session): Database session.
        record_id (int): ID of the test record to update.
        test_record (TestRecordCreate): Updated test record data.

    Returns:
        Optional[TestRecord]: The updated test record, if found; otherwise, None.
    """
    db_test_record = get_test_record(db, record_id)
    if db_test_record:
        for key, value in test_record.dict().items():
            setattr(db_test_record, key, value)
        db.commit()
        db.refresh(db_test_record)
    return db_test_record


def delete_test_record(db: Session, record_id: int) -> Optional[TestRecord]:
    """
    Delete a test record from the database.

    Args:
        db (Session): Database session.
        record_id (int): ID of the test record to delete.

    Returns:
        Optional[TestRecord]: The deleted test record, if found; otherwise, None.
    """
    db_test_record = get_test_record(db, record_id)
    if db_test_record:
        db.delete(db_test_record)
        db.commit()
    return db_test_record


# Appointment API
def create_appointment(db: Session, appointment: AppointmentCreate) -> Appointment:
    """
    Create a new appointment in the database.

    Args:
        db (Session): Database session.
        appointment (AppointmentCreate): Data for creating a new appointment.

    Returns:
        Appointment: The newly created appointment record.
    """
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session) -> List[Appointment]:
    """
    Retrieve all appointments from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Appointment]: A list of all appointments.
    """
    return db.query(Appointment).all()


def get_appointment(db: Session, appointment_id: int) -> Optional[Appointment]:
    """
    Retrieve a specific appointment by ID.

    Args:
        db (Session): Database session.
        appointment_id (int): ID of the appointment to retrieve.

    Returns:
        Optional[Appointment]: The appointment record, if found; otherwise, None.
    """
    return db.query(Appointment).filter(Appointment.Appointment_ID == appointment_id).first()


def update_appointment(db: Session, appointment_id: int, appointment: AppointmentCreate) -> Optional[Appointment]:
    """
    Update an existing appointment's details.

    Args:
        db (Session): Database session.
        appointment_id (int): ID of the appointment to update.
        appointment (AppointmentCreate): Updated appointment data.

    Returns:
        Optional[Appointment]: The updated appointment record, if found; otherwise, None.
    """
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment:
        for key, value in appointment.dict().items():
            setattr(db_appointment, key, value)
        db.commit()
        db.refresh(db_appointment)
    return db_appointment


def delete_appointment(db: Session, appointment_id: int) -> Optional[Appointment]:
    """
    Delete an appointment from the database.

    Args:
        db (Session): Database session.
        appointment_id (int): ID of the appointment to delete.

    Returns:
        Optional[Appointment]: The deleted appointment record, if found; otherwise, None.
    """
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment


def get_appointments_by_doctor_id(db: Session, doctor_id: int):
    """
    Query appointment information based on doctor ID, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        doctor_id (int): Doctor ID

    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        Appointment.Appointment_ID,
        Appointment.Appointment_Date,
        Appointment.Statusof,
        Appointment.Typeof,
        Appointment.Speciality,
        Appointment.Notes,
    ).filter(Appointment.Doc_ID == doctor_id).all()


def get_appointments_by_speciality(db: Session, speciality: str) -> List[dict]:
    """
    Query appointment information based on speciality, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        speciality (str): Speciality of the doctor

    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        Appointment.Appointment_ID,
        Appointment.Appointment_Date,
        Appointment.Statusof,
        Appointment.Typeof,
        Appointment.Speciality,
        Appointment.Notes).filter(Appointment.Speciality == speciality).all()

def get_appointments_by_patient_id(db: Session, patient_id: int) -> List[dict]:
    """
    Query appointment information based on patient ID, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        patient_id (int): Patient ID

    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        Appointment.Appointment_ID,
        Appointment.Appointment_Date,
        Appointment.Statusof,
        Appointment.Typeof,
        Appointment.Speciality,
        Appointment.Notes
    ).filter(Appointment.Patient_ID == patient_id).all()


# Medical History API
def create_medical_history(db: Session, history: MedicalHistoryCreate) -> MedicalHistory:
    """
    Create a new appointment in the database.

    Args:
        db (Session): Database session.
        history (MedicalHistoryCreate): Data for creating a new MedicalHistory.

    Returns:
        Appointment: The newly created MedicalHistory record.
    """
    db_history = MedicalHistory(**history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


def get_medical_historys(db: Session) -> List[MedicalHistory]:
    """
    Retrieve all MedicalHistory from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[MedicalHistory]: A list of all MedicalHistory.
    """
    return db.query(MedicalHistory).all()


def get_medical_history(db: Session, history_id: int) -> Optional[MedicalHistory]:
    """
    Retrieve a specific MedicalHistory by ID.

    Args:
        db (Session): Database session.
        history_id (int): ID of the medical history to retrieve.

    Returns:
        Optional[MedicalHistory]: The medical history record, if found; otherwise, None.
    """
    return db.query(MedicalHistory).filter(MedicalHistory.History_ID == history_id).first()


def update_medical_history(db: Session, history_id: int, history: MedicalHistoryCreate) -> Optional[MedicalHistory]:
    """
    Update an existing appointment's details.

    Args:
        db (Session): Database session.
        history_id (int): ID of the Medical History to update.
        History (MedicalHistoryCreate): Updated Medical History data.

    Returns:
        Optional[MedicalHistory]: The updated medical history record, if found; otherwise, None.
    """
    db_history = get_medical_history(db, history_id)
    if db_history:
        for key, value in history.dict().items():
            setattr(db_history, key, value)
        db.commit()
        db.refresh(db_history)
    return db_history


def delete_medical_history(db: Session, history_id: int) -> Optional[MedicalHistory]:
    """
    Delete an Medical History from the database.

    Args:
        db (Session): Database session.
        history_id (int): ID of the history to delete.

    Returns:
        Optional[MedicalHistory]: The deleted Medical History record, if found; otherwise, None.
    """
    db_history = get_medical_history(db, history_id)
    if db_history:
        db.delete(db_history)
        db.commit()
    return db_history


def get_medical_history_by_doctor_id(db: Session, doctor_id: int) -> List[dict]:
    """
    Query Medical History information based on doctor ID, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        doctor_id (int): Doctor ID

    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        MedicalHistory.History_ID,
        MedicalHistory.Diagnosis,
        MedicalHistory.Treatment,
        MedicalHistory.Record_Date,
        Doctor.Doc_Name,
        Patient.Patient_Name
    ).join(Doctor, MedicalHistory.Doc_ID == Doctor.Doc_ID)\
     .join(Patient, MedicalHistory.Patient_ID == Patient.Patient_ID)\
     .filter(MedicalHistory.Doc_ID == doctor_id).all()


def get_medical_history_by_patient_id(db: Session, patient_id: int) -> List[dict]:
    """
    Query Medical History information based on patient ID, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        patient_id (int): Patient ID

    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        MedicalHistory.History_ID,
        MedicalHistory.Diagnosis,
        MedicalHistory.Treatment,
        MedicalHistory.Record_Date,
        Doctor.Doc_Name,
        Patient.Patient_Name
    ).join(Doctor, MedicalHistory.Doc_ID == Doctor.Doc_ID)\
     .join(Patient, MedicalHistory.Patient_ID == Patient.Patient_ID)\
     .filter(MedicalHistory.Patient_ID == patient_id).all()


def get_bed(db: Session, bed_id: int) -> Optional[Bed]:
    """
    Retrieve a specific Bed by ID.

    Args:
        db (Session): Database session.
        bed_id (int): ID of the Bed to retrieve.

    Returns:
        Optional[Bed]: The Bed record, if found; otherwise, None.
    """
    return db.query(Bed).filter(Bed.Bed_ID == bed_id).first()


def get_available_bed(db: Session) -> List[Bed]:
    '''
    Retrieve a available Bed.

    Args:
        db (Session): Database session.
    Returns:
        Optional[Bed]: The Bed record, if found; otherwise, None.
    '''
    return db.query(Bed).filter(Bed.Status == 'Available').all()


def get_occupied_bed(db: Session) -> List[Bed]:
    '''
    Retrieve a occupied Bed.

    Args:
        db (Session): Database session.
    Returns:
        Optional[Bed]: The Bed record, if found; otherwise, None.
    '''
    return db.query(Bed).filter(Bed.Status == 'Occupied').all()


def update_bed(db: Session, bed_id: int, bed: BedCreate) -> Optional[Bed]:
    """
    Update an existing Bed's details.

    Args:
        db (Session): Database session.
        bed_id (int): ID of the Bed to update.
        Bed (BedBase): Updated Bed data.

    Returns:
        Optional[BedBase]: The updated bed record, if found; otherwise, None.
    """
    db_bed = get_bed(db, bed_id)
    if db_bed:
        for key, value in bed.dict().items():
            setattr(db_bed, key, value)
        db.commit()
        db.refresh(db_bed)
    return db_bed


# Prescription API
def create_prescription(db: Session, prescription: PrescriptionCreate) -> Prescription:
    """
    Create a new Prescription in the database.

    Args:
        db (Session): Database session.
        prescription (PrescriptionCreate): Data for creating a new Prescription.
    Returns:
        Prescription: The newly created Prescription record.
    """
    db_prescription = Prescription(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription


def create_prescription_detail(db: Session, prescriptiondetail: PrescriptionDetailCreate) -> PrescriptionDetail:
    """
    Create a new Prescription in the database.

    Args:
        db (Session): Database session.
        prescriptiondetail (PrescriptionDetailCreate): Data for creating a new Prescriptionetail.
    Returns:
        PrescriptionDetail: The newly created Prescription Detail record.
    """
    prescriptiondetail = PrescriptionDetail(**prescriptiondetail.dict())
    db.add(prescriptiondetail)
    db.commit()
    db.refresh(prescriptiondetail)
    return prescriptiondetail


def get_prescriptions_id(db: Session, prescription_id: int) -> Optional[Prescription]:
    """
    Retrieve a specific Prescription by ID.

    Args:
        db (Session): Database session.
        Prescription_id (int): ID of the Prescription to retrieve.

    Returns:
        List[Prescription]: The Prescription record, if found; otherwise, None.
    """
    return db.query(Prescription).filter(Prescription.Prescription_ID == prescription_id).first()


def get_prescriptions_by(db: Session, searchby: str, value: int) -> List[dict]:
    """
    Query Prescription information based on patient ID or Doc ID, instead of displaying doctor ID and patient ID,
    it displays doctor's name and patient's name.

    Args:
        db (Session): SQLAlchemy Session
        column_name (str): String
        value (int): Doc_ID or Patent_ID
    Returns:
        List[dict]: List of dictionaries containing reservation information
    """
    return db.query(
        Prescription.Prescription_ID,
        Doctor.Doc_Name,
        Patient.Patient_Name,
        Prescription.Date_Issued,
        Prescription.Notes,
        PrescriptionDetail.Medication_Name,
        PrescriptionDetail.Dosage,
        PrescriptionDetail.Frequency,
        PrescriptionDetail.Duration

    ).join(Doctor, Prescription.Doctor_ID == Doctor.Doc_ID)\
     .join(Patient, Prescription.Patient_ID == Patient.Patient_ID)\
     .join(PrescriptionDetail, Prescription.Prescription_ID == PrescriptionDetail.Prescription_ID) \
     .filter(eval(searchby)).all()


def update_prescription(db: Session, prescription_id: int, prescription: PrescriptionCreate) -> Optional[Prescription]:
    """
    Update an existing Prescription's info.

    Args:
        db (Session): Database session.
        prescription_id (int): ID of the prescription to update.
        prescription (PrscriptionBase): Updated prescription data.

    Returns:
        Optional[Prescription]: The updated Prescription record, if found; otherwise, None.
    """
    db_prescription = get_prescriptions_id(db, prescription_id)
    if db_prescription:
        for key, value in prescription.dict().items():
            setattr(db_prescription, key, value)
        db.commit()
        db.refresh(db_prescription)
    return db_prescription


def get_prescriptions_detail_id(db: Session, prescriptiondetail_id: int) -> Optional[PrescriptionDetail]:
    """
    Retrieve a specific PrescriptionDetail by ID.

    Args:
        db (Session): Database session.
        prescriptiondetail_id (int): ID of the Prescription Detail to retrieve.

    Returns:
        List[PrescriptionDetail]: The PrescriptionDetail record, if found; otherwise, None.
    """
    return db.query(PrescriptionDetail).filter(PrescriptionDetail.Prescription_ID == prescriptiondetail_id).first()


def update_prescription_detail(db: Session, prescription_id: int, prescriptiondetail: PrescriptionDetailCreate) -> Optional[PrescriptionDetail]:
    """
    Update an existing Prescription's details.

    Args:
        db (Session): Database session.
        prescription_id (int): ID of the prescription to update.
        prescriptiondetail (PrscriptionDetailBase): Updated prscripiton data.

    Returns:
        Optional[PrescriptionDetail]: The updated Prescription record, if found; otherwise, None.
    """
    db_prescription_detail = get_prescriptions_detail_id(db, prescription_id)
    if db_prescription_detail:
        for key, value in prescriptiondetail.dict().items():
            setattr(db_prescription_detail, key, value)
        db.commit()
        db.refresh(db_prescription_detail)
    return db_prescription_detail


def create_notification(db: Session, notification: NotificationCreate) -> Notification:
    """
    Create a new notification in the database.

    Args:
        db (Session): Database session.
        notification (NotificationCreate): Data for the new notification.

    Returns:
        Notification: The created notification record.
    """
    db_notification = Notification(
        Recipient_Type=notification.Recipient_Type,
        Recipient_ID=notification.Recipient_ID,
        Message=notification.Message,
        Status='Unread',
        Created_At=datetime.now()
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def mark_notification_as_read(db: Session, notification_id: int) -> Optional[Notification]:
    """
    Mark a notification as read.

    Args:
        db (Session): Database session.
        notification_id (int): ID of the notification to mark as read.


    Returns:
        Notification: The updated notification record.
    """
    db_notification = db.query(Notification).filter(Notification.Notification_ID == notification_id).first()
    if db_notification:
        db_notification.Status = 'Read'
        db_notification.Read_At = datetime.now()
        db.commit()
        db.refresh(db_notification)
    return db_notification


def get_notifications_for_recipient(db: Session, recipient_type: str, recipient_id: int) -> List[Notification]:
    """
    Retrieve all notifications for a specific recipient.

    Args:
        db (Session): Database session.
        recipient_type (str): Type of the recipient ('Doctor', 'Patient', 'Staff').
        recipient_id (int): ID of the recipient.

    Returns:
        List[Notification]: List of notifications for the recipient.
    """
    return db.query(Notification).filter(
        Notification.Recipient_Type == recipient_type,
        Notification.Recipient_ID == recipient_id
    ).all()
