import pymysql

conn = pymysql.connect(host='ec2-54-237-33-253.compute-1.amazonaws.com',user='EU_AMZL_OR_READ',password='1IkOzu37sf7sj',database='EU_AMZL_OR')

try:
	with conn.cursor() as cur:
            cur.execute(launches_bycountry_query('AT'))
            data = pd.read_sql(launches_bycountry_query('AT'), conn)
            print('Going Connection') 
finally:
        conn.close()