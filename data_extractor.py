import requests
import etl_constants

# This component implements extracting data from the input source
# It uses factory ethod design pattern to decide which implementation
# to use
class DataExtractor:
    source_type=''
    source_connection=''
    def __init__(self,source_type,source_connection):
        self.source_type=source_type
        self.source_connection=source_connection
    def extract_data(self):
        extractor=get_data_extractor(self.source_type)
        return extractor(self.source_connection)

def get_data_extractor(source_type):  
    if(source_type==etl_constants.REST_API_JSON):
        return _extract_from_rest_api
    else:
        raise ValueError(source_type)

#********************************************************************
# extractor implementations
#********************************************************************
def _extract_from_rest_api(apiurl):
    # GET the data from the REST API
    resp = requests.get(apiurl,timeout=etl_constants.RESTAPI_TIMEOUT)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /data/ {}'.format(resp.status_code))
    yield from resp.json()
# any implementation for other types of sources can be added here.