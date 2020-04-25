# Simple ETL Tool
This tool gets data from an input source, transforms the data into desired format and saves it into an output target.

Its design is very flexible which allows you to add any data source for input, any target for output and any transformation you want to apply on data.
To achive this the tool provides three basic components which should be available in any ETL tool; namely Extractor, Transformer and Loader.
For demo purposes following implementations are provided for these components:
    - a REST API data extractor which reads data in JSON format from a REST API.
    - a transformation mapping format which allows any field from the input can be chosen to take place in the output 
    with a specified name(both input and output are in JSON format)
    - a MongoDB data loader which saves the transformed data into a MongoDb database.

It is scalable by allowing to run multiple configurations sequentialy. It is also possible to run multiple instances at the same time to 
achive making transfers in parellel.

To run the program:
- Python 3.x should be installed 
- requests should be installed (pip install requests)
- pymongo should be installed (pip install pymongo)
- MongoDb should be installed locally
    - or OUTPUT configuration should be made properly(in config.py) to access an external MongoDb
- internet connection should be available to read the input data from ONA platform
- run the program with this command: python task.py

Possible improvements 
- In current version if the program crashes or it is stopped before completing whole data transfer, the data transferred to that point should be deleted manually before restarting the transfer operation. Different measures can be taken such as transaction control, flagging the records etc.
to solve this issue depending on the output environments.
- Configuration file can be combersome if multiple configurations are defined. To solve this issue it can be moved to a relational table in which every configuration item can be defined as a column.




