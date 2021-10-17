from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)
name = input("What is your name ")
quote = input("What is your quote ")
#es.indices.create("new_index")
es.index(index="new_index",
         body={
             "name": name,
             "quote": quote
         })

print(es.info())
