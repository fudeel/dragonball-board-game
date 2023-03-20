from models.card import Card

card_1 = Card(
    id=1,
    tar='me',
    desc='Increase attack power by 2',
    eff_code=0000
)


def generate_cards():
    cards = []
    for i in range(200):
        cards.append(card_1)

    return cards