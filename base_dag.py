import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


class BaseDAG:

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

    def make_output_port(self, dag, **kwargs):
        return PythonOperator(
            task_id='output_port',
            python_callable=self.load,
            dag=dag)

    def make_dependencies(self, dag):
        self.make_input_port(dag) >> self.make_transformation(dag) >> self.make_output_port(dag)

    def generate_dag(self, dag_id, args):
        with DAG(dag_id, default_args=args) as dag:
            self.make_dependencies(dag)
            return dag


default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
base_dag = BaseDAG()


# Client Code
si_st_so = base_dag.generate_dag(
    dag_id='si_st_so',
    args=default_args
)
