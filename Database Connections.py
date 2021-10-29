import pymysql

conn = pymysql.connect(host='.compute-1.amazonaws.com',user='EU_R_READ',password='balbblad',database='EU_R')

try:
	with conn.cursor() as cur:
            cur.execute(launches_bycountry_query('AT'))
            data = pd.read_sql(launches_bycountry_query('AT'), conn)
            print('Going Connection') 
finally:
        conn.close()
