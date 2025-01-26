# Write your MySQL query statement below
SELECT IFNULL(ROUND((SELECT COUNT(DISTINCT requester_id, accepter_id) FROM RequestAccepted) / COUNT(DISTINCT sender_id, send_to_id), 2), 0.00) AS accept_rate
FROM FriendRequest
LEFT JOIN RequestAccepted
ON RequestAccepted.requester_id = FriendRequest.sender_id AND RequestAccepted.accepter_id = FriendRequest.send_to_id
