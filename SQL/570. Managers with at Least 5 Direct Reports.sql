# Write your MySQL query statement below
SELECT name FROM Employee
WHERE id IN (
    SELECT ManagerID FROM Employee
    GROUP BY ManagerID
    HAVING count(*) >= 5
)