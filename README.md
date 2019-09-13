## Udacity Data Engineer Nanodegree - Data Pipelines with Airflow Project 

### The goal of this project was to create a workflow using Apache Airflow to execute an ETL of Sparkify log and song data from S3 to Redshift. 

### I created two workflows. One to create the tables in redshift (create_table_task.py) and one executing the ETL (udac_example_dag.py). 

### File Descriptions
    * README.md - Overview of the project with instructions
    
    * dags - Folder containing DAGs
        * create_tables_statements.py - SQL statements to create tables
        * create_tables_task.py - DAG to create tables in redshift by executing statements in 'create_tables_statements.py'
        * etl.py - DAG to execute ETL
     
     * plugins - Folder containg DAG operators and SQL statements for loading data
        * operators 
            * data_quality.py     - operator to perform data quality checks
            * load_dimension.py   - operator to load dimension tables 
            * load_fact.py        - operator to load fact table
            * stage_redshift.py   - operator to extract data from S3 to Redshift
            
        * helpers 
            * sql_queries.py - SQL statements for loading data from staging tables 
            
## Step 1: 
	* Create redshift cluster
	* Make sure to add an IAM role with Administrator Access
    
## Step 2: 
	* Launch Airflow UI 
	* Add connection 'redshift' connecting to your redshift cluster
        * Add connection 'aws_credentials' with your AWS access key and secret key 

## Step 3: 
	* From the Airflow UI turn on 'create_tables_task' and trigger the dag
 
## Step 4: 
	* Once 'create_tables_task' has succesfully ran turn on 'etl_workflow' and trigger the dag

### Once 'etl_workflow' has run successfully the data has been properly loaded into Redshift 
