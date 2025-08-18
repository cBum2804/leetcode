# Write your MySQL query statement below
SELECT u.unique_id, e.name from Employees as e LEFT JOIN EmployeeUNI as u on
e.id = u.id where e.id = u.id or unique_id is NULL