import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
from decouple import config

USER = config('PG_USER')
PASS = config('PG_PASS')
DB = config('PG_DB')
PORT = config('PG_PORT')

def ingest_data(parquet_file, table_name):
    parquet_file = pq.ParquetFile(parquet_file)

    engine = create_engine(f'postgresql://{USER}:{PASS}@de_postgres:{PORT}/{DB}')

    for batch in parquet_file.iter_batches(batch_size = 100000):
        t_start = time()
        batch_df = batch.to_pandas()
        batch_df.columns = [c.lower() for c in batch_df.columns]
        batch_df.to_sql(name=table_name,con=engine, if_exists='append',index=False)
        t_end = time()
        print("inserted next chunck.. %.3f seconds" % (t_end - t_start))