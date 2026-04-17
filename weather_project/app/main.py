import extract.take_weather_data as extcwtdt
from load.ssms_add_data import add_ssms


extcwtdt.create_temporery_table()
add_ssms()




