# Write your MySQL query statement below
(SELECT name AS results
FROM Users
JOIN MovieRating
USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM Movies 
JOIN MovieRating
USING(movie_id)
WHERE LEFT(created_at, 7) = '2020-02'
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1)