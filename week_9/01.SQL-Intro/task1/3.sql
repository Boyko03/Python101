ALTER TABLE languages
  ADD COLUMN rating INTEGER
  CHECK (rating BETWEEN 0 and 9);

UPDATE languages
  SET rating = 9 - id;

