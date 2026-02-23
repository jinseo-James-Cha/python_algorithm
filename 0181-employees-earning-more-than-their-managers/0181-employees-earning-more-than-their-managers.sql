# Write your MySQL query statement below
# self join


SELECT e.name as Employee
  FROM Employee e
  JOIN Employee m ON e.ManagerId = m.id
 WHERE e.salary > m.salary
;