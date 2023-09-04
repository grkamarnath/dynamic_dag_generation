from airflow.operators.python import PythonOperator

from one_input_one_transform_one_output import OneInputOneTransformOneOutput


class OneInputOneTransformMultiOutput(OneInputOneTransformOneOutput):

    def __init__(self, config):
        super().__init__(config)
        self.output_ports = config["output"]

    def make_dependencies(self, dag):
        input_port = self.make_input_port(dag)
        transform = self.make_transformation(dag)
        for task in self.output_ports:
            input_port >> transform >> self.certify_data_quality(dag, task=task) >> \
            self.make_output_port(dag, task=task)

    def make_output_port(self, dag, **kwargs):
        return PythonOperator(
            task_id=kwargs['task'],
            python_callable=self.load,
            dag=dag)

