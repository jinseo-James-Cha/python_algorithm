# Write your MySQL query statement below
# visit_date is UNIQUE
# 3 <= consecutive ids 1,2,3 for id -> people >= 100 for each

WITH base AS (
    SELECT *,
           LEAD(id, 1) OVER (ORDER BY id) AS next_id,
           LEAD(id, 2) OVER (ORDER BY id) AS second_next_id,
           LAG(id, 1) OVER (ORDER BY id) AS last_id,
           LAG(id, 2) OVER (ORDER BY id) AS second_last_id
      FROM stadium
     WHERE people >= 100
)

SELECT b.id,
       b.visit_date,
       b.people
  FROM base b
 WHERE (b.second_next_id - 2 = b.id AND b.next_id - 1 = b.id)
    OR (b.last_id + 1 = b.id AND b.next_id - 1 = b.id)
    OR (b.last_id + 1 = b.id AND b.second_last_id + 2 = b.id)
;



-- SELECT 
--     DISTINCT a.*
-- FROM 
--     stadium AS a, stadium AS b, stadium AS c
-- WHERE
--      a.people >= 100 AND b.people >= 100 AND c.people >= 100
-- AND 
--     (
--        (a.id - b.id = 1 AND b.id - c.id = 1)
--     OR (c.id - b.id = 1 AND b.id - a.id = 1)
--     OR (b.id - a.id = 1 AND a.id - c.id = 1)
--     )
-- ORDER BY visit_date


# CTE for 100 people



-- WITH hundred_people AS (
--     SELECT s.*
--       FROM Stadium s
--      WHERE s.people >= 100
-- )

