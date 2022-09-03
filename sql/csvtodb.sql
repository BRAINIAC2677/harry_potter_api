COPY dialogues(id, chapter_id,place_id,character_id,dialogue)
FROM '/home/brainiac77/github/harry_potter_api/database/dialogues.csv'
DELIMITER ','
CSV HEADER;