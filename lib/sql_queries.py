# lib/sql_queries.py

select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex='F';
"""


