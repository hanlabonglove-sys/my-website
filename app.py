from flask import Flask, render_template, request
import logging
import time

app = Flask(__name__)

# 기본 Flask 로그 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def get_client_ip():
    """
    프록시를 통해 전달된 클라이언트 IP를 확인합니다.
    여러 IP가 전달되면 첫 번째 값을 사용합니다.
    """

    forwarded_for = request.headers.get("X-Forwarded-For")

    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    return request.remote_addr or "unknown"


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    elapsed = time.time() - request.start_time
    ip = get_client_ip()

    print(
        f"VISITOR | "
        f"IP={ip} | "
        f"{request.method} {request.path} | "
        f"STATUS={response.status_code} | "
        f"TIME={elapsed:.3f}s",
        flush=True
    )

    return response


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello! 👋"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )


@app.route("/hello")
def hello():
    return "Hello! 👋"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)