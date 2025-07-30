# Write your MySQL query statement below
Select email AS Email from Person
Group by email Having Count(*)>1;