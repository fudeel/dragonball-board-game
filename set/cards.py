from models.card import Card

card_1 = Card(
    id=1,
    name="Piccolo's training",
    tar="me",
    desc="Increase attack power by 1",
    eff_code=0000
)

cards = [card_1]


def generate_cards():
    cards = []
    for i in range(200):
        cards.append(card_1)

    return cards
