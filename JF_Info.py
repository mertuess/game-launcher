import PySimpleGUI as sg
import webbrowser

sg.theme('darkAmber')

layout = [
    [sg.Text('John Folsonner\'s Launcher', font=('VinnytsiaSansReg'))],
    [sg.HorizontalSeparator()],
    [sg.Text('# scripts by John Folsonner\n# create on python 3.7\n# contact with me:', font=('VinnytsiaSansReg'))],
    [sg.Text('VK group', font=('VinnytsiaSansReg'), text_color=('#00C0FF'), enable_events=True, key='group'),
     sg.Text('Discord', font=('VinnytsiaSansReg'), text_color=('#00C0FF'), enable_events=True, key='discord'),
     sg.Text('Twitter', font=('VinnytsiaSansReg'), text_color=('#00C0FF'), enable_events=True, key='twitter')
    ],
    [sg.Image('./images/python_icon.png', size=(50, 50)),
     sg.Image('./images/JF_Launcher_Icon.png', size=(50, 50)),
     sg.VerticalSeparator(),
     sg.Image('./images/vk_icon.png', size=(50, 50)),
     sg.Image('./images/discord_icon.png', size=(50, 50)),
     sg.Image('./images/twitter_icon.png', size=(50, 50))
    ],
    [sg.Text('version: dev0.1', font=('VinnytsiaSansReg', [10]))],
]

window = sg.Window('About...', layout, icon=('./icons/JF_InfoIcon.ico'))
while True:
    # Слежка за действиями в программе
    event, values = window.read()
    if event == 'group':
        webbrowser.open('https://vk.com/deadsoulcompany') # VK
    if event == 'discord':
        webbrowser.open('https://discord.gg/UU2pjXy') # discord
    if event == 'twitter':
        webbrowser.open('https://twitter.com/exxodvsTwix') # twitter
    # Выход из приложения
    if event in (None, 'Exit', 'Cancel'):
        break