# coding: utf-8

from flask import Flask
from apis import bot
from apis import provider

app = Flask(__name__)

app.register_blueprint(bot.app)
app.register_blueprint(provider.app)

# Set the secret key to some random bytes. Keep this really secret!
# using session in provider
# notice: This is experimental implement. Don't share session between apis.provider and apis.bot.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hello():
    return "Hello root!"

if __name__ == "__main__":
    app.run()
