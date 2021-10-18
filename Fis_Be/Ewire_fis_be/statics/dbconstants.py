from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log
class MongoAPI:
    def __init__(self, settings):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        self.client = MongoClient("mongodb://192.168.0.238:27017/")  # When only Mongo DB is running on Docker.
        # self.client = MongoClient("mongodb://192.168.0.238:27017/")     # When both Mongo and This application is running on
                                                                    # Docker and we are using Docker Compose
        database = settings['database']
        collection = settings['collection']
        print(database)
        print(collection)
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = settings
    def read(self):
        log.info('Reading All Data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    def readAll(self, query):
        log.info('Reading All Data')
        documents = self.collection.find(query)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    def readOne(self, query):
        log.info('Reading One Data')
        print(":::::::")
        documents = self.collection.find_one(query)
        del documents['_id']
        # output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return documents
    def write(self, data):
        response = self.collection.insert_one(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output
    def update(self):
        log.info('Updating Data')
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    def delete(self, data):
        log.info('Deleting Data')
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output