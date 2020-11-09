import json
from tests.basetest import BaseTest

class LoginTest(BaseTest):
    def test_successful_Login(self):
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

        payload = json.dumps({
            "name":"daniel",
            "password":"daniel"
        })
        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)

        response = self.app.get('/api/accountdetail/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(200, response.status_code)

    def test_Incorrect_Username(self):
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

        payload = json.dumps({
            "name":"hfjdhj",
            "password":"daniel"
        })
        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)

        response = self.app.get('/api/accountdetail/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)

    def test_Incorrect_Password(self):
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

        payload = json.dumps({
            "name":"daniel",
            "password":"da"
        })
        response = self.app.post('/api/accountdetail', headers={"Content-Type": "application/json"}, data=user)

        response = self.app.get('/api/accountdetail/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)


   