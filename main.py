from jinja2 import Environment, FileSystemLoader

from one_input_one_transform_multi_output import OneInputOneTransformMultiOutput
from one_input_one_transform_one_output import OneInputOneTransformOneOutput
from only_serving_layer import ServingLayer


def dag(dag_class, config):
    env = Environment(loader=FileSystemLoader('src/'))
    variables = {
        "module": dag_class.__module__,
        "class": dag_class.__name__,
        "dag_id": f"{dag_class.__module__}",
        "config": config
    }
    dag_template = env.get_template('dag_template.jinja2')
    return dag_template.render(variables)


def write_file(name: str, file_content: str):
    with open(f"sample_folder/{name}", "w") as f:
        f.write(file_content)


def read_file(file_path: str):
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents


def upload_dag(condition):
    if condition == "one_input_one_transform_one_output":
        dag_client_content = dag(OneInputOneTransformOneOutput, config={})
        # upload_dag_to_airflow
        write_file(name="one_input_one_transform_one_output.py",
                   file_content=read_file(f"src/{OneInputOneTransformOneOutput.__module__}.py"))
        write_file(name="req1_one_input_one_transform_one_output.py", file_content=dag_client_content)
    elif condition == 'one_input_one_transform_multi_output':
        config = {"output": ["output_port_id1", "output_port_id2"]}
        dag_client_content = dag(OneInputOneTransformMultiOutput, config=config)
        # upload_dag_to_airflow
        write_file(name="one_input_one_transform_one_output.py",
                   file_content=read_file(f"src/{OneInputOneTransformOneOutput.__module__}.py"))
        write_file(name="one_input_one_transform_multi_output.py",
                   file_content=read_file(f"src/{OneInputOneTransformMultiOutput.__module__}.py"))
        write_file(name="req1_one_input_one_transform_multi_output.py", file_content=dag_client_content)
    else:
        dag(ServingLayer, config={})


upload_dag("one_input_one_transform_multi_output")

# Problem: How to integrate these dags into client request
#   Approach 1:
#   1. select the dag based on user request
#   2. Pass the required variables to the DAG class
#   3. load selected dag as byte string and construct unique file name and upload into DAG bucket folder
#   In this approach I need to upload required dag files like one_input_one_transform_one_output.py or/and
#   one_input_one_transform_multi_output.py files and client file that contains the generate dag
#
#   Approach 2: No client file needed instead config will be passed to direct selected dag class
#   **#
