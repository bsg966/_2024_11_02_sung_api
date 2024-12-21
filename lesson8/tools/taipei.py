import requests
from requests import Response
from io import StringIO
from csv import DictReader
from requests.exceptions import RequestException, HTTPError
import streamlit as st

@st.cache_data
def get_youbikes() -> list[dict]:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        response: Response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        raise Exception("伺服器有問題") from http_err
    except RequestException as req_err:
        raise Exception("連線有問題") from req_err
    else:
        print("下載成功")
        file = StringIO(response.text)
        reader = DictReader(file)
        youbike_data: list[dict] = list(reader)
        return youbike_data