# AudSpeech-to-Text Transcription Script
This script uses the SpeechRecognition library in Python to transcribe audio files into text. It is particularly useful for transcribing recorded speech into written form.

## Installation
To use this script, you need to have Python 3 and the SpeechRecognition library installed on your computer. You can install SpeechRecognition using pip:io-Transcription-Script

pip install SpeechRecognition

## Usage

1. Set up your audio and text folders: In the script, set the audio_folder and text_folder variables to the file paths for your audio and text folders, respectively.

2. Place your audio files in the audio folder: This script is designed to transcribe all text files in the text folder that correspond to audio files in the audio folder. So, make sure you place the audio files that you want to transcribe in the audio folder.

3. Run the script: Open a terminal window, navigate to the directory where the script is saved, and run the script using the following command:

python speech_to_text.py

4. Check the text files: The script will create new text files in the text folder with the same name as the corresponding audio file. If a text file already exists with that name, the script will skip it. If the text file is empty, the script will transcribe the corresponding audio file and write the transcription to the text file.

## Supported Audio Formats
The SpeechRecognition library supports many different audio formats. However, not all formats are supported on all platforms. For best results, use WAV files encoded with PCM.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
