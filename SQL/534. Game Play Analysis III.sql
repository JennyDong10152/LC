# Write your MySQL query statement below
SELECT a2.player_id, a2.event_date, SUM(a1.games_played) AS games_played_so_far
FROM Activity a1
JOIN Activity a2
ON a1.player_id = a2.player_id AND a1.event_date <= a2.event_date
GROUP BY a2.player_id, a2.event_date