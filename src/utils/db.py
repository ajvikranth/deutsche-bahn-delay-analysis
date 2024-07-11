"""
This module contains functions that interact with database
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client


def insert_timetable(station, timetable:list) -> bool:
    """
    This function inserts data into database

    :timetable:list of transformed train detail
    """
    load_dotenv()
    url = os.getenv("url")
    key = os.getenv("key")

    if station == "mannheim":
        supabase: Client = create_client(url, key)
        data, _ = supabase.table('deutschebahn_mannheim').upsert(timetable).execute()
        data, ls = data
    elif station == "karlsruhe":
        supabase: Client = create_client(url, key)
        data, _ = supabase.table('deutschebahn_karlsruhe').upsert(timetable).execute()
        data, ls = data
    elif station == "stuttgart":
        supabase: Client = create_client(url, key)
        data, _ = supabase.table('deutschebahn_stuttgart').upsert(timetable).execute()
        data, ls = data
    elif station == "freiburg":
        supabase: Client = create_client(url, key)
        data, _ = supabase.table('deutschebahn_freiburg').upsert(timetable).execute()
        data, ls = data

    if len(ls)>0:
        return True
    return False
