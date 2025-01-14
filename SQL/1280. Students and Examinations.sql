# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, 
Subjects.subject_name, COALESCE(exam.attended_exams, 0) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) as attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) exam
ON Students.student_id = exam.student_id AND Subjects.subject_name = exam.subject_name
ORDER BY student_id, subject_name