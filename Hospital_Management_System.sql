USE master

CREATE DATABASE Hospital;
GO

USE Hospital;
GO


CREATE TABLE Doctors (
    Doc_ID INT IDENTITY(1,1) PRIMARY KEY,
    Doc_Name VARCHAR(100) NOT NULL,
    Speciality VARCHAR(56) NOT NULL,
    Phone_Num VARCHAR(15),
    Email VARCHAR(56) NOT NULL
);

CREATE TABLE Staff (
    Staff_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Department VARCHAR(56) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Hire_Date DATE NOT NULL DEFAULT GETDATE()
);

CREATE TABLE StaffShifts (
    Shift_ID INT IDENTITY(1,1) PRIMARY KEY,
    Staff_ID INT,
    Shift_Start DATETIME NOT NULL,
    Shift_End DATETIME NOT NULL,
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

CREATE TABLE Patients (
    Patient_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_Name VARCHAR(100) NOT NULL,
    Patient_Records VARCHAR(56) NOT NULL,
    Phone_Num VARCHAR(15),
    Email VARCHAR(56) NOT NULL,
    Doc_ID INT, -- Foreign key related to Doctors
    Staff_ID INT, -- Foreign key related to Staff
    FOREIGN KEY (Doc_ID) REFERENCES Doctors(Doc_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

CREATE TABLE Test_Records (
    Record_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT, -- Foreign key related to Patients
    Record_Name VARCHAR(56),
    Test_Date DATETIME,
    Remarks VARCHAR(56),
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID)
);

CREATE TABLE Appointments (
    Appointment_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT,
    Doc_ID INT NOT NULL,
    Appointment_Date DATETIME NOT NULL,
    Statusof TINYINT DEFAULT 0,-- 0-Open, -- 1-Scheduled, 2-Completed, 3-Cancelled, 4-Expired
    Typeof VARCHAR(56), -- Empty at first, to be filled by user. Online or In Person.
    Speciality VARCHAR(56) NOT NULL, -- Easier to look for when filling an appoinmnent. 
    Notes VARCHAR(255),
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID),
    FOREIGN KEY (Doc_ID) REFERENCES Doctors(Doc_ID)
);

CREATE TABLE MedicalHistory (
    "History_ID" int IDENTITY(1,1) NOT NULL,
    "Patient_ID" int NOT NULL,
    "Doc_ID" int NOT NULL,
    "Diagnosis" varchar(255) NOT NULL,
    "Treatment" varchar(255),
    "Record_Date" datetime NOT NULL DEFAULT GETDATE(),
    PRIMARY KEY ("History_ID"),
    CONSTRAINT FK__MedicalHistory__Doc_ID FOREIGN KEY ("Doc_ID") REFERENCES "Doctors" ("Doc_ID"),
    CONSTRAINT FK__MedicalHistory__Patient_ID FOREIGN KEY ("Patient_ID") REFERENCES "Patients" ("Patient_ID")
);


CREATE TABLE Wards (
    "Ward_ID" INT IDENTITY(1,1) NOT NULL,
    "Ward_Name" VARCHAR(100) NOT NULL,
    "Capacity" INT NOT NULL,
    PRIMARY KEY ("Ward_ID")
);


CREATE TABLE Beds (
    "Bed_ID" INT IDENTITY(1,1) NOT NULL,
    "Ward_ID" INT NOT NULL,
    "Patient_ID" INT NULL, -- (NULL means the bed is available)
    "Status" VARCHAR(15) NOT NULL DEFAULT 'Available', -- Available / Occupied
    "Assigned_Date" DATETIME NULL,
    PRIMARY KEY ("Bed_ID"),
    CONSTRAINT FK__Beds__Ward_ID FOREIGN KEY ("Ward_ID") REFERENCES "Wards" ("Ward_ID"),
    CONSTRAINT FK__Beds__Patient_ID FOREIGN KEY ("Patient_ID") REFERENCES "Patients" ("Patient_ID")
);


CREATE TABLE Prescriptions (
    "Prescription_ID" INT IDENTITY(1,1) NOT NULL,
    "Patient_ID" INT NOT NULL,
    "Doctor_ID" INT NOT NULL,
    "Date_Issued" DATETIME NOT NULL,
    "Notes" VARCHAR(255),
    PRIMARY KEY ("Prescription_ID"),
    CONSTRAINT FK__Prescriptions__Patient_ID FOREIGN KEY ("Patient_ID") REFERENCES "Patients"("Patient_ID"),
    CONSTRAINT FK__Prescriptions__Doctor_ID FOREIGN KEY ("Doctor_ID") REFERENCES "Doctors"("Doc_ID")
);


CREATE TABLE Prescription_Details (
    "Detail_ID" INT IDENTITY(1,1) NOT NULL,
    "Prescription_ID" INT NOT NULL,
    "Medication_Name" VARCHAR(100) NOT NULL,
    "Dosage" VARCHAR(50) NOT NULL,
    "Frequency" VARCHAR(50) NOT NULL,
    "Duration" VARCHAR(50) NOT NULL,
    PRIMARY KEY ("Detail_ID"),
    CONSTRAINT FK__Prescription_Details__Prescription_ID FOREIGN KEY ("Prescription_ID") REFERENCES "Prescriptions"("Prescription_ID")
);

CREATE TABLE Notifications (
    "Notification_ID" INT IDENTITY(1,1) NOT NULL,
    "Recipient_Type" VARCHAR(15) NOT NULL, -- 'Doctor', 'Patient', 'Staff'
    "Recipient_ID" INT NOT NULL,          -- ID of the doctor, patient, or staff receiving the notification
    "Message" TEXT NOT NULL,              -- Notification message
    "Status" VARCHAR(15) NOT NULL DEFAULT 'Unread', -- 'Unread', 'Read'
    "Created_At" DATETIME NOT NULL DEFAULT GETDATE(), -- Timestamp of notification creation
    "Read_At" DATETIME NULL,              -- Timestamp when the notification was read
    PRIMARY KEY ("Notification_ID")
);

INSERT INTO Doctors (Doc_Name, Speciality, Phone_Num, Email)
VALUES 
('Dr. John Smith', 'Cardiologist', '123-456-7890', 'john.smith@hospital.com'),
('Dr. Emily Brown', 'Neurologist', '234-567-8901', 'emily.brown@hospital.com'),
('Dr. James Wilson', 'Orthopedic', '345-678-9012', 'james.wilson@hospital.com'),
('Dr. Lisa Adams', 'Dermatologist', '456-789-0123', 'lisa.adams@hospital.com'),
('Dr. Mark Taylor', 'Gastroenterologist', '567-890-1234', 'mark.taylor@hospital.com'),
('Dr. Sarah Clark', 'Pediatrician', '678-901-2345', 'sarah.clark@hospital.com'),
('Dr. Robert Miller', 'Ophthalmologist', '789-012-3456', 'robert.miller@hospital.com'),
('Dr. Laura Davis', 'Psychiatrist', '890-123-4567', 'laura.davis@hospital.com'),
('Dr. Brian White', 'Endocrinologist', '901-234-5678', 'brian.white@hospital.com'),
('Dr. Karen Hall', 'Radiologist', '012-345-6789', 'karen.hall@hospital.com');


INSERT INTO Staff (Name, Department, Email, Hire_Date)
VALUES 
('Alice Johnson', 'Nursing', 'alice@hospital.com', '2024-10-01'),
('Bob Williams', 'Administration', 'bob@hospital.com', '2024-10-02'),
('Charlie Brown', 'Maintenance', 'charlie@hospital.com', '2024-10-03'),
('David Davis', 'Housekeeping', 'davod@hospital.com', '2024-10-04'),
('Eva Wilson', 'Security', 'eva@hospital.com', '2024-10-05'),
('Frank Thomas', 'IT', 'frank@hospital.com', '2024-10-06'),
('Grace Lee', 'Pharmacy', 'grace@hospital.com', '2024-10-07'),
('Henry Clark', 'Dietary', 'henry@hospital.com', '2024-10-08'),
('Ivy Moore', 'Transportation', 'ivy@hospital.com', '2024-10-09'),
('Jack King', 'Billing', 'jack@hospital.com', '2024-10-10');

INSERT INTO StaffShifts (Staff_ID, Shift_Start, Shift_End)
VALUES 
(1, '2024-11-01 08:00:00', '2024-11-01 16:00:00'),
(2, '2024-11-02 09:00:00', '2024-11-02 17:00:00'),
(3, '2024-11-03 10:00:00', '2024-11-03 18:00:00'),
(4, '2024-11-04 11:00:00', '2024-11-04 19:00:00'),
(5, '2024-11-05 12:00:00', '2024-11-05 20:00:00'),
(6, '2024-11-06 13:00:00', '2024-11-06 21:00:00'),
(7, '2024-11-07 14:00:00', '2024-11-07 22:00:00'),
(8, '2024-11-08 15:00:00', '2024-11-08 23:00:00'),
(9, '2024-11-09 16:00:00', '2024-11-10 00:00:00'),
(10, '2024-11-10 17:00:00', '2024-11-11 01:00:00');

INSERT INTO Patients (Patient_Name, Patient_Records, Phone_Num, Email, Doc_ID, Staff_ID)
VALUES 
('Tom Harris', 'Heart Disease', '456-789-0123', 'tom.harris@patient.com', 1, 1),
('Linda Carter', 'Migraines', '567-890-1234', 'linda.carter@patient.com', 2, 2),
('George Anderson', 'Fractured Arm', '678-901-2345', 'george.anderson@patient.com', 3, 3),
('Helen Moore', 'Skin Rash', '789-012-3456', 'helen.moore@patient.com', 4, 4),
('Frank Lewis', 'Stomach Pain', '890-123-4567', 'frank.lewis@patient.com', 5, 5),
('Alice King', 'Fever', '901-234-5678', 'alice.king@patient.com', 6, 6),
('Peter Evans', 'Vision Issues', '012-345-6789', 'peter.evans@patient.com', 7, 7),
('Sophia Green', 'Anxiety', '123-456-7890', 'sophia.green@patient.com', 8, 8),
('Ethan Lee', 'Diabetes', '234-567-8901', 'ethan.lee@patient.com', 9, 9),
('Grace Adams', 'Broken Leg', '345-678-9012', 'grace.adams@patient.com', 3, 10);


INSERT INTO Test_Records (Patient_ID, Record_Name, Test_Date, Remarks)
VALUES 
(1, 'ECG', '2024-10-20', 'Normal'),
(1, 'Blood Test', '2024-10-21', 'Slightly Elevated Cholesterol'),
(2, 'MRI Scan', '2024-10-22', 'No abnormalities'),
(3, 'X-Ray', '2024-10-23', 'Fracture healing well'),
(4, 'Skin Biopsy', '2024-10-25', 'Benign'),
(5, 'Endoscopy', '2024-10-26', 'Mild Gastritis'),
(6, 'Blood Test', '2024-10-27', 'High Fever Detected'),
(7, 'Eye Test', '2024-10-28', 'Prescribed Glasses'),
(8, 'Mental Health Evaluation', '2024-10-29', 'Referred to Therapy'),
(9, 'HbA1c Test', '2024-10-30', 'Controlled'),
(10, 'Bone Density Scan', '2024-10-31', 'Healing in Progress'),
(1, 'Stress Test', '2024-11-01', 'Slight Arrhythmia'),
(3, 'Follow-up X-Ray', '2024-11-02', 'Significant Improvement'),
(6, 'Blood Culture', '2024-11-03', 'Negative for Infection'),
(9, 'Glucose Tolerance Test', '2024-11-04', 'Stable');

INSERT INTO Appointments (Doc_ID, Appointment_Date, Speciality)
VALUES
( 1, '2024-12-21 09:00:00', 'Cardiologist'), 
( 2, '2024-12-22 10:30:00', 'Neurologist'),
( 3, '2024-12-23 11:45:00', 'Orthopedic'),
( 4, '2024-12-24 14:00:00', 'Dermatologist'),
( 5, '2024-12-25 16:00:00', 'Gastroenterologist'),
( 6, '2024-12-26 09:15:00', 'Pediatrician'),
( 7, '2024-12-27 13:30:00', 'Ophthalmologist'),
( 8, '2024-12-28 15:45:00', 'Psychiatrist'),
( 9, '2024-12-29 08:00:00', 'Endocrinologist'),
( 10, '2024-12-30 12:00:00', 'Radiologist'),
( 10, '2024-12-31 10:00:00', 'Radiologist'),
( 10, '2025-01-01 09:30:00', 'Radiologist'),
( 10, '2025-01-02 11:00:00', 'Radiologist'),
( 10, '2025-01-04 14:30:00', 'Radiologist'),
( 10, '2025-01-06 09:45:00', 'Radiologist'),
( 10, '2025-01-08 13:15:00', 'Radiologist');


INSERT INTO MedicalHistory ("Patient_ID", "Doc_ID", "Diagnosis", "Treatment", "Record_Date")
VALUES
(1, 1, 'Hypertension', 'Lifestyle changes and medication', '2024-01-15'),
(1, 2, 'Diabetes', 'Insulin therapy and diet control', '2024-01-20'),
(1, 3, 'Common Cold', 'Rest and fluids', '2024-01-25'),
(2, 1, 'Asthma', 'Inhaler prescription', '2024-02-10'),
(2, 2, 'Flu', 'Antiviral medication', '2024-02-15'),
(3, 3, 'Allergic Rhinitis', 'Antihistamines', '2024-02-20'),
(3, 1, 'Migraine', 'Pain relievers', '2024-02-25'),
(3, 2, 'Bronchitis', 'Antibiotics and rest', '2024-03-01'),
(4, 3, 'Back Pain', 'Physical therapy', '2024-03-05'),
(4, 1, 'High Cholesterol', 'Statin medication', '2024-03-10'),
(4, 2, 'Acne', 'Topical treatments', '2024-03-15'),
(5, 3, 'Eczema', 'Moisturizers and steroids', '2024-03-20'),
(5, 1, 'Osteoarthritis', 'Pain relief and physiotherapy', '2024-03-25'),
(5, 2, 'Psoriasis', 'Phototherapy and ointments', '2024-04-01'),
(6, 3, 'Gastritis', 'Proton pump inhibitors', '2024-04-05'),
(6, 1, 'Insomnia', 'Behavioral therapy', '2024-04-10'),
(6, 2, 'Pneumonia', 'Antibiotics and rest', '2024-04-15'),
(7, 3, 'Hypertension', 'Lifestyle changes', '2024-04-20'),
(7, 1, 'Diabetes', 'Oral medication', '2024-04-25'),
(7, 2, 'Fracture', 'Casting and physiotherapy', '2024-05-01'),
(8, 3, 'Headache', 'Painkillers', '2024-05-05'),
(8, 1, 'Chest Pain', 'ECG and monitoring', '2024-05-10'),
(8, 2, 'Thyroid Disorder', 'Hormone therapy', '2024-05-15'),
(9, 3, 'Sinusitis', 'Decongestants', '2024-05-20'),
(9, 1, 'Appendicitis', 'Surgery', '2024-05-25'),
(9, 2, 'Urinary Tract Infection', 'Antibiotics', '2024-06-01'),
(10, 3, 'Gout', 'Urate-lowering drugs', '2024-06-05'),
(10, 1, 'Anemia', 'Iron supplements', '2024-06-10'),
(10, 2, 'Vertigo', 'Vestibular therapy', '2024-06-15'),
(10, 3, 'Gallstones', 'Surgery', '2024-06-20');
Go



INSERT INTO Wards ("Ward_Name", "Capacity")
VALUES
('General Ward 301', 3),
('General Ward 302', 2),
('ICU 201', 2),
('ICU 202', 1),
('Pediatrics Ward 303', 3),
('Pediatrics Ward 304', 2),
('Surgical Ward 101', 3),
('Surgical Ward 102', 2),
('Maternity Ward 103', 3),
('Recovery Ward 104', 1);
GO

INSERT INTO Beds ("Ward_ID", "Patient_ID", "Status", "Assigned_Date")
VALUES
-- General Ward 301
(1, 1, 'Occupied', '2024-11-30 10:00:00'),
(1, NULL, 'Available', NULL),
(1, 2, 'Occupied', '2024-11-30 11:00:00'),
-- General Ward 302
(2, 3, 'Occupied', '2024-11-29 15:00:00'),
(2, NULL, 'Available', NULL),
-- ICU 201
(3, 4, 'Occupied', '2024-11-28 09:00:00'),
(3, NULL, 'Available', NULL),
-- ICU 202
(4, 5, 'Occupied', '2024-11-27 14:00:00'),
-- Pediatrics Ward 303
(5, 6, 'Occupied', '2024-11-30 12:00:00'),
(5, 7, 'Occupied', '2024-11-30 13:00:00'),
(5, NULL, 'Available', NULL),
-- Pediatrics Ward 304
(6, NULL, 'Available', NULL),
(6, 8, 'Occupied', '2024-11-29 16:00:00'),
-- Surgical Ward 101
(7, 9, 'Occupied', '2024-11-28 10:00:00'),
(7, NULL, 'Available', NULL),
(7, NULL, 'Available', NULL),
-- Surgical Ward 102
(8, 10, 'Occupied', '2024-11-27 17:00:00'),
(8, NULL, 'Available', NULL),
-- Maternity Ward 103
(9, NULL, 'Available', NULL),
(9, NULL, 'Available', NULL),
(9, 1, 'Occupied', '2024-11-30 14:00:00'),
-- Recovery Ward 104
(10, 2, 'Occupied', '2024-11-29 18:00:00');
GO



INSERT INTO Prescriptions ("Patient_ID", "Doctor_ID", "Date_Issued", "Notes")
VALUES
(1, 1, '2024-12-01 10:00:00', 'Take medications after meals.'),
(2, 3, '2024-12-02 11:30:00', 'Monitor closely for allergic reactions.'),
(3, 2, '2024-12-03 14:45:00', 'Apply ointment twice daily.'),
(4, 5, '2024-12-01 09:15:00', 'Complete the full course of antibiotics.'),
(5, 7, '2024-11-30 13:20:00', 'Pain relief as needed.'),
(6, 4, '2024-11-29 16:40:00', 'Daily dosage required.'),
(7, 6, '2024-11-28 08:10:00', 'Follow up in one week.'),
(8, 8, '2024-11-27 12:50:00', 'Take with food.'),
(9, 9, '2024-11-26 10:20:00', 'Use medication for 5 days.'),
(10, 10, '2024-11-25 15:30:00', 'Stay hydrated.'),
(1, 2, '2024-11-24 11:00:00', 'Avoid sunlight after applying medication.'),
(2, 4, '2024-11-23 13:45:00', 'Check blood pressure daily.'),
(3, 6, '2024-11-22 09:30:00', 'Apply once every night.'),
(4, 7, '2024-11-21 14:10:00', 'No alcohol during treatment.'),
(5, 9, '2024-11-20 08:20:00', 'Contact doctor if symptoms persist.');
GO

INSERT INTO Prescription_Details ("Prescription_ID", "Medication_Name", "Dosage", "Frequency", "Duration")
VALUES
(1, 'Amoxicillin', '500mg', 'Twice a day', '7 days'),
(1, 'Ibuprofen', '200mg', 'Three times a day', '5 days'),
(2, 'Ciprofloxacin', '250mg', 'Twice a day', '10 days'),
(3, 'Paracetamol', '650mg', 'Three times a day', '5 days'),
(3, 'Hydrocortisone Cream', '1%', 'Twice a day', '7 days'),
(4, 'Metformin', '500mg', 'Once daily', '30 days'),
(5, 'Omeprazole', '20mg', 'Once daily', '14 days'),
(6, 'Losartan', '50mg', 'Once daily', '30 days'),
(7, 'Cetirizine', '10mg', 'Once daily', '7 days'),
(8, 'Azithromycin', '500mg', 'Once daily', '3 days'),
(9, 'Prednisone', '20mg', 'Once daily', '5 days'),
(10, 'Loratadine', '10mg', 'Once daily', '10 days'),
(11, 'Doxycycline', '100mg', 'Twice a day', '7 days'),
(12, 'Fluconazole', '150mg', 'Once weekly', '2 weeks'),
(13, 'Fexofenadine', '180mg', 'Once daily', '5 days'),
(14, 'Hydroxyzine', '25mg', 'Once at night', '7 days'),
(15, 'Clindamycin', '300mg', 'Four times a day', '10 days'),
(15, 'Ranitidine', '150mg', 'Twice daily', '14 days');
GO


INSERT INTO Notifications ("Recipient_Type", "Recipient_ID", "Message", "Status", "Created_At")
VALUES
('Doctor', 1, 'Your appointment with Patient 5 is scheduled for tomorrow.', 'Unread', GETDATE()),
('Patient', 5, 'Your appointment with Dr. Smith is confirmed for 2024-12-05.', 'Unread', GETDATE()),
('Staff', 3, 'Monthly meeting scheduled for 2024-12-10.', 'Unread', GETDATE()),
('Doctor', 2, 'New lab results are available for Patient 7.', 'Unread', GETDATE()),
('Patient', 8, 'Your lab results are ready for review.', 'Unread', GETDATE());
GO
