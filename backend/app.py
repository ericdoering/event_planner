import os 
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

CORS(app)

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_API_URL="https://api.groq.com/openai/v1/chat/completions"

def ask_llama(prompt):
    headers={
        "authorization": f"Bearer{GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body={
        "model": "illama3-70b-8192",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
    }

    response=request.post(GROQ_API_URL, headers=headers, json=body)
    response.raise_for_status()
    data=response.json()

    return data["choices"][0]["message"]["content"]

@app.route("/plan_event", methods=["POST"])
def plan_event():
    data=request.json
    event_type=data.get("event_type", "")
    guests=data.get("guests", "")
    budget=data.get("budget", "")

    prompt=f"""
        You are an expert event planner.
        Create a detailed event plan for a {event_type}
        with a total of {guests} guests and a budget of around
        {budget} dollars. Include theme idea, food and drinks,
        a shedule, and a checklist of things to prepare. Make this
        useful and fun.
    """

    try:
        result=ask_llama(prompt)
        return jsonify({"plan": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(debug=True)

