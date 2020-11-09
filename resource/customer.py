import json
from flask import  request, Response
from flask_restful import  Resource
from database.models import Customers,Loan
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resource.errors import SchemaValidationError, NameAlreadyExistsError, UnauthorizedError,InternalServerError,UserNotExistsError

class Customer(Resource):
    def post(self):
        try:
            customer = request.get_json()
            customers = Customers(**customer)
            customers.save()
            name=customers.username
            return (str(name)),200

        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise NameAlreadyExistsError
        except Exception as e:
            raise InternalServerError
    
    def get(self,name):
        try:
            customer= Customers.objects.get(name=name).to_json()
            return Response(customer, mimetype="application/json", status=200)

        except DoesNotExist:
            raise  UserNotExistsError

    def put(self,name):
        try:
            user= Customers.objects.get(name=name)
            body = request.get_json()
            Customers.objects.get(name=name).update(**body)
            return "Record Successfully Updated",202

        except DoesNotExist:
            raise  UserNotExistsError
        except Exception as e:
            raise InternalServerError

class Login(Resource):
    def get(self):
        try:
            login = request.get_json()
            customer = Customers.objects.get(name=login.get('name'))
            authorized = Customers.objects.get(password=login.get('password'))
            return 'User Login Sucessfully', 200
            if not authorized:
                raise UnauthorizedError

        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError 

class Loans(Resource):
    def post(self):
        try:
            loandetails = request.get_json()
            customer = Customers.objects.get(name=loandetails.get('name'))
            loan = Loan(**loandetails)
            loan.save()
            return "loan added successfully",200
            if not customer:
                raise UnauthorizedError

        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
    