"""Este script se corre para obtener las palabras sin silencios, para realizar la última calibración"""

#Configuración:
dir = r'F:\Desktop\uSound\Listas logoaudiometría\Bisílabos fonéticamente balanceados para adultos. Matrtínez y cols'
group_name = 'bisilabos_martinez_cols'

if __name__ == '__main__':
    from segundo_paso.juntar_palabras import delete_silence
    import os
    os.chdir(dir)

    delete_silence(group_name)

    print('Audios creados!')