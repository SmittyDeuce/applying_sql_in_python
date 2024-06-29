use gym_db;
CREATE TABLE if not exists members (
    id INT auto_increment primary key,
    name varchar(255) not null,
    age INT not null,
    trainer_id INT,
    foreign key (trainer_id) references trainers (id)
);

USE gym_db;

SELECT * from members;