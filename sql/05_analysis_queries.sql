SELECT *
FROM market_analysis
WHERE median_income > 50000
	AND population > 10000
	and median_income > 50000
ORDER BY people_per_business DESC;