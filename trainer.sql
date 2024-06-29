use gym_db;
CREATE TABLE if not exists trainers (
    id INT auto_increment primary key,
    name varchar(255) not null
);

INSERT INTO trainers (name) VALUES ('Brock');
INSERT INTO trainers (name) VALUES ('Misty');
INSERT INTO trainers (name) VALUES ('Lt. Surge');
INSERT INTO trainers (name) VALUES ('Erika');
INSERT INTO trainers (name) VALUES ('Koga');
INSERT INTO trainers (name) VALUES ('Sabrina');
INSERT INTO trainers (name) VALUES ('Blaine');
INSERT INTO trainers (name) VALUES ('Giovanni');

SELECT * from trainers;