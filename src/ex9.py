def print_cards(crds, current_card, player='-'):
    output = f"[{player}] 0"
    card = crds[0]
    while card != 0:
        if card == current_card:
            output += f" ({card})"
        else:
            output += f" {card}"
        card = crds[card]
    print(output)


def play_game(_n_players, _max_card, pt):
    cards = {0: 0}
    cards_inverse = {0: 0}

    score = {p: 0 for p in range(1, _n_players + 1)}
    current_card = 0

    for i in range(1, _max_card + 1):
        player = ((i-1) % _n_players) + 1
        if i % 23 == 0:
            score[player] += i
            remove = cards_inverse[current_card]
            for _ in range(6):
                remove = cards_inverse[remove]
            score[player] += remove
            cards[cards_inverse[remove]] = cards[remove]
            cards_inverse[cards[remove]] = cards_inverse[remove]
            current_card = cards[remove]
        else:
            nxt = cards[current_card]
            next_next = cards[nxt]
            cards[nxt] = i
            cards_inverse[i] = nxt
            cards[i] = next_next
            cards_inverse[next_next] = i
            current_card = i
        # print_cards(cards, current_card, str(player))
    print(f"ans pt {pt} = {max(score.values())}")


if __name__ == '__main__':
    n_players = 412
    max_card = 71646

    play_game(n_players, max_card, 1)
    play_game(n_players, max_card*100, 2)