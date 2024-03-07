import unittest
from asyncio import sleep

from infra.api_wrapper import APIWrapper
from logic.cards_endpoints import CardsLogic
from logic.deck_endpoints import DeckLogic
from logic.piles_endpoints import PilesLogic


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.piles_endpoints = PilesLogic(self.my_api)
        deck_endpoint = DeckLogic(self.my_api)
        deck_data = deck_endpoint.brand_new_deck()
        self.deck_id = deck_data['deck_id']

    def test_add_to_piles(self):
        cards_list = ['AS', '2S']
        piles_name = 'newPiles'
        data = self.piles_endpoints.adding_to_piles(self.deck_id, piles_name, cards_list)
        discard_pile = data['piles'].get('newPiles')
        # Test success key
        self.assertTrue(data['success'])
        # Test deck_id key
        self.assertIsNotNone(data['deck_id'])
        # Test remaining key
        self.assertEqual(data['remaining'], 52)
        # Test piles key
        self.assertIn('piles', data)
        # Test discard pile
        self.assertEqual(discard_pile['remaining'], 0)

    def test_shuffle_piles(self):
        cards_list = ['AS', '2S']
        piles_name = 'newPiles'
        data = self.piles_endpoints.adding_to_piles(self.deck_id, piles_name, cards_list)
        deck_id = data['deck_id']
        data = self.piles_endpoints.shuffle_piles(deck_id, piles_name)
        discard_pile = data['piles'].get('newPiles')
        # Test success key
        self.assertTrue(data['success'])
        # Test deck_id key
        self.assertIsNotNone(data['deck_id'])
        # Test remaining key
        self.assertEqual(data['remaining'], 52)
        # Test piles key
        self.assertIn('piles', data)
        # Test discard pile
        self.assertEqual(discard_pile['remaining'], 0)

    def test_list_cards_in_piles(self):
        cards_list = ['AS', '2S']
        piles_name = 'newPiles'
        data = self.piles_endpoints.adding_to_piles(self.deck_id, piles_name, cards_list)
        deck_id = data['deck_id']
        data = self.piles_endpoints.listing_cards_in_piles(deck_id, piles_name)        # Check if the 'success' key exists and its value is True
        self.assertTrue(data.get('success', False))
        # Check if the 'deck_id' key exists
        self.assertTrue('deck_id' in data)
        # Check if the 'remaining' key exists and its value is a string
        self.assertTrue('remaining' in data)

    def test_drawing_from_piles(self):
        cars_endpoints = CardsLogic(self.my_api)
        cars_endpoints.draw_cards(self.deck_id)
        cards_list = ['AS']
        piles_name = 'newPiles'
        self.piles_endpoints.adding_to_piles(self.deck_id, piles_name, cards_list)
        data = self.piles_endpoints.drawing_from_piles(self.deck_id, piles_name, cards_list)
        self.assertTrue(data.get('success', False))
        # Check if the 'deck_id' key exists
        self.assertTrue('deck_id' in data)






