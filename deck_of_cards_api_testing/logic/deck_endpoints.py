
class DeckLogic:
    def __init__(self, api_object):
        self.my_api = api_object

    def brand_new_deck(self):
        endpoint = f"api/deck/new/"
        response = self.my_api.api_get_request(endpoint)
        return response.json()

    def partial_deck(self, cards_list):
        endpoint = f"api/deck/new/shuffle/"
        output_string = ",".join(cards_list)
        cards_endpoint = f"?cards={output_string}"
        response = self.my_api.api_get_request(endpoint + cards_endpoint)
        return response.json()

    def return_cards_to_deck(self, deck_id):
        endpoint = f"api/deck/{deck_id}/return/"
        response = self.my_api.api_get_request(endpoint)
        return response.json()









