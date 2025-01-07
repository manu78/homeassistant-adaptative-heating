
"""Sensor platform for Adaptive Heating."""
from datetime import datetime
import logging

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from .const import DOMAIN, NAME, VERSION

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([AdaptiveHeatingSensor()])

class AdaptiveHeatingSensor(SensorEntity):
    """Representation of a Adaptive Heating Sensor."""

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_name = "Adaptive Heating Sensor"
        self._attr_unique_id = f"{DOMAIN}_main_sensor"
        self._attr_native_value = 0
        self._attr_device_class = SensorDeviceClass.POWER
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return self._attr_native_value