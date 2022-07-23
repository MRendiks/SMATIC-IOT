import jwt
import os

from ..models.user_model import User
from ..schemas.user_schema import RegisterBody, RegisterSuccess, UserLoginBody, UserLoginSuccess, \
    UserLoginErrorResponse
from django.contrib.auth.hashers import check_password
from ninja.errors import ValidationError
from django.utils import timezone


class UserService:

    def register_logistic_owner(self, data: RegisterBody):
        self.__validate_register_request_body(data.email, data.phone)

        user = User.objects.create_logistic_owner(
            name=data.name,
            email=data.email,
            password=data.password,
            phone=data.phone,
            address=data.address
        )

        user.save()

        return 200, RegisterSuccess()

    def login(self, data: UserLoginBody):
        user = self.__authenticate(data.email, data.password)

        if user is not None:
            access_token_payload = {
                "exp": timezone.now() + timezone.timedelta(minutes=120),
                "iat": timezone.now(),
                "data": {
                    "user_id": str(user.id),
                    "email": user.email
                }
            }

            access_token = jwt.encode(access_token_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256")

            refresh_token_payload = {
                "exp": timezone.now() + timezone.timedelta(days=7),
                "iat": timezone.now(),
                "data": {
                    "user_id": str(user.id),
                    "email": user.email
                }
            }

            refresh_token = jwt.encode(refresh_token_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256")

            user.last_login = timezone.now()
            user.save()

            return 200, UserLoginSuccess(code=200, message="Login success.", payload={
                "access_token": access_token,
                "refresh_token": refresh_token
            })
        else:
            return 401, UserLoginErrorResponse(code=401, message="Incorrect email or password.")

    @staticmethod
    def refresh_token(token: str):
        try:
            refresh_token_payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=['HS256'], options={
                'verify_signature': False,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            })
            if refresh_token_payload["exp"] < timezone.now().timestamp():
                return 401, UserLoginErrorResponse(code=401, message="Token Expired.")

            user = User.objects.get(id=refresh_token_payload["data"]["user_id"])

            access_token_payload = {
                "exp": timezone.now() + timezone.timedelta(minutes=120),
                "iat": timezone.now(),
                "data": {
                    "user_id": refresh_token_payload["data"]["user_id"],
                    "email": refresh_token_payload["data"]["email"]
                }
            }

            access_token = jwt.encode(access_token_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256")

            refresh_token_payload = {
                "exp": timezone.now() + timezone.timedelta(days=7),
                "iat": timezone.now(),
                "data": {
                    "user_id": refresh_token_payload["data"]["user_id"],
                    "email": refresh_token_payload["data"]["email"]
                }
            }

            refresh_token = jwt.encode(refresh_token_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256")

            user.last_login = timezone.now()
            user.save()

            return 200, UserLoginSuccess(code=200, message="Login success.", payload={
                "access_token": access_token,
                "refresh_token": refresh_token
            })
        except jwt.exceptions.PyJWTError as e:
            print(e)
            return 401, UserLoginErrorResponse(code=401, message="Invalid Token")
        except User.DoesNotExist:
            return 401, UserLoginErrorResponse(code=401, message="Invalid User")

    @staticmethod
    def __authenticate(email, password):
        try:
            login_valid = User.objects.get(email=email)
            pwd_valid = check_password(password, login_valid.password)

            if login_valid and pwd_valid:
                return login_valid

            return None
        except User.DoesNotExist:
            return None

    def __validate_register_request_body(self, email, phone):
        is_email_duplicate = self.__validate_duplicate_email(email)
        is_phone_duplicate = self.__validate_duplicate_phone(phone)

        if is_email_duplicate | is_phone_duplicate:
            duplicate_errors = []
            duplicate_errors.append(
                {
                    'loc': ['body', 'data', 'email'],
                    'msg': 'Email already exists.',
                    'type': 'value_error'
                }) if is_email_duplicate else None
            duplicate_errors.append(
                {
                    'loc': ['body', 'data', 'phone'],
                    'msg': 'Phone number already exists.',
                    'type': 'value_error'
                }) if is_phone_duplicate else None

            raise ValidationError(duplicate_errors)

    @staticmethod
    def __validate_duplicate_email(email):
        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                return False
            else:
                return True
        except User.DoesNotExist:
            return False

    @staticmethod
    def __validate_duplicate_phone(phone):
        try:
            user = User.objects.get(phone=phone)
            if not user.is_active:
                return False
            else:
                return True
        except User.DoesNotExist:
            return False
