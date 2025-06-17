# Write your MySQL query statement below
SELECT user_id
  FROM Loans
 WHERE user_id IN (SELECT user_id FROM Loans WHERE loan_type = 'Refinance')
   AND user_id IN (SELECT user_id FROM Loans WHERE loan_type = 'Mortgage')
 GROUP BY user_id
 ORDER BY user_id ASC

