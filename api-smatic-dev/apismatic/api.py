from ninja import NinjaAPI
from ninja.errors import ValidationError
from apismatic.user.controllers.user_controller import router as user_router
from apismatic.logistic.controllers.logistic_controller import router as logistic_router

api = NinjaAPI(
    title="Smatic Backend API",
    version="1.0",
    description="A documentation for Smatic API",
)


api.add_router('/auth', user_router)
api.add_router('/logistic', logistic_router)


@api.exception_handler(ValidationError)
def handle_validation_error(request, exception):
    for error in exception.errors:
        error['field'] = error['loc'][-1]
        error['message'] = error['msg']
        del error['loc']
        del error['msg']
        del error['type']
    return api.create_response(
        request,
        {'code': 400, 'message': 'One or more errors occurred.', 'payload': exception.errors},
        status=400)
