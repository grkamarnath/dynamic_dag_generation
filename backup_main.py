import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator


class BaseDAG:
    def create_dag(self, dag_id, default_args, task_1_func):
        with DAG(dag_id, default_args=default_args) as dag:
            task_1 = PythonOperator(
                task_id='task_1',
                python_callable=task_1_func,
                dag=dag)

            dummy_task1 = PythonOperator(
                task_id='dummy_task1',
                python_callable=task_1_func,
                dag=dag)

            dummy_task2 = PythonOperator(
                task_id='dummy_task2',
                python_callable=task_1_func,
                dag=dag)

            def output_port(task_id):
                return PythonOperator(
                    task_id=task_id,
                    python_callable=self.task_2_func,
                    dag=dag
                )

            for task in output_ports:
                if task == "task_id1":
                    task_1 >> dummy_task1 >> output_port(task)
                else:
                    task_1 >> dummy_task2 >> output_port(task)
            return dag

    def task_1_func(self):
        print("Executing task 1")

    def task_2_func(self):
        print("Executing task 2")


default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
base_dag = BaseDAG()

# Client code
output_ports = ["task_id1", "task_id2"]
my_dag_id = base_dag.create_dag(
    dag_id='my_dag_id',
    default_args=default_args,
    task_1_func=base_dag.task_1_func
)
