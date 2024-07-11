"""
This is the main module 
"""
from datetime import datetime
from utils import bahn, transform, db
import time


def main() -> None:
    """
    This function utilizes the utils module and ETLs deutsche bahn 
    timetable data into supabase database.
    """
    stations = ["mannheim", "karlsruhe", "stuttgart", "freiburg"]
    for station in stations:
        station_obj = bahn.get_station(station)
        timetable = bahn.get_data(station_obj)
        transformed_timetable = transform.transform(timetable)
        inserted = db.insert_timetable(station, transformed_timetable)

        if inserted:
            print("successful",datetime.now())
        else:
            print("not successful",datetime.now())

        time.sleep(30)


if __name__ =="__main__":
    main()
