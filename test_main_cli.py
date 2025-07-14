import unittest
from datetime import datetime
from unittest.mock import MagicMock
from db_operator import get_staff_shift_by_staff_id, create_staff_shift, update_patient, delete_doctor
from models import StaffShift, Patient, Doctor
from schemas import StaffShiftCreate, PatientCreate

class TestDbOperator(unittest.TestCase):

    # test READ
    def test_get_staff_shift_by_staff_id(self):
        # Create a mock database session
        db_session = MagicMock()

        # Create a mock query result
        mock_shifts = [
            StaffShift(Shift_ID=1, Staff_ID=1, Shift_Start='2024-11-01 08:00:00', Shift_End='2024-11-01 16:00:00'),
            StaffShift(Shift_ID=2, Staff_ID=1, Shift_Start='2024-11-02 09:00:00', Shift_End='2024-11-02 17:00:00')
        ]

        # Configure the mock session to return the mock query result
        db_session.query().filter().all.return_value = mock_shifts

        # Call the function with the mock session and a staff_id
        result = get_staff_shift_by_staff_id(db_session, 1)

        # Assert that the result matches the mock query result
        self.assertEqual(result, mock_shifts)
        self.assertEqual(result[0].Shift_ID, 1)
        self.assertEqual(result[0].Staff_ID, 1)
        self.assertEqual(result[0].Shift_Start, '2024-11-01 08:00:00')
        self.assertEqual(result[0].Shift_End, '2024-11-01 16:00:00')

    # test CREATE
    def test_create_staff_shift(self):
        # Create a mock database session
        db_session = MagicMock()

        # Create a mock staff shift data
        staff_shift_data = StaffShiftCreate(
            Staff_ID=1,
            Shift_Start='2024-11-01 08:00:00',
            Shift_End='2024-11-01 16:00:00'
        )

        # Create a mock staff shift object
        mock_staff_shift = StaffShift(
            Shift_ID=1,
            Staff_ID=1,
            Shift_Start='2024-11-01 08:00:00',
            Shift_End='2024-11-01 16:00:00'
        )

        # Configure the mock session to return the mock staff shift object
        db_session.add.return_value = None
        db_session.commit.return_value = None
        db_session.refresh.return_value = None
        db_session.query().filter().first.return_value = mock_staff_shift

        # Call the function with the mock session and staff shift data
        result = create_staff_shift(db_session, staff_shift_data)

        # Assert that the result matches the mock staff shift object
        self.assertEqual(result.Staff_ID, 1)
        self.assertEqual(result.Shift_Start, datetime.strptime('2024-11-01 08:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(result.Shift_End, datetime.strptime('2024-11-01 16:00:00', '%Y-%m-%d %H:%M:%S'))

    # test UPDATE
    def test_update_patient(self):
        # Create a mock database session
        db_session = MagicMock()

        # Create a mock patient update data
        patient_update_data = PatientCreate(
            Patient_ID=1,
            Patient_Name='John Smith',
            Patient_Records='Heart Attack',
            Phone_Num='555-123455',
            Email='john.smith@example.com'
        )

        # Create a mock patient object
        mock_patient = Patient(
            Patient_ID=1,
            Patient_Name='John Smith 2',
            Patient_Records='Heart Attack 2',
            Phone_Num='555-123455',
            Email='john.smith@example.com'
        )

        # Configure the mock session to return the mock patient object
        db_session.query().filter().first.return_value = mock_patient

        # Call the function with the mock session, patient ID, and update data
        result = update_patient(db_session, 1, patient_update_data)

        # Assert that the result matches the updated patient object
        self.assertEqual(result.Patient_ID, 1)
        self.assertEqual(result.Patient_Name, 'John Smith')
        self.assertEqual(result.Patient_Records, 'Heart Attack')
        self.assertEqual(result.Phone_Num, '555-123455')
        self.assertEqual(result.Email, 'john.smith@example.com')

    # test DELETE
    def test_delete_doctor(self):
        # Create a mock database session
        db_session = MagicMock()

        # Create a mock doctor object
        mock_doctor = Doctor(
            Doc_ID=1,
            Doc_Name='John Smith',
            Speciality='Cardiology',
            Phone_Num='123-456-7890',
            Email='john.smith@hospital.com'
        )

        # Configure the mock session to return the mock doctor object
        db_session.query().filter().first.return_value = mock_doctor

        # Call the function with the mock session and doctor ID
        result = delete_doctor(db_session, 1)

        # Assert that the result matches the mock doctor object
        self.assertEqual(result.Doc_ID, 1)
        self.assertEqual(result.Doc_Name, 'John Smith')
        self.assertEqual(result.Speciality, 'Cardiology')
        self.assertEqual(result.Phone_Num, '123-456-7890')
        self.assertEqual(result.Email, 'john.smith@hospital.com')

        # Assert that the delete and commit methods were called
        db_session.delete.assert_called_once_with(mock_doctor)
        db_session.commit.assert_called_once()
    
if __name__ == '__main__':
    unittest.main()

