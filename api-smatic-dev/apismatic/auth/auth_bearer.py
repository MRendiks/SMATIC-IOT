from ninja.security import HttpBearer
import jwt
import os
from django.utils import timezone
from apismatic.user.models.user_model import User


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):

        try:
            jwt_options = {
                'verify_signature': False,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            }
            jwt_payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=['HS256'], options=jwt_options)

            if jwt_payload["exp"] < timezone.now().timestamp():
                return False

            try:
                User.objects.get(id=jwt_payload["data"]["user_id"])
                return True
            except User.DoesNotExist:
                return False
        except jwt.exceptions.InvalidAudienceError as e:
            return False
        except jwt.exceptions.InvalidAlgorithmError as e:
            return False
        except jwt.exceptions.DecodeError as e:
            return False
        except jwt.exceptions.InvalidTokenError as e:
            return False
