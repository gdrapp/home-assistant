"""Make sure that Vocolinc Flowerbud is enumerated properly."""

from homeassistant.components.humidifier.const import SUPPORT_MODES
from homeassistant.components.light import SUPPORT_BRIGHTNESS, SUPPORT_COLOR

from tests.components.homekit_controller.common import (
    DeviceTestInfo,
    EntityTestInfo,
    assert_devices_and_entities_created,
    setup_accessories_from_file,
    setup_test_accessories,
)


async def test_vocolinc_flowerbud_setup(hass):
    """Test that a Vocolinc Flowerbud can be correctly setup in HA."""
    accessories = await setup_accessories_from_file(hass, "vocolinc_flowerbud.json")
    await setup_test_accessories(hass, accessories)

    assert_devices_and_entities_created(
        hass,
        DeviceTestInfo(
            unique_id="00:00:00:00:00:00",
            name="VOCOlinc-Flowerbud-0d324b",
            model="Flowerbud",
            manufacturer="VOCOlinc",
            sw_version="3.121.2",
            hw_version="0.1",
            serial_number="AM01121849000327",
            devices=[],
            entities=[
                EntityTestInfo(
                    entity_id="humidifier.vocolinc_flowerbud_0d324b",
                    friendly_name="VOCOlinc-Flowerbud-0d324b",
                    unique_id="homekit-AM01121849000327-30",
                    supported_features=SUPPORT_MODES,
                    state="off",
                ),
                EntityTestInfo(
                    entity_id="light.vocolinc_flowerbud_0d324b",
                    friendly_name="VOCOlinc-Flowerbud-0d324b",
                    unique_id="homekit-AM01121849000327-9",
                    supported_features=SUPPORT_BRIGHTNESS | SUPPORT_COLOR,
                    state="on",
                ),
                EntityTestInfo(
                    entity_id="number.vocolinc_flowerbud_0d324b_spray_quantity",
                    friendly_name="VOCOlinc-Flowerbud-0d324b Spray Quantity",
                    unique_id="homekit-AM01121849000327-aid:1-sid:30-cid:38",
                    state="5",
                ),
                EntityTestInfo(
                    entity_id="sensor.vocolinc_flowerbud_0d324b_current_humidity",
                    friendly_name="VOCOlinc-Flowerbud-0d324b - Current Humidity",
                    unique_id="homekit-AM01121849000327-aid:1-sid:30-cid:33",
                    state="45.0",
                ),
            ],
        ),
    )
