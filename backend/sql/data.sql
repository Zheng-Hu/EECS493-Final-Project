PRAGMA foreign_keys = ON;

insert into users(username,password)
values ('awdeorio', '123456'),
    ('jflinn', '123456'),
    ('michjc', '123456'),
    ('jag', '123456');


insert into posts(postid,filename,owner)
values (1, '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg',
'awdeorio'),
(2, 'ad7790405c539894d25ab8dcf0b79eed3341e109.jpg',
'jflinn'),
(3, '9887e06812ef434d291e4936417d125cd594b38a.jpg',
'awdeorio'),
(4, '2ec7cf8ae158b3b1f40065abfb33e81143707842.jpg',
'jag');