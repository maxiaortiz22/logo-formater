"""Este script se corre primero para generar las carpetas de las listas y el template
de los audios con low, medium y high."""

#Configuración:
dir = r'C:\Users\maxia\OneDrive\Desktop\uSound\Logoaudiometría\Trisilabos srt' 
excel_lists = 'trisilabos_srt.xlsx' 
group_name = 'trisilabos_srt'

if __name__ == '__main__':
    from primer_paso.logo_formater import Logo

    logo = Logo(dir, excel_lists, group_name)

    logo.crear_listas()
    logo.crear_carpetas_calibradas()

    print('Audios creados!')