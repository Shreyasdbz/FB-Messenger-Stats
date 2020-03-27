import os
import json

path = "../"

class parser:
    def __init__(self):
        self.fName = "example.json" 

    def printData(self):
        with open('Data/example.json') as f:
            data = json.load(f)
            print(data['quiz']['maths'])
    

test = parser()
test.printData()