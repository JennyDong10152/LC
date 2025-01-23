# Write your MySQL query statement below
SELECT a.machine_id, ROUND(
    (SELECT AVG(a1.timestamp) FROM Activity a1 WHERE a1.machine_id = a.machine_id AND a1.activity_type = 'end') -
    (SELECT AVG(a1.timestamp) FROM Activity a1 WHERE a1.machine_id = a.machine_id AND a1.activity_type = 'start'),
    3
) AS processing_time
FROM Activity a
GROUP BY a.machine_id
ORDER BY a.machine_id