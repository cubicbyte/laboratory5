from random import randint, shuffle

class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
    
    def toString(self):
        return self.name + ' ' + self.suit

class DeckOfCards:
    __cards = []
    template = {
        'suits': [
            'Піка',
            'Хреста',
            'Бубна',
            'Чірва'
        ],
        'names': [
            '6', '7', '8', '9', '10',
            'Валет',
            'Дама',
            'Король',
            'Туз'
        ]
    }

    def __init__(self):
        suits = self.template['suits']
        names = self.template['names']
        for i in range(len(suits)):
            for j in range(len(names)):
                card = Card(suits[i], names[j])
                self.__cards.append(card)
        self.shuffle()

    def shuffle(self):
        shuffle(self.__cards)
    
    def print(self):
        for i in range(len(self.__cards)):
            print(self.__cards[i].toString())
    
    def getCard(self, position):
        if position < 1 or position > len(self.__cards):
            print('Ошибка: неверная позиция карты')
            return None
        return self.__cards[position - 1]
    
    def getRandomCard(self):
        return self.__cards[randint(0, len(self.__cards))]

    def get6RandomCards(self):
        cards = []
        for i in range(6):
            cards.append(self.getRandomCard())
        return cards

def main():
    deck = DeckOfCards()

    print('Колода карт:')
    deck.print()

    print('\n\nЩе раз перемішана колода карт:')
    deck.shuffle()
    deck.print()

    print('\n\nКарта під номером #18:', deck.getCard(18).toString())
    print('\n\nВипадкова карта:', deck.getRandomCard().toString())
    print('\n\n6 випадкових карт:')

    for card in deck.get6RandomCards():
        print(card.toString())

if __name__ == '__main__':
    main()