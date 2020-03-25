from asrtest import test_stream
from helpers import audio_info, split_channel, split_by_silence

file_path_mono = "/home/user/afftdn.wav"
file_path_stereo = "/home/user/datasets/realweb_okkervil/kkc_20190803172902_from_79117139559_to_78124459660_28752092.mp3"

channels = audio_info(file_path_stereo)["streams"][0]["channels"]

if channels == 1:  # mono
    print("mono")
elif channels == 2:  # stereo
    print("stereo")
    speaker0, speaker1 = split_channel(file_path_stereo)  # две дорожки из двух каналов
    a = split_by_silence(speaker0)
    for i in a:
        test_stream(i)
    # 2. отправляем в диаризацию

# вот тут должны получить два списка для двух спикеров

speaker1 = [1, 2]
speaker2 = [1, 2]

# Для vosk, необходимо использовать формат 8khz 16bit mono PCM

for s1, s2 in speaker1, speaker2:
    print(s1, s2)
