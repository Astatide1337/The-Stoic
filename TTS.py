import os
import json
import random
from scipy.io import wavfile
import noisereduce as nr
# python synthesize.py --text "his mother, however, was a little shy of the company for him, and besides she could not always spare him."  --speaker_id 207 --restore_step 800000 --mode single -p config/LibriTTS/preprocess.yaml -m config/LibriTTS/model.yaml -t config/LibriTTS/train.yaml
def generateAudio():
    with open("./quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)

    quote = quotes["quotes"][random.randint(0, len(quotes["quotes"])-1)]
    quoteText = quote["text"]
    quoteAuthor = quote["author"]
    attribute = ""
    attributes = [
        f"{quoteAuthor} once said,",
        f"{quoteAuthor} said,",
        f"{quoteAuthor} once told me,",
    ]
    starter = ""
    starters = [
        f"A life quote from {quoteAuthor},",
        f"A life quote by {quoteAuthor},",
        f"A life lesson from {quoteAuthor},",
        f"A life lesson by {quoteAuthor},",
        f"A quote from {quoteAuthor},",
        f"A quote by {quoteAuthor},",
        f"How beautiful it was when {quoteAuthor} said,",
    ]
    #either add a starter or an attribute
    if random.randint(0, 1) == 0:
        starter = random.choice(starters)
    else:
        attribute = random.choice(attributes)

    prompt = f"{starter}{attribute} {quoteText}"
    os.system(f'python synthesize.py --text "{prompt}" --speaker_id 742 --restore_step 900000 --mode single -p config/LibriTTS/preprocess.yaml -m config/LibriTTS/model.yaml -t config/LibriTTS/train.yaml --energy_control 0.6 --pitch_control 0.66')
    # title = max(os.listdir("./GeneratedTTS"), key=lambda x: os.path.getctime(os.path.join("./GeneratedTTS", x)))
    # rate, data = wavfile.read(f"./GeneratedTTS/{title}")
    # reduced_noise = nr.reduce_noise(y=data, sr=rate)    
    # wavfile.write(f"./GeneratedTTS/{title}", rate, reduced_noise)