from pyspark.sql import SparkSession
from pyspark.sql.functions import count
import io

@custom
def count_records(df):
    # Inicializar a sessão do Spark
    spark = SparkSession.builder \
        .appName("Aggregation") \
        .getOrCreate()

    # Converter o DataFrame do Pandas para DataFrame do PySpark
    #spark_df = spark.createDataFrame(df)

    # Realizar a agregação e contar a quantidade de registros
    #aggregated_df = spark_df.groupBy("brewery_type", "state_province").agg(count("*").alias("Count"))

    aggregated_df = df.groupby(["state_province", "brewery_type"]).size().reset_index(name="Count")

    # Retornar o DataFrame resultante
    return aggregated_df