"""Este script se corre primero para generar las carpetas de las listas y el template
de los audios con low, medium y high."""

#Configuración:
dir = r'C:\Users\maxia\OneDrive\Desktop\Palabras Audiocom Colombia' 
group_name = 'audiocom'

if __name__ == '__main__':
    from segundo_paso.juntar_palabras import delete_silence
    import os
    os.chdir(dir)

    delete_silence(group_name)

    print('Audios creados!')