import pymongo 

client= pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb=client['Employee']

information=mydb.employeeInformation


record=[
        {
        'first_name':'Manideep',
        'Last_name':'Mittapalli'
        },
                
        {
        'first':'Krishna',
        'last':'Naik'
        }
       ]


information.insert_many(record)