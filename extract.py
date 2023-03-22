#%%
import os
from kaggle.api.kaggle_api_extended import KaggleApi
#%%
def extract_data():
    try:
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(dataset='katehighnam/beth-dataset', path='./data', unzip=True)
        val = os.listdir('./data')
    except Exception as e:
        val = str(e)
    return val
