# Workforce

This projects demonstrate example workflow for fetching, validating and storing data from 
an external source. It uses [Apache Airflow](https://github.com/apache/incubator-airflow)
package, which helps in designing powerful and complex workflows in a very sophisticated
manner. It uses the concept of DAGs(Directed Acyclic graphs), which is a very natual way
of defining workflows. It is a really powerful package with a lot of built in [operators](http://pythonhosted.org/airflow/concepts.html#operators) and sensors are available and you can make your own as well. Check [this article](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/) for more information on these topic.

Addtionally it provides monitoring and maintainence dashboard to montitor and schedule jobs.
It also lets you define connections and hooks from the admin dashboard to be used inside your
workflow.

# Installation and Running

 - `git clone git@github.com:sohaibfarooqi/workforce.git`
 - `export AIRFLOW_HOME=/path/to/airflow-home`
 - `pip install -r requirements.txt`
 - `airflow initdb`
 - `airflow webserver -p 8080`
 - `airflow scheduler`

Further configuration can be done using `airflow.cfg` file in `AIRFLOW_HOME` directory.
By default it will use sqlite as tasks metadata database. This can be changes by either
editing `sql_alchemy_conn` in `airflow.cfg` or it can also be set using 
`AIRFLOW__CORE__SQL_ALCHEMY_CONN` environment variables. There are several other configurations
available please check [configuration docs](http://pythonhosted.org/airflow/configuration.html) 
for more info.

# DAG

The DAG in this project looks like this:

![alt text](https://uxsjdg.bn1302.livefilestore.com/y4m1IrYcF6e_DCqV9j5RrIXWxQskpU0jigJHltHRna3gQqU2J80xh0goo0wzxJIAV2D7iT6vrOFV9rumSc_UEKofqdvg-B_7tBGUkJbMYjUOFcBVBndqOqVwI91EJwZ_j1C3C7VCSeQsidW2px9D7jeQc5Cq8RuJcpsfCQ5_aGB1KCAEzmbNS0JKe9KnpPqtTJp1WtZwoX3KbkhbXphOHgT-g?width=757&height=347&cropmode=none)

 - **Fetch Entity**

	This task will query an external service to fetch entity or list of entities. It invlove
	querying an API and upon successful response it will forward the received data for validation.
	Note that this is PythonOperator. It has a python callable registered in DAG definition.
 			
 - **Validate Entity**
 - **Failed Validation**
 
 - **Continue**
  
  - **Insert Entity**
  - **Upload Original Photo**
  - **Upload Resize Photos**
  - **Insert ES**

 - **Email Notification**