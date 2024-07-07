"""
This module contains functions to transform api data suitable for inserting into database
"""
from datetime import datetime
from utils.bahn import get_stops_lat_log

def transform(timetable:list) -> list:
    """
    This function transforms  api data suitable for inserting into database
    
    :timetable:list list train details from api
    """

    for train_details in timetable:

        train_details["train_number"] = int(train_details["train_number"])
        train_details["train_departure"] = datetime.strptime(
                                train_details["train_departure"], '%y%m%d%H%M'
                                ).isoformat()
        train_details["train_delay_departure"] = datetime.strptime(
                                train_details["train_delay_departure"], '%y%m%d%H%M'
                                ).isoformat()

        train_details["train_stops"] = train_details["train_stops"].split("|")
        train_details["stops_coordinate"] = get_stops_lat_log(train_details["train_stops"])

        if train_details["train_delay_msg"]:
            train_delay_msgs = list(filter(None,train_details["train_delay_msg"]))
            if train_delay_msgs:
                train_details["train_delay_msg"] = max(
                                set(train_delay_msgs),
                                key=train_delay_msgs.count
                                )
            else:
                train_details["train_delay_msg"] = None
        else:
            train_details["train_delay_msg"] = None

    return timetable
