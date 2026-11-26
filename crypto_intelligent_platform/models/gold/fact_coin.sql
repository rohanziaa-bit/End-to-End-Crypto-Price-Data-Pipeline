{{
    config(
        materialized="table"
    )
}}

SELECT 
   MD5(
    CONCAT(
        S.COIN_ID,
        '|',
        TO_VARCHAR(S.LAST_UPDATED),
        '|',
        TO_VARCHAR(S.INGESTED_AT)
    )
   ) AS MARKET_KEY,
   
   D.COIN_KEY,
   S.PRICE_USD,
   S.MARKET_CAP_USD,
   S.HIGH_24_HOUR_USD,
   S.LOW_24_HOUR_USD,
   S.PRICE_CHANGE_24H_PCT,
   S.LAST_UPDATED,
   S.INGESTED_AT

FROM {{ ref('silver_crypto_data') }} S

inner join {{ ref('COIN') }} D
      ON S.COIN_ID = D.COIN_ID
