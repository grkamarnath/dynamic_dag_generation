# pylint: disable=duplicate-code
import airflow
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

from base_dag import BaseDAG


class SiSTMo(BaseDAG):
    def make_certify_data_quality(self, dag, **kwargs):  # pylint: disable=duplicate-code
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

    def make_dependencies(self, dag):
        input_port = self.make_input_port(dag)
        transform = self.make_transformation(dag)
        for task in output_ports:
            input_port >> transform >> self.make_certify_data_quality(dag, task=task) >> \
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
si_st_mo_dag = SiSTMo()

# Client Code
output_ports = ["output_port_id1", "output_port_id2"]

si_st_mo = si_st_mo_dag.generate_dag(
    dag_id='si_st_mo',
    args=default_args
)
