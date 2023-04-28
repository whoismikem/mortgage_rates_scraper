from MortgageRates import MortgageRates
from InfluxPoint import InfluxPoint
from influxdb_client import InfluxDBClient, Point
from dotenv import dotenv_values
from time import sleep

config = dotenv_values(".env") 

influx_server_url = config["INFLUX_SERVER_URL"]
influx_token = config["INFLUX_TOKEN"]
influx_org = config["INFLUX_ORG"]
influx_bucket = config["INFLUX_BUCKET"]
fetch_timeout = 60

# Get influxdb client ready
try:
    ic = InfluxDBClient(url=influx_server_url, token=influx_token, org=influx_org)
    print("Influxdb server url: ", influx_server_url)
    write_api = ic.write_api()
except Exception as e:
    print("Error connecting to influxdb database")
    print(e)


while True:
    try:
        rates = MortgageRates().get_rates()
        print("Rates: ", rates)
        point_tag_name = 'MortgageRates_30fixed'
        point_location = 'MortgageRates'
        rate_30year = rates[0]
        dict_structure = {
            "measurement": rate_30year["product_name"],
            "tags": {"location": point_location},
            "fields": {"rate": rate_30year["rate"], "apr": rate_30year["apr"]}}

        point = Point.from_dict(dict_structure)
        print("POINT: ", point)
        write_api.write(bucket=influx_bucket, record=point)
    except Exception as e:
        print("Error fetching/writing data")
        print(e)

    sleep(fetch_timeout)
