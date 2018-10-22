from sodapy import Socrata
import psycopg2


def connect_api(endpoint, api_token):
    # Initiate connection using api token, username and pw
    client = Socrata(endpoint,
                     api_token,
                     username='Jawaun.Brown95@gmail.com',
                     password='CannabisPassword$')
    return client


def connect_psql(db_name, user, pw, cursor=False):
    # Try to connect

    try:
        conn = psycopg2.connect("dbname="+db_name + " user=" + user + " password="+pw)
    except:
        print("I am unable to connect to the database.")

    conn.set_isolation_level(0)

    if cursor is True:
        cur = conn.cursor()
        return cur
    else:
        return conn


# if __name__ == "__main__":
#     a = connect_api('https://data.cityofnewyork.us/resource/waf7-5gvc.json', '7KJkvCjyntX41xdWFhHqTyQ7i')
#     b = connect_psql('etltest', 'testuser', 'testpw', cursor=True)
#     c = b.fetchall()
#     print(c)
#     print('done')


