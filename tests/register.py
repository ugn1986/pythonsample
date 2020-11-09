import json
from tests.basetest import BaseTest

class RegisterTest(BaseTest):
    def test_successful_Register(self):
        user = json.dumps({
            "name":"daniel",
            "username":"daniel",
            "password":"daniel",
            "address":"address",
            "state":"tn",
            "country":"india",
            "email":"daniel@gmail.com",
            "pan":"7834287",
            "contact":"7978349",
            "dob":"984389",
            "accounttype":"loan"
        })

        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)
        self.assertEqual(200, response.status_code)

    
    def test_Register2(self):
        user = json.dumps({
            "nam":"daniel",
            "username":"daniel",
            "password":"daniel",
            "address":"address",
            "state":"tn",
            "country":"india",
            "email":"daniel@gmail.com",
            "pan":"7834287",
            "contact":"7978349",
            "dob":"984389",
            "accounttype":"loan"
        })

        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)
        
        self.assertEqual(400, response.status_code)

    def test_Register3(self):
        user = json.dumps({
            "name":"dani",
            "username":"daniel",
            "password":"daniel",
            "address":"address",
            "state":"tn",
            "country":"india",
            "email":"daniel@gmail.com",
            "pan":"7834287",
            "contact":"7978349",
            "dob":"984389",
            "accounttype":"loan"
        })

        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)
        
        self.assertEqual(500, response.status_code)

    def test_Register4(self):
        user = json.dumps({
            "name":"daniel",
            "username":"daniel",
            "password":"daniel",
            "address":"address",
            "state":"tn",
            "country":"india",
            "email":"daniel@gmail.com",
            "pan":"7834287",
            "contact":"7978349",
            "dob":"984389",
            "accounttype":"loan"
        })
       
       
        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)

        self.assertEqual(400, response.status_code)
        
    
        

   