from dhanhq import dhanhq

dhan = dhanhq("1100991747","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA2NzczNDQxLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMDk5MTc0NyJ9.Fstdn58QGolglxuW-jpwI4UKtVF9updjrms9dcxy9-Grzk9MzEbedoUy2IhVr0_kOAybflMScN9Xd4HtXahcTQ")


print(dhan.get_holdings())

# print(dhan.historical_minute_charts(
#     symbol='TCS',
#     exchange_segment='NSE_EQ',
#     instrument_type='EQUITY',
#     expiry_code=0,
#     from_date='2022-01-08',
#     to_date='2022-02-08'
# ))
