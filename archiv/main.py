#!/usr/bin/python3

from vosk import Model, KaldiRecognizer
import sys
import json
import os

model = "/home/user/vosk/alphacep-model-android-ru-0.3"

if not os.path.exists(model):
    print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
    exit (1)


model = Model(model)

# Large vocabulary free form recognition
#rec = KaldiRecognizer(model, 16000)

rec = KaldiRecognizer(model, 16000, "отделстрой")

wf = open(sys.argv[1], "rb")
wf.read(44) # skip header

while True:
    data = wf.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        print (res['text'])

res = json.loads(rec.FinalResult())
print (res['text'])
