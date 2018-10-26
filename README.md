# line-messaging-api-sampler

## heroku api endpoint
https://line-messaging-api-sampler.herokuapp.com/

### line bot
![](images/qr.png)

## develop (local server)

```
direnv allow
```

### run flask

```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
```

### run ngrok

```
ngrok http 5000
```
