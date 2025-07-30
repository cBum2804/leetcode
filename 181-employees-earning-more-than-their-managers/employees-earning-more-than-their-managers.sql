# Write your MySQL query statement below
SELECT e.name as Employee from Employee AS e JOIN Employee as m ON e.managerID = m.id 
WHERE e.salary>m.salary;