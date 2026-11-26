import pandas as pd
from datetime import datetime, timezone

def transform(rows):

    df = pd.DataFrame(rows)

    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "high_24h",
        "low_24h",
        "price_change_percentage_24h",
        "last_updated"
    ]]

     # Rename columns
    df = df.rename(columns={
        "id": "coin_id",
        "symbol": "symbol",
        "name": "coin_name",
        "current_price": "price_usd",
        "market_cap": "market_cap_usd",
        "total_volume": "volume_24h_usd",
        "high_24h": "high_24h_usd",
        "low_24h": "low_24h_usd",
        "price_change_percentage_24h": "price_change_24h_pct"
    })


    df["ingested_at"] = datetime.now(timezone.utc).isoformat()


    df = df.drop_duplicates(subset=["coin_id","last_updated"])

    df = df.dropna(subset=["coin_id","price_usd"])

    return df.to_dict(orient="records")