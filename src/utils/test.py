"""
this modules is for getting necessary data related to dbahn
"""
import os
from dotenv import load_dotenv

from deutsche_bahn_api import (api_authentication,
                                station_helper)
                                
def main():
    """
    this function gets station object from various 
    """
    load_dotenv()
    api = api_authentication.ApiAuthentication(client_id=os.getenv("client_id"),
                                            client_secret=os.getenv("client_secret"))

    success: bool = api.test_credentials()


    if success:

        stationhelper = station_helper.StationHelper()
        # station = stationhelper.find_stations_by_name("Mannh")
        #station = stationhelper.find_stations_by_name("Karlsruhe")
        # station = stationhelper.find_stations_by_name("Stuttgart")
        station = stationhelper.find_stations_by_name("Freiburg")

        print(station)

if __name__=="__main__":
    main()
