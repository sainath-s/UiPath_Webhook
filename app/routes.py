from flask import render_template , request , Response as res
from app import flask_app
from app.corefunctions import get_authdetail,create_incident_Ticket
from json import load,dump
from app.models import History


@flask_app.route('/')
@flask_app.route('/index')
def index():
    #print(History.query.all())
    '''
        This function renders the index.html file and fills it with data from DB
    '''
    return render_template('index.html',title='Home',botevents=History.query.all())

@flask_app.route('/webhook',methods=['POST'])
def webhook():
    '''
        This routes is responsible for handling the incoming webhook.
        First Validates the Signature from the request.
            If it is valid , script continues to create an Incident
                If Incident Creation is success sends "201" response
                If Incident Creation is failed or event Type not supported sends "422" response
            If it is invalid , print the error
    '''
    signature = get_authdetail(request.data)
    signature_header = request.headers.get('X-Uipath-Signature')
    #Validate Signature from Header against the signature generated using SECRET 
    if signature == signature_header:
        request_data = request.get_json()
        eventType =  request_data['Type']
        #Check if event Type is Faulted
        if(eventType == "job.faulted"):
            ticket_status = create_incident_Ticket(request_data)
            if(ticket_status['status']):
                return res(status=201,response="Ticket Created")
            else:
                return res(status=422,response="Ticket failed to create")
        else:
            return res(status=422,response="Event Type not supported")
    else:
        print("Signature_Mismatch")
        return res(status=401,response="UnAuthorized")