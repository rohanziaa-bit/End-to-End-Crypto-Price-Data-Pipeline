{{
    config(
        materialized = "incremental",
        unique_key= "COIN_KEY",
        increamental_strategy='merge'

    )
}}

SELECT 
   MD5(TO_VARCHAR(COIN_ID)) AS COIN_KEY,
   COIN_ID,
   COIN_NAME,
   SYMBOL,
   LAST_UPDATED,
   INGESTED_AT
FROM {{ ref('silver_crypto_data') }}

Qualify ROW_NUMBER() OVER(
    PARTITION BY COIN_ID
    ORDER BY LAST_UPDATED DESC, INGESTED_AT DESC
) = 1