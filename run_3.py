"""Este script se corre para cargar los nombres de las palabras al csv"""

#Configuración:
dir = r'C:\Users\maxia\OneDrive\Desktop\Palabras Audiocom Colombia' 

excel_name = 'Listas Audiocom.xlsx' #Excel con las listas nuevas
list_name_excel = 'Audiocom' 
list_name_internal_excel = 'audiocom'
voice_excel = 'audiocom_colombia'

if __name__ == '__main__':
    from tercer_paso.add_names import add_names_to_words_excel_file
    import os
    os.chdir(dir)

    add_names_to_words_excel_file(excel_name, list_name_excel, list_name_internal_excel, voice_excel)

    print('Audios cargados en el csv!')