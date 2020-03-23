import ffmpeg

from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
from pydub import AudioSegment


def audio_info(file_path):
    return ffmpeg.probe(file_path)


def split_channel(intput_file, output_file=None):
    if not output_file:
        output_file = intput_file

    file_extension = "." + intput_file.split(".")[-1]
    output_file = output_file.split(file_extension)[0] + "_splitted_{}" + file_extension
    ffmpeg.input(intput_file).output(output_file.format("0"), map_channel="0.0.0").run()
    ffmpeg.input(intput_file).output(output_file.format("1"), map_channel="0.0.1").run()
    return output_file.format("0"), output_file.format("1")


def split_by_silence(file):
    fs, x = aIO.readAudioFile(file)
    segments = aS.silenceRemoval(x, fs, 0.020, 0.020, smoothWindow=1.0, weight=0.3, plot=False)
    audio_segment = AudioSegment.from_mp3(file)
    out = []
    for segment in segments:
        start_time = segment[0] * 1000
        end_time = segment[1] * 1000
        segment_name = str(segment[0]) + "-" + str(segment[1])
        extract = audio_segment[start_time:end_time]
        # Saving
        # extract.export(file.split("/")[-1].split(".")[0] + segment_name + ".wav", format="wav")
        filename = file.split("/")[-1].split(".")[0] + segment_name + ".wav"
        extract.export(filename, format="wav")
        out.append(filename)
    return out

if __name__ == "__main__":
    print(audio_info("/home/user/afftdn.wav"))
    print(audio_info(
        "/home/user/datasets/realweb_okkervil/kkc_20190803172902_from_79117139559_to_78124459660_28752092.mp3"))
    split_channel(
        intput_file="/home/user/datasets/realweb_okkervil/kkc_20190803172902_from_79117139559_to_78124459660_28752092.mp3",
        # output_file="/home/user/datasets/righ.mp3"
    )
