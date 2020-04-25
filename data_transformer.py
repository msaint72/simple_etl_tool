import etl_constants
import json

# this component implements data transformations from one format to another.
# it uses factory method design pattern to decide which transformation to use

class DataTransformer:
    source_type=''
    dest_type=''
    mapping_data=''
    def __init__(self,source_type,dest_type,mapping_data):
        self.source_type=source_type
        self.dest_type=dest_type
        self.mapping_data=mapping_data
    def transform_data(self,item):
        transformer=get_data_transformer(self.source_type,self.dest_type)
        return transformer(item,self.mapping_data)

def get_data_transformer(source_type,dest_type):
    if(source_type==etl_constants.REST_API_JSON and dest_type==etl_constants.MONGODB):
        return _transform_json_to_json
    else:
        raise ValueError(source_type,dest_type)

#********************************************************************
# transformer implementations
#********************************************************************
# this is a simple implementation of a json to json transformation
# it uses the mapping data to decide which fields will be available 
# in the output
def _transform_json_to_json(item,mapping_data):
    try:
        mappings=json.loads(mapping_data)
    except:
        raise ValueError("Problem in mapping configuration; invalid JSON!")
    result={}
    for mapping in mappings:
        try:
           result[mapping['output_field']]=item[mapping['input_field']]
        except:
            raise ValueError("Problem in mapping configuration:",mapping)
    return  result

# any other transformation implementation can be added here