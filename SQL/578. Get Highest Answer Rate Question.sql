# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM (
    SELECT question_id, (SUM(action = 'answer') / SUM(action = 'show')) AS fraction
    FROM SurveyLog
    GROUP BY question_id
    ORDER BY fraction DESC, question_id 
    LIMIT 1
) Helper