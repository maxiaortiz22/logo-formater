import pandas as pd
import os

dir = r'C:\Users\maxia\OneDrive\Desktop\uSound\Logoaudiometría' #Cambiar por el que corresponda

columns = ['word_group_name'] #list_name_internal
values_to_search = ['Bisilabos Srt'] #pt_BR_Wavene_A
values_to_change = ['Bisilabos SRT'] #pt-br-wavenet-a

if __name__ == '__main__':
    os.chdir(dir)

    df = pd.read_csv('words_logoaudiometry.csv', sep='\t', encoding='utf-8')

    for i, colum in enumerate(columns):
        df.loc[df[colum] == values_to_search[i], colum] = values_to_change[i]

    df.to_csv('words_logoaudiometry_new.csv', encoding = "utf-8",index=False, sep='\t')