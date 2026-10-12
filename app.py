# Testing automatic deployment through GitHub webhook

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud CI/CD Pipeline</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
            }

            .container {
                background: white;
                width: 600px;
                padding: 50px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
            }

            .icon {
                font-size: 60px;
                margin-bottom: 20px;
            }

            h1 {
                color: #333;
                margin-bottom: 15px;
            }

            p {
                color: #666;
                font-size: 18px;
                line-height: 1.6;
            }

            .status {
                display: inline-block;
                margin-top: 25px;
                padding: 10px 22px;
                background: #22c55e;
                color: white;
                border-radius: 25px;
                font-weight: bold;
            }

            .tech {
                margin-top: 25px;
                color: #555;
                font-size: 14px;
            }

            .tech span {
                color: #667eea;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <div class="icon">🚀</div>

            <h1>Cloud CI/CD Pipeline</h1>

            <p>
                Welcome to my Flask application!
                This application is automatically built and deployed
                using a CI/CD pipeline.
            </p>

            <div class="status">
                ✓ Deployment Successful
            </div>

            <div class="tech">
                Powered by
                <span>GitHub</span> •
                <span>Jenkins</span> •
                <span>Docker</span> •
                <span>AWS EC2</span>
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
