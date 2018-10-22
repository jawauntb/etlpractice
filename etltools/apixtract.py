from sodapy import Socrata
import pandas as pd
from configs


def get_client():
    # Example authenticated client (needed for non-public datasets):
    client = connect_api('https://data.cityofnewyork.us/resource/waf7-5gvc.json', '7KJkvCjyntX41xdWFhHqTyQ7i')

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get(limit=2000)
    print(results)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df
