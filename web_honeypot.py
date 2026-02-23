# Libraries
import logging
from flask import Flask, render_template, request
from logging.handlers import RotatingFileHandler

# Logging Format
logging_format = logging.Formatter('%(asctime)s %(message)s')

# HTTP Logger
funnel_logger = logging.getLogger('HTTP_Logger')
funnel_logger.setLevel(logging.INFO)

funnel_handler = RotatingFileHandler(
    'http_audits.log',
    maxBytes=2000,
    backupCount=5
)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)


def web_honeypot(input_username="admin", input_password="password"):

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            ip_address = request.remote_addr

            funnel_logger.info(
                f"IP: {ip_address} | Username: {username} | Password: {password}"
            )

            if username == input_username and password == input_password:
                return "Login Successful!"
            else:
                return "Invalid username or password."

        return render_template("wp-admin.html")

    return app


def run_web_honeypot(port=5000, input_username="admin", input_password="password"):
    app = web_honeypot(input_username, input_password)
    app.run(debug=True, port=port, host="0.0.0.0")