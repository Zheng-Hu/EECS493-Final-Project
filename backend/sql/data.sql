PRAGMA foreign_keys = ON;

insert into users(username,password)
values ('awdeorio', '123456'),
    ('jflinn', '123456'),
    ('michjc', '123456'),
    ('jag', '123456');


insert into posts(postid,filename,owner,time, distance, caption)
values (2, '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg',
'awdeorio',8.3,1.2,'Took a run through downtown!'),
(6, 'ad7790405c539894d25ab8dcf0b79eed3341e109.jpg',
'jflinn',20.9,2.7,'My run from Monday')