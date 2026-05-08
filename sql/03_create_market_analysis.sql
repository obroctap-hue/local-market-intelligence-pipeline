DROP TABLE IF EXISTS market_analysis;

CREATE TABLE market_analysis AS
SELECT
    c.zip_code,
    c.location_name,
    c.population,
    c.median_income,
    b.business_count,
    (c.population / NULLIF(b.business_count, 0)) AS people_per_business
FROM clean_census_demographics c
LEFT JOIN zip_business_patterns b
ON c.zip_code = b.zip_code;