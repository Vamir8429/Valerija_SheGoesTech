-- TODO
-- 1. get total sales for all years using invoice table
-- you will want to use SUBSTR to get the year from the invoice date
-- you will want to use SUM to get the total sales for each year

SELECT 
	InvoiceId, 
	SUBSTRING(InvoiceDate,1,4) as Year, 
	SUM(Total) as TotalSales
FROM invoices
GROUP BY Year

-- 2. get total sales for each country - use invoice table
-- you will also need to join with the customer table - those have country info

SELECT 
	b.Country, 
	SUM(Total) as TotalSales
FROM invoices a
JOIN customers b 
ON a.CustomerId = b.CustomerId 
GROUP BY b.Country 

-- 3. a count tracks in each playlist - use playlist_track table

SELECT PlaylistId, sum(TrackId) TotalTracks
FROM playlist_track
GROUP BY PlaylistId 
ORDER BY PlaylistId ASC 

-- 3. b extra challenge get total track lenght in minutes for each playlist
-- you will need to join with the track table

SELECT 
	a.PlaylistId, 
	SUM(a.TrackId) TotalTracks,
	SUM(b.Milliseconds)/(1000*60) TrackLenghtMinutes
FROM playlist_track a
JOIN tracks b 
ON a.TrackId = b.TrackId 
GROUP BY a.PlaylistId 
ORDER BY a.PlaylistId ASC 

-- 3. c cherry on top - provide names of these playlists
-- so you will want to join with the playlist table as well

SELECT 
	a.PlaylistId, 
	c.Name,
	SUM(a.TrackId) TotalTracks,
	SUM(b.Milliseconds)/(1000*60) TrackLenghtMinutes
FROM playlist_track a
JOIN tracks b 
ON a.TrackId = b.TrackId 
JOIN playlists c 
ON a.PlaylistId = c.PlaylistId 
GROUP BY a.PlaylistId 
ORDER BY a.PlaylistId ASC 