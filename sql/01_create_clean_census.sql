DROP TABLE IF EXISTS clean_census_demographics;

CREATE TABLE clean_census_demographics AS
SELECT
    "NAME" AS location_name,
    "zip code tabulation area" AS zip_code,
    CAST("B01003_001E" AS INTEGER) AS population,
    CAST("B19013_001E" AS INTEGER) AS median_household_income
FROM raw_census_demographics;