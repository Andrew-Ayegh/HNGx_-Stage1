from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route("/api", methods=['GET'])
def get_info():
    # Get parameters form the request
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    
    # Getting the Day of the week
    day = datetime.now().strftime("%A")
    
    # Getting the UTC time 
    utc_time = datetime.now().strftime("%Y-%m-%DT%H:%M:%SZ")
    
    # Response Data
    response = {
        "slack_name":slack_name,
        "current_day":day,
        "utc_time":utc_time,
        "track":track,
        "github_file_url":"https://github.com/Andrew-Ayegh/HNGx_Stage1/blob/252e919191aad8aa96ef4a208bbfb99b946bbb4b/main.py",
        "github_repo_link":"https://github.com/Andrew-Ayegh/HNGx_Stage1",
        "status_code":200
    }
    
    return jsonify(response)

if __name__== "__main__":
    app.run(debug=True)
