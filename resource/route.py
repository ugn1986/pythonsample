from resource.customer import Customer,Login,Loans

def initialize_routes(api):

    api.add_resource(Customer, '/api/accountdetail','/api/accountdetail/<string:name>')
    api.add_resource(Login, '/api/accountdetail/login')
    api.add_resource(Loans, '/api/loans')  