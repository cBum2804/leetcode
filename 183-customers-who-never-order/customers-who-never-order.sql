# Write your MySQL query statement below
SELECT name as Customers From Customers
Where id NOT IN(SELECT customerId FROM Orders);