from .resources import (
    RegisterApi,
    LoginApi,
    UserDetailsApi,
    PagesApi,
    SinglePageApi,
    DetailsApi
)


def initialize_routes(api):
    api.add_resource(RegisterApi, '/api/auth/register')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(UserDetailsApi, '/api/user/details')
    api.add_resource(DetailsApi, '/api/details/<user_id>')
    api.add_resource(PagesApi, '/api/page')
    api.add_resource(SinglePageApi, '/api/page/<page_id>')