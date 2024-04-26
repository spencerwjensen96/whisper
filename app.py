import whisper

audio = "/Users/spencer.jensen/Desktop/university/speechsynth/my_arctic_voice/wav/arctic_a0003.wav"

model = whisper.load_model("base")
result = model.transcribe(audio)
print(result["text"])