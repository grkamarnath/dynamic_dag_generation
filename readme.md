**Project Objective:**  The main moto of the project will be the accelerator/library/idea to generate airflow dags 
programmatically/dynamically to effectively handle multiple scenarios in real world data projects.
- To demonstrate dag generation dynamically, I will be taking below combinations scenarios/challenges and 
selecting dag at run-time for given scenario.
  - All combinations of `Single/Multiple Input Port, Single/Multiple Transformation and Single/Multiple Output Port` 
  it will be total 8 combinations(2! * 2! * 2!)
      - Single Input Port, Single Transformation and Single Output Port(SISTSO)
      - Single Input Port, Single Transformation and Multiple Output Port(SISTMO)
      - Single Input Port, Multiple Transformation and Single Output Port(SIMTSO)
      - Single Input Port, Multiple Transformation and Multiple Output Port(SIMTMO)
      - Multiple Input Port, Single Transformation and Single Output Port(MISTSO)
      - Multiple Input Port, Multiple Transformation and Single Output Port(MIMTSO)
      - Multiple Input Port, Single Transformation and Multiple Output Port(MISTMO)
      - Multiple Input Port, Multiple Transformation and Multiple Output Port(MIMTMO)
  - Dag contains only one task or few tasks remaining all tasks are optional
  - Multiple inputs in single input port & Multiple outputs in single Output port


**Advantages of dynamic dag generation:**
  - **Consistency:** All the dags across projects/streams within project will be consistent, and 
  it allows us to implement all best practices in place and effectively use across organization. 
  - **Faster development:** It will enable other devs who didn't know much about airflow also able 
  create dag without knowing much context on the airflow.
  - **Flexibility:** Having dynamic dag setup in platform services allows a lot of flexibility to cover
  wide range scenarios with minimal effort.
  - **Code reliability**
