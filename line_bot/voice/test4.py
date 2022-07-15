import wave, struct, math, random


# f = wave.open("./voice/Ub23b4d69bd05b25c866909172a57b48b.wav","rb")
# parms = f.getparms()

# sampleRate = 44100.0 # hertz
# duration = 1.0 # seconds
# frequency = 440.0 # hertz
# obj = wave.open('Ub23b4d69bd05b25c866909172a57b48b.wav','w')
# obj.setnchannels(1) # mono
# obj.setsampwidth(2)
# obj.setframerate(sampleRate)
# obj.close()

obj = wave.open('temp1.wav','rb')
print( "Number of channels",obj.getnchannels())
print ( "Sample width",obj.getsampwidth())
print ( "Frame rate.",obj.getframerate())
print ("Number of frames",obj.getnframes())
print ( "parameters:",obj.getparams())
obj.close()


# audio_to_wav("Ub23b4d69bd05b25c866909172a57b48b.wav",44100)