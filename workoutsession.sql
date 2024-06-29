use gym_db;
CREATE TABLE if not exists Workout_Sessions (
    id INT auto_increment primary key,
    date date not null,
    duration_minutes INT not null,
    calories_burned INT not null,
    member_id INT not null,
    foreign key (member_id) references members (id),
    trainer_id int not null,
    foreign key (trainer_id) references trainers (id)
);

SELECT * FROM Workout_Sessions;