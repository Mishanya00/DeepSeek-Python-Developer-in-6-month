from datetime import datetime, timezone
from t2_utc_offsets import utc_offsets

country = input('Country: ').lower()

if country not in utc_offsets:
    print('Error: Non-existing country entered!')
else:
    utc_datetime = datetime.now(timezone.utc)
    utc_datetime_str = datetime.strftime(utc_datetime, '%d-%m-%Y %H:%M')

    country_datetime = datetime.now(utc_offsets[country])
    country_datetime_str = datetime.strftime(country_datetime, '%d-%m-%Y %H:%M')

    print('UTC Date & Time: ' + utc_datetime_str)
    print(country.upper() + ' Date & Time: ' + country_datetime_str)
