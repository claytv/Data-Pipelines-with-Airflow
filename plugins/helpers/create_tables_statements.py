DROP_TABLE_ARTISTS = """
    DROP TABLE IF EXISTS public.artists;
"""

CREATE_TABLE_ARTISTS = """
    CREATE TABLE public.artists (
        artist_id varchar(256) PRIMARY KEY,
        name varchar(256),
        location varchar(256),
        lattitude numeric(18,0),
        longitude numeric(18,0)
    );
"""

DROP_TABLE_SONGPLAYS = """
    DROP TABLE IF EXISTS public.songplays;
"""

CREATE_TABLE_SONGPLAYS = """
    CREATE TABLE public.songplays (
        play_id INT IDENTITY(0,1) PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int4 NOT NULL,
        "level" varchar(256),
        song_id varchar(256),
        artist_id varchar(256),
        session_id int4,
        location varchar(256),
        user_agent varchar(256)
    );
"""

DROP_TABLE_SONGS = """
    DROP TABLE IF EXISTS public.songs;
"""

CREATE_TABLE_SONGS = """
    CREATE TABLE public.songs (
        song_id varchar(256) PRIMARY KEY,
        title varchar(256),
        artist_id varchar(256),
        "year" int4,
        duration numeric(18,0)
    );
"""

DROP_TABLE_STAGING_EVENTS = """
    DROP TABLE IF EXISTS public.staging_events;
"""

CREATE_TABLE_STAGING_EVENTS = ("""
    CREATE TABLE public.staging_events (
        artist varchar(256),
        auth varchar(256),
        firstname varchar(256),
        gender varchar(256),
        iteminsession int4,
        lastname varchar(256),
        length numeric(18,0),
        "level" varchar(256),
        location varchar(256),
        "method" varchar(256),
        page varchar(256),
        registration numeric(18,0),
        session_id int4,
        song varchar(256),
        status int4,
        ts int8,
        user_agent varchar(256),
        user_id int4
    );
""")

DROP_TABLE_STAGING_SONGS = """
    DROP TABLE IF EXISTS public.staging_songs;
"""

CREATE_TABLE_STAGING_SONGS = """
    CREATE TABLE public.staging_songs (
        num_songs int4,
        artist_id varchar(256),
        artist_name varchar(256),
        artist_latitude numeric(18,0),
        artist_longitude numeric(18,0),
        artist_location varchar(256),
        song_id varchar(256),
        title varchar(256),
        duration numeric(18,0),
        "year" int4
    );
"""

DROP_TABLE_TIME = """
    DROP TABLE IF EXISTS public."time";
"""

CREATE_TABLE_TIME = """
    CREATE TABLE public."time" (
        start_time timestamp PRIMARY KEY,
        "hour" int4,
        "day" int4,
        week int4,
        "month" varchar(256),
        "year" int4,
        weekday varchar(256)
    ) ;
"""

DROP_TABLE_USERS = """
    DROP TABLE IF EXISTS public.users;
"""

CREATE_TABLE_USERS = """
    CREATE TABLE public.users (
        user_id int4 PRIMARY KEY,
        first_name varchar(256),
        last_name varchar(256),
        gender varchar(256),
        "level" varchar(256)
    );
"""

