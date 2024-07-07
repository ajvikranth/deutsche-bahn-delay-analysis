"""
This is the main module 
"""
from datetime import datetime
from utils import bahn, transform, db


def main() -> None:
    """
    This function utilizes the utils module and ETLs deutsche bahn 
    timetable data into supabase database.
    """
    timetable = bahn.get_data()
    transformed_timetable = transform.transform(timetable)
    inserted = db.insert_timetable(transformed_timetable)

    if inserted:
        print("successful",datetime.now())
    else:
        print("not successful",datetime.now())


if __name__ =="__main__":
        main()
