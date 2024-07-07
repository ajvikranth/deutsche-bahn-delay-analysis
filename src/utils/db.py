"""
This module contains functions that interact with database
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client


def insert_timetable(timetable:list) -> bool:
    """
    This function inserts data into database

    :timetable:list of transformed train detail
    """
    load_dotenv()
    url = os.getenv("url")
    key = os.getenv("key")

    supabase: Client = create_client(url, key)
    data, _ = supabase.table('deutschebahn').upsert(timetable).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False
