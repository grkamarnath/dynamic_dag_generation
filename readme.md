# <span style="color:#1f77b4;"> Dynamic Airflow DAG Generation Accelerator </span>

## <span style="color:#2ca02c;">Project Objective</span>

The main objective of this project is to provide an accelerator, library, or idea to generate Directed Acyclic Graphs (DAGs) programmatically and dynamically(runtime). This tool is designed to effectively demonstrate DAG generation for various scenarios encountered in real-world data projects.

To demonstrate dynamic DAG generation, we will address the following combinations of scenarios and challenges at runtime:
- **All combinations of Single/Multiple Input Port, Single/Multiple Transformation, and Single/Multiple Output Port (Total: 8 combinations)**
  1. Single Input Port, Single Transformation, and Single Output Port (SISTSO)
  2. Single Input Port, Single Transformation, and Multiple Output Port (SISTMO)
  3. Single Input Port, Multiple Transformation, and Single Output Port (SIMTSO) - Not Yet Implemented
  4. Single Input Port, Multiple Transformation, and Multiple Output Port (SIMTMO) - Not Yet Implemented
  5. Multiple Input Port, Single Transformation, and Single Output Port (MISTSO) - Not Yet Implemented
  6. Multiple Input Port, Multiple Transformation, and Single Output Port (MIMTSO) - Not Yet Implemented
  7. Multiple Input Port, Single Transformation, and Multiple Output Port (MISTMO) - Not Yet Implemented
  8. Multiple Input Port, Multiple Transformation, and Multiple Output Port (MIMTMO) - Not Yet Implemented
- **Additional Scenarios:**
  1. DAG containing only one task or with few tasks, where the remaining tasks are optional.


These combinations cover a wide range of scenarios, allowing us to choose the appropriate DAG configuration for a given use case or enhance it for new scenarios.

## <span style="color:#2ca02c;">Advantages of Dynamic DAG Generation</span>

- **Consistency:** By using this approach, all DAGs across projects or streams within a project will be consistent. It enables the implementation of best practices consistently and can be effectively used across the organization.

- **Faster Development:** This accelerator empowers developers who may not have in-depth knowledge of Apache Airflow to create DAGs without requiring extensive context on the airflow platform.

- **Flexibility:** Dynamic DAG generation provides a high degree of flexibility, enabling the platform services or frameworks to handle a wide range of scenarios with minimal effort. It adapts to evolving project requirements.

- **Code Reliability:** The generated DAGs follow a consistent and well-tested pattern, enhancing the reliability and maintainability of the codebase.

By leveraging dynamic DAG generation, this project aims to streamline the development process, improve consistency, and empower a wider range of team members to work with Apache Airflow efficiently.

## <span style="color:#2ca02c;">How to Run</span>

### Installation and Dependencies

Before running the script to generate DAGs, you'll need to install the necessary dependencies. We recommend using `pipenv` for managing the project's virtual environment. If you don't have `pipenv` installed, you can install it using pip:

```bash
pip install pipenv
```

Once pipenv is installed, navigate to your project directory in the terminal and run the following command to install the project dependencies, including development dependencies:
```bash
pipenv install --dev
```
To generate DAGs dynamically, you can run the following command:
```bash
pipenv run python main.py
```
Alternatively, you can activate the project's virtual environment using pipenv shell and then run the script:
```bash
pipenv shell
python main.py
```

## <span style="color:#2ca02c;">Important Notes:</span>

- Whenever you run the above commands, the generated DAGs will be written to the local directory. In a real-world production environment, you can directly upload these generated DAGs into your Apache Airflow environment.

- Please note that this project currently uses Python operators for all tasks, but it can effectively be used with any other operators supported by Apache Airflow to suit your specific use cases.

- Currently, the conditions and rules for DAG generation are hardcoded in the `main.py` i.e. upload_dag(condition="one_input_one_transform_multi_output") file. However, you have the flexibility to modify these conditions and rules to align with your specific project requirements.
By customizing the conditions and rules in the `main.py` file, you can tailor the dynamic DAG generation process to suit your use cases. This adaptability ensures that the generated DAGs align with the unique needs of your data projects.
