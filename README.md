# OptiManuAI: All-in-One AI Solution for Manufacturing

Welcome to OptiManuAI, your comprehensive AI solution tailored for the manufacturing industry. OptiManuAI is designed to revolutionize the way manufacturing processes are managed by seamlessly integrating cutting-edge technologies to enhance efficiency, predict future trends, and optimize every aspect of your operations.

## Architectural Setup
![Fabric Global Hack](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/9764a3a6-bab8-46d9-87cf-20a908aabc10)

## Table of Contents
- [Introduction](#introduction)
- [Key Components](#key-components)
  - [1. Data Ingestion & Processing](#data-ingestion--processing)
  - [2. Predictive Analytics Engine](#predictive-analytics-engine)
  - [3. Optimization Algorithms](#optimization-algorithms)
  - [4. Data Visualization Tools](#data-visualization-tools)
  - [5. Integration Layer](#integration-layer)
- [Getting Started](#getting-started)
- [License](#license)

## Introduction

OptiManuAI is an all-encompassing solution designed to meet the specific needs of the manufacturing industry. By leveraging advanced artificial intelligence, predictive analytics, and optimization algorithms, OptiManuAI empowers manufacturers to make informed decisions, streamline processes, and enhance overall productivity.

## Data Lifecycle within Fabric
Our Solution Puts the `Fabric Medallion Architecture` into Consideration. The `Bronze Layer` being our raw zone(Simply raw data), the `Silver layer` being the enriched zone, and the `Gold Layer` being the Validated Zone(With data for Enterprise wide use)
![Data Lifecycle](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/4fdc5cd4-f4f9-4d6e-87a0-3fb26e4f53d5)



### 1. Data Ingestion & Processing
#### Storage in the Bronze Layer
We begin by collecting data from diverse sources, including IoT sensors, sales data, and supply chain information and storing that in our Bronze Layer-Raw data
![Data Load](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/3bbd66cd-52b1-4529-828f-780bd27dcca7)

#### 2. Transforming the Data for Silver Layer
Next we use attach the Lakehouse onto the new notebook and transform the data for the silver layer
![image](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/5843ef2e-6140-4cdd-88a6-1f77871a7c48)

#### Load data to Gold Layer
After transformaion we load our data to the Gold Layer- which consits of the Curated Data
![image](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/079ee1e0-63cb-454d-a3a7-7abe1dba0e10)


### 3. Data Visualization

We utlize PowerBI to generrate the insights and detect the temperature changes beyond the threshold value using `Data activator` and send notifications via teams
![Temperature threshold](https://github.com/AnthonyByansi/OptiManuAI/assets/101401469/7035f802-455e-4f80-8103-09ceaa001b06)


## Getting Started
To Gain insights from the `OptiManuAI` solution, we built a custom copilot- `ManuMate` to help in the interpretation of the insights generated from the Fabric Solution

### User Interaction: 
- `ManuMate Copilot` interacts with the users, answering their questions about the System, guiding them through its features, and helping them interprete the insights it generates

### Data Exploration:
- `ManuMate Copilot` explains the results generated b the predictive analytics engine from `Fabric` and Optimization algorithms in a user-friendly way. It provides recommendations based on these results

### System Monitoring
- `ManuMate Copliot` monitors the system's performance, alerting users to any potential issue or anomalies

### Integration with Other Systems
- `ManuMate Copilot` integrates with the rest of the company systems like `ERP`, `CRM` pulling in relevant data to provide a more comprehensive view of the manufacturing process

### Continuous Learning
- `ManuMate Copilot` learns from user interactions, continuously improves its ability to provide relevant and useful information

### Security and Compliance
- Just like any other copilot built by help of Copilot studio, `ManuMate Copilot` ensures all interactions comply with relevant regulations and standards,and user data is secure.

## License

OptiManuAI is licensed under the [MIT License](./LICENSE). Feel free to explore, modify, and distribute this solution according to the terms of the license.
