# Workforce

This projects demonstrate example workflow for fetching, validating and storing data from 
an external source. It uses [Apache Airflow](https://github.com/apache/incubator-airflow)
package, which helps in designing powerful and complex workflows in a very sophisticated
manner. It uses the concept of DAGs(Directed Acyclic graphs), which is a very natual way
of defining workflows. It is a really powerful package with a lot of built in [operators](http://pythonhosted.org/airflow/concepts.html#operators) and sensors are available and you can make your own as well. Check [this article](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/) for more information on this topic.

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

![alt text](https://uxsjdg.bn1302.livefilestore.com/y4pJ2WaWIXSBYItHO1EMh4f3bqP8ZmA8mmsaFnHNtrIB9CMpKjr4r11V1OqN5Z8Dz-MNxWfROczYW7vWgZprXqK51WDMdwMw7m-mdk4p0VZSY-HZ6mRhWOQM8eC4vrQXZ9Fp-HW5jmaTQH0lkJpaTda9sbkguoJhBYKHlYv_PYQwdKRZSYI0LR-xygdLnl8qizhoAdPfYpB3eC2bVrfoc4dqA/workflow.png?psid=1)

