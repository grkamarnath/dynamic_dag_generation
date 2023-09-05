from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup


class OneInputOneTransformOneOutput:
    def __init__(self, config):
        pass

    @staticmethod
    def extract():
        print("Extracting data from source system")

    @staticmethod
    def transform():
        print("Transforming the data as per requirement")

    @staticmethod
    def load():
        print("Loading data to Data Warehouse")

    def make_input_port(self, dag):
        return PythonOperator(
            task_id='input_port',
            python_callable=self.extract,
            dag=dag
        )

    def make_transformation(self, dag):
        return PythonOperator(
            task_id='transform',
            python_callable=self.transform,
            dag=dag
        )

    def certify_data_quality(self, dag, **kwargs):  # pylint: disable=unused-argument
        with TaskGroup(group_id=f"initiate_quality_checks_{kwargs['task']}",
                       tooltip="initiate quality checks") as initiate_quality_checks:
            reshape = PythonOperator(
                task_id='reshape',
                python_callable=self.transform,
                dag=dag
            )

            run_data_quality_checks = PythonOperator(
                task_id='run_data_quality_checks',
                python_callable=self.transform,
                dag=dag
            )

            certify_data_quality = PythonOperator(
                task_id='certify_data_quality',
                python_callable=self.transform,
                dag=dag
            )
            reshape >> run_data_quality_checks >> certify_data_quality
            return initiate_quality_checks

    def make_output_port(self, dag, **kwargs):  # pylint: disable=unused-argument
        return PythonOperator(
            task_id='output_port',
            python_callable=self.load,
            dag=dag)

    def make_dependencies(self, dag):
        self.make_input_port(dag) >> self.make_transformation(dag) >> \
        self.certify_data_quality(dag, task='output_port') >> self.make_output_port(dag)

    def generate_dag(self, dag_id, args):
        with DAG(dag_id, default_args=args) as dag:
            self.make_dependencies(dag)
            return dag

