import pandas as pd
from etltools.configs import connect_api
from time import sleep


def get_client(limiter):
    # Example authenticated client (needed for non-public datasets):
    client = connect_api('data.cityofnewyork.us', '7KJkvCjyntX41xdWFhHqTyQ7i')

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get('waf7-5gvc', limit=limiter)
    sleep(2)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results


if __name__ == "__main__":
    a = get_client(100)
    print(a)
    print('done')
