from pyttpass import app

if __name__ == "__main__":
    # trunk-ignore(bandit/B104)
    app.run(host="0.0.0.0", port=8080)