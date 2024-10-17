
-- Creación de la base de datos
CREATE DATABASE MedicalAppointment_DB;
GO

USE MedicalAppointment_DB;
GO

-- Esquema: Appointments
CREATE SCHEMA Appointments;
GO

-- Tabla de Appointments
CREATE TABLE Appointments.Appointment (
    AppointmentID INT IDENTITY(1,1) PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATETIME NOT NULL,
    StatusID INT NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    DeletedAt DATETIME NULL, -- Para soporte de borrado lógico
    CreatedBy INT NULL, -- Para auditoría
    UpdatedBy INT NULL -- Para auditoría
);
-- Disponibilidad de Doctores
CREATE TABLE Appointments.DoctorAvailability (
    AvailabilityID INT IDENTITY(1,1) PRIMARY KEY,
    DoctorID INT NOT NULL,
    AvailableDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE()
);
-- Estado de las Citas
CREATE TABLE Appointments.AppointmentStatus (
    StatusID INT IDENTITY(1,1) PRIMARY KEY,
    StatusName VARCHAR(50) NOT NULL
);
-- Claves foráneas
ALTER TABLE Appointments.Appointment ADD CONSTRAINT FK_Appointment_Patient FOREIGN KEY (PatientID) REFERENCES Users.Patient(PatientID);
ALTER TABLE Appointments.Appointment ADD CONSTRAINT FK_Appointment_Doctor FOREIGN KEY (DoctorID) REFERENCES Users.Doctor(DoctorID);

-- Índice en AppointmentDate para mejorar consultas por fecha
CREATE INDEX IDX_Appointment_AppointmentDate ON Appointments.Appointment(AppointmentDate);

-- Esquema: Users
CREATE SCHEMA Users;
GO

-- Tabla de Usuarios
CREATE TABLE Users.User (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    RoleID INT NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    DeletedAt DATETIME NULL -- Para soporte de borrado lógico
);
-- Tabla de Doctores
CREATE TABLE Users.Doctor (
    DoctorID INT IDENTITY(1,1) PRIMARY KEY,
    SpecialtyID SMALLINT NOT NULL,
    LicenseNumber VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    YearsOfExperience INT NOT NULL,
    Bio NVARCHAR(MAX) NULL,
    ConsultationFee DECIMAL(10, 2) NULL,
    AvailabilityModeID SMALLINT NULL,
    LicenseExpirationDate DATE NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    CONSTRAINT DF_Doctor_ConsultationFee DEFAULT 0.00 FOR ConsultationFee -- Default para fee nulo
);
-- Tabla de Pacientes
CREATE TABLE Users.Patient (
    PatientID INT IDENTITY(1,1) PRIMARY KEY,
    DateOfBirth DATE NOT NULL,
    Gender CHAR(1) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    BloodType CHAR(2) NOT NULL,
    Allergies NVARCHAR(MAX) NOT NULL,
    InsuranceProviderID INT NOT NULL,
    EmergencyContactName VARCHAR(100) NOT NULL,
    EmergencyContactPhone VARCHAR(15) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL
);
-- Claves foráneas adicionales
ALTER TABLE Users.Doctor 
ADD CONSTRAINT FK_Doctor_Specialty FOREIGN KEY (SpecialtyID) REFERENCES Medical.Specialty(SpecialtyID);

ALTER TABLE Users.Patient 
ADD CONSTRAINT FK_Patient_InsuranceProvider FOREIGN KEY (InsuranceProviderID) REFERENCES Insurance.InsuranceProvider(InsuranceProviderID);

-- Índice en Email para mejorar consultas
CREATE INDEX IDX_User_Email ON Users.User(Email);

-- Esquema: Employees
CREATE SCHEMA Employees;
GO

-- Tabla de Empleados
CREATE TABLE Employees.Employee (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    RoleID INT NOT NULL,
    HireDate DATE NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL
);
-- Tabla de Enfermeros
CREATE TABLE Employees.Nurse (
    NurseID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeID INT NOT NULL,
    LicenseNumber VARCHAR(50) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees.Employee(EmployeeID)
);
-- Tabla de Recepcionistas
CREATE TABLE Employees.Receptionist (
    ReceptionistID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeID INT NOT NULL,
    Shift VARCHAR(50) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees.Employee(EmployeeID)
);
-- Índice en Email para empleados
CREATE INDEX IDX_Employee_Email ON Employees.Employee(Email);

-- Esquema: Medical
CREATE SCHEMA Medical;
GO

-- Tabla de Historial Médico
CREATE TABLE Medical.MedicalRecord (
    RecordID INT IDENTITY(1,1) PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    Diagnosis TEXT NOT NULL,
    Treatment TEXT NOT NULL,
    DateOfVisit DATETIME NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    FOREIGN KEY (PatientID) REFERENCES Users.Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Users.Doctor(DoctorID)
);
-- Tabla de Especialidades
CREATE TABLE Medical.Specialty (
    SpecialtyID SMALLINT IDENTITY(1,1) PRIMARY KEY,
    SpecialtyName VARCHAR(100) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL
);
-- Tabla de Recetas Médicas
CREATE TABLE Medical.Prescription (
    PrescriptionID INT IDENTITY(1,1) PRIMARY KEY,
    MedicalRecordID INT NOT NULL,
    Medication TEXT NOT NULL,
    Dosage TEXT NOT NULL,
    Frequency TEXT NOT NULL,
    Duration TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (MedicalRecordID) REFERENCES Medical.MedicalRecord(RecordID)
);
-- Tabla de Género
CREATE TABLE Medical.Gender (
    Gender CHAR(1) PRIMARY KEY, 
    Description VARCHAR(50) NOT NULL
);
-- Tabla de Tipos de Sangre
CREATE TABLE Medical.BloodType (
    BloodType CHAR(2) PRIMARY KEY, 
    Description VARCHAR(50) NOT NULL
);

-- Esquema: Insurance
CREATE SCHEMA Insurance;
GO

-- Proveedores de Seguros
CREATE TABLE Insurance.InsuranceProvider (
    InsuranceProviderID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Website VARCHAR(255) NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL
);
-- Planes de Seguro
CREATE TABLE Insurance.InsurancePlan (
    PlanID INT IDENTITY(1,1) PRIMARY KEY,
    InsuranceProviderID INT NOT NULL,
    PlanName VARCHAR(100) NOT NULL,
    CoverageDetails TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME NULL,
    FOREIGN KEY (InsuranceProviderID) REFERENCES Insurance.InsuranceProvider(InsuranceProviderID)
);

-- Esquema: System
CREATE SCHEMA System;
GO

-- Notificaciones
CREATE TABLE System.Notification (
    NotificationID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    Message TEXT NOT NULL,
    SentAt DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES Users.User(UserID)
);
-- Registro de Notificaciones
CREATE TABLE System.NotificationLog (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    NotificationID INT NOT NULL,
    SentAt DATETIME DEFAULT GETDATE(),
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (NotificationID) REFERENCES System.Notification(NotificationID)
);
-- Roles
CREATE TABLE System.Role (
    RoleID INT IDENTITY(1,1) PRIMARY KEY,
    RoleName VARCHAR(50) NOT NULL
);
