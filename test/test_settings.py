import unittest
import fail2slack
from fail2slack.settings import Settings


class TestSettings(unittest.TestCase):

    def setUp(self):
        pass

    def test_invalid_delivery_method(self):
        settings = {
            "delivery" : -1,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Delivery method should be 0 (Print) or 1 (Slack)")

    def test_invalid_jails(self):
        settings = {
            "delivery" : 0,
            "jails" : None,
            "webhook" : "https://webhook.url",
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "One or more Jails are required.")

    def test_invalid_webhook_print(self):
        settings = {
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : None,
        }

        test_settings = Settings()
        test_settings.validate_settings(settings)

        self.assertEqual(0, test_settings.get_delivery_method())

    def test_invalid_webhook_no_protocol(self):
        settings = {
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "webhook.url",
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Webhook value is not a value URL.")

    def test_invalid_webhook_missing_slack(self):
        settings = {
            "delivery" : 1,
            "jails" : ['test', 'also-test'],
            "webhook" : None,
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Webhook required for delivery setting 1 (Slack)")


if __name__ == '__main__':
    unittest.main()
