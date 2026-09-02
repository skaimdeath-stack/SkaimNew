import random

def calculate_score(cards):
    """Подсчитывает сумму карт, учитывая туз как 1 или 11."""
    total = sum(cards)
    ace_count = cards.count(11)
    while total > 21 and ace_count:
        total -= 10  # Туз считается как 1 вместо 11
        ace_count -= 1
    return total

def deal_card():
    """Возвращает случайную карту."""
    card = random.randint(2, 11)
    # 11 будет означать туз
    if card == 11:
        # В начале туз считается как 11
        return 11
    else:
        return card

def print_cards(player_cards, dealer_cards, reveal_dealer=False):
    """Выводит карты игрока и дилера."""
    print(f"Ваши карты: {player_cards} - сумма: {calculate_score(player_cards)}")
    if reveal_dealer:
        print(f"Карты дилера: {dealer_cards} - сумма: {calculate_score(dealer_cards)}")
    else:
        print(f"Карты дилера: [{dealer_cards[0]}, ?]")

def blackjack():
    print("Добро пожаловать в игру Блэкджек!")
    
    # Начинаем игру
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        print_cards(player_cards, dealer_cards)
        player_score = calculate_score(player_cards)

        # Проверка блэкджека
        if player_score == 21:
            print("У вас блэкджек! Вы победили!")
            game_over = True
            continue

        choice = input("Хотите взять еще карту? (да/нет): ").lower()
        if choice == "да":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            if player_score > 21:
                print_cards(player_cards, dealer_cards, reveal_dealer=True)
                print("Перебор! Вы проиграли.")
                game_over = True
        else:
            # Игрок останавливается, дилер играет
            while calculate_score(dealer_cards) < 17:
                dealer_cards.append(deal_card())
            print_cards(player_cards, dealer_cards, reveal_dealer=True)
            dealer_score = calculate_score(dealer_cards)

            if dealer_score > 21:
                print("Дилер перебрал! Вы победили!")
            elif dealer_score > player_score:
                print("Дилер выиграл!")
            elif dealer_score < player_score:
                print("Вы выиграли!")
            else:
                print("Ничья!")
            game_over = True

if __name__ == "__main__":
    blackjack()
input("Нажмите Enter, чтобы выйти...")
# После блока, где выводится результат сравнения
if dealer_score > 21:
    print("Дилер перебрал! Вы победили!")
    print("Дилер: Чёрт! Перебрал! Ну и ну!")
elif dealer_score > player_score:
    print("Дилер выиграл!")
    print("Дилер: Ух-ха! Я победил! Мои навыки на высоте!")
elif dealer_score < player_score:
    print("Вы выиграли!")
elif dealer_score == player_score:
    print("Ничья!")