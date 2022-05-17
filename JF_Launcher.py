import PySimpleGUI as sg
import threading
from google_drive_downloader import GoogleDriveDownloader as gdd
import subprocess
import sys
import os
#import simpleaudio as sa
import time

downloading = False

#CLICK_SOUND = sa.WaveObject.from_wave_file('./sounds/click.wav')
#PLAY_CLICK = CLICK_SOUND.play()
#PLAY_CLICK.wait_done()

# Функции
# def click():
#     threading.Thread(
#         target=click_thread(),
#         args=(),
#         daemon=True).start(
#     )

# def click_thread():
#     PLAY_CLICK = CLICK_SOUND.play()
#     PLAY_CLICK.wait_done()

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def downloadingFile_thread(dwld_url):
    progress(True)
    gdd.download_file_from_google_drive(
        file_id=dwld_url,
        dest_path=(download_path + '/' + s_game + '.zip'),
        unzip=True,
        showsize=True,
        overwrite = True
    )
    window.FindElement('Download').Update(disabled=False)
    window.FindElement('choose_game').Update(disabled=False)
    window.FindElement('folderbrowse').Update(disabled=False)
    window.FindElement('Browse').Update(disabled=False)
    file = os.path.join(os.path.abspath(os.path.dirname(download_path+'/')), s_game + '.zip')
    os.remove(file)
    threading.current_thread()
    window.FindElement('log').Update(
        'The game ' + s_game + ' has been successfully wrote to disc!'
    )
def downloadingFile(downl_url):
    threading.Thread(
        target=downloadingFile_thread,
        args=(downl_url,),
        daemon=True).start(
    )
def progress_thread(downloading):
    while downloading == True:
        if os.path.exists(download_path + '/' + s_game + '.zip') == True:
            statinfo = os.stat(download_path + '/' + s_game + '.zip')
            file_size = float(statinfo.st_size)
            numObj = file_size/(pow(1024, 2))
            file_size_converted = toFixed(numObj, 2)
            window.FindElement('log').Update(
                'Downloading ' + s_game + ': ' + str(file_size_converted) + ' MiB'
            )
        else:
            window.FindElement('log').Update(
                'Downloading ' + s_game + ': ' + '0 B'
            )
    #else:
    #    window.FindElement('log').Update(
    #        'Downloading complete!'
    #    )
def progress(downloading):
    threading.Thread(
        target=progress_thread,
        args=(downloading,),
        name='prog',
        daemon=True).start(
    )
# Название игры
s_game = ''

# Тема приложения
sg.theme('darkAmber')

# Ссылки на игры
MXNM_url = "1aSorluHjHQa26GoDii_HSaLQtMyP-DWJ"
ITG_url = ''

# Расположение файла
download_path = ''

# Лейаут основного окна
layout = [
    [sg.Text('Download Folder:', font=('VinnytsiaSansReg')),
     sg.InputText(key='folderbrowse', default_text='', font=('VinnytsiaSansReg'), size=(25,0)),
     sg.FolderBrowse(font=('VinnytsiaSansReg'), enable_events=True),
     sg.Sizer(435, 0),
     sg.Button('i', font=('Grafier'), size=(3, 1))],
    [sg.Text('Selected Game: ' + s_game, size=(100, 1),
             key='game_name_text',
             font=('VinnytsiaSansReg'))
    ],
    [sg.HorizontalSeparator(pad=(100, 10))],
    [sg.Text('Select game: ', font=('VinnytsiaSansReg'))],
    [sg.Listbox(['My X-Mas Nightmare', 'It\'s That Guy!'],
        size=(43, 20),
        enable_events=True,
        key='choose_game',
        font=('VinnytsiaSansReg')),
     sg.Frame(layout=[

     ],title='Game Information', size=(1000, 506), font=('VinnytsiaSansReg'))],
    [sg.Button('Download', size=(15, 5), font=('VinnytsiaSansReg')),
     sg.Text('', key='log', size=(55, 1), font=('VinnytsiaSansReg')),
     sg.Button('Exit', size=(10, 5), font=('VinnytsiaSansReg'))
    ]
]
# Объявление окна
window = sg.Window('John Folsonner\'s Launcher',
                   layout,
                   size=(1280, 720),
                   icon=('./icons/JF_Icon.ico')
                   )
while True:
    # События и значения
    event, values = window.read()
    chGame = values['choose_game']
    print(event, values)
    # Выбор игры
    if chGame == ['My X-Mas Nightmare']:
        s_game = 'My X-Mas Nightmare'
    if chGame == ['It\'s That Guy!']:
        s_game = 'It\'s That Guy'
    # Обновление выбранной игры
    window.FindElement('game_name_text').Update('Selected Game: ' + s_game)
    # Скачивание игры
    if event == 'Download':
        #click()
        print(download_path)
        download_path = window.FindElement('folderbrowse').Get()
        if s_game!='' and window.FindElement('folderbrowse').Get()!='':
            window.FindElement('Download').Update(disabled=True)
            window.FindElement('choose_game').Update(disabled=True)
            window.FindElement('folderbrowse').Update(disabled=True)
            window.FindElement('Browse').Update(disabled=True)
            if s_game == 'My X-Mas Nightmare':
                downloadingFile(MXNM_url)
            elif s_game == 'It\'s That Guy!':
                downloadingFile(ITG_url)
        else:
            window.FindElement('log').Update(
                'Select a game or select the correct installation path'
            )
    #Информационное окно
    if event == 'i':
        #click()
        subprocess.Popen([sys.executable, './JF_Info.py'])
    if event == 'choose_game':
        #click()
        pass
    # Выход из приложения
    if event in (None, 'Exit', 'Cancel'):
        #click()
        time.sleep(1)
        break
