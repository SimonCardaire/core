"""Allows to configure a switch using RPi GPIO."""

from homeassistant.components import rpi_gpio
from homeassistant.components.rpi_gpio.const import (
    CONF_SWITCH,
    CONF_SWITCH_INVERT_LOGIC,
    CONF_SWITCH_PORTS,
    DOMAIN,
    PLATFORMS,
)
from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.helpers.entity import ToggleEntity
from homeassistant.helpers.reload import setup_reload_service


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Raspberry PI GPIO devices."""

    setup_reload_service(hass, DOMAIN, PLATFORMS)
    config_switch = hass.data[DOMAIN][CONF_SWITCH]
    invert_logic = config_switch[CONF_SWITCH_INVERT_LOGIC]

    switches = []
    ports = config_switch[CONF_SWITCH_PORTS]
    for port, name in ports.items():
        switches.append(RPiGPIOSwitch(name, port, invert_logic))
    add_entities(switches)


class RPiGPIOSwitch(ToggleEntity):
    """Representation of a  Raspberry Pi GPIO."""

    def __init__(self, name, port, invert_logic):
        """Initialize the pin."""
        self._name = name or DEVICE_DEFAULT_NAME
        self._port = port
        self._invert_logic = invert_logic
        self._state = False
        rpi_gpio.setup_output(self._port)
        rpi_gpio.write_output(self._port, 1 if self._invert_logic else 0)

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Turn the device on."""
        rpi_gpio.write_output(self._port, 0 if self._invert_logic else 1)
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn the device off."""
        rpi_gpio.write_output(self._port, 1 if self._invert_logic else 0)
        self._state = False
        self.schedule_update_ha_state()
