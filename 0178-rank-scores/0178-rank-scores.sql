# Write your MySQL query statement below
# DENSE_RANK 1 1 2


SELECT s.score,
       DENSE_RANK() OVER (
        ORDER BY s.score DESC
       ) AS 'rank'
  FROM Scores s
;