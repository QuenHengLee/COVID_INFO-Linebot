from pydub import AudioSegment

# def trans_to_mp3(filepath, out_name):
#     song = AudioSegment.from_mp3(filepath)
#     song.export(out_name + ".wav", format="mp3")
# wav = trans_to_mp3('Ub23b4d69bd05b25c866909172a57b48b.mp3', 'Ub23b4d69bd05b25c866909172a57b48b_mp3')

def trans_mp3_to_wav(filepath, out_name):
    AudioSegment.converter = 'D:ffmpeg-N-104005-g2761a7403b-win64-gpl/bin/ffmpeg.exe'
    with open(filepath,'rb') as f:
        song = AudioSegment.from_file(f,format='m4a')
        song.export(out_name + ".wav", format="wav")
trans_mp3_to_wav('Ub23b4d69bd05b25c866909172a57b48b.m4a', 'temp1')


