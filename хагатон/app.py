from flask import Flask, request, jsonify
import requests
import cv2
import numpy as np

app = Flask('newflask')
@app.route("/")
def home():
    return "HI!!!"