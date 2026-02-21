# Write your MySQL query statement below

#Department.name, Employee.name, Salary
#Get each departments' highest salary and its employee(s)

#- join
#- group by department
#- max salary by department

SELECT d.name as Department, e.name as Employee, e.salary as Salary
  FROM Employee e
  JOIN Department d on(e.departmentId = d.id)
 WHERE (e.departmentId, e.salary) IN (
    SELECT m.departmentId, MAX(m.salary)
      FROM Employee m
     GROUP BY m.departmentID
    )
;