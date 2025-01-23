# Write your MySQL query statement below
SELECT name
FROM Employee employees
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
