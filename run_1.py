"""Este script se corre primero para generar las carpetas de las listas y el template
de los audios con low, medium y high."""

#Configuración:
dir = r'F:\Desktop\uSound\Listas logoaudiometría\Bisílabos de Godoy' 
excel_lists = 'bisílabos de godoy.xlsx' 
group_name = 'bisilabos_godoy'

if __name__ == '__main__':
    from primer_paso.logo_formater import Logo

    logo = Logo(dir, excel_lists, group_name)

    logo.crear_listas()
    logo.crear_carpetas_calibradas()

    print('Audios creados!')