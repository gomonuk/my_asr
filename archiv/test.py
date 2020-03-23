from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
from pydub import AudioSegment

file = "/home/gomonuk/PycharmProjects/diaris/afftdn.wav"

[Fs, x] = aIO.readAudioFile(file)
segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow=1.0, weight=0.3, plot=False)
print(segments)


song = AudioSegment.from_mp3(file)

for segment in segments:
    start_time = segment[0] * 1000
    end_time = segment[1] * 1000
    segment_name = str(segment[0]) + "-" + str(segment[1])
    extract = song[start_time:end_time]

    # Saving
    extract.export(file.split("/")[-1].split(".")[0] + segment_name + ".wav", format="wav")
