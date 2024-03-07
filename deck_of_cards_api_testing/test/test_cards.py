import unittest
from infra.api_wrapper import APIWrapper
from logic.cards_endpoints import CardsLogic
from logic.deck_endpoints import DeckLogic


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        deck_endpoint = DeckLogic(self.my_api)
        deck_data = deck_endpoint.brand_new_deck()
        self.deck_id = deck_data['deck_id']
        self.cards_logic = CardsLogic(self.my_api)

    def test_shuffle_the_cards(self, dec_count=1):
        data = self.cards_logic.shuffle_the_cards(dec_count)
        assert data['success'] is True
        assert 'deck_id' in data
        assert data['shuffled'] is True
        assert data['remaining'] == 52

    def test_draw_cards(self):
        number_of_cards_to_dry = 2
        data = self.cards_logic.draw_cards("new", number_of_cards_to_dry)
        assert data['success'] is True
        assert data['remaining'] == 52 - number_of_cards_to_dry
        assert len(data['cards']) == number_of_cards_to_dry

    def test_reshuffle_cards(self):
        data = self.cards_logic.reshuffle_cards(self.deck_id)
        assert data['success'] is True
        assert data['remaining'] == 52
