INSERT INTO users(username, password, created, points)
VALUES
    ('jack', 'password', DEFAULT, 21),
    ('jill', 'password', DEFAULT, 12),
    ('kevin', 'password', DEFAULT, 5);

INSERT INTO posts(postid, filename, caption, created, owner)
VALUES
    (DEFAULT, 'c779560fd34245f0b3c0acbd6afda970.jpeg', 'Had a great run today! Can''t wait to get back out this weekend!', DEFAULT, 'jack'),
    (DEFAULT, '3ce034d523584fc4a095055c1950206c.jpeg', 'Got everyone out for a run today!', DEFAULT, 'jill'),
    (DEFAULT, 'c69e4b5b304d4a7c9422755d34469120.jpeg', 'Picked up some new shoes today!', DEFAULT, 'jack'),
    (DEFAULT, '916b783887a14c10accda230c2c07bbb.jpeg', 'Beautiful view of the mountains', DEFAULT, 'kevin'),
    (DEFAULT, '1102ad45443f4cbd97d489cf33ce3b8f.jpeg', 'Ann Arbor, MI - Nov 14, 2021', DEFAULT, 'jill');

INSERT INTO workouts(workoutid, time, distance, created, owner, postid, points)
VALUES
    (DEFAULT, 21.4, 2.9, DEFAULT, 'jack', 1, 3),
    (DEFAULT, 38.8, 5.2, DEFAULT, 'jack', 3, 7),
    (DEFAULT, 22.3, 3.2, DEFAULT, 'jill', 2, 5),
    (DEFAULT, 18.1, 1.7, DEFAULT, 'jill', 5, 3),
    (DEFAULT, 9.8, 1.1, DEFAULT, 'kevin', 4, 2),
    (DEFAULT, 52.3, 7.1, DEFAULT, 'jack', NULL, 11),
    (DEFAULT, 19.0, 2.5, DEFAULT, 'jill', NULL, 4),
    (DEFAULT, 12.1, 1.4, DEFAULT, 'kevin', NULL, 3);
