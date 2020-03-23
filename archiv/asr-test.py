#!/usr/bin/python3.6

from websocket import create_connection

import sys

inf = "/home/user/fmpeg_out.wav"
if len(sys.argv) > 1:
    inf = sys.argv[1]


def process_chunk(ws, buf):
    ws.send_binary(buf)
    res = ws.recv()
    print(res)


def process_final_chunk(ws):
    ws.send('{"eof" : 1}')
    res = ws.recv()
    print(res)
    ws.close()


def test_stream():
    ws = create_connection("ws://localhost:2700")

    infile = open(inf, "rb")

    while True:
        buf = infile.read(8000)
        if not buf:
            break
        process_chunk(ws, buf)

    process_final_chunk(ws)


test_stream()
