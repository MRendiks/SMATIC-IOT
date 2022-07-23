from ninja import Router

from ..schemas import GetAllLogistic
from ..services import LogisticService
from apismatic.auth.auth_bearer import AuthBearer


router = Router(tags=["Logistic"], auth=AuthBearer())


@router.get('/', response={200: GetAllLogistic})
def get_all_logistic(request):
    return LogisticService().get_all_logistic()
