from flask import Flask, request
from threading import Timer
import socket
import time
import os

app = Flask(__name__)

BOT_NICK = os.getenv("mibotpizza")
CHANNEL = os.getenv("mery_soldier")
TOKEN = os.getenv("048ttawrrqpc20b5rqxlxtq7nh7zu6")

def send_message(msg):
    server = 'irc.chat.twitch.tv'
    port = 6667
    with socket.socket() as s:
        s.connect((server, port))
        s.send(f"PASS {TOKEN}\n".encode('utf-8'))
        s.send(f"NICK {BOT_NICK}\n".encode('utf-8'))
        s.send(f"JOIN #{CHANNEL}\n".encode('utf-8'))
        time.sleep(1)
        s.send(f"PRIVMSG #{CHANNEL} :{msg}\n".encode('utf-8'))

@app.route('/timer', methods=['GET'])
def start_timer():
    try:
        minutes = int(request.args.get('text'))
        send_message(f"Se ha iniciado un temporizador de {minutes} minutos")
        Timer(minutes * 60, send_message, args=[f"Temporizador de {minutes} minutos finalizado"]).start()
        return f"Temporizador iniciado por {minutes} minutos"
    except:
        return "Error: uso correcto !pizza 15"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
