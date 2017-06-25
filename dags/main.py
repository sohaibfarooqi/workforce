import airflow
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
from datetime import date, timedelta

def fetch_entity():
	return None

def validate_entity(ds, **kwargs):
	return None

def failed_validation():
	return None

def insert_entity():
	return None

def upload_original_photo():
	return None

def upload_resize_photos():
	return None

def insert_es():
	return None

def email_notification():
	return None



"""
Specify DAG's default arguments.
"""
default_args = {
    'owner': 'Sohaib',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(5),
    'email': ['sohaibfarooqi@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}



dag = DAG('entity_creation_dag', 
	default_args=default_args,
	schedule_interval="@daily")

"""
Invoke API to fetch list of entities.
"""
fetch_entity = PythonOperator(
    task_id='fetch-entity',
    python_callable=fetch_entity,
    dag=dag)

"""
Apply validation rules to all the entites received from API.
Perform fields validation and content validation.
"""
validate_entity = BranchPythonOperator(
	task_id='validate-entity',
	provide_context=True,
	python_callable=validate_entity,
    dag=dag)

validate_entity.set_upstream(fetch_entity)

"""
In case of validation gets failed fire a notification
to user with reason of failure.
"""
failed_validation = PythonOperator(
	task_id='failed-validation',
	python_callable=failed_validation,
    dag=dag)

failed_validation.set_upstream(validate_entity)

"""
If validation passes continue with workflow.
"""
continue_process = DummyOperator(
	task_id='continue-process',
	dag=dag)

continue_process.set_upstream(validate_entity)

"""
Insert Entity in our main database
"""
insert_entity = PythonOperator(
	task_id='insert-entity',
	python_callable=insert_entity,
    dag=dag)

insert_entity.set_upstream(continue_process)


"""
Upload orginal image posted by user to S3.
"""
upload_original_photo = PythonOperator(
		task_id='upload-original-photo',
		python_callable=upload_original_photo,
    	dag=dag)

upload_original_photo.set_upstream(continue_process)


"""
Resize the original image and upload multiple sizes to S3.
"""
upload_resize_photos = PythonOperator(
		task_id='upload-resize-photos',
		python_callable=upload_resize_photos,
    	dag=dag)

upload_resize_photos.set_upstream(continue_process)

"""
Insert entity into ElasticSearch to make it searchable.
"""
insert_es = PythonOperator(
	task_id='insert-es',
	python_callable=insert_es,
    dag=dag)

insert_es.set_upstream(continue_process)

"""
Notify user for task's success
"""
email_notification = PythonOperator(
		task_id='email-notification',
		python_callable=email_notification,
    	dag=dag)

email_notification.set_upstream(insert_entity)
email_notification.set_upstream(upload_original_photo)
email_notification.set_upstream(upload_resize_photos)
email_notification.set_upstream(insert_es)

