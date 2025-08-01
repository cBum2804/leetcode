# Write your MySQL query statement below
SELECT ranked.department_name AS Department, ranked.employee_name AS Employee, ranked.salary 
AS Salary
FROM (SELECT d.name as department_name, e.name as employee_name, e.salary,
DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rn
FROM Employee e JOIN Department d ON departmentID= d.id
) AS ranked
WHERE ranked.rn<=3
