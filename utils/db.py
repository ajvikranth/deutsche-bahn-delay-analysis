from dotenv import load_dotenv
import os
from supabase import create_client, Client
from datetime import datetime


def insert_timetable(timetable:dict) -> bool:
    load_dotenv()
    url = os.getenv("url")
    key = os.getenv("key")

    supabase: Client = create_client(url, key)
    data, count = supabase.table('deutschebahn').upsert(timetable).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False

if __name__=="__main__":
    timetable = [{'train_number': 19277, 
                  'train_type': 'RE', 
                  'train_line': '10b', 
                  'train_departure': '2024-07-07T14:49:00', 
                  'train_stops': [
                                    'Heidelberg Hbf', 
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
                  'train_delay_msg': 'Bauarbeiten', 
                  'stops_coordinate': [
                      (49.403567, 8.675442), 
                      (49.393678, 8.788425), 
                      (49.320658, 8.812836), 
                      (49.250353, 8.8751), 
                      (49.241239, 8.899932), 
                      (49.237765, 9.101529), 
                      (49.229848, 9.187046), 
                      (49.231571, 9.199771), 
                      (49.188973, 9.220068), 
                      (49.143306, 9.207715)]}]

    print(insert_timetable(timetable))