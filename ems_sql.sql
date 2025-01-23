CREATE TABLE Employe (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) ,
    LastName VARCHAR(50) ,
    Department VARCHAR(50),
    JoinDate DATE
);
INSERT INTO Employees (FirstName, LastName, Department, JoinDate)
VALUES ('Ram', 'Sharma', 'IT', '2025-01-15');
SELECT * FROM Employees;
UPDATE Employees
SET Department = 'HR'
WHERE EmployeeID = 1;
DELETE FROM Employees
WHERE EmployeeID = 1;

