# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, Subjects.subject_name, Coalesce(Exam.frequency, 0) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS frequency
    FROM Examinations
    GROUP BY student_id, subject_name
) AS Exam
ON Exam.student_id = Students.student_id AND Subjects.subject_name = Exam.subject_name
ORDER BY Students.student_id, Subjects.subject_name