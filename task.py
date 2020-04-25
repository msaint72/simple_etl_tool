import data_extractor as data_extractor
import data_transformer as data_transformer
import data_loader as data_loader
import config

# This component is the main program for the requested task 
# It uses a configuration file (config.py) for input, output and transformation configurations

# defining multiple configurations is possible in config.py.
# runs the transfer operation for each configuration.
for configNo in range(0,config.CONFIGURATIONS_COUNT):
    # get the proper implementations of extractor, transformer and loader based on the configurations 
    extractor=data_extractor.DataExtractor(config.INPUT_TYPE[configNo],
                                        config.INPUT_DATA_CONNECTION[configNo])
    transformer=data_transformer.DataTransformer(config.INPUT_TYPE[configNo],
                                                config.OUTPUT_TYPE[configNo],
                                                config.INPUT_TO_OUTPUT_MAPPING[configNo])
    loader=data_loader.DataLoader(config.OUTPUT_TYPE[configNo],
                                    config.OUTPUT_DATA_CONNECTION[configNo],
                                    config.OUTPUT_DB[configNo],
                                    config.OUTPUT_COLLECTION[configNo])

    counter=1
    # loop through the data extracted from the input source
    for item in extractor.extract_data():
        # transform the item into desired format
        out_item=transformer.transform_data(item)
        # insert the transformed item into output destination
        insert_id=loader.load_data(out_item)
        print("Created item {0} with id {1}".format(counter,insert_id))
        counter+=1

