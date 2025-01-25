# Write your MySQL query statement below
SELECT employ.name AS Employee
FROM Employee employ
JOIN Employee manager
ON manager.id = employ.managerId
WHERE employ.salary > manager.salary
