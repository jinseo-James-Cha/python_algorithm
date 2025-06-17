# Write your MySQL query statement below
# avg per items per order rounded to 2 demimal
SELECT ROUND(SUM(item_count * order_occurrences)/SUM(order_occurrences), 2) as average_items_per_order
  FROM Orders