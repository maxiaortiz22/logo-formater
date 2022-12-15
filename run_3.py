"""Este script se corre para cargar los nombres de las palabras al csv"""

#Configuración:
dir = r'C:\Users\maxia\OneDrive\Desktop\uSound\Logoaudiometría\Trisilabos srt' 

excel_name = 'trisilabos_srt.xlsx' #Excel con las listas nuevas
list_name_excel = 'Ibero SRT (LI-SRT)' 
list_name_internal_excel = 'ibero_srt_li_srt'
voice_excel = 'es_us_wavenet_b'

if __name__ == '__main__':
    from tercer_paso.add_names import add_names_to_words_excel_file
    import os
    os.chdir(dir)

    add_names_to_words_excel_file(excel_name, list_name_excel, list_name_internal_excel, voice_excel)

    print('Audios cargados en el csv!')