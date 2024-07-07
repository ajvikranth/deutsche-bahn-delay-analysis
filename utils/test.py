from dotenv import load_dotenv
import os
from deutsche_bahn_api import (api_authentication,
                                station,
                                timetable_helper)
import json

def get_data():
    load_dotenv()
    api = api_authentication.ApiAuthentication(client_id=os.getenv("client_id"),
                                            client_secret=os.getenv("client_secret"))
    success: bool = api.test_credentials()
    print(success)

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
    train_delays = timetablehelper.get_timetable_changes(trains_in_this_hour)

    timetable_list = []

    for train in trains_in_this_hour:
        timetable = {
        "train_number": "",
        "train_type": "",
        "train_line": "",
        "train_departure": "",
        "train_stops": "",
        "train_delay_departure": "",
        "train_delay_msg": []
        }
        timetable['train_number']= train.train_number
        timetable['train_type']= train.train_type
        timetable['train_departure']= train.departure
        timetable['train_stops']= train.stations

        try:
            timetable['train_line']= train.train_line
        except AttributeError:
            timetable['train_line']= 'unk'
        # for d_train in  train_delays:
        #     if train.train_number == d_train.train_number:
        #         try:
        #             timetable["train_delay_departure"] = d_train.train_changes.
        #         for j in d_train.train_changes.messages:
        #             timetable["train_delay_msg"].append(j.message)
        #     else:
        #         timetable["train_delay_departure"] = train.departure
        dtrain = timetablehelper.get_timetable_changes([train])
        try:
            timetable["train_delay_departure"] = dtrain[0].train_changes.departure
        except:
            timetable["train_delay_departure"] = train.departure

        timetable_list.append(timetable)
        

    json_object = json.dumps(timetable_list, indent=4, ensure_ascii=False)
 
    # Writing to sample.json

    with open("sample.json", "wb") as outfile:
        outfile.write(json_object.encode('utf-8'))
        
if __name__ == "__main__":
    get_data()
