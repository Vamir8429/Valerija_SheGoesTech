-- https://sqlbolt.com/lesson/select_queries_review

-- LESSON 6 SQL Lesson 6: Multi-table queries with JOINs

--Find the domestic and international sales for each movie
SELECT * 
FROM movies a
inner join boxoffice b
on a.id = b.movie_id;

--Show the sales numbers for each movie that did better internationally rather than domestically
SELECT * 
FROM movies a
inner join boxoffice b
on a.id = b.movie_id
where b.domestic_sales < b.international_sales;

--List all the movies by their ratings in descending order
SELECT * 
FROM movies a
inner join boxoffice b
on a.id = b.movie_id
order by b.rating desc;

-- SQL Lesson 7: OUTER JOINs

--Find the list of all buildings that have employees
SELECT Distinct Building
FROM employees

--Find the list of all buildings and their capacity
SELECT *
from buildings a

--List all buildings and the distinct employee roles in each building (including empty buildings)
SELECT distinct a.building_name, b.role
from buildings a
left join employees b
on a.building_name = b.building

--SQL Lesson 8: A short note on NULLs

--Find the name and role of all employees who have not been assigned to a building
SELECT *
FROM employees
where building is null

--Find the names of the buildings that hold no employees
SELECT distinct a.building_name, b.role
from buildings a
left join employees b
on a.building_name = b.building
where b.role is null

--SQL Lesson 9: Queries with expressions

--List all movies and their combined sales in millions of dollars 
SELECT a.title, (b.domestic_sales + b.international_sales)/1000000 as total_sales
FROM movies a
INNER JOIN boxoffice b
on a.id = b.movie_id

--List all movies and their ratings in percent
SELECT a.title, b.rating * 10 as rating_percentage
FROM movies a
INNER JOIN boxoffice b
on a.id = b.movie_id

--List all movies that were released on even number years
SELECT title, year
FROM movies
WHERE year % 2 = 0

--SQL Lesson 10: Queries with aggregates (Pt. 1)

--Find the longest time that an employee has been at the studio
SELECT name, max(years_employed)
FROM employees

--For each role, find the average number of years employed by employees in that role
SELECT role, AVG(years_employed) as average
FROM employees
group by role

--Find the total number of employee years worked in each building
SELECT building, SUM(years_employed) as total_years
FROM employees
group by building

--SQL Lesson 11: Queries with aggregates (Pt. 2)

--Find the number of Artists in the studio (without a HAVING clause)
SELECT role, count(role)
FROM employees
where role in ("Artist")

--Find the number of Employees of each role in the studio
SELECT role, count(name)
FROM employees
group by role

--Find the total number of years employed by all Engineers
SELECT role, sum(years_employed)
FROM employees
where role in ("Engineer")


-- SQL Lesson 12: Order of execution of a Query

--Find the number of movies each director has directed
SELECT director, count(title)
FROM movies a
inner join boxoffice b
on a.id = b.movie_id
group by director

--Find the total domestic and international sales that can be attributed to each director
SELECT director, sum(domestic_sales) + sum(international_sales) as total_sales
FROM movies a
inner join boxoffice b
on a.id = b.movie_id
group by director

-- SQL Lesson 13: Inserting rows

--Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
INSERT INTO movies VALUES (15, "Toy Story 4", "Valerija Miribian", 2022, 99);

--Toy Story 4 has been released to critical acclaim! 
--It had a rating of 8.7, and made 340 million domestically and 270 million internationally. 
--Add the record to the BoxOffice table.
INSERT INTO boxoffice
(movie_id, rating, domestic_sales, international_sales)
VALUES (15, 8.7, 340000000, 270000000);

--SQL Lesson 14: Updating rows

--The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
UPDATE movies
SET director = "John Lasseter"
WHERE id = 2

--The year that Toy Story 2 was released is incorrect, it was actually released in 1999
UPDATE movies
SET year = "1999"
WHERE id = 3

--Both the title and director for Toy Story 8 is incorrect! 
--The title should be "Toy Story 3" and it was directed by Lee Unkrich
UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE id = 11

--SQL Lesson 15: Deleting rows

--This database is getting too big, lets remove all movies that were released before 2005.
DELETE FROM movies
WHERE year < 2005

--Andrew Stanton has also left the studio, so please remove all movies directed by him.
DELETE FROM movies
WHERE director in ("Andrew Stanton")

--SQL Lesson 16: Creating tables

--Create a new table named Database with the following columns:
--– Name A string (text) describing the name of the database
--– Version A number (floating point) of the latest version of this database
--– Download_count An integer count of the number of times this database was downloaded
--This table has no constraints.
CREATE TABLE Database (
    Id INTEGER PRIMARY KEY,
    Name TEXT,
    Version INTEGER,
    Download_count INTEGER
);

--SQL Lesson 17: Altering tables

--Add a column named Aspect_ratio with a FLOAT data type 
--to store the aspect-ratio each movie was released in.
ALTER TABLE movies
ADD Aspect_ratio DataType FLOAT 
    DEFAULT default_value;

--Add another column named Language with a TEXT data type to store the 
--language that the movie was released in. 
--Ensure that the default for this language is English.
ALTER TABLE movies
ADD Language DataType TEXT
    DEFAULT "English";

--SQL Lesson 18: Dropping tables

--We've sadly reached the end of our lessons, lets clean up by removing the Movies table
DROP TABLE IF EXISTS movies;

--And drop the BoxOffice table as well
DROP TABLE IF EXISTS boxoffice;

--SQL Lesson X: To infinity and beyond!
--You've finished the tutorial!