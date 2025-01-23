# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sub.subject_name, COALESCE(e.frequency, 0) as attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS frequency
    FROM Examinations
    GROUP BY student_id, subject_name
) AS e
ON s.student_id = e.student_id AND e.subject_name = sub.subject_name
ORDER BY s.student_id, sub.subject_name