import airflow

from base_dag import BaseDAG


class ServingLayer(BaseDAG):

    def make_dependencies(self, dag):
        self.make_output_port(dag)


default_args = {
    'owner': 'me',
    'start_date': airflow.utils.dates.days_ago(2),
}
only_serving = ServingLayer()

# Client Code
only_serving = only_serving.generate_dag(
    dag_id='only_serving',
    args=default_args
)
