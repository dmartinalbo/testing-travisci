import configcatclient
import os


class SpanishJoke:
    def __init__(self):

        if "CONFIGCAT_TEST_TOKEN" in os.environ:
            configcat_token = os.environ["CONFIGCAT_TEST_TOKEN"]
        else:
            configcat_token = "NgLYCNlqy0GD2zYrTE_p_w/GNzk7N3Sa0KzKJrhdqfUQw"

        self.configcat_client = configcatclient.create_client(configcat_token)

    def joke(self):
        new_joke_flag = self.configcat_client.get_value('newjoke', False)
        if new_joke_flag:
            return self.new_joke()
        else:
            return self.old_joke()

    def old_joke(self):
        return "¿En que se parecen...?"

    def new_joke(self):
        return "¿Por qué las focas del circo miran...?"
