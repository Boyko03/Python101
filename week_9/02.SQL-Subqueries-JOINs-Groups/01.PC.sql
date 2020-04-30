SELECT AVG(speed)
    FROM pc;

SELECT maker, AVG(screen)
    FROM laptop
    JOIN product
        ON product.model = laptop.model
    GROUP BY maker;

SELECT AVG(speed)
    FROM laptop
    WHERE price > 1000; 

SELECT hd, AVG(price)
    FROM pc
    GROUP BY hd;

SELECT speed, AVG(price)
    FROM pc
    WHERE speed >= 500
    GROUP BY speed;

SELECT AVG(price)
    FROM pc
    JOIN product
        ON pc.model = product.model
    WHERE maker = 'A';

SELECT AVG(price)
    FROM(
        SELECT pc.price
            FROM pc
            JOIN product
                ON pc.model = product.model
            WHERE product.maker = 'B'
        UNION
        SELECT laptop.price
        FROM laptop
            JOIN product
                ON product.model = laptop.model
    ); 

SELECT maker
    FROM product
    WHERE type = 'PC'
    GROUP BY maker
    HAVING COUNT(maker) >= 3; 

SELECT maker
    FROM product
    JOIN pc
        ON product.model = pc.model
    ORDER BY price DESC
    LIMIT 1;

SELECT AVG(pc.hd)
    FROM pc 
    INNER JOIN product ON product.model = pc.model 
    WHERE maker IN (
        SELECT DISTINCT maker
        FROM product
        INNER JOIN printer ON product.model = printer.model
        WHERE product.type = "Printer"
    );
