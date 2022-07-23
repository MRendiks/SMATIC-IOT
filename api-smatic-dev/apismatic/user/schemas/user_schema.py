from ninja import Schema


class RegisterBody(Schema):
    name: str
    email: str
    password: str
    phone: str
    address: str

    class Config:
        schema_extra = {
            'example': {
                'name': 'Jhonatan Doe',
                'email': 'jhonatan.doe@gmail.com',
                'password': 'Password1234!',
                'phone': '089123848847',
                'address': 'Gg. Anggur No 14b, Krodan, Maguwoharjo, Depok, Sleman, Daerah Istimewa Yogyakarta 55281',
            }
        }


class RegisterSuccess(Schema):
    code: int = 200
    message: str = 'User successfully registered.'

    class Config:
        schema_extra = {
            'example': {
                'code': 200,
                'message': 'User successfully registered.',
            }
        }


class UserLoginBody(Schema):
    email: str
    password: str

    class Config:
        schema_extra = {
            'title': 'Login',
            'example': {
                'email': 'admin@smatic.com',
                'password': 'Password1234!',
            }
        }


class UserLoginErrorResponse(Schema):
    code: int
    message: str

    class Config:
        schema_extra = {
            'title': 'Login Error',
            'example': {
                'code': 401,
                'message': 'Email or password is incorrect.'
            }
        }


class UserLoginSuccess(Schema):
    code: int
    message: str
    payload: dict

    class Config:
        schema_extra = {
            'title': 'Login Success',
            'example': {
                'code': 200,
                'message': 'Login successful',
                'payload': {
                    'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                             '.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'
                             '.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
                    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                             '.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'
                             '.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
                }
            }
        }
