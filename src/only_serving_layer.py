from one_input_one_transform_one_output import OneInputOneTransformOneOutput


class ServingLayer(OneInputOneTransformOneOutput):
    def __init__(self, config):
        super().__init__(config)

    def make_dependencies(self, dag):
        self.make_output_port(dag)


# default_args = {
#     'owner': 'me',
#     'start_date': airflow.utils.dates.days_ago(2),
# }
# pipeline = ServingLayer()
#
# # Client Code
# only_serving = pipeline.generate_dag(
#     dag_id='only_serving',
#     args=default_args
# )
