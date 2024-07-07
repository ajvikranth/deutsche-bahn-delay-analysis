from datetime import datetime
import json

def transform(timetable:list) -> list:

    # timetable = json.loads(timetable)

    for train_details in timetable:

        train_details["train_number"] = int(train_details["train_number"])
        train_details["train_departure"] = datetime.strptime(
                                train_details["train_departure"], '%y%m%d%H%M'
                                ).isoformat()
        train_details["train_delay_departure"] = datetime.strptime(
                                train_details["train_delay_departure"], '%y%m%d%H%M'
                                ).isoformat()
        
        train_details["train_stops"] = train_details["train_stops"].split("|")
             
        if train_details["train_delay_msg"]:
            train_details["train_delay_msg"] = max(
                            set(train_details["train_delay_msg"]),
                            key=train_details["train_delay_msg"].count
                            )
        else:
            train_details["train_delay_msg"] = None
    
    return timetable

# def get_stops_lat_log(stops:list)

if __name__=="__main__":
    timetable = [{
        "train_number": "19277",
        "train_type": "RE",
        "train_line": "10b",
        "train_departure": "2407071449",
        "train_stops": "Heidelberg Hbf|Neckargemⁿnd|Meckesheim|Sinsheim(Elsenz) Hbf|Sinsheim Museum/Arena|Bad Rappenau|Bad Wimpfen|Bad Friedrichshall Hbf|Neckarsulm|Heilbronn Hbf",
        "train_delay_departure": "2407071449",
        "train_delay_msg": [
            "Bauarbeiten",
            "Bauarbeiten"
        ]
    }]

    t_timetable = [
        {'train_number': 19277, 
         'train_type': 'RE', 
         'train_line': '10b', 
         'train_departure': '2024-07-07T14:49:00', 
         'train_stops': ['Heidelberg Hbf', 
                         'Neckargemⁿnd', 
                         'Meckesheim', 
                         'Sinsheim(Elsenz) Hbf', 
                         'Sinsheim Museum/Arena', 
                         'Bad Rappenau', 
                         'Bad Wimpfen', 
                         'Bad Friedrichshall Hbf', 
                         'Neckarsulm', 
                         'Heilbronn Hbf'], 
         'train_delay_departure': '2024-07-07T14:49:00', 
         'train_delay_msg': 'Bauarbeiten'
                         }]



    print(transform(timetable))
    