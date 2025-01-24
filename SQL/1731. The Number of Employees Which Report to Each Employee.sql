# Write your MySQL query statement below
SELECT Manager.employee_id, 
    Manager.name,
    COUNT(DISTINCT Employee.employee_id) AS reports_count,
    ROUND(AVG(Employee.age), 0) AS average_age
FROM Employees Manager
INNER JOIN Employees Employee
ON Manager.employee_id = Employee.reports_to
GROUP BY Manager.employee_id
ORDER BY Manager.employee_id