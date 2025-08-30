# Write your MySQL query statement below
SELECT c.name
  FROM Customer c
 WHERE referee_id != 2 
    OR referee_id IS NULL
