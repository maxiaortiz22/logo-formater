import numpy as np
import pandas as pd
import glob

def get_audios_info(excel_name, list_name_excel, list_name_internal_excel, voice_excel):
    
    str1 = 'áéíóúñçãêôâüäàåëèïîìöòûùÿ' 
    str2 = 'aeiouncaeoauaaaeeiiioouuy'
    
    listas = pd.read_excel(excel_name)
    lists_names = list(listas.columns)

    words, index = [], []
    voice, list_name = [], []
    list_name_internal = []
    word_group_name, word_group_name_iternal = [], []
    index_word_group = []
    file_name_low_intensity, file_name_medium_intensity = [], []
    file_name_high_intensity = []

    for i, list_names in enumerate(lists_names):
        i+=1
        lista = listas[list_names].to_numpy()

        low = glob.glob(f"Listas - Calibradas/{list_names}/*_low.wav")
        low = [word.split('\\')[-1] for word in low]

        medium = glob.glob(f"Listas - Calibradas/{list_names}/*_medium.wav")
        medium = [word.split('\\')[-1] for word in medium]

        high = glob.glob(f"Listas - Calibradas/{list_names}/*_high.wav")
        high = [word.split('\\')[-1] for word in high]

        for t, audio in enumerate(lista):
            audio = audio.lower()
            list_name.append(list_name_excel)
            list_name_internal.append(list_name_internal_excel)
            word_group_name.append(list_names.title())
            word_group_name_iternal.append(list_names.lower().replace(' ', '_'))
            index_word_group.append(i)
            index.append(t)
            words.append(audio)
            voice.append(voice_excel.lower().replace(' ', '_'))

            table = audio.maketrans(str1, str2)
            audio = audio.translate(table)

            for low_name in low:
                if audio in low_name:
                    name = low_name.split('.wav')[0]
                    file_name_low_intensity.append(name)

            for medium_name in medium:
                if audio in medium_name:
                    name = medium_name.split('.wav')[0]
                    file_name_medium_intensity.append(name)

            for high_name in high:
                if audio in high_name:
                    name = high_name.split('.wav')[0]
                    file_name_high_intensity.append(name)

    assert(len(list_name)==len(list_name_internal))
    assert(len(list_name_internal)==len(word_group_name))
    assert(len(word_group_name)==len(word_group_name_iternal))
    assert(len(word_group_name_iternal)==len(index_word_group))
    assert(len(index_word_group)==len(file_name_low_intensity))
    assert(len(file_name_low_intensity)==len(file_name_medium_intensity))
    assert(len(file_name_medium_intensity)==len(file_name_high_intensity))
    assert(len(file_name_high_intensity)==len(index))
    assert(len(index)==len(words))
    assert(len(words)==len(voice))
    
    df = pd.DataFrame(data= {'list_name': list_name,
                         'list_name_internal': list_name_internal,
                         'word_group_name': word_group_name,
                         'word_group_name_iternal': word_group_name_iternal,
                         'index_word_group': index_word_group,
                         'file_name_low_intensity': file_name_low_intensity,
                         'file_name_medium_intensity': file_name_medium_intensity,
                         'file_name_high_intensity': file_name_high_intensity,
                         'index':index,
                         'word':words,
                         'voice':voice})

    return df

def add_names_to_words_excel_file(excel_name, list_name_excel, list_name_internal_excel, voice_excel):
    
    logo = pd.read_csv('words_logoaudiometry.csv', sep='\t', encoding='utf-8')

    data = get_audios_info(excel_name, list_name_excel, list_name_internal_excel, voice_excel)

    logo = logo.append(data, ignore_index = True)

    logo.to_csv('words_logoaudiometry_new.csv', encoding = "utf-8",index=False, sep='\t')