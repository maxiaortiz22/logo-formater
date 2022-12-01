import pandas as pd
import os

dir = r'F:\Desktop\uSound\Listas logoaudiometría' #Cambiar por el que corresponda

columns = ['voice'] #list_name_internal
values_to_search = ['pt_BR_Wavene_A'] #pt_BR_Wavene_A
values_to_change = ['pt-br-wavenet-a'] #pt-br-wavenet-a

if __name__ == '__main__':
    os.chdir(dir)

    df = pd.read_csv('words_logoaudiometry.csv', sep='\t', encoding='utf-8')

    for i, colum in enumerate(columns):
        df.loc[df[colum] == values_to_search[i], colum] = values_to_change[i]

    df.to_csv('words_logoaudiometry_new.csv', encoding = "utf-8",index=False, sep='\t')