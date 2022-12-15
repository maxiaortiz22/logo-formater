import pandas as pd
import glob
from librosa import load 
from scipy.io import wavfile
import os
from glob import glob
import numpy as np

class Logo:
    
    def __init__(self, dir, excel_lists, group_name):
        self.excel_lists = excel_lists # Str: Nombre del excel!
        self.dir = dir # Str: El directorio en donde quiero que se almacenen los datos
        self.group_name = group_name # Str: Nombre del grupo.

        os.chdir(self.dir)

    def crear_listas(self):
        listas = pd.read_excel(self.excel_lists)

        print(listas.to_string)

        lists_names = list(listas.columns)

        words = glob('audios/*.wav')

        str1 = 'áéíóúñçãêôâüäàåëèïîìöòûùÿ' 
        str2 = 'aeiouncaeoauaaaeeiiioouuy'

        i = 1
        for list_name in lists_names:

            # Creo la carpeta Listas si no existe:
            isExist = os.path.exists('Listas')
            if not isExist:
                os.makedirs('Listas')

            # Creo la carpeta de la lista que no exista:
            isExist = os.path.exists(f'Listas/{list_name}')
            if not isExist:
                os.makedirs(f'Listas/{list_name}')

            lista = listas[list_name].to_numpy()

            for t, audio in enumerate(lista):
                audio = audio.upper()

                for word in words:
                    word = word.upper()
                    
                    if audio in word:
                        data, fs = load(word, sr=48000)

                        data = data/np.max(np.abs(data))

                        audio = audio.lower()
                        table = audio.maketrans(str1, str2)
                        audio = audio.translate(table)

                        if (t<10):
                            for gain in ['high', 'low', 'medium']:
                                audio_name = f'{i}_0{t}_{audio}_{self.group_name}_01_{gain}.wav'
                                #write(audio_name, data=data, samplerate=fs)
                                audio_path = f'Listas/{list_name}/{audio_name}'
                                wavfile.write(audio_path, fs, data)

                                print(audio_path)
                        else:
                            for gain in ['high', 'low', 'medium']:
                                audio_name = f'{i}_{t}_{audio}_{self.group_name}_01_{gain}.wav'
                                #write(audio_name, data=data, samplerate=fs)
                                audio_path = f'Listas/{list_name}/{audio_name}'
                                wavfile.write(audio_path, fs, data)

                                print(audio_path)

            i+=1

    def crear_carpetas_calibradas(self):
        listas = glob("Listas/*", recursive = True)
        listas = [x[0].split('\\')[-1] for x in os.walk('Listas')]
        listas.remove('Listas')

        os.makedirs('Palabras juntas')
        
        os.makedirs('Listas - Calibradas')
        os.makedirs('Listas - Calibradas Final')

        for lista in listas:
            os.makedirs(f'Listas - Calibradas/{lista}')
            os.makedirs(f'Listas - Calibradas Final/{lista}')