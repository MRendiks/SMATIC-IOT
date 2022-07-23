from ninja import Schema


class GetAllLogistic(Schema):
    code: int = 200
    message: str = "ok"
    payload: dict

    class Config:
        schema_extra = {
            'example': {
                'code': 200,
                'message': 'ok',
                'payload': {
                    'racks': [
                        {
                            'id': 1,
                            'name': 'John',
                            'logistics': [
                                {
                                    'id': 'g24g2-24g2gh',
                                    'owner__name': 'Jhon'
                                }
                            ]
                        }
                    ]
                }
            }
        }