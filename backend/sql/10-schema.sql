CREATE TABLE users(
  username VARCHAR(20) PRIMARY KEY,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE posts(
  postid SERIAL PRIMARY KEY,
  filename VARCHAR(64),
  caption TEXT,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  owner VARCHAR(20) NOT NULL REFERENCES USERS(username) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE workouts(
  workoutid SERIAL PRIMARY KEY,
  time REAL NOT NULL,
  distance REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  owner VARCHAR(20) NOT NULL REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
  postid INTEGER REFERENCES posts ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE routes(
  routeid SERIAL PRIMARY KEY,
  created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  workoutid INTEGER REFERENCES workouts ON DELETE CASCADE ON UPDATE CASCADE
);
