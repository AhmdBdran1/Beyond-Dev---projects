import unittest
from infra.mobile_wrapper import MobileWrapper
from logic.create_new_event_page import CreateNewEventPage
from logic.events_page import EventsPage
from logic.home_page import HomePage


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        mobile_wrapper = MobileWrapper()
        self.driver = mobile_wrapper.get_driver()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_add_new_event(self):
        home_page = HomePage(self.driver)
        home_page.start_new_event_for_today()
        create_new_event_page = CreateNewEventPage(self.driver)
        create_new_event_page.add_new_event()
        events_page = EventsPage(self.driver)
        result = events_page.check_exist_of_added_task()
        self.assertEqual(result, "test")

    def test_delete_an_event(self):
        home_page = HomePage(self.driver)
        home_page.start_new_event_for_today()
        create_new_event_page = CreateNewEventPage(self.driver)
        create_new_event_page.add_new_event()
        events_page = EventsPage(self.driver)
        self.assertTrue(events_page.delete_an_task())

    def test_edit_an_event(self):
        home_page = HomePage(self.driver)
        home_page.start_new_event_for_today()
        create_new_event_page = CreateNewEventPage(self.driver)
        create_new_event_page.add_new_event()
        events_page = EventsPage(self.driver)
        new_event_name = events_page.edit_name_of_an_event()
        self.assertEqual(new_event_name, "test changed")


if __name__ == "__main__":
    unittest.main()
