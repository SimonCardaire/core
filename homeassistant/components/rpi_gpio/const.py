"""Consts used by rpi_gpio."""
DOMAIN = "rpi_gpio"
PLATFORMS = ["binary_sensor", "cover", "switch", "light"]

# Light const
CONF_LIGHT = "light"
CONF_LIGHT_LIST = "lights"
CONF_LIGHT_RELAY_PIN = "relay_pin"
CONF_LIGHT_BUTTON_PIN = "light_button_pin"
CONF_LIGHT_BUTTON_PULL_MODE = "light_button_pull_mode"
CONF_LIGHT_INVERT_BUTTON = "invert_light_button"
CONF_LIGHT_INVERT_RELAY = "invert_relay"
CONF_LIGHT_BUTTON_BOUNCETIME_MILLIS = "light_button_bouncetime_millis"
CONF_LIGHT_BUTTON_DOUBLE_CHECK_TIME_MILLIS = "light_button_double_check_time_millis"

DEFAULT_LIGHT_BUTTON_PULL_MODE = "UP"
DEFAULT_LIGHT_INVERT_BUTTON = False
DEFAULT_LIGHT_INVERT_RELAY = False
DEFAULT_LIGHT_BUTTON_BOUNCETIME_MILLIS = 150
DEFAULT_LIGHT_DOUBLE_CHECK_TIME_MILLIS = 25

# Binary sensor const
CONF_SENSOR = "binary_sensor"
CONF_SENSOR_BOUNCETIME = "bouncetime"
CONF_SENSOR_INVERT_LOGIC = "invert_logic"
CONF_SENSOR_PORTS = "ports"
CONF_SENSOR_PULL_MODE = "pull_mode"

DEFAULT_SENSOR_BOUNCETIME = 50
DEFAULT_SENSOR_INVERT_LOGIC = False
DEFAULT_SENSOR_PULL_MODE = "UP"

# Cover const
CONF_COVER = "cover"
CONF_COVER_LIST = "covers"
CONF_COVER_RELAY_PIN = "relay_pin"
CONF_COVER_RELAY_TIME = "relay_time"
CONF_COVER_STATE_PIN = "state_pin"
CONF_COVER_STATE_PULL_MODE = "state_pull_mode"
CONF_COVER_INVERT_STATE = "invert_state"
CONF_COVER_INVERT_RELAY = "invert_relay"

DEFAULT_COVER_RELAY_TIME = 0.2
DEFAULT_COVER_STATE_PULL_MODE = "UP"
DEFAULT_COVER_INVERT_STATE = False
DEFAULT_COVER_INVERT_RELAY = False

# Switch const
CONF_SWITCH = "switch"
CONF_SWITCH_PORTS = "ports"
CONF_SWITCH_INVERT_LOGIC = "invert_logic"

DEFAULT_SWITCH_INVERT_LOGIC = False
