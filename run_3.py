"""Este script se corre para cargar los nombres de las palabras al csv"""

#Configuración:
dir = r'F:\Desktop\uSound\Listas logoaudiometría\Bisílabos fonéticamente balanceados para adultos. Matrtínez y cols' 

excel_name = 'bisilabos martínez y cols.xlsx' #Excel con las listas nuevas
list_name_excel = 'Bisílabos fonéticamente balanceados para adultos' 
list_name_internal_excel = 'bisilabos_martinez_cols'
voice_excel = 'original'

if __name__ == '__main__':
    from tercer_paso.add_names import add_names_to_words_excel_file
    import os
    os.chdir(dir)

    add_names_to_words_excel_file(excel_name, list_name_excel, list_name_internal_excel, voice_excel)

    print('Audios cargados en el csv!')