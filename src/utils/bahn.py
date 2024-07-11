"""
This module has function to interact with Deutsche-bahn API
"""
import os
from dotenv import load_dotenv

from deutsche_bahn_api import (api_authentication,
                                station,
                                timetable_helper,
                                station_helper)

def get_station(station_name:str) -> station.Station:
    """
    given the station name among ["mannheim", "karlsruhe", "stuttgart", "freiburg"]
    in string format returns station object
    """

    if station_name == "mannheim":
        base_station = station.Station(EVA_NR=8000244,
                                       DS100='RM',
                                       IFOPT='de:08222:2417',
                                       NAME='Mannheim Hbf',
                                       Verkehr='FV',
                                       Laenge='8,468921',
                                       Breite='49,479354',
                                       Betreiber_Name='DB Station und Service AG',
                                       Betreiber_Nr=3925,
                                       Status='')

    elif station_name == "karlsruhe":
        base_station = station.Station(EVA_NR=8000191,
                                       DS100='RK',
                                       IFOPT='de:08212:90',
                                       NAME='Karlsruhe Hbf',
                                       Verkehr='FV',
                                       Laenge='8,402181',
                                       Breite='48,993515',
                                       Betreiber_Name='DB Station und Service AG',
                                       Betreiber_Nr=3107,
                                       Status='')
    elif station_name == "stuttgart":
        base_station = station.Station(EVA_NR=8000096,
                                       DS100='TS',
                                       IFOPT='de:08111:6115',
                                       NAME='Stuttgart Hbf',
                                       Verkehr='FV',
                                       Laenge='9,181635',
                                       Breite='48,784084',
                                       Betreiber_Name='DB Station und Service AG',
                                       Betreiber_Nr=6071,
                                       Status='')

    elif station_name == "freiburg":
        base_station = station.Station(EVA_NR=8000107,
                                       DS100='RF',
                                       IFOPT='de:08311:6508',
                                       NAME='Freiburg(Breisgau) Hbf',
                                       Verkehr='FV',
                                       Laenge='7,84117',
                                       Breite='47,997697',
                                       Betreiber_Name='DB Station und Service AG',
                                       Betreiber_Nr=1893,
                                       Status='')

    elif station_name == "heidelberg":
        base_station = station.Station(EVA_NR=8000156,
                        DS100='RH',
                        IFOPT='de:08221:1160',
                        NAME='Heidelberg Hbf',
                        Verkehr='FV',
                        Laenge='8,675442',
                        Breite='49,403567',
                        Betreiber_Name='DB Station und Service AG',
                        Betreiber_Nr=2628,
                        Status='')

    return base_station


def get_data(base_station:station.Station) -> list:
    """
    This function gets timetable data from Deutsche-bahn API
    """
    load_dotenv()
    api = api_authentication.ApiAuthentication(client_id=os.getenv("client_id"),
                                            client_secret=os.getenv("client_secret"))

    success: bool = api.test_credentials()

    if success:
        timetablehelper = timetable_helper.TimetableHelper(base_station, api)
        trains_in_this_hour = timetablehelper.get_timetable()

        timetable = []

        for train in trains_in_this_hour:

            train_details = {
                            "train_number": "",
                            "train_type": "",
                            "train_line": "",
                            "train_departure": "",
                            "train_stops": "",
                            "train_delay_departure": "",
                            "train_delay_msg": []
                            }

            train_details['train_number']= train.train_number
            train_details['train_type']= train.train_type
            train_details['train_departure']= train.departure
            train_details['train_stops']= base_station.NAME + "|" + train.stations

            try:
                train_details['train_line']= train.train_line
            except AttributeError:
                train_details['train_line']= 'unk'

            dtrain = timetablehelper.get_timetable_changes([train])

            try:
                train_details["train_delay_departure"] = dtrain[0].train_changes.departure

                for j in dtrain[0].train_changes.messages:
                    train_details["train_delay_msg"].append(j.message)

            except Exception as e:
                print(e,"while getting bahn info")
                train_details["train_delay_departure"] = train.departure


            timetable.append(train_details)

        # json_object = json.dumps(timetable, indent=4, ensure_ascii=False)

        return timetable

def get_stops_lat_log(stops:list) -> list:
    """
    This function gets latitude and longitude of the list of stations
    :stops:list of train station stops
    """

    load_dotenv()
    api = api_authentication.ApiAuthentication(client_id=os.getenv("client_id"),
                                            client_secret=os.getenv("client_secret"))

    success: bool = api.test_credentials()
    stationhelper = station_helper.StationHelper()
    stops_coordinates = []
    if success:
        for stop in stops:
            found_stations_by_name =[]
            for i in range(len(stop)//3):

                found_stations_by_name = stationhelper.find_stations_by_name(stop[0:len(stop)-i])
                if  found_stations_by_name:
                    break

            if found_stations_by_name:
                lat = float(found_stations_by_name[0].Breite.replace(",","."))
                long = float(found_stations_by_name[0].Laenge.replace(",","."))

                stops_coordinates.append((lat,long))
            else:
                stops_coordinates.append(())

        return stops_coordinates
