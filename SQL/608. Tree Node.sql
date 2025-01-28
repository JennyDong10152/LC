# Write your MySQL query statement below
SELECT id, 'Root' AS type
FROM Tree
WHERE p_id IS NULL
UNION ALL
SELECT id, 'Inner' AS type
FROM Tree
WHERE p_id IS NOT NULL AND id IN (
    SELECT DISTINCT p_id
    FROM Tree
)
UNION ALL
SELECT id, 'Leaf' AS type
FROM Tree
WHERE p_id IS NOT NULL AND id NOT IN (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id is NOT NULL
)
