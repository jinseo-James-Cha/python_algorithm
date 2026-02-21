# Write your MySQL query statement below
# select id which has warmer temp than yesterday
# date should compare itself with yesterday temp
# how can we compare with date-1
# if cannot have yesterday? -> ignore the dates

WITH PreviousWeatherData AS
(
    SELECT 
        id,
        recordDate,
        temperature, 
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS PreviousTemperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) AS PreviousRecordDate
    FROM 
        Weather
)
SELECT id
  FROM PreviousWeatherData
 WHERE temperature > PreviousTemperature
   AND DATEDIFF(recordDate, PreviousRecordDate) = 1
;


-- SELECT w1.id
--   FROM weather w1
--   JOIN weather w2 on(DATEDIFF(w1.recordDate, w2.recordDate) = 1)
--  WHERE w1.temperature > w2.temperature
-- ;