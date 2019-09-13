from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from operators  import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

default_args = {
    'owner': 'claytv',
    'start_date': datetime(2019, 9, 8),
    'depend_on_past': False, 
    'retries': 3, 
    'retry_delay': timedelta(minutes=5),
    'catchup': False, 
    'email_on_failure': False,
    'schedule_interval': '@hourly'
}

dag = DAG('udac_example_dag',
          default_args = default_args,
          description='Load and transform data in Redshift with Airflow',
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Staging_events',
    dag=dag,
    redshift_conn_id = 'redshift',
    aws_credentials_id = 'aws_credentials',
    table = 'staging_events', 
    s3_path = 's3://udacity-dend/log_data',
    extra = "format as json 's3://udacity-dend/log_json_path.json'"
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Staging_songs',
    dag=dag,
    redshift_conn_id = 'redshift',
    aws_credentials_id = 'aws_credentials',
    table = 'staging_songs', 
    s3_path = 's3://udacity-dend/song_data',
    extra = "json 'auto' compupdate off region 'us-west-2'"
)


load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    table = "songplays",
    columns_sql = "(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)",
    redshift_conn_id = 'redshift',
    sql = SqlQueries.songplay_table_insert
    
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dimension_table',
    dag=dag,
    table = "users",
    redshift_conn_id = 'redshift',
    delete = False, 
    sql = SqlQueries.user_table_insert
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    table = "songs",
    redshift_conn_id = 'redshift',
    delete = False, 
    sql = SqlQueries.song_table_insert
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    table = "artists",
    redshift_conn_id = 'redshift',
    delete = False, 
    sql = SqlQueries.artist_table_insert
)

load_time_dimension_table = LoadDimensionOperator(
     task_id='Load_time_dim_table',
     dag=dag,
     table = "time",
     redshift_conn_id = 'redshift',
     delete = False, 
     sql = SqlQueries.time_table_insert
)

run_quality_checks = DataQualityOperator(
     task_id='Run_data_quality_checks',
     dag=dag,
     redshift_conn_id = 'redshift',
     tables = ["songplays", "artists", "users", "songs", "time"]
 )
end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)




start_operator>>stage_events_to_redshift
start_operator>>stage_songs_to_redshift
stage_songs_to_redshift>>load_songplays_table
stage_events_to_redshift>>load_songplays_table
load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table
load_song_dimension_table >> run_quality_checks 
load_user_dimension_table >> run_quality_checks 
load_artist_dimension_table >> run_quality_checks 
load_time_dimension_table >> run_quality_checks 
run_quality_checks  >> end_operator 
