# Write your MySQL query statement below

#Approach 1
select name 
from Customer
where referee_id != 2 or referee_id is null

#Approach 2
-- select name 
-- from customer
-- where coalesce(referee_id, 0) != 2
