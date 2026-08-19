from flask import Flask, render_template, request
import logging
import time

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def get_client_ip():
    # Render 같은 프록시 환경에서 전달되는 원래 클라이언트 IP
    forwarded_for = request.headers.get("X-Forwarded-For")

    if forwarded_for:
        # 여러 IP가 있으면 첫 번째가 원래 클라이언트 IP
        return forwarded_for.split(",")[0].strip()

    return request.remote_addr or "unknown"


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    elapsed = time.time() - request.start_time
    ip = get_client_ip()

    app.logger.info(
        "IP=%s | %s %s | %s | %.3fs",
        ip,
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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)