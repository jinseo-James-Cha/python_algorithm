# Write your MySQL query statement below
# state = "approved" or "declined"

# each month and country -> group by month and country
# the number of transaction -> count(rows)
# their total amount -> sum(amount)

# the number of transaction -> count(rows) for state -> "approved"
# their total amount -> sum(amount) for state -> "approved"
SELECT LEFT(trans_date, 7) as month,
       country,
       COUNT(*) as trans_count,
       SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
       SUM(amount) as trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
      FROM Transactions
     GROUP BY month, country
;


-- SELECT LEFT(trans_date, 7) as month,
--            country,
--            COUNT(*) as trans_count,
--            SUM(state = 'approved') AS approved_count,
--            SUM(amount) as trans_total_amount,
--            SUM((state = 'approved') * amount) AS approved_total_amount
--       FROM Transactions
--      GROUP BY month, country
-- ;

-- WITH total_data AS (
--     SELECT LEFT(trans_date, 7) AS month,
--            country,
--            COUNT(*) AS trans_count,
--            SUM(amount) AS trans_total_amount
--       FROM Transactions
--      GROUP BY LEFT(trans_date, 7), country
-- ),
-- approved_data AS (
--     SELECT LEFT(trans_date, 7) AS month,
--            country,
--            COUNT(*) AS approved_count,
--            SUM(amount) AS approved_total_amount
--       FROM Transactions
--      WHERE state = 'approved'
--      GROUP BY LEFT(trans_date, 7), country
-- )

-- SELECT 
--     t.month, 
--     t.country, 
--     t.trans_count, 
--     COALESCE(a.approved_count, 0) AS approved_count, 
--     t.trans_total_amount, 
--     COALESCE(a.approved_total_amount, 0) AS approved_total_amount
-- FROM total_data t
-- LEFT JOIN approved_data a 
--     ON t.month = a.month 
--    AND (t.country = a.country OR (t.country IS NULL AND a.country IS NULL))
-- ;