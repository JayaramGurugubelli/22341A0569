from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello Jayaram!</h1>
    <p>🎉 Welcome to the CI/CD Demo App!</p>
    <p>👨‍💻 This app is designed to demonstrate the power of Continuous Integration and Continuous Deployment.</p>
    <p>🔧 With CI/CD, we can automate the testing and deployment of our applications, making it easier to deliver high-quality software faster.</p>
    <p>🌟 Enjoy exploring the world of CI/CD and happy coding!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)