import airflow
from airflow.operators.python import PythonOperator

from one_input_one_transform_one_output import OneInputOneTransformOneOutput


class OneInputOneTransformMultiOutput(OneInputOneTransformOneOutput):

    def make_dependencies(self, dag):
        input_port = self.make_input_port(dag)
        transform = self.make_transformation(dag)
        for task in output_ports:
            input_port >> transform >> self.certify_data_quality(dag, task=task) >> \
            self.make_output_port(dag, task=task)

    def make_output_port(self, dag, **kwargs):
        return PythonOperator(
            task_id=kwargs['task'],
            python_callable=self.load,
            dag=dag)


default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
pipeline = OneInputOneTransformMultiOutput()

# Client Code
output_ports = ["output_port_id1", "output_port_id2"]

one_input_one_transform_multi_output = pipeline.generate_dag(
    dag_id='one_input_one_transform_multi_output',
    args=default_args
)
