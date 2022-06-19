from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for,request, jsonify
import pandas as pd
import numpy as np
from pycaret.classification import *

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


app = Flask(__name__)    
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)

oauth.register(
        "auth0",
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
    )

############################################################################### Auth #############
    # Controllers API
@app.route("/")
def home():
        return render_template(
            "home.html",
            session=session.get("user"), indent=4)
        
    ##pretty=json.dumps(session.get("user")

@app.route("/callback", methods=["GET", "POST"])
def callback():
        token = oauth.auth0.authorize_access_token()
        session["user"] = token
        return redirect("/")


@app.route("/login")
def login():
        return oauth.auth0.authorize_redirect(
            redirect_uri=url_for("callback", _external=True)
        )


@app.route("/logout")
def logout():
        session.clear()
        return redirect(
            "https://"
            + env.get("AUTH0_DOMAIN")
            + "/v2/logout?"
            + urlencode(
                {
                    "returnTo": url_for("home", _external=True),
                    "client_id": env.get("AUTH0_CLIENT_ID"),
                },
                quote_via=quote_plus,
            )
        )

############################################################################### views #############
model = load_model('tuned_model')
#model = pickle.load(open('tuned_model.pkl', 'rb'))
cols = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']

@app.route('/templates/form.html')    ### form page
def nav():
    return render_template('form.html')


@app.route('/templates/Result.html')
def res():
    return render_template('Result.html')


@app.route('/templates/about.html')
def about():
    return render_template('about.html')


@app.route('/templates/description.html')
def description():
    return render_template('description.html')

@app.route('/templates/activity.html')
def activity():
    return render_template('activity.html')


@app.route('/predict', methods=['POST'])
def form_get():
    peru=request.form['name']
    data1 = int(request.form['age'])
    data2 = int(request.form['gender'])
    data3 = int(request.form['chestpain'])
    data4 = int(request.form['rbp'])
    data5 = int(request.form['chol'])
    data6 = int(request.form['fbs'])
    data7 = int(request.form['recg'])
    data8 = int(request.form['hr'])
    data9 = int(request.form['ani'])
    data10 = float(request.form['oldpeak'])
    data11= int(request.form['slope'])
    data12= int(request.form['vessels'])
    data13= int(request.form['thal'])
    arr = np.array([data1, data2, data3, data4,data5, data6, data7, data8,data9, data10, data11, data12,data13])
    data_unseen = pd.DataFrame([arr], columns=cols)
    prediction = predict_model(model, data=data_unseen)
    pred = int(prediction.Label[0])
    return render_template('Result.html', data=pred, name=peru)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))