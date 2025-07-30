# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary 
FROM Employee as e join Department as d ON e.departmentId = d.id
where e.salary = (SELECT MAX(salary) From Employee WHERE 
departmentId=e.departmentId)