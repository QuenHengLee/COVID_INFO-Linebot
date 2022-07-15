import azure.cognitiveservices.speech as speechsdk

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription="8e620401f2ba40099233671f7e8bd081", region="southeastasia", speech_recognition_language='zh-tw')
    audio_input = speechsdk.AudioConfig(filename="Ub23b4d69bd05b25c866909172a57b48b.wva")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)

from_file()