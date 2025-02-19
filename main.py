from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Portal</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f0f0; /* Light gray background */
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center; /* Center the content */
        }

        img {
            max-width: 300px; /* Adjust as needed */
            margin-bottom: 20px;
        }

        label {
            display: block; /* Make labels stack on top of inputs */
            margin-bottom: 5px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            padding: 10px 20px;
            background-color: #007bff; /* Blue button */
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        .terms-and-conditions {
          margin-top: 10px;
        }

    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.ibb.co/Fkj0FpRz/20250213-232639.jpg" alt="">  <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <button onclick="checkCredentials()">Login</button>

        <div class="terms-and-conditions">
          
        </div>
    </div>

    <script>
        function checkCredentials() {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            if (username === "SERVERX" && password === "007") {
                // Redirect or open a new window
                window.location.href = "https://service-jlh6.onrender.com"; // Replace with the link you want to open
                // or
                // window.open("YOUR_SUCCESS_LINK", "_blank"); // Opens in a new tab
            } else {
                alert("Incorrect username or password.");
            }
        }
    </script>

</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
