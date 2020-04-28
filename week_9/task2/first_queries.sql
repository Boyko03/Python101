SELECT address
  FROM STUDIO
  WHERE name = "MGM";
  
------------------------------------------------------------

SELECT birthdate
  FROM MOVIESTAR
  WHERE name = "Kim Basinger";
  
------------------------------------------------------------

SELECT name
  FROM MOVIEEXEC
  WHERE networth > 10000000;
  
------------------------------------------------------------

SELECT * FROM MOVIESTAR
  WHERE gender = "M" OR address = "Prefect Rd.";
  
------------------------------------------------------------

INSERT INTO MOVIESTAR
  VALUES ("Zahari Baharov", "some address", "M", 1980-08-12);
  
------------------------------------------------------------

DELETE FROM STUDIO
  WHERE address LIKE ("%5%");
  
------------------------------------------------------------

UPDATE MOVIE
  SET studioname = "Fox"
  WHERE title LIKE ("%star%");

