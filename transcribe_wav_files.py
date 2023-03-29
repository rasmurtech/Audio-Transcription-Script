import os
import speech_recognition as sr

# set up folders
audio_folder = r'C:\Users\Rasim Muratovic\Desktop\wav_files'
text_folder = r'C:\Users\Rasim Muratovic\Desktop\txt_files'

# create text folder if it doesn't exist
if not os.path.exists(text_folder):
    os.makedirs(text_folder)

# create recognizer object
r = sr.Recognizer()

# loop through audio files in audio folder
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith('.wav'):
        audio_path = os.path.join(audio_folder, audio_file)

        # check if text file already exists
        text_file = os.path.splitext(audio_file)[0] + '.txt'
        text_path = os.path.join(text_folder, text_file)
        if os.path.exists(text_path):
            print(f'{text_file} already exists, skipping...')
            continue

        # transcribe audio
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print(f'Unable to transcribe {audio_file}')
            continue

        # create corresponding text file
        with open(text_path, 'w') as f:
            f.write(text)
        print(f'{text_file} created.')
