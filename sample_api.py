# import flask dependencies
from flask import Flask, request, make_response, jsonify
from classes_dict import *
import re
from retrieval_based_Reply import my_response

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    request_data = request.get_json()
    user_input=request_data["Text"]
    print(user_input)
    response= my_response(user_input)
    # req = request.get_json(force=True)
    # fetch action from json
    # action = req.get('queryResult')
    # name=action.get('parameters').get("name")

    # return a fulfillment response
    # {
    # type : "action",
    # action : "schedule_a_followup"
    # parameters : {
    # event_time : <full datetime timestamp indicating 9 PM>
    # },
    # {
    # type : "action",
    # action : "create_ticket"
    # parameters : {
    # tags : ["refund", ".."]
    # }
    # }
    return response

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()

