SELECT *
  FROM MOVIESTAR
  JOIN STARSIN on MOVIESTAR.name = STARSIN.starname
  WHERE movietitle = "Terms of Endearment";

---------------------------------------------------

SELECT name
  FROM MOVIESTAR
  JOIN STARSIN on MOVIESTAR.name = STARSIN.STARNAME
  JOIN MOVIE on STARSIN.MOVIETITLE = MOVIE.TITLE
  WHERE studioname = "MGM" AND movieyear = 1995;

---------------------------------------------------

ALTER TABLE STUDIO
  ADD COLUMN president VARCHAR(30);

UPDATE STUDIO
  SET president = "Bob Maxey"
  WHERE name = "MGM";

UPDATE STUDIO
  SET president = "David Rogers"
  WHERE name = "USA Entertainm.";

SELECT president
  FROM STUDIO
  WHERE name = "MGM";
