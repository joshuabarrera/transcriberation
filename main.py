import whisper_timestamped as whisper
import json

audio = whisper.load_audio("audio.mp3")

model = whisper.load_model("small", device="cuda")

result = whisper.transcribe(model, audio, language="en")

print(json.dumps(result, indent = 2, ensure_ascii = False))

with open("result.json", "w") as f:
    f.write(json.dumps(result, indent = 2, ensure_ascii = False))