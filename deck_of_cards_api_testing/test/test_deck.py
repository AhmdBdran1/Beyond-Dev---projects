import unittest
from infra.api_wrapper import APIWrapper
from logic.cards_endpoints import CardsLogic
from logic.deck_endpoints import DeckLogic
from logic.piles_endpoints import PilesLogic


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.deck_endpoints = DeckLogic(self.my_api)

    def test_new_deck(self):
        data = self.deck_endpoints.brand_new_deck()
        self.assertTrue(data['success'])
        # Test deck_id key
        self.assertIsNotNone(data['deck_id'])
        self.assertFalse(data['shuffled'])
        self.assertEqual(data['remaining'], 52)

    def test_partial_deck(self):
        expected_remaining = 12
        cards_list = ['AS', '2S', 'KS', 'AD', '2D', 'KD', 'AC', '2C', 'KC', 'AH', '2H', 'KH']
        data = self.deck_endpoints.partial_deck(cards_list)
        assert data['success'] is True
        assert 'deck_id' in data
        assert data['shuffled'] is True
        assert data['remaining'] == expected_remaining

    def test_return_cards_to_the_deck(self):
        data = self.deck_endpoints.brand_new_deck()
        deck_id = data['deck_id']
        cars_endpoints = CardsLogic(self.my_api)
        cars_endpoints.draw_cards(deck_id)
        cards_list = ['AS']
        piles_name = 'newPiles'
        piles_endpoints = PilesLogic(self.my_api)
        piles_endpoints.adding_to_piles(deck_id, piles_name, cards_list)
        data = piles_endpoints.drawing_from_piles(deck_id, piles_name, cards_list)
        assert data['success'] is True
