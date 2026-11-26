import os 
from datetime import datetime, timezone


def load(records):

    import boto3
    import pandas as pd


    bucket = os.environ["S3_BUCKET"]

    now = datetime.now(timezone.utc)

    local = f"/tmp/prices_{now:%Y%m%d_%H%M%S}.parquet"


    pd.DataFrame(records).to_parquet(
        local,
        index=False
    )


    key = (
        f"raw/coingecko/"
        f"dt={now:%Y-%m-%d}/"
        f"hour={now:%H}/"
        f"prices_{now:%H%M%S}.parquet"
   )

    s3 = boto3.client("s3")

    s3.upload_file(local,bucket,key)

    os.remove(local)

    return key