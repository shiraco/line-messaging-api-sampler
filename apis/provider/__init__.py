# coding: utf-8

from flask import session, redirect, url_for, escape, request, Blueprint, current_app

app = Blueprint('provider', __name__, url_prefix='/provider')
# app = Flask(__name__)

LINE_CALLBACK_URL = 'https://access.line.me/dialog/bot/accountLink'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session.get('username'))
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/link_account', methods=['GET', 'POST'])
def link():

    current_app.logger.debug("request.form: {}".format(request.form))

    if request.method == 'POST':
        if 'user_id' not in session:
            # TODO handle case user not found
            user_name = request.form.get('user_name')
            user_id = users[user_name]
            session['user_id'] = user_id

        user_id = session['user_id']
        line_link_token = session['line_link_token']
        session['line_link_token'] = None

        url = get_line_callback_url(line_link_token, user_id)
        return redirect(url)

    elif request.method == 'GET':
        line_link_token = request.args.get('linkToken')
        session['line_link_token'] = line_link_token

    return '''
        <form method="post">
            <p><input type=text name=user_name>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/unlink_account', methods=['GET', 'POST'])
def unlink():
    pass

def get_line_callback_url(line_link_token, user_id):

    secure_token = user_id  # TODO secure and random(onetime)
    nonce = base64_encode(secure_token)

    # TODO save nonce with user_id

    current_app.logger.debug("nonce: {}".format(nonce))

    assert 10 <= len(nonce) <= 255

    url = LINE_CALLBACK_URL + '?linkToken=' + line_link_token + '&nonce=' + nonce
    return url

def base64_encode(string):
    """
    Removes any `=` used as padding from the encoded string.
    """
    import base64

    encoded = base64.urlsafe_b64encode(string.encode('utf-8')).decode('utf-8')
    return encoded.rstrip("=")

users = {'Taro': 'id-00001', 'Jiro': 'id-00002', 'Saburo': 'id-00003'}
