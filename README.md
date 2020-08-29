
# Uipath JobFailure reporting in ServiceNow using UiPath_Webhook

This Project focuses on setting up a Centralized server (based on flask framework) to listen for Bot Failure events in UiPath Orchestrator and create an Incident in ServiceNow.This project can be extended to listen to various events and act accorrdingly.

## Installtion

Prerequisite:  ServiceNow Developer Instance with REST API User for creating Incidents 

### Setting up Flask Sever for Listening to UiPath events via webhook

1.  Set up the Project in your local 

    ```bash
      git clone https://github.com/sainath-s/UiPath_Webhook.git
      cd <path_to_the_project>
      python -m venv venv
      venv\Scripts\activate
      pip install -r requirements.txt
    ```

    create .env file in root directory and copy paste the details from .env.test and Update with your details.Your project folder should look this

    ```bash
      UiPath_Webhook\
                venv\
                 app\
                    __init__.py
                    routes.py
                    models.py
                    config.py
                    corefunctions.py
                    templates\
                          base.html
                          index.html
                monitoruipath.py
                .env
    ```

    Run flask in root directory

     ```bash
      flask run
    ```

    Once flask is up and running you can visit [localhost](http://127.0.0.1:5000/index) . You can visit the Index Page

    ![Index Page](/images/bot_monitor_index.JPG)

2.  Exposing the Flask to Internet

      Since this is for learning i have used [ngork](https://ngrok.com/) to acheive tunneling. Download the exe to your root directory or one step above the root directory

      ```bash
        cd <path_to_ngork.exe>
        ngork http 5000
      ```

      In the termincal you could see the Public address Ex.http://<some_random_number>.ngrok.io


3.  Configuring Webhook in UiPath

      [About Webhook](https://docs.uipath.com/orchestrator/docs/about-webhooks)
      [Creation a new Webhook in UiPath] (https://docs.uipath.com/orchestrator/docs/managing-webhooks)

      * In the URL section proivde the URL which you got in ngork Terminal Ex:http://<some_random_number>.ngrok.io/webhook and Subscribe only to Jobs.Faulted event. 
      * Provide a SECRET in this section if want to authicate the Webhooks request(recommended) before taking any action.Same SECRET should be provided in the .env file for             "SECRET_KEY"
  
  ## Demo:
