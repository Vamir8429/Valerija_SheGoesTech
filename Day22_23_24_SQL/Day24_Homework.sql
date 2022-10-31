-- TODO 

-- Task 1
-- provide a query that shows total sales by each sales agent
-- will require to join with the customer table
-- will require to join with the invoice table

WITH employee_sales AS (
        SELECT
            c.supportrepid AS employeeid,
            SUM(i.total) AS total_purchased
        FROM invoices i
        INNER JOIN customers c ON c.customerid = i.customerid
        GROUP BY 1
        )

SELECT
    e.employeeid AS employeeid,
    e.firstname || ' ' || e.lastname AS employeename,
    e.title AS title,
    es.total_purchased AS employee_sales
FROM employees e
INNER JOIN employee_sales es ON e.employeeid = es.employeeid
ORDER BY 2

-- Task 2
-- QUERY TO find the top selling track of 2012
-- will require use track table
-- will requiret to join with invoice items table
-- will require to join with the invoice table

SELECT 
    t.name trackname,
    a.title album_title,
    ar.name artist,
    COUNT(*) as total_purchases,
    SUM(il.unitprice) total_cost
FROM tracks t 
JOIN albums a on a.albumid = t.albumid
JOIN artists ar on ar.artistid = a.artistid
JOIN invoice_items il on il.trackid = t.trackid
GROUP BY 1
ORDER BY total_purchases desc
LIMIT 10