"""Este script se corre para obtener las palabras sin silencios, para realizar la última calibración"""

#Configuración:
dir = r'C:\Users\maxia\OneDrive\Desktop\uSound\Logoaudiometría\Bisilabos srt'
group_name = 'bisilabos_srt'

if __name__ == '__main__':
    from segundo_paso.juntar_palabras import delete_silence
    import os
    os.chdir(dir)

    delete_silence(group_name)

    print('Audios creados!')