from dotenv import load_dotenv
import os
from supabase import create_client, Client
from datetime import datetime


def insert_timetable(timetable:dict) -> bool:
    load_dotenv()
    url = os.getenv("url")
    key = os.getenv("key")

    timetable["train_number"] = int(timetable["train_number"])
    timetable["train_departure"] = datetime.strptime(timetable["train_departure"], '%y%m%d%H%M').isoformat()
    timetable["train_delay_departure"] = datetime.strptime(timetable["train_delay_departure"], '%y%m%d%H%M').isoformat()

    supabase: Client = create_client(url, key)
    data, count = supabase.table('deutschebahn').upsert(timetable).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False

if __name__=="__main__":
    timetable = {
    'train_number': '38559',
    'train_type': 'S',
    'train_line': '5', 
    'train_departure': '2407051731', 
    'train_stops': 'Heidelberg-Weststadt/Sⁿdstadt|Heidelberg-Altstadt|Heidelberg-Schlierbach/Ziegelhausen|Heidelberg OrthopΣdie|Neckargemⁿnd|Bammental|Reilsheim|Mauer(b Heidelberg)|Meckesheim|Zuzenhausen|Hoffenheim|Sinsheim(Elsenz) Hbf', 
    'train_delay_departure': '2407051725', 
    'train_delay_msg': ['keine VerspΣtungsbegrⁿndung',
                        'Bauarbeiten', 
                        'Stellwerksst÷rung /-ausfall', 
                        'Stellwerksst÷rung /-ausfall', 
                        'Stellwerksst÷rung /-ausfall', 
                        'VerspΣtung eines vorausfahrenden Zuges', 
                        'keine VerspΣtungsbegrⁿndung', 
                        'Bauarbeiten', 
                        'Stellwerksst÷rung /-ausfall', 
                        'Stellwerksst÷rung /-ausfall', 
                        'Stellwerksst÷rung /-ausfall', 
                        'VerspΣtung eines vorausfahrenden Zuges'
                        ]
    }

    print(insert_timetable(timetable))