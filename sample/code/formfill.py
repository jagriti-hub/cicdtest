from flask import Flask, jsonify
from flask import Blueprint
from flask import request
import os,json,sys
import time,math,random

formfill_api = Blueprint('formfill_api', __name__)

@formfill_api.route('/', methods=['GET'])
def fillform():
        return({"message":"Hello js!"})
