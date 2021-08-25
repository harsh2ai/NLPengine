""" Copyright 2021, Scanta Inc., All rights reserved. """
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from fastapi import FastAPI
from pydantic import BaseModel
from EmotionDetection.EmotionDetection import *

from TextualAnalysis.GetTextAnalysis.GetTextAnalysis import GetTextualAnalysis
from PIIDetection.PIDetector import *

class request_body(BaseModel):
    '''
    Defining the variable/fields and their data types,
    which will be used by fastapi to validate a request.
    '''

    message_type: str
    user_id: str
    text: str
    time_stamp: float
    message:str


app= FastAPI()

@app.post("/textAnalysis")
def textAnalysis(request: request_body):
    # get content from the request packet to further process:
    message_type=request.message_type
    user_id= request.user_id
    text= request.text
    time_stamp=request.time_stamp
    analysis_result=GetTextualAnalysis().get_textual_analysis(text)
    return{"Text":text,"Analysis":analysis_result}

@app.post("/personalInfo")
def personal_info_detction(request:request_body):
    text=request.text
    detector=PIIDetection()
    return({"text":text,"personal_info":detector.detect_pii(text)})


@app.post("/emotiondetection/")
def emotion_detection(request:request_body):
    message=request.message
    detector=EmotionDetections()
    return({"emotion is":detector.detect_emotion(message)})
