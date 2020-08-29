import os, json
import hashlib
import hmac
import base64
from app import flask_app,db
import requests
import re
from app.models import History
import dateutil.parser  as dparser


def get_authdetail(data):
    '''
        Generates the Signature to be checked against the Header
    '''
    request_data = data
    hmac_obj = hmac.new(flask_app.config["SECRET_KEY"].encode("ascii"),request_data,hashlib.sha256)
    return base64.b64encode(hmac_obj.digest()).decode()


def create_incident_Ticket(data):
    '''
        Creates incident Ticket in ServiceNow
    '''
    try:
        #Information to written in Ticket
        Job           = data['Job']
        start_time    = Job['StartTime']
        end_time      = Job['EndTime']
        machine_name  =  Job['Robot']['MachineName']
        error_message = "StartTime:" + start_time +"; End_Time:"+ end_time + ",Machine_Name:" + machine_name +",Error_Mesage:" +  Job['Info']
        process_name  = Job['Release']['ProcessKey']
       
        # ServiceNow Information gathered from .env File
        url      = flask_app.config['SERVICENOW_URL']
        username = flask_app.config['SERVICENOW_USERNAME']
        password = flask_app.config['SERVICENOW_SECRET']
        assignment_group =flask_app.config['SERVICENOW_ASSIGNMENT_GROUP']
        caller_id = flask_app.config['SERVICENOW_CALLER_ID']

        #setting Headers and Payload
        sn_headers = {'Content-Type':"application/json",'Accept':"application/json"}
        payload = {"short_description": process_name + " - bot Failed","description": error_message,
                    "assignment_group":assignment_group,"caller_id":caller_id}
       
        #Send POST request to Create Ticket
        response = requests.post(url,auth=(username,password),headers=sn_headers,json=payload)
       

        if(response.status_code !=  201):
            # print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
            incident_number = "NA"
            response_return = {"TicketStatus":"Ticket Creation Error",
                               "responseCode":response.status_code,
                               "response":response.json(),
                               "number":incident_number}
            ticket_status = {"status":False, "data":response_return}
        else:
            data = response.json()
            incident_number = data['result']['number']
            response_return = {"TicketStatus":"CREATED",
                               "responseCode":response.status_code,
                               "response":response.json(),
                               "number":incident_number}
            ticket_status = {"status":True, "data":response_return}

        #Load the Response to DB
        dataload_status = load_to_db(process_name,machine_name,start_time,end_time,error_message,ticket_status,Job)
        return ticket_status

    except Exception as error:
        print("Error:" + str(error))
        incident_number = "NA"
        response_return = ("Corefunction Error",'500',str(error),incident_number)
        return {"status":False,"data":response_return}


def load_to_db(process_name,machine_name,start_time,end_time,error_message,ticket_status,event_rawrepsonse):
    '''
        Loads the Information to DB
    '''
    try:
        data_to_db = History(
            processname=process_name,
            machinename=machine_name,
            starttime=convertStrintoDateTime(start_time),
            endtime=convertStrintoDateTime(end_time),
            boterrormessage=event_rawrepsonse['Info'],
            incidentnumber=ticket_status['data']['number'],
            incidentstatus=ticket_status['data']['TicketStatus'],
            incidentrawresponse=json.dumps(ticket_status['data']),
            eventrawresponse=json.dumps(event_rawrepsonse))
        db.session.add(data_to_db)
        db.session.commit()
        return True
    except Exception as error:
        print("Data Add error: " + str(error))
        return False

def convertStrintoDateTime(str_datetime):
    '''
        Converts DateTime from String to Python Object
    '''    
    return dparser.parse(str_datetime,fuzzy=True)
