
# UiPath_Webhook

## Installtion

### Set up Flask Sever for Listen to UiPath Webhook

1. Set up the Project in your local 

  ```bash
    git clone https://github.com/sainath-s/UiPath_Webhook.git
    cd <path_to_the_project>
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
  ```

  create .env file in root directory and copy paste the details from .env.test and Update with your details

  ```bash
    flask run
  ```

  Once flask is up and running you can visit [localhost](http://127.0.0.1:5000/index) . You can visit the Index Page

  ![Index Page](/images/bot_monitor_index.JPG)

2. Exposing the Flask to Internet

  I have used the [ngork](https://ngrok.com/) to acheive this. Download the exe to your root directory or one step above the root directory
  
  ```bash
    cd <path_to_ngork.exe>
    ngork http 5000
  ```
  In the termincal you could see the Public address Ex.http://<some_random_number>.ngrok.io
