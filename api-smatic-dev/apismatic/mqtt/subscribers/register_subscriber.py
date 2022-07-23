from ..models import DeviceModel
import logging

logger = logging.getLogger(__name__)


def register_subscriber(payload: str):
    mac_address, vendor, device_name = payload.split(",")
    try:
        DeviceModel.objects.get(mac_address=mac_address)
        logger.warning("device: {}, mac_address: {}, vendor: {} already exists".format(device_name, mac_address, vendor))

    except DeviceModel.DoesNotExist:
        DeviceModel.objects.create(
            mac_address=mac_address,
            vendor=vendor,
            name=device_name
        )
        logger.info("device: {}, mac_address: {}, vendor: {} registered".format(device_name, mac_address, vendor))
