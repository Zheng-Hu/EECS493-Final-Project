/* Note: we are storing plain-text passwords
   because this project is more proof-of-concept 
   than anything, especially for the backend */
CREATE TABLE users(
  username VARCHAR(20) PRIMARY KEY,
  password TEXT NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  points INTEGER NOT NULL
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
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  owner VARCHAR(20) NOT NULL REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
  postid INTEGER REFERENCES posts ON DELETE CASCADE ON UPDATE CASCADE,
  points INTEGER NOT NULL
);

CREATE TABLE routes(
  routeid SERIAL PRIMARY KEY,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  workoutid INTEGER REFERENCES workouts ON DELETE CASCADE ON UPDATE CASCADE
);
