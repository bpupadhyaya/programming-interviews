// Table: Logs
// +-------------+---------+
// | Column Name | Type    |
// +-------------+---------+
// | id          | int     |
// | num         | varchar |
// +-------------+---------+
// In SQL, id is the primary key for this table.
// id is an autoincrement column.
// Find all numbers that appear at least three times consecutively.
// Return the result table in any order.
// The result format is in the following example.
// Sample 1:
// Input:
// Logs table:
// +----+-----+
// | id | num |
// +----+-----+
// | 1  | 1   |
// | 2  | 1   |
// | 3  | 1   |
// | 4  | 2   |
// | 5  | 1   |
// | 6  | 2   |
// | 7  | 2   |
// +----+-----+
// Output:
// +-----------------+
// | ConsecutiveNums |
// +-----------------+
// | 1               |
// +-----------------+
// Explanation: 1 is the only number that appears consecutively for at least three times.

with cte as (
    select num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    from logs

)

select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)

or

SELECT DISTINCT L1.num  AS ConsecutiveNums FROM Logs L1,
   Logs L2,Logs L3 WHERE L1.id=L2.id - 1 AND L1.num=L2.num
   and  L2.id=L3.id-1 and L2.num=L3.num

or

select distinct t1.num as ConsecutiveNums
from logs t1
join logs t2
on t1.id=t2.id+1 and t1.num=t2.num
join logs t3
on t2.id=t3.id+1 and t2.num=t3.num;

or

select distinct Num as ConsecutiveNums
from Logs
where (Id + 1, Num) in (select * from Logs) and (Id + 2, Num) in (select * from Logs)


