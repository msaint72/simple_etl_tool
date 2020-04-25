import etl_constants as const

# any number of configurations can be defined. This file would be very complicated if the number of
# confgurations increases. To solve this issue this file can be transferred to a relational database
# in which each configuration item would be a column in a configuration table. 
CONFIGURATIONS_COUNT=1
# input configuration
INPUT_TYPE=[const.REST_API_JSON]
INPUT_DATA_CONNECTION=['https://api.ona.io/api/v1/data/185260']
# output configuration
OUTPUT_TYPE=[const.MONGODB]
OUTPUT_DATA_CONNECTION=['mongodb://localhost:27017/']
OUTPUT_DB=['wfp']
OUTPUT_COLLECTION=['ona_platform']
# mapping configuration
# this simple mapping format is introduced here to show that a transformatin can be done
# more complex mappings can be added with providing a proper implementation is data_transformers component  
INPUT_TO_OUTPUT_MAPPING=(['['
        '{"input_field":"_id","output_field":"_id"},'
        '{"input_field":"avoid_eating","output_field":"avoid_eating_changed_name"}]'])