import requests
import json
import pymongo

class Jenkins_Redwood:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://118.24.252.42:30001")
        self.db = self.client.get_database("automationframework")
        self.db.authenticate("Redwood_user123", "Redwood_password123", "automationframework", "MONGODB-CR")
        self.host = "http://118.24.252.42:30005"

    def get_test_case_id_by_name(self, test_case_name):
        test_case_id = str(self.db.get_collection("testcases").find_one({'name':test_case_name})['_id'])
        
        executiontestcases_id = str(self.db.get_collection('executiontestcases').find_one({'testcaseID':test_case_id})['_id'])
#         return executiontestcases_id
        return {'testcaseID':test_case_id,'_id':executiontestcases_id}
      
    def get_execution_id_by_name(self, execution_name):
        return str(self.db.get_collection("executions").find_one({'name':execution_name})['_id'])
    

    def get_machines_by_description(self, description):
        with open('machine_template.json', 'r') as f:
            machine = json.load(f)
        collection = self.db["machines"].find_one({'description':description})
        machine.update({'host': collection['host']})
        machine.update({'description': collection['description']})
        machine.update({'_id': str(collection['_id'])})
        return machine                

    def generate_execution_date(self, **kwargs):
        with open('execution_template.json', 'r') as f:
            execution = json.load(f)
        execution.update({'testcases': kwargs.get('testcases')})
        execution.update({'executionID': kwargs.get('executionID')})
        execution.update({'machines': kwargs.get('machines')})
        return execution


j = Jenkins_Redwood()
test_case = j.get_test_case_id_by_name('print')
print test_case
execution_id = j.get_execution_id_by_name('print')
machines = j.get_machines_by_description('host name is:283fef42d37a')
execution_data = j.generate_execution_date(testcases=[test_case], executionID=execution_id, machines=[machines])
print execution_data
payload1 = '{"username":"admin","password":"admin"}'
headers1 = {'Content-Type':'application/json'}
r1 = requests.post(j.host + '/login', data=payload1, headers=headers1, allow_redirects=False)
cookie = "project={};role={};sessionid={};username={}".format(r1.cookies['project'],r1.cookies['role'],r1.cookies['sessionid'],r1.cookies['username'],)
headers = {'Content-Type':'application/json', 'Cookie': cookie}
r = requests.post(j.host + '/executionengine/startexecution', json=execution_data, headers=headers)
   
print r.status_code
print r.text

