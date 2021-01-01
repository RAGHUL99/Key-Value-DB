import sys
import os
import signal
import json
from threading import Thread

class KeyValue(object):

    def __init__(self):
        '''Creates a database object and loads the data from the location path.
        If the file does not exist it will be created on the first update.
        '''
        key_string_error = TypeError('Key/name must be a string!')
        self.dthread = None
        self.y={}
        if(os.path.exists('Datab.json')):
            with open('Datab.json') as database:
                        self.y = json.load(database)
        else:
                self.dumpdb()
                self.dthread = Thread(
                    target=json.dump,
                    args=('./Datab.json', open('./Datab.json', 'wt')))
                self.dthread.start()
                self.dthread.join()
                
    def dumpdb(self):
        '''Force dump memory db to file'''
        with open('./Datab.json', 'w') as json_file:
            json.dump(self.y, json_file)
            return True

    def set(self, key, value):
        '''Used to set Key Value pair'''
        if isinstance(key, str):
            self.y[key] = value
            self.dumpdb()
            print("\nKey value Successfully added!")
            return True
        else:
            print(self.key_string_error)

    def get(self, key):
        '''Get the value of a key'''
        if key in self.y:
            print(self.y[key])
            self.dumpdb()
            print("\n")
        else:
            print("invalid key")

    def rem(self, key):
        '''Delete a key'''
        if not key in self.y: # return False instead of an exception
            return False
        del self.y[key]
        self.dumpdb()
        print("Key Deleted successfully\n")
        print("The Updated DB is \n")
        self.getall()
        print("\n")
        return True

    def getall(self):
        '''Return everything in db'''
        json_formatted_DB = json.dumps(self.y, indent=2)
        print(json_formatted_DB)
        

Value=1
DB=KeyValue()
while(Value<=3 and Value>0):
        
        print("Welcome to KeyValue Miniature DB")
        print("Enter your Options!")
        print("1 Add a new KeyValue \n2 Get the Value for the Key \n3 Del a value for the Key \n4 Show DB and exit ")
        Value=int(input("Enter Your Option : "))
        if(Value==1):
                print("\n")
                key = str(input("enter the key : "))
                
                if (len(key)<32):
                    if key not in DB.y:
                        value = str(input("enter the value : "))
                        if(sys.getsizeof(value)<16384):
                            DB.set(key=key, value = value)
                            print("\n")
                        else:
                            print("Value is Greater than 16KB. Try entering lesser value\n")
                    else:
                        print("Key Already Present!. Try using new Key\n")
                else:
                    print("Enter a Valid key which is a string with 32 chars \n")
        elif(Value==2):
                print("\n")
                key = str(input("enter the key : "))
                if key in DB.y:
                    DB.get(key=key)
                    print("\n")
                else:
                    print("Key not present \n")
        elif(Value==3):
                print("\n")
                key = str(input("enter the key : "))
                if key in DB.y:   
                    DB.rem(key = key)
                    print("\n")
                else:
                    print("Key Aint Present! \n")
        elif(Value==4):
                print("\n")
                DB.getall()
                
                print("\n")
        else:
            break
        