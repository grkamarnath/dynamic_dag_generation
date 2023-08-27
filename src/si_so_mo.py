import airflow
from airflow.operators.python import PythonOperator

from base_dag import BaseDAG


class SiSTMo(BaseDAG):

    @staticmethod
    def make_certify_data_quality_task_group_id(**kwargs):
        return f"initiate_quality_checks_{kwargs['task']}"

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
si_st_mo_dag = SiSTMo()

# Client Code
output_ports = ["output_port_id1", "output_port_id2"]

si_st_mo = si_st_mo_dag.generate_dag(
    dag_id='si_st_mo',
    args=default_args
)
