"""

"""
import json

import os
from dotenv import load_dotenv

from deutsche_bahn_api import (api_authentication,
                                station,
                                timetable_helper)

def get_data() -> json:
    """
    
    """
    load_dotenv()
    api = api_authentication.ApiAuthentication(client_id=os.getenv("client_id"),
                                            client_secret=os.getenv("client_secret"))

    success: bool = api.test_credentials()

    if success:
        heidelberg = station.Station(EVA_NR=8000156,
                        DS100='RH',
                        IFOPT='de:08221:1160',
                        NAME='Heidelberg Hbf',
                        Verkehr='FV',
                        Laenge='8,675442',
                        Breite='49,403567',
                        Betreiber_Name='DB Station und Service AG',
                        Betreiber_Nr=2628,
                        Status='')

        timetablehelper = timetable_helper.TimetableHelper(heidelberg, api)
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
            train_details['train_stops']= heidelberg.NAME + "|" + train.stations

            try:
                train_details['train_line']= train.train_line
            except AttributeError:
                train_details['train_line']= 'unk'

            dtrain = timetablehelper.get_timetable_changes([train])

            try:
                train_details["train_delay_departure"] = dtrain[0].train_changes.departure

                for j in dtrain[0].train_changes.messages:
                    train_details["train_delay_msg"].append(j.message)

            except AttributeError:
                train_details["train_delay_departure"] = train.departure

            timetable.append(train_details)

        # json_object = json.dumps(timetable, indent=4, ensure_ascii=False)

        return timetable

if __name__ == "__main__":
    print(get_data())
