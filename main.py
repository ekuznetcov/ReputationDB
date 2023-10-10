import os
import datetime
import requests
from connection import MongoDB

# make request
def request_iocs() -> dict:
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer github;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;null'
    }
    response = requests.get('https://labs.inquest.net/api/repdb/list', headers = headers)
    recived_data = response.json()["data"]
    return recived_data


def add_ioc(db: MongoDB, object:dict):
        try:
            if db._collection.find_one({'data':object.get('data')}) == None:
                # object['created_date'] = datetime.datetime.strptime(object['created_date'], '%Y-%m-%d')
                db._collection.insert_one(object)
                print(f"""Add NEW ioc: f"{object['data']}, {object['source_url']} {object['created_date']}\n" in collection""")
            else:
                 print(f"IOC: {object.get('data')} in collection")
        except Exception as ex:
            print("[create_user] Some problem...")
            print(ex)
    
def get_all_iocs(db: MongoDB):
        try: 
            data = db._collection.find()
            print('Get all iocs')
            return data
        except Exception as ex:
            print("[get_all] Some problem...")
            print(ex)

def get_daily_iocs(db: MongoDB):
        try: 
            yesterday = datetime.datetime.today() - datetime.timedelta(1)
            data = db._collection.find({'created_date':{"$gte": datetime.datetime.strftime(yesterday, '%Y-%m-%d') }})
            print(yesterday)
            print('Get all iocs')
            return data
        except Exception as ex:
            print("[get_all] Some problem...")
            print(ex)
            
            
conn = MongoDB(db_name='repdb', collection='replist')
for obj in request_iocs():
    add_ioc(conn, obj)
# save_data
today_str = datetime.datetime.today().strftime('%Y-%m-%d')
with open(f'reputation-{today_str}.csv', 'a') as rep_db:
    fetched_data = get_daily_iocs(conn)
    for object in fetched_data:
        rep_db.write(f"{object['data']}, {object['source_url']} {object['created_date']}\n")