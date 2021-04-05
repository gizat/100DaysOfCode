from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

ORIGIN_CITY_IATA = "TSE"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )