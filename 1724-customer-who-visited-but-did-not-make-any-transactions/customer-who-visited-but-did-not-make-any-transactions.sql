# Write your MySQL query statement below
SELECT customer_id , COUNT(visit_id) as count_no_trans from Visits Where
visit_id NOT IN(Select visit_id FROM Transactions) Group by customer_id