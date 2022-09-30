import glob
from scipy.io import wavfile
import librosa as lb
import numpy as np

def juntar(group_name):
    wavs_high_m = []
    wavs_medium_m = []
    wavs_low_m = []
    for filename in glob.glob('Listas - Calibradas/**/*_high.wav'):
        #print(filename)
        data, sr = lb.load(filename, sr=None)
        wavs_high_m.append(data)

    for filename in glob.glob('Listas - Calibradas/**/*_medium.wav'):
        #print(filename)
        data, sr = lb.load(filename, sr=None)
        wavs_medium_m.append(data)

    for filename in glob.glob('Listas - Calibradas/**/*_low.wav'):
        #print(filename)
        data, sr = lb.load(filename, sr=None)
        wavs_low_m.append(data)

    audios_high = np.concatenate(np.array(wavs_high_m))
    audios_medium = np.concatenate(np.array(wavs_medium_m))
    audios_low = np.concatenate(np.array(wavs_low_m))

    #wavfile.write(f"{group_name}_high.wav", sr, audios_high)
    #wavfile.write(f"{group_name}_medium.wav", sr, audios_medium)
    #wavfile.write(f"{group_name}_low.wav", sr, audios_low)

    return audios_high, audios_medium, audios_low, sr

def delete_silence(group_name):
    
    thresh = 1.0
    segment_size_t = 0.3

    audios_high, audios_medium, audios_low, sr = juntar(group_name)
    audios = [audios_high, audios_medium, audios_low]

    for i, audio in enumerate(audios):
        signal = audio

        # ventaneo
        signal_len = len(signal)
        segment_size = int(segment_size_t * sr)  # [segs]->[samps]
        segments = np.array([signal[x:x + segment_size] for x in
                            np.arange(0, signal_len, segment_size)])  # Vectorización posible?
        # ojo con la duración del último: no arroja IndexOutOfRangeError aunque sea más corto

        energies = [(s**2).sum() / len(s) for s in segments]

        # (attention: integer overflow would occure without normalization here!) — ké, por qué? en la línea anterior en todo caso...
        thresh *= np.median(energies)  # mediana de potencia - 3 dB, lo podríamos cambiar
        index_of_segments_to_keep = (np.where(energies > thresh)[0])
        segments2 = segments[index_of_segments_to_keep]

        new_signal = np.concatenate(segments2)

        if i==0:
            wavfile.write(f"Palabras juntas/{group_name}_high.wav", sr, new_signal)
            print(f"Audio creado: {group_name}_high.wav")
        elif i==1:
            wavfile.write(f"Palabras juntas/{group_name}_medium.wav", sr, new_signal)
            print(f"Audio creado: {group_name}_medium.wav")
        elif i==2:
            wavfile.write(f"Palabras juntas/{group_name}_low.wav", sr, new_signal)
            print(f"Audio creado: {group_name}_low.wav")
