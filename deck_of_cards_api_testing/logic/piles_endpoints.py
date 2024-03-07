class PilesLogic:
    def __init__(self, api_object):
        self.my_api = api_object

    def adding_to_piles(self, deck_id, pile_name, cards_list):
        output_string = ",".join(cards_list)
        cards_endpoint = f"?cards={output_string}"
        endpoint = f"api/deck/{deck_id}/pile/{pile_name}/add/"
        response = self.my_api.api_get_request(endpoint + cards_endpoint)
        return response.json()

    def shuffle_piles(self, deck_id, pile_name):
        endpoint = f"api/deck/{deck_id}/pile/{pile_name}/shuffle/"
        response = self.my_api.api_get_request(endpoint)
        return response.json()

    def listing_cards_in_piles(self, deck_id, pile_name):
        endpoint = f"api/deck/{deck_id}/pile/{pile_name}/list/"
        response = self.my_api.api_get_request(endpoint)
        return response.json()

    def drawing_from_piles(self, deck_id, pile_name, cards):
        endpoint = f"api/deck/{deck_id}/pile/{pile_name}/draw/?count=1"
        response = self.my_api.api_get_request(endpoint)
        return response.json()















