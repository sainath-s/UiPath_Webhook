from app import db

class History(db.Model):
    '''
        Model of the data stored in app.db
    '''
    id = db.Column(db.Integer,primary_key=True)
    processname  = db.Column(db.String(240))
    machinename  = db.Column(db.String(240))
    starttime    = db.Column(db.DateTime)
    endtime      = db.Column(db.DateTime)
    boterrormessage = db.Column(db.Text)
    incidentnumber  = db.Column(db.String(240))
    incidentstatus  = db.Column(db.String(240))
    incidentrawresponse = db.Column(db.Text)
    eventrawresponse    = db.Column(db.Text)

    def __ref__(self):
        return '<BotDetails:Name -  {} ,Error - {} ,IncidentStatus:{},IncidentNumber:{}>'.format(self.botname,self.boterrormessage,self.incidentstatus,self.incidentnumber)



