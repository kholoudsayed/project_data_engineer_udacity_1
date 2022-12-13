# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users ; "
song_table_drop = "drop table if exists songs ; "
artist_table_drop = "drop table if exists artists ;"
time_table_drop = "drop table if exists time ; "

# CREATE TABLES
#columns names
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
#psycopg2.ProgrammingError: column "start_time" is of type timestamp without time zone but expression is of type bigint

# so i make start_time big int
#psycopg2.IntegrityError: null value in column "songplay_id" violates not-null constraint 
# so i make songplay_id SERIAL
"""songplay_table_create = ("""

#create table if not exists songplays (
 #   songplay_id varchar PRIMARY KEY,
#    start_time timestamp NOT NULL,
#    user_id INT NOT NULL,
#    level varchar,
#    song_id varchar,
#    artist_id varchar,
#    session_id int NOT NULL,
#    location varchar,
#    user_agent varchar
#);""")



songplay_table_create = ("""
create table if not exists songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time bigint NOT NULL,
    user_id INT NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar,
    user_agent varchar
);
""")
#columns names
#user_id, first_name, last_name, gender, level
user_table_create = ("""
create table if not exists  users (
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
);
""")

#columns names
#song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY, 
    title varchar, 
    artist_id varchar NOT NULL, 
    year int,
    duration numeric 
  );
""")
#columns names
#artist_id, name, location, latitude, longitude
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    longitude numeric,
    latitude numeric
);
""")

#columns names
#start_time, hour, day, week, month, year, weekday
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time bigint PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar
); """)


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);

""")
# when uodate user update level also
#user_table_insert = ("""
#INSERT INTO users ( user_id, first_name,last_name,gender,level)
#VALUES (%s, %s, %s, %s, %s)
#ON CONFLICT (user_id) DO NOTHING;
#""")

user_table_insert = ("""
INSERT INTO users ( user_id, first_name,last_name,gender,level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title,artist_id,year,duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id,name,location,latitude,longitude) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time,hour,day,week,month,year,weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id,songs.artist_id FROM artists 
JOIN songs ON artists.artist_id = songs.artist_id
WHERE songs.title = (%s)
AND artists.name = (%s)
AND songs.duration = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]