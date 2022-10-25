--SELECT * FROM north_american_cities;

--SELECT City, Population 
--FROM north_american_cities 
--WHERE Country in ("Canada");


--SELECT City, Latitude 
--FROM north_american_cities 
--where Country in ("United States") 
--order by Latitude desc;

--SELECT city, longitude 
--FROM north_american_cities 
--WHERE longitude < -87.629798 
--ORDER BY longitude ASC;

--SELECT City 
--FROM north_american_cities 
--where Country in ("Mexico") 
--order by Population desc 
--limit 2;

--SELECT City 
--FROM north_american_cities 
--where Country in ("United States") 
--order by Population desc 
--limit 2 offset 2;