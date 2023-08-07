import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

@custom
def transform_json_parquet(df, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block (if applicable)
        args: The output from any additional upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Convert pandas DataFrame to PyArrow Table
    table = pa.Table.from_pandas(df)

    # Write PyArrow Table to PARQUET file
    pq.write_table(table, './S3/Silver/list_breweries.parquet')

    return df

