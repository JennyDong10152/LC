# Write your MySQL query statement below
SELECT *, IF(X+Y>Z AND Y+Z>X AND X+Z>Y, 'Yes', 'No') AS triangle
FROM Triangle