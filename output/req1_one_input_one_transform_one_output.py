import airflow

from one_input_one_transform_one_output import OneInputOneTransformOneOutput

dag = OneInputOneTransformOneOutput(config={})
default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
dag_id = dag.generate_dag(
    dag_id="one_input_one_transform_one_output",
    args=default_args
)