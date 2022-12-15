import os
import pandas as pd #  pip install numpy==1.19.3
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"modern-index-371513-25e04072b080.json"

# Instantiates a client
client = texttospeech_v1.TextToSpeechClient()


if __name__ == '__main__':

    #Datos:
    genero = 'hombre' # 'mujer'
    dir = r'C:\Users\maxia\OneDrive\Desktop\uSound\Logoaudiometría\Trisilabos srt'
    excel_lists = 'trisilabos_srt.xlsx'
    
    os.chdir(dir)
    list_name = pd.read_excel(excel_lists)

    lists_names = list(list_name.columns)

    for name in lists_names:
        lista = list_name[name].to_numpy()
        for audio in lista:
            synthesis_input = texttospeech_v1.SynthesisInput(text=audio)

            if genero == 'hombre':
                voice = texttospeech_v1.VoiceSelectionParams(
                    name='es-US-Wavenet-B', language_code="es-US" #Hombre
                )
            elif genero == 'mujer':
                voice = texttospeech_v1.VoiceSelectionParams(
                    name='es-US-Wavenet-A', language_code="es-US" #Mujer
                )

            # Select the type of audio file you want returned
            audio_config = texttospeech_v1.AudioConfig(
                # https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1#audioencoding
                audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16,
                speaking_rate = 1
            )

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # The response's audio_content is binary.
            with open(f"audios/{str(audio)}.wav", "wb") as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print(f'Audio creado {audio}.wav')