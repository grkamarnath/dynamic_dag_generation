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

    def make_output_port(self, dag):
        return PythonOperator(
            task_id='output_port',
            python_callable=self.load,
            dag=dag)

    @staticmethod
    def make_dependencies(input_, transform, output):
        return input_ >> transform >> output

    def generate_dag(self, dag_id, args):
        with DAG(dag_id, default_args=args) as dag:
            input_port = self.make_input_port(dag)
            transform = self.make_transformation(dag)
            output_port = self.make_output_port(dag)
            self.make_dependencies(input_port, transform, output_port)
            return dag


default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
base_dag = BaseDAG()


# Client Code
# output_ports = ["task_id1", "task_id2"]
my_dag_id = base_dag.generate_dag(
    dag_id='my_dag_id',
    args=default_args
)
