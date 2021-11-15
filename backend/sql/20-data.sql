INSERT INTO users(username, created)
VALUES
    ('jack', DEFAULT),
    ('jill', DEFAULT),
    ('kevin', DEFAULT);

INSERT INTO posts(postid, filename, caption, created, owner)
VALUES
    (DEFAULT, '/media/man_running.jpeg', 'Had a great run today! Can''t wait to get back out this weekend!', DEFAULT, 'jack'),
    (DEFAULT, '/media/running_group.jpeg', 'Got everyone out for a run today!', DEFAULT, 'jill'),
    (DEFAULT, '/media/running_shoes.jpeg', 'Picked up some new shoes today!', DEFAULT, 'jack'),
    (DEFAULT, '/media/mountain_run.jpeg', 'Beautiful view of the mountains', DEFAULT, 'kevin'),
    (DEFAULT, '/media/running_trail.jpeg', 'Ann Arbor, MI - Nov 14, 2021', DEFAULT, 'jill');

INSERT INTO workouts(workoutid, time, distance, created, owner, postid)
VALUES
    (DEFAULT, 21.4, 2.9, DEFAULT, 'jack', 1),
    (DEFAULT, 38.8, 5.2, DEFAULT, 'jack', 3),
    (DEFAULT, 22.3, 3.2, DEFAULT, 'jill', 2),
    (DEFAULT, 18.1, 1.7, DEFAULT, 'jill', 5),
    (DEFAULT, 9.8, 1.1, DEFAULT, 'kevin', 4),
    (DEFAULT, 52.3, 7.1, DEFAULT, 'jack'),
    (DEFAULT, 19.0, 2.5, DEFAULT, 'jill'),
    (DEFAULT, 12.1, 1.4, DEFAULT, 'kevin');
