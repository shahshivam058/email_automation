from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route("/sms",methods=["GET","POST"])
def sms_reply():
    automatic_response = MessagingResponse()
    automatic_response.message("auto reply from python and twilio")
    print(automatic_response)
    return str(automatic_response)



if __name__ == "__main__":
    app.debug=True
    app.run()