"""
This module defines the SQLAlchemy ORM models for a healthcare database.

Classes:
    Doctor: Represents doctors in the healthcare system.
    Staff: Represents staff members in the healthcare system.
    Patient: Represents patients and their association with doctors and staff.
    TestRecord: Represents medical test records associated with patients.
    Appointment: Represents appointments between patients and doctors.
    MedicalHistory: Represents the medical history of patients.
    Ward: Represents hospital wards.
    Bed: Represents beds in the hospital wards.
    Prescription: Represents medical prescriptions issued to patients.
    PrescriptionDetail: Represents detailed information about medications in a prescription.

Each class corresponds to a table in the database, with relationships defined
between doctors, staff, patients, and test records.
"""
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from database import Base


class Doctor(Base):
    """
    Represents a doctor in the healthcare system.

    Attributes:
        Doc_ID (int): The primary key identifier for the doctor.
        Doc_Name (str): The full name of the doctor.
        Speciality (str): The medical specialty of the doctor.
        Phone_Num (str): The doctor's phone number (optional).
        Email (str): The doctor's email address.
        patients (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = "Doctors"

    Doc_ID = Column(Integer, primary_key=True, index=True)
    Doc_Name = Column(String, nullable=False)
    Speciality = Column(String, nullable=False)
    Phone_Num = Column(String)
    Email = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="doctor")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Staff(Base):
    """
    Represents a staff member in the healthcare system.

    Attributes:
        Staff_ID (int): The primary key identifier for the staff member.
        Name (str): The full name of the staff member.
        Department (str): The department or role of the staff member.
        Email (str): The staff member's email address.
        Hire_Date (datetime): The date when the staff member was hired.
        patients (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = "Staff"

    Staff_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Hire_Date = Column(DateTime, nullable=False)

    patients = relationship("Patient", back_populates="staff")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class StaffShift(Base):
    """
    Represents a staff shift in the healthcare system.

    Attributes:
        Shift_ID (int): The primary key identifier for the staff shift.
        Staff_ID (int): Foreign key referencing the associated staff member.
        Shift_Date (datetime): The date of the shift.
        Shift_Type (str): The type of shift (e.g., 'Morning', 'Evening', 'Night').
        Staff (relationship): Relationship to the `Staff` table.
    """
    __tablename__ = "StaffShifts"

    Shift_ID = Column(Integer, primary_key=True, index=True)
    Staff_ID = Column(Integer, ForeignKey("Staff.Staff_ID"))
    Shift_Start = Column(DateTime, nullable=False)
    Shift_End = Column(String, nullable=False)

    staff = relationship("Staff", backref="staffshifts")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Patient(Base):
    """
    Represents a patient in the healthcare system.

    Attributes:
        Patient_ID (int): The primary key identifier for the patient.
        Patient_Name (str): The full name of the patient.
        Patient_Records (str): Medical records or notes associated with the patient.
        Phone_Num (str): The patient's phone number (optional).
        Email (str): The patient's email address.
        Doc_ID (int): Foreign key referencing the associated doctor.
        Staff_ID (int): Foreign key referencing the associated staff member.
        doctor (relationship): Relationship to the `Doctor` table.
        staff (relationship): Relationship to the `Staff` table.
        test_records (relationship): Relationship to the `TestRecord` table.
    """
    __tablename__ = "Patients"

    Patient_ID = Column(Integer, primary_key=True, index=True)
    Patient_Name = Column(String, nullable=False)
    Patient_Records = Column(String, nullable=False)
    Phone_Num = Column(String)
    Email = Column(String, nullable=False)
    Doc_ID = Column(Integer, ForeignKey("Doctors.Doc_ID"))
    Staff_ID = Column(Integer, ForeignKey("Staff.Staff_ID"))

    doctor = relationship("Doctor", back_populates="patients")
    staff = relationship("Staff", back_populates="patients")
    test_records = relationship("TestRecord", back_populates="patient")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TestRecord(Base):
    """
    Represents a test record associated with a patient.

    Attributes:
        Record_ID (int): The primary key identifier for the test record.
        Patient_ID (int): Foreign key referencing the associated patient.
        Record_Name (str): Name or type of the test.
        Test_Date (datetime): Date when the test was conducted.
        Remarks (str): Additional remarks or observations about the test.
        patient (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = "Test_Records"

    Record_ID = Column(Integer, primary_key=True, index=True)
    Patient_ID = Column(Integer, ForeignKey("Patients.Patient_ID"))
    Record_Name = Column(String)
    Test_Date = Column(DateTime)
    Remarks = Column(String)

    patient = relationship("Patient", back_populates="test_records")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Appointment(Base):
    """
    Represents an appointment in the healthcare system.

    Attributes:
        Appointment_ID (int): The primary key identifier for the appointment.
        Patient_ID (int): Foreign key referencing the associated patient.
        Doc_ID (int): Foreign key referencing the associated doctor.
        Appointment_Date (datetime): The scheduled date and time of the appointment.
        Status (str): The current status of the appointment (e.g., 0-Open,  1-Scheduled, 2-Completed, 3-Cancelled, 4-Expired).
        Notes STR: Notes for the appointment.

        doctor (relationship): Relationship to the `Doctor` table.
        patient (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = "Appointments"

    Appointment_ID = Column(Integer, primary_key=True, index=True)
    Patient_ID = Column(Integer, ForeignKey("Patients.Patient_ID"))
    Doc_ID = Column(Integer, ForeignKey("Doctors.Doc_ID"), nullable=False)
    Appointment_Date = Column(DateTime, nullable=False)
    Statusof = Column(String)
    Typeof = Column(String)
    Speciality = Column(String, nullable=False)
    Notes = Column(String)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Doctor.appointments = relationship("Appointment", back_populates="doctor")
Patient.appointments = relationship("Appointment", back_populates="patient")


class MedicalHistory(Base):
    """
    Represents Medical History in the healthcare system.

    Attributes:
        History_ID (int): The primary key identifier for the Medical History.
        Patient_ID (int): Foreign key referencing the associated patient.
        Doc_ID (int): Foreign key referencing the associated doctor.
        Diagnosis (str): The Diagnosis note of Doctor.
        Treatment (str): The Treatment.
        Record_Date (datetime): Record Date.

        doctor (relationship): Relationship to the `Doctor` table.
        patient (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = 'MedicalHistory'
    History_ID = Column(Integer, primary_key=True, autoincrement=True)
    Patient_ID = Column(Integer, ForeignKey('Patients.Patient_ID'), nullable=False)
    Doc_ID = Column(Integer, ForeignKey('Doctors.Doc_ID'), nullable=False)
    Diagnosis = Column(String(255), nullable=False)
    Treatment = Column(String(255))
    Record_Date = Column(DateTime, nullable=False)

    patient = relationship("Patient", backref="medical_history")
    doctor = relationship("Doctor", backref="medical_history")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Ward(Base):
    """
    Represents Ward in the Hospital.

    Attributes:
        Ward_ID (int): The primary key identifier for the Wards.
        Ward_Name (str): The Name of Wards.
        Capacity (int): How Many bed in the Wards.

        beds (relationship): Relationship to the `Beds` table.
    """
    __tablename__ = 'Wards'
    Ward_ID = Column(Integer, primary_key=True, autoincrement=True)
    Ward_Name = Column(String(100), nullable=False)
    Capacity = Column(Integer, nullable=False)

    beds = relationship("Bed", back_populates="ward")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Bed(Base):
    """
    Represents Beds in the Hospital.

    Attributes:
        Bed_ID (int): The primary key identifier for the Beds
        Ward_ID (int): Foreign key referencing the associated Ward.
        Patient_ID (int): Foreign key referencing the associated patient.
        Status (str): The Status of Beds (Occupied, Available)
        Assigned_Date (datetime): Assigned Date

        beds (relationship): Relationship to the `Beds` table.
        patient (relationship): Relationship to the `Patient` table.
    """
    __tablename__ = 'Beds'
    Bed_ID = Column(Integer, primary_key=True, autoincrement=True)
    Ward_ID = Column(Integer, ForeignKey('Wards.Ward_ID'), nullable=False)
    Patient_ID = Column(Integer, ForeignKey('Patients.Patient_ID'))
    Status = Column(String(15), nullable=False, default='Available')
    Assigned_Date = Column(DateTime, nullable=True)

    ward = relationship("Ward", back_populates="beds")
    patient = relationship("Patient", backref="bed")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Prescription(Base):
    """
    Represents a medical prescription issued by a doctor to a patient.

    Attributes:
        Prescription_ID (int): Unique identifier for the prescription. Auto-incremented.
        Patient_ID (int): Foreign key referencing the patient receiving the prescription.
        Doctor_ID (int): Foreign key referencing the doctor issuing the prescription.
        Date_Issued (datetime): The date and time when the prescription was issued.
        Notes (str): Additional notes or instructions provided by the doctor. Optional.
        details (relationship): Relationship with the PrescriptionDetail class, representing
            the list of detailed medications prescribed under this prescription.
    """
    __tablename__ = "Prescriptions"
    Prescription_ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Patient_ID = Column(Integer, ForeignKey("Patients.Patient_ID"), nullable=False)
    Doctor_ID = Column(Integer, ForeignKey("Doctors.Doc_ID"), nullable=False)
    Date_Issued = Column(DateTime, default=datetime.now, nullable=False)
    Notes = Column(String(255), nullable=True)

    # Relationships
    details = relationship("PrescriptionDetail", back_populates="prescription")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class PrescriptionDetail(Base):
    """
    Represents the detailed information of medications under a specific prescription.

    Attributes:
        Detail_ID (int): Unique identifier for the prescription detail. Auto-incremented.
        Prescription_ID (int): Foreign key referencing the parent Prescription record.
        Medication_Name (str): The name of the medication prescribed.
        Dosage (str): The dosage of the medication (e.g., '500mg').
        Frequency (str): How often the medication should be taken (e.g., 'Twice a day').
        Duration (str): The length of time the medication should be taken (e.g., '7 days').
    """
    __tablename__ = "Prescription_Details"
    Detail_ID = Column(Integer, primary_key=True, autoincrement=True)
    Prescription_ID = Column(Integer, ForeignKey("Prescriptions.Prescription_ID"), nullable=False)
    Medication_Name = Column(String(100), nullable=False)
    Dosage = Column(String(50), nullable=False)
    Frequency = Column(String(50), nullable=False)
    Duration = Column(String(50), nullable=False)

    # Relationships
    prescription = relationship("Prescription", back_populates="details")

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Notification(Base):
    """
    Represents the detailed information of notifications for doctors, patients, and staff.

    Attributes:
        Notification_ID (int): Unique identifier for the notification. Auto-incremented primary key.
        Recipient_Type (str): The type of recipient ('Doctor', 'Patient', 'Staff').
        Recipient_ID (int): The unique identifier of the recipient.
        Message (str): The content of the notification message.
        Status (str): The current status of the notification, such as 'Unread' or 'Read'.
        Created_At (datetime): The timestamp when the notification was created.
        Read_At (datetime, optional): The timestamp when the notification was marked as read.
    """
    __tablename__ = "Notifications"

    Notification_ID = Column(Integer, primary_key=True, autoincrement=True)
    Recipient_Type = Column(String(15), nullable=False)
    Recipient_ID = Column(Integer, nullable=False)
    Message = Column(String, nullable=False)
    Status = Column(String(15), default="Unread", nullable=False)
    Created_At = Column(DateTime, default=datetime.now, nullable=False)
    Read_At = Column(DateTime, nullable=True)

    def as_dict(self):
        """
        Convert to Dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}