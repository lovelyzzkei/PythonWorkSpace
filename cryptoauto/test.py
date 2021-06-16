import pyupbit

access = "cYr06LCxWexxZ3CdUVx5YZUb8u8IH9Rtt3Ton0km"
secret = "qJxEwGiaue0Y5zTqRQVytpwLFDCyzGXQ4goPLnXd"

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))