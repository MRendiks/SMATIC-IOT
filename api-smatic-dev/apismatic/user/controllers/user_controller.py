from ninja import Router, Body
from ..schemas.user_schema import RegisterSuccess, RegisterBody, UserLoginSuccess, UserLoginErrorResponse, UserLoginBody
from ..services.user_service import UserService


router = Router(tags=["Auth"])


@router.post(
    '/logistic-owner/register',
    response={200: RegisterSuccess})
def register_logistic_owner(request, data: RegisterBody = Body(...)):
    return UserService().register_logistic_owner(data)


@router.post('/login', response={200: UserLoginSuccess, 401: UserLoginErrorResponse})
def login(request, data: UserLoginBody = Body(...)):
    return UserService().login(data)


@router.get('/refresh', response={200: UserLoginSuccess, 401: UserLoginErrorResponse})
def refresh_token(request, token: str):
    return UserService.refresh_token(token)
