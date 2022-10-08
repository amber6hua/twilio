from flask import Flask, request, redirect, json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from settings import FROM_EMAIL, TO_EMAIL, KEY, SMTP_SSL

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    content = json.dumps(request.args)
    print(content)
    send_email(content)

    return json.dumps(request.args)


def send_email(text):
    msg = MIMEText(text, "html", "utf-8")
    msg["From"] = formataddr(["hello", FROM_EMAIL])
    msg["Subject"] = "test"

    server = smtplib.SMTP_SSL(SMTP_SSL)
    server.login(FROM_EMAIL, KEY)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    server.quit()


if __name__ == "__main__":
    app.run(debug=True)
