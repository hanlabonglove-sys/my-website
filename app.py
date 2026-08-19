from flask import Flask, render_template, request
import logging
import time

app = Flask(__name__)

# 로그 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed = time.time() - request.start_time

    app.logger.info(
        "%s %s | %s | %.3fs",
        request.method,
        request.path,
        response.status_code,
        elapsed
    )

    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello! 👋"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)