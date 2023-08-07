# Mage-Development

This repository contains the Mage development code for data processing and transformation pipelines. It includes a pipeline called "Brewery" that performs the following treatments on the data:

## Pipeline: Brewery

The Brewery pipeline consists of the following data treatments:

1. Bronze Layer:

    * The raw data is stored as a JSON file in the Bronze layer.
    * The JSON file contains information about breweries.

2. Silver Layer:

    * The data from the Bronze layer is transformed into columnar storage format using the Parquet format.
    * The transformed data is stored in the Silver layer.
    * The columnar storage format provides efficient querying and processing of the data.

3. Gold Layer:

    * An aggregation of breweries is performed based on their type and location.
    * The aggregated data provides insights into the distribution of breweries by type and location.
    * The aggregated view is stored in the Gold layer.
    * By organizing the data into these layers, the Brewery pipeline enables efficient data processing and analysis, allowing for easier exploration and retrieval of information.

# Getting Started
To run the Brewery pipeline, follow these steps:

1.  Install Mage

    ```bash
    pip install mage-ai

2. Create new project

    ```bash
    mage init [project_name]

3. Launch Mage

    ```bash
    mage start [project_name]

4. Clone the repository in the Mage Project directory:

    ```bash
    cd [project_name]
    git clone https://github.com/lecarnevali/Mage-Development.git

5. Create the S3 mocked directory:

    ```bash
    mkdir -p ./S3/Bronze
    mkdir -p ./S3/Silver
    mkdir -p ./S3/Gold

5. Run the brewery pipeline:

    ```bash
    mage run [project_name] brewery