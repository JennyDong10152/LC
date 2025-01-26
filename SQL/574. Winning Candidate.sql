# Write your MySQL query statement below
SELECT name
FROM Candidate
LEFT JOIN Vote
ON Candidate.id = Vote.candidateId
GROUP BY Vote.candidateId
ORDER BY COUNT(Vote.id) DESC LIMIT 1