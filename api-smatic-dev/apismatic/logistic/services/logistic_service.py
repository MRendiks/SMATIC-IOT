from ..models import LogisticModel
from ..schemas import GetAllLogistic


class LogisticService:

    @staticmethod
    def get_all_logistic():
        list_rack = LogisticModel.objects.get_logistic_of_each_rack()

        return 200, GetAllLogistic(payload={
            'racks': list_rack
        })


