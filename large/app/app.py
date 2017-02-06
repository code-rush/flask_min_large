from flask import Flask

app = Flask('large')
app.secret_key = 'DEV_SECRET_KEY'