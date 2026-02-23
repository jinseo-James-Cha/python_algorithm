# Write your MySQL query statement below

#Department.name, Employee.name, Salary
#Get each departments' highest salary and its employee(s)

#- join
#- group by department
#- max salary by department

SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
  FROM Employee e
  JOIN Department d ON e.departmentId = d.id
 WHERE (e.departmentId, e.salary) IN (
    SELECT m.departmentId, MAX(m.salary)
      FROM Employee m
     GROUP BY m.departmentID
 )
;
