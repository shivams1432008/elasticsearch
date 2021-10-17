from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)
run = True
while run:
    option = input("close to shutdown")
    if option == "close":
        run = False

    else:
        name = input("What is your name ")
        quote = input("What is your quote ")
        es.index(index="new_index",
            body={
                "name": name,
                "quote": quote
         })
