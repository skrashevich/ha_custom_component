"""Const file for the BMW Connected Drive integration."""
from homeassistant.const import (
    LENGTH_KILOMETERS,
    LENGTH_MILES,
    VOLUME_GALLONS,
    VOLUME_LITERS,
)

DOMAIN = "bmw_connected_drive"
ATTRIBUTION = "Data provided by BMW Connected Drive"

ATTR_DIRECTION = "direction"
ATTR_VIN = "vin"

CONF_ALLOWED_REGIONS = ["china", "north_america", "rest_of_world"]
CONF_READ_ONLY = "read_only"
CONF_ACCOUNT = "account"

DATA_HASS_CONFIG = "hass_config"

UNIT_MAP = {
    "KILOMETERS": LENGTH_KILOMETERS,
    "MILES": LENGTH_MILES,
    "LITERS": VOLUME_LITERS,
    "GALLONS": VOLUME_GALLONS,
}

SERVICE_MAP = {
    "light_flash": "trigger_remote_light_flash",
    "sound_horn": "trigger_remote_horn",
    "activate_air_conditioning": "trigger_remote_air_conditioning",
    "deactivate_air_conditioning": "trigger_remote_air_conditioning_stop",
    "find_vehicle": "trigger_remote_vehicle_finder",
}
