# Flask app to run the Blackjack game
from flask import Flask, render_template, request
import random

app = Flask(__name__, static_folder='static')

CARD_IMAGE_MAPPING = {
    2: '2.png',
    3: '3.png',
    4: '4.png',
    5: '5.png',
    6: '6.png',
    7: '7.png',
    8: '8.png',
    9: '9.png',
    10: '10.png',
    11: '11.png'
}


# Main route


@app.route("/", methods=["GET", "POST"])
def blackjack():
    # In-memory storage for the deck of cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
    rand_card1= random.choice(deck)
    rand_card2= random.choice(deck)
    rand_card3= random.choice(deck)
    rand_card4= random.choice(deck)

    # In-memory storage for the player and dealer hands
    player_hand = [rand_card1, rand_card2]
    dealer_hand = [rand_card3, rand_card4] 

    player_wins= None
    

    # Game logic to determine the winner
    if sum(player_hand) == 21:
        result = "Blackjack! You win!"
        player_wins = True
    elif sum(dealer_hand) == 21:
        result = "Dealer has Blackjack. You lose."
        player_wins = False
    elif request.method == "POST":
        action = request.form["action"]
        if action == "hit":
            player_hand.append(random.choice(deck))
            if sum(player_hand) > 21:
                result = "You busted with " + \
                    str(sum(player_hand)) + ". You lose."
                player_wins = False
        elif action == "stand":
            while sum(dealer_hand) < 17:
                dealer_hand.append(random.choice(deck))
            if sum(dealer_hand) > 21:
                result = "Dealer busted with " + \
                    str(sum(dealer_hand)) + ". You win!"
                player_wins = True
            elif sum(dealer_hand) < sum(player_hand):
                result = "You win with " + str(sum(player_hand)) + "!"
                player_wins = True
            elif sum(dealer_hand) > sum(player_hand):
                result = "You lose with " + str(sum(player_hand)) + "."
                player_wins = False
            else:
                result = "Push."
                player_wins = False
    else:
        result = ""



    return render_template("blackjack.html", CARD_IMAGE_MAPPING=CARD_IMAGE_MAPPING, player_hand=player_hand, dealer_hand=dealer_hand, result=result, player_wins=player_wins)


if __name__ == "__main__":
    app.run(debug=True)
