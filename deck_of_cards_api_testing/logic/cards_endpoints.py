from infra.api_wrapper import APIWrapper


class CardsLogic:
    def __init__(self, api_object):
        self.my_api = api_object

    def shuffle_the_cards(self, deck_count):
        endpoint = f"api/deck/new/shuffle/?{deck_count}"
        response = self.my_api.api_get_request(endpoint)
        return response.json()

    def draw_cards(self, deck_id, count=1):
        endpoint = f"api/deck/{deck_id}/draw/"
        count_endpoint = f"?count={count}"
        response = self.my_api.api_get_request(endpoint + count_endpoint)
        return response.json()

    def reshuffle_cards(self, deck_id):
        endpoint = f"api/deck/{deck_id}/shuffle/"
        response = self.my_api.api_get_request(endpoint)
        return response.json()










