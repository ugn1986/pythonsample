from database.db import db

class Customers(db.Document):
    name=db.StringField(required=True, unique=True, min_length=6)
    username=db.StringField(required=True)
    password=db.StringField(required=True)
    address=db.StringField(required=True)
    state=db.StringField(required=True)
    country=db.StringField(required=True)
    email=db.EmailField(required=True)
    pan=db.StringField(required=True)
    contact=db.IntField(required=True)
    dob=db.StringField(required=True)
    accounttype=db.StringField(required=True)

class Loan(db.Document):
    name=db.StringField(required=True, min_length=6)
    loantype=db.StringField(required=True, min_length=3)
    loanamount=db.StringField(required=True)
    date=db.StringField(required=True)
    rateofinterest=db.StringField(required=True)
    durationofloan=db.IntField(required=True)