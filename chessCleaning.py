import chess.pgn
from datetime import datetime
from pymongo import MongoClient
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

# Set Up MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
db = client['chess']
# Set Up Twilio SMS Notification Client
account_sid = os.getenv("twilioSID")
auth_token = os.getenv("twiliotoken")
twilioClient = Client(account_sid, auth_token)

def main():
    pgn = open('files/lichess_db_standard_rated_2016-01.pgn', encoding="utf-8-sig")
    matches = db.matches


    game = chess.pgn.read_game(pgn)
    moves = 0
    counter = 0
    for i in pgn:
        game = chess.pgn.read_game(pgn)

        matches.insert_one({'white': game.headers['White'], 'whiteELO': game.headers['WhiteElo'],
                            'result': game.headers['Result'], 'black': game.headers['Black'],
                            'blackELO': game.headers['BlackElo'],
                            'eco': game.headers['ECO'],
                            'opening': game.headers['Opening'],
                            'time': game.headers['TimeControl'],
                            'termination': game.headers['Termination'],
                            'played': game.headers['UTCDate']
                            }).inserted_id
        print(counter)
        counter += 1



if __name__ == '__main__':
    init_time = datetime.now()
    main()
    fin_time = datetime.now()
    message = twilioClient.messages.create(
        to = os.getenv("myphone"),
        from_ = os.getenv("twilioPhone"),
        body = f"I finished importing all the data 2016 in {(fin_time - init_time)}")

    message.sid
    print("Execution time: ", (fin_time - init_time))
