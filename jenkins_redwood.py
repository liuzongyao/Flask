import requests
import json
import pymongo


class Jenkins_Redwood:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://52.80.107.116:27017/")
        self.db = self.client["automationframework"]

    def get_test_case_id_by_name(self, test_case_name):
        collection = self.db["executiontestcases"]
        for x in collection.find():
            print x.keys()
            if 'name' in x.keys():
                if x['name'] == test_case_name:
                    #bson_object = x['_id']
                    test_case_id = {'testcaseID': x['testcaseID'], '_id': x['_id']}
                    return test_case_id

    def get_execution_id_by_name(self, execution_name):
        collection = self.db["executions"]
        for x in collection.find():
            if x['name'] == execution_name:
                execution_id = x['_id']
                return execution_id

    def get_machines_by_description(self, description):
        with open('machine_template.json', 'r') as f:
            machine = json.load(f)
        collection = self.db["machines"]
        for x in collection.find():
            if x['description'] == description:
                machine.update({'host': x['host']})
                machine.update({'description': x['description']})
                machine.update({'_id': str(x['_id'])})
                return machine

    def generate_execution_date(self, **kwargs):
        print self.db

        with open('execution_template.json', 'r') as f:
            execution = json.load(f)
        execution.update({'testcases': kwargs.get('testcases')})
        execution.update({'executionID': kwargs.get('executionID')})
        execution.update({'machines': kwargs.get('machines')})
        return execution


j = Jenkins_Redwood()
test_case = j.get_test_case_id_by_name('pet store')
print test_case
execution_id = j.get_execution_id_by_name('pet store')
print execution_id
machines = j.get_machines_by_description('host name is:qaimages1-98dcb6749-ncgkl')
print machines

execution_data = j.generate_execution_date(testcases=[test_case], executionID=execution_id, machines=[machines])
print execution_data


json.dump(execution_data, open('execution_data.json', 'w'))


payload1 = '{"username":"admin","password":"admin"}'
headers1 = {'Content-Type':'application/json'}
r1 = requests.post('http://qaimages1.petrochina.haproxy-52-80-107-116-testorg001.myalauda.cn:3000/login', data=payload1, headers=headers1, allow_redirects=False)
# r = r1.history[0]
# print r.cookies
print r1.status_code
print r1.cookies.keys()
print r1.cookies.values()
print r1.text


# with open('./bin/test.json', 'r') as f:
#     data = json.load(f)

cookie = "project={};role={};sessionid={};username={}".format(r1.cookies['project'],r1.cookies['role'],r1.cookies['sessionid'],r1.cookies['username'],)

headers = {'Content-Type':'application/json', 'Cookie': cookie}

print json.dumps(headers)

r = requests.post('http://qaimages1.petrochina.haproxy-52-80-107-116-testorg001.myalauda.cn:3000/executionengine/startexecution', json=execution_data, headers=headers)

print r.status_code
print r.text

