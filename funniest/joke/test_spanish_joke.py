import os
import configcatclient
from ..joke import SpanishJoke


def test_joke():
    if "CONFIGCAT_TEST_TOKEN" in os.environ:
        configcat_token = os.environ["CONFIGCAT_TEST_TOKEN"]
    else:
        configcat_token = "NgLYCNlqy0GD2zYrTE_p_w/GNzk7N3Sa0KzKJrhdqfUQw"

    configcat_client = configcatclient.create_client(configcat_token)

    new_joke_flag = configcat_client.get_value('newjoke', False)

    if new_joke_flag:
        assert "¿Por qué las focas del circo miran...?" == SpanishJoke().joke()
    else:
        assert "¿En que se parecen...?" == SpanishJoke().joke()
