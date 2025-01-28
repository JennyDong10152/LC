# Write your MySQL query statement below
SELECT ROUND(SQRT(min((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))),2) as shortest
FROM Point2D p1,Point2D p2
WHERE p1.x <> p2.x or p1.y <> p2.y;