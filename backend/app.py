import os 
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

CORS(app)

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_API_URL="https://api.groq.com/openai/v1/chat/completions"