"""
This module defines the Pydantic schemas for a healthcare management system.
It includes schemas for Doctors, Staff, Patients, and Test Records, each 
with their respective base, create, and read models for API integration.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

# Doctors schemas
class DoctorBase(BaseModel):
    """
    Base schema for Doctor entity.

    Attributes:
        Doc_Name (str): Name of the doctor.
        Speciality (str): Specialization of the doctor.
        Phone_Num (Optional[str]): Phone number of the doctor (optional).
        Email (EmailStr): Email address of the doctor.
    """
    Doc_Name: str
    Speciality: str
    Phone_Num: Optional[str] = None
    Email: EmailStr

class DoctorCreate(DoctorBase):
    """
    Schema for creating a new Doctor record.
    Inherits all attributes from DoctorBase.
    """
    pass

class DoctorRead(DoctorBase):
    """
    Schema for reading a Doctor record.

    Attributes:
        Doc_ID (int): Unique identifier of the doctor.
    """
    Doc_ID: int
    class Config:
        from_attributes = True

# Staff schemas
class StaffBase(BaseModel):
    """
    Base schema for Staff entity.

    Attributes:
        Name (str): Name of the staff member.
        Department (str): Department the staff member belongs to.
        Email (EmailStr): Email address of the staff member.
        Hire_Date (datetime): Date of hire for the staff member.
    """
    Name: str
    Department: str
    Email: EmailStr
    Hire_Date: datetime

class StaffCreate(StaffBase):
    """
    Schema for creating a new Staff record.
    Inherits all attributes from StaffBase.
    """
    Name: str
    Department: str 
    Email: EmailStr
    Hire_Date: datetime


class StaffRead(StaffBase):
    """
    Schema for reading a Staff record.

    Attributes:
        Staff_ID (int): Unique identifier of the staff member.
    """
    Staff_ID: int
    class Config:
        from_attributes = True

class StaffShiftBase(BaseModel):
    """
    Base schema for StaffShift entity.

    Attributes:
        Staff_ID (int): ID of the staff member.
        Shift_Start (datetime): Date start of the shift.
        Shift_End (datetime): Date end of the shift.
    """
    Staff_ID: int
    Shift_Start: datetime
    Shift_End: datetime

class StaffShiftCreate(StaffShiftBase):
    """
    Schema for creating a new StaffShift record.
    Inherits all attributes from StaffShiftBase.
    """
    Staff_ID: int
    Shift_Start: datetime
    Shift_End: datetime

class StaffShiftRead(StaffShiftBase):
    """
    Schema for reading a StaffShift record.

    Attributes:
        Shift_ID (int): Unique identifier of the staff shift.
    """
    Shift_ID: int
    class Config:
        from_attributes = True

class StaffShiftUpdate(StaffShiftBase):
    """
    Schema for updating a StaffShift record.

    Attributes:
        Shift_ID (int): Unique identifier of the staff shift.
    """
    Shift_ID: int
    Shift_Start: datetime
    Shift_End: datetime
    class Config:
        from_attributes = True



# Patients schemas
class PatientBase(BaseModel):
    """
    Base schema for Patient entity.

    Attributes:
        Patient_Name (str): Name of the patient.
        Patient_Records (str): Medical records of the patient.
        Phone_Num (Optional[str]): Phone number of the patient (optional).
        Email (EmailStr): Email address of the patient.
        Doc_ID (Optional[int]): ID of the doctor assigned to the patient (optional).
        Staff_ID (Optional[int]): ID of the staff assigned to the patient (optional).
    """
    Patient_Name: str
    Patient_Records: str
    Phone_Num: Optional[str] = None
    Email: EmailStr
    Doc_ID: Optional[int] = None
    Staff_ID: Optional[int] = None

class PatientCreate(PatientBase):
    """
    Schema for creating a new Patient record.
    Inherits all attributes from PatientBase.
    """
    pass

class PatientRead(PatientBase):
    """
    Schema for reading a Patient record.

    Attributes:
        Patient_ID (int): Unique identifier of the patient.
    """
    Patient_ID: int
    class Config:
        from_attributes = True

# TestRecords schemas
class TestRecordBase(BaseModel):
    """
    Base schema for Test Record entity.

    Attributes:
        Patient_ID (int): ID of the patient associated with the test record.
        Record_Name (Optional[str]): Name of the test record (optional).
        Test_Date (Optional[datetime]): Date of the test (optional).
        Remarks (Optional[str]): Additional remarks for the test record (optional).
    """
    Patient_ID: int
    Record_Name: Optional[str] = None
    Test_Date: Optional[datetime] = None
    Remarks: Optional[str] = None

class TestRecordCreate(TestRecordBase):
    """
    Schema for creating a new Test Record.
    Inherits all attributes from TestRecordBase.
    """
    pass


class TestRecordRead(TestRecordBase):
    """
    Schema for reading a Test Record.

    Attributes:
        Record_ID (int): Unique identifier of the test record.
    """
    Record_ID: int
    class Config:
        from_attributes = True

# Appointments schemas
class AppointmentBase(BaseModel):
    """
    Base schema for Appointment entity.

    Attributes:
        Appointment_Date (datetime): Date and time of the appointment.
        Doctor_ID (int): ID of the doctor.
        Patient_ID (int): ID of the patient.
        Status (int): Status of Appointment.
        Notes (str): Note of Appointment.
    """
    Patient_ID: Optional[int] = None
    Doc_ID: int
    Appointment_Date: datetime
    Statusof: Optional[int] = None
    Typeof: Optional[str] = None
    Speciality: str
    Notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    """
    Schema for creating a new Appointment record.

    Attributes:
        Doctor_ID (int): ID of the doctor assigned to the appointment.
        Patient_ID (int): ID of the patient assigned to the appointment.
    """
    Doctor_ID: int
    Patient_ID: int


class AppointmentRead(AppointmentBase):
    """
    Schema for reading an Appointment record.

    Attributes:
        Appointment_ID (int): Unique identifier of the appointment.
    """
    Appointment_ID: int
    class Config:
        from_attributes = True


# Medical History schemas
class MedicalHistoryBase(BaseModel):
    """
    Base schema for Medical History entity.

    Attributes:
        Patient_Name (Optional[str]): Name of the patient.
        Doctor_ID (Optional[str]): Name of the doctor.

        Appointment_Date (datetime): Date and time of the appointment.
    """
    Patient_ID: int
    Doc_ID: int

    Diagnosis: Optional[str] = None
    Treatment: Optional[str] = None
    Record_Date: datetime


class MedicalHistoryCreate(MedicalHistoryBase):
    """
    Schema for creating a new Medical History record.

    Attributes:
        Doctor_ID (int): ID of the doctor assigned to the Medical History.
        Patient_ID (int): ID of the patient assigned to the Medical History.
    """
    Doctor_ID: int
    Patient_ID: int


class MedicalHistoryRead(MedicalHistoryBase):
    """
    Schema for reading an MedicalHistory record.

    Attributes:
        History_ID (int): Unique identifier of the MedicalHistory.
    """
    History_ID: int
    class Config:
        from_attributes = True


# Medical Beds schemas
class BedBase(BaseModel):
    """
    Base schema for Beds entity.

    Attributes:
        Bed_ID (int): ID of Bed.
        Ward_ID (int): Ward ID of Bed.
        Patient_ID (Optional[int]): ID of the patient.
        Status (str): Status of Bed.
        Assigned_Date (datetime): Date and time of the Assigned.
    """
    Bed_ID: int
    Ward_ID: int
    Patient_ID: Optional[int] = None
    Status: str
    Assigned_Date: Optional[datetime] = None


class BedCreate(BedBase):
    """
    Schema for creating a new Bed record.

    Attributes:
        Bed_ID (int): ID of the Bed.
        Ward_ID (int): ID of the ward where the bed is located.
    """
    Bed_ID: int
    Ward_ID: int


class BedRead(BedBase):
    """
    Schema for reading an Bed record.

    Attributes:
        Appointment_ID (int): Unique identifier of the MedicalHistory.
    """
    Bed_ID: int
    class Config:
        from_attributes = True


class PrescriptionBase(BaseModel):
    """
    Base schema for Prescription entity.

    Attributes:
        Prescription_ID (int): Unique identifier for the prescription.
        Patient_ID (int): ID of the patient receiving the prescription.
        Doctor_ID (int): ID of the doctor issuing the prescription.
        Date_Issued (datetime): Date and time when the prescription was issued.
        Notes (Optional[str]): Additional notes or instructions provided by the doctor.
    """
    Patient_ID: int
    Doctor_ID: int
    Date_Issued: datetime
    Notes: Optional[str] = None


class PrescriptionCreate(PrescriptionBase):
    """
    Schema for creating a new Prescription record.

    Attributes:
        Patient_ID (int): ID of the patient receiving the prescription.
        Doctor_ID (int): ID of the doctor issuing the prescription.
    """
    Patient_ID: int
    Doctor_ID: int
    Date_Issued: datetime
    Notes: Optional[str] = None


class PrescriptionRead(PrescriptionBase):
    """
    Schema for reading a Prescription record.

    Attributes:
        Prescription_ID (int): Unique identifier for the prescription.
    """
    Prescription_ID: int
    class Config:
        from_attributes = True


class PrescriptionDetailBase(BaseModel):
    """
    Base schema for PrescriptionDetail entity.

    Attributes:
        Detail_ID (int): Unique identifier for the prescription detail.
        Prescription_ID (int): Foreign key referencing the parent Prescription record.
        Medication_Name (str): The name of the medication prescribed.
        Dosage (str): The dosage of the medication (e.g., '500mg').
        Frequency (str): How often the medication should be taken (e.g., 'Twice a day').
        Duration (str): Duration for which the medication should be taken (e.g., '7 days').
    """
    Prescription_ID: int
    Medication_Name: str
    Dosage: str
    Frequency: str
    Duration: str


class PrescriptionDetailCreate(PrescriptionDetailBase):
    """
    Schema for creating a new PrescriptionDetail record.

    Attributes:
        Prescription_ID (int): Foreign key referencing the parent Prescription record.
    """
    Prescription_ID: int
    Medication_Name: str
    Dosage: str
    Frequency: str
    Duration: str


class PrescriptionDetailRead(PrescriptionDetailBase):
    """
    Schema for reading a PrescriptionDetail record.

    Attributes:
        Detail_ID (int): Unique identifier for the prescription detail.
    """
    Detail_ID: int
    class Config:
        from_attributes = True


class NotificationBase(BaseModel):
    """
    Base schema for Notifications entity.

    Attributes:
        Notification_ID (int): Unique identifier for the notification.
        Recipient_Type (str): Type of recipient ('Doctor', 'Patient', 'Staff').
        Recipient_ID (int): ID of the recipient.
        Message (str): Notification message.
        Status (str): Notification status ('Unread', 'Read').
        Created_At (datetime): Timestamp of when the notification was created.
        Read_At (Optional[datetime]): Timestamp of when the notification was read.
    """
    Notification_ID: int
    Recipient_Type: str
    Recipient_ID: int
    Message: str
    Status: str = "Unread"
    Created_At: datetime
    Read_At: Optional[datetime] = None


class NotificationCreate(BaseModel):
    """
    Schema for creating a new Notification record.

    Attributes:
        Recipient_Type (str): Type of recipient ('Doctor', 'Patient', 'Staff').
        Recipient_ID (int): ID of the recipient.
        Message (str): Notification message.
    """
    Recipient_Type: str
    Recipient_ID: int
    Message: str


class NotificationRead(NotificationBase):
    """
    Schema for reading a Notification record.

    Attributes:
        Notification_ID (int): Unique identifier for the notification.
    """
    Notification_ID: int
    class Config:
        from_attributes = True