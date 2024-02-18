import requests
import pandas as pd
import re


# ------------------------------Limpieza de archivo --------------------------------------------------------------------


url = 'https://storage.googleapis.com/media-help-ots-geomarketing-odoo/Situaci_n_V_ctimas_Minas_Antipersonal_en_Colombia_20240103.csv'

response = requests.get(url)
with open('Situaci_n_V_ctimas_Minas_Antipersonal_en_Colombia_20240103.csv', 'wb') as f:
    f.write(response.content)

df = pd.read_csv('Situaci_n_V_ctimas_Minas_Antipersonal_en_Colombia_20240103.csv')


def limpiar(registro):
    return re.sub(r'[^a-zA-Z0-9\s]', '', registro) if isinstance(registro, str) else registro


for columna in df.columns:
    df[columna] = df[columna].apply(limpiar)

df.to_csv('nuevo_archivo.csv', index=False)


# -------------------------------------Operaciones de archivo limpio ---------------------------------------------------

df_limpio = pd.read_csv('nuevo_archivo.csv')

valores_ano = df_limpio['ano'].unique()
valores_mes = df_limpio['mes'].unique()
valores_departamento = df_limpio['departamento'].unique()
valores_actividad = df_limpio['Actividad'].unique()
valores_genero = df_limpio['genero'].unique()
valores_estado = df_limpio['estado'].unique()


with open('archivo_final.txt', 'w') as archivo:

    print('***'*60)
    archivo.write('***' * 20 + '\n')
    archivo.write('total víctimas por año\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_ano):
        total_registros_ano = df_limpio['ano'].value_counts()[val]
        archivo.write(f'- en el año "{val}" el total de registros fueron: {total_registros_ano}\n')
        print(f'- en el año "{val}" el total de registros fueron: {total_registros_ano}')

    print('***'*60)
    archivo.write('\n\n\n')
    archivo.write('***' * 20 + '\n')
    archivo.write('total víctimas por mes (Independiente del año)\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_mes):
        total_registros_mes = df_limpio['mes'].value_counts()[val]
        archivo.write(f'- en el mes "{val}" el total de registros fueron: {total_registros_mes}\n')
        print(f'- en el mes "{val}" el total de registros fueron: {total_registros_mes}')

    print('***'*60)
    archivo.write('\n\n\n')
    archivo.write('***' * 20 + '\n')
    archivo.write('total víctimas por departamento\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_departamento):
        total_registros_departamento = df_limpio['departamento'].value_counts()[val]
        archivo.write(f'- en el departamento "{val}" el total de registros fueron: {total_registros_departamento}\n')
        print(f'- en el departamento "{val}" el total de registros fueron: {total_registros_departamento}')

    print('***'*60)
    archivo.write('\n\n\n')
    archivo.write('***' * 20 + '\n')
    archivo.write('total víctimas por actividad\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_actividad):
        total_registros_actividad = df_limpio['Actividad'].value_counts()[val]
        archivo.write(f'- en la actividad "{val}" el total de registros fueron: {total_registros_actividad}\n')
        print(f'- en la actividad "{val}" el total de registros fueron: {total_registros_actividad}')

    print('***'*60)
    archivo.write('\n\n\n')
    archivo.write('***' * 20 + '\n')
    archivo.write('total de víctimas por género\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_genero):
        total_registros_genero = df_limpio['genero'].value_counts()[val]
        archivo.write(f'- para el genero "{val}" el total de registros fueron: {total_registros_genero}\n')
        print(f'- para el genero "{val}" el total de registros fueron: {total_registros_genero}')

    print('***'*60)
    archivo.write('\n\n\n')
    archivo.write('***' * 20 + '\n')
    archivo.write('total de víctimas por estado\n')
    archivo.write('***'*20 + '\n')

    for val in sorted(valores_estado):
        total_registros_estado = df_limpio['estado'].value_counts()[val]
        archivo.write(f'- para el estado "{val}" el total de registros fueron: {total_registros_estado}\n')
        print(f'- para el estado "{val}" el total de registros fueron: {total_registros_estado}')
