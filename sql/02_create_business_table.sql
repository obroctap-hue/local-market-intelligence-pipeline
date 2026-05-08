DROP TABLE IF EXISTS zip_business_patterns;

CREATE TABLE zip_business_patterns AS
SELECT
    LPAD(zip::text, 5, '0') AS zip_code,
    name AS location_name,
    naics,
    est::integer AS business_count,
    city,
    stabbr AS state,
    cty_name AS county
FROM zip_business_patterns_raw
WHERE naics = '------';