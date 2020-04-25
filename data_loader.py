import etl_constants
import pymongo

# This component implements loading the transformation result into target db/file
# It uses factory method design pattern to decide which load implementation to be used

class DataLoader:
    collection=None;
    dest_type=''
    def __init__(self,dest_type,target_connection,target_db,target_collection):
        self.dest_type=dest_type
        if(self.dest_type==etl_constants.MONGODB):
            try:
                mongo_client= pymongo.MongoClient(target_connection)
                mongo_db=mongo_client[target_db]
                self.collection=mongo_db[target_collection]
            except Exception as e:
                print("Problem connecting to MongoDB:",type(e))
                raise e

    def load_data(self,item):
        loader=get_data_loader(self.dest_type)
        return loader(self.collection,item)

def get_data_loader(dest_type):
    if(dest_type==etl_constants.MONGODB):
        return _load_to_mongodb
    else:
        raise ValueError(dest_type)

#********************************************************************
# loader implementations
#********************************************************************
# this implementation loads the data into a mongodb database
def _load_to_mongodb(collection,item):
    try:
        result=collection.insert_one(item)
        return result.inserted_id
    except Exception as e:
        print("Problem inserting to MongoDB:",type(e))
        raise e

# any other loader implementation can be added here