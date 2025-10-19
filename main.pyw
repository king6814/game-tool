import tkinter as tk
from tkinter import ttk
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
from subprocess import Popen
import webbrowser
import requests
from bs4 import BeautifulSoup
import os
import datetime

# Tkinter 애플리케이션 생성
app = tk.Tk()
app.title("게임 툴 v1.3")
app.geometry('336x400')

element={
    'choose_area':[],
    'quick_start_area':[]
}

headers = {'User-Agent' : 'Mozilla/5.0'}

def get_new_Genshin_version_image():
    response = requests.get('https://namu.wiki/w/%EC%9B%90%EC%8B%A0/%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8',headers=headers)
    soup=BeautifulSoup(response.text, 'html.parser').find_all('table')
    
    soup=soup[64].find_all('img')
    img_link=soup[1]['data-src']
    
    img_url = 'https:' + img_link
    img_response = requests.get(img_url, headers=headers)

    save_path = os.path.join('data', f'Genshin_recent_version_image.webp')
    with open(save_path, 'wb') as f:
        f.write(img_response.content)

    choose_main_display_game('Genshin')


def get_new_StarRail_version_image():
    response = requests.get('https://namu.wiki/w/%EB%B6%95%EA%B4%B4:%20%EC%8A%A4%ED%83%80%EB%A0%88%EC%9D%BC/%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8',headers=headers)
    soup=BeautifulSoup(response.text, 'html.parser').find_all('img')
    soup=list(map(str,soup))
    
    count=0
    for i in soup:
        if ' src="//i.namu.wiki' in i and 'webp"' in i:
            if count==1:
                img_link=i[i.index('i.namu') : i.find('webp"')+4]
                break
            else:
                count+=1

    img_url = 'https://' + img_link
    img_response = requests.get(img_url, headers=headers)

    save_path = os.path.join('data', 'StarRail_recent_version_image.webp')
    with open(save_path, 'wb') as f:
        f.write(img_response.content)

    choose_main_display_game('StarRail')


def get_new_Honkai_version_image():
    response = requests.get('https://namu.wiki/w/%EB%B6%95%EA%B4%B43rd/%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8',headers=headers)
    soup=BeautifulSoup(response.text, 'html.parser').find_all('img')
    soup=list(map(str,soup))
    
    count=0
    for i in soup:
        if ' src="//i.namu.wiki' in i and 'webp"' in i:
            if count==1:
                img_link=i[i.index('i.namu') : i.find('webp"')+4]
                break
            else:
                count+=1

    img_url = 'https://' + img_link
    img_response = requests.get(img_url, headers=headers)

    save_path = os.path.join('data', 'Honkai_recent_version_image.webp')
    with open(save_path, 'wb') as f:
        f.write(img_response.content)

    choose_main_display_game('Honkai')


def destroy_element_in(key):
    for i in range(len(element[key])):
        element[key][-1].destroy()
        del element[key][-1]

def open_game_exe(game_name):
    
    game_path={
        'Minecraft':r"C:\\XboxGames\\Minecraft Launcher\\Content\\gamelaunchhelper.exe",
        'Genshin':r"C:\\Program Files\\HoYoPlay\\games\\Genshin Impact game\\GenshinImpact.exe",
        'StarRail':r"C:\\Program Files\\HoYoPlay\\games\\Star Rail Games\\StarRail.exe",
        'Honkai':r"C:\\Program Files\\HoYoPlay\\games\\Honkai Impact 3rd kr game\\BH3.exe",
        'nikke':r"C:\\NIKKE\\Launcher\\nikke_launcher.exe",
        'lol':r"C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
    }
    Popen([
        "powershell",
        "Start-Process",
        f"'{game_path[game_name]}'",
        "-Verb",
        "RunAs"
        ], shell=True)

def chang_wiki_to(wiki_name):
    if wiki_name=='namu':
        element['quick_start_area'][1].configure(background='#0DA77F')
        element['quick_start_area'][2].configure(text='변경 : 호요위키',command=lambda : chang_wiki_to('hoyo'),background='#5E80FF')
    elif wiki_name=='hoyo':
        element['quick_start_area'][1].configure(background='#5E80FF')
        element['quick_start_area'][2].configure(text='변경 : 나무위키',command=lambda : chang_wiki_to('namu'),background='#0DA77F')

    element['quick_start_area'][1].wiki=wiki_name
    
def open_website(game,Kategorie):
    wiki={
        'Genshin':{
            'character' :('genshin/aggregate/2','%EC%9B%90%EC%8B%A0/%EC%BA%90%EB%A6%AD%ED%84%B0'),
            'weapon'    :('genshin/aggregate/4','%EC%9B%90%EC%8B%A0/%EB%AC%B4%EA%B8%B0/%ED%95%9C%EC%86%90%EA%B2%80'),
            'artifacts' :('genshin/aggregate/5','%EC%9B%90%EC%8B%A0/%EC%84%B1%EC%9C%A0%EB%AC%BC')},
        'StarRail':{
            'character' :('hsr/aggregate/104','%EB%B6%95%EA%B4%B4:%20%EC%8A%A4%ED%83%80%EB%A0%88%EC%9D%BC/%EC%BA%90%EB%A6%AD%ED%84%B0'),
            'weapon'    :('hsr/aggregate/107','%EB%B6%95%EA%B4%B4:%20%EC%8A%A4%ED%83%80%EB%A0%88%EC%9D%BC/%EA%B4%91%EC%B6%94/%ED%8C%8C%EB%A9%B8'),
            'artifacts' :('hsr/aggregate/108','%EB%B6%95%EA%B4%B4:%20%EC%8A%A4%ED%83%80%EB%A0%88%EC%9D%BC/%EC%9C%A0%EB%AC%BC')}
            
            }
    if element['quick_start_area'][1].wiki == 'hoyo':
        webbrowser.open('https://wiki.hoyolab.com/pc/'+wiki[game][Kategorie][0])
    elif element['quick_start_area'][1].wiki == 'namu':
        webbrowser.open('https://namu.wiki/w/'+wiki[game][Kategorie][1])

def open_youtube(game):
    if game in ('Genshin','StarRail'):
        youtuber = element['quick_start_area'][8].get()
    elif game in ('Honkai',):
        youtuber = element['quick_start_area'][3].get()
    elif game in ('Minecraft',):
        youtuber = element['quick_start_area'][2].get()
    
    youtuber_link={
        'Genshin':{
            '원신':'@Genshinimpact_KR',
            '상덕':'@Sangduck',
            '상덕 - 다시보기':'@sangduck2_replay',
            '최슬':'@%EC%B5%9C%EC%8A%AC',
            '몽키매직':'@MonkeyMagic',
            '호요믹스':'channel/UC6pM_fjt__KO-KS61goPlGQ',
            '원신 - 영어':'@GenshinImpact',
            '원신 - 일본':'@Genshin_JP',
            '원신 - 중국':'@Genshinimpact_ZH'},
        
        'StarRail':{
            '스타레일':'@Honkaistarrail_kr',
            '상덕':'@Sangduck',
            '상덕 - 다시보기':'@sangduck2_replay',
            '최슬':'@%EC%B5%9C%EC%8A%AC',
            '몽키매직':'@MonkeyMagic',
            '호요믹스':'channel/UC6pM_fjt__KO-KS61goPlGQ',
            '원신 - 영어':'@HonkaiStarRail',
            '원신 - 일본':'@Houkaistarrail_jp',
            '원신 - 중국':'@HonkaiStarRail_ZH'},
        
        'Honkai':{
            '붕괴3rd':'@HonkaIimpact3rd_KR',
            '상덕':'@Sangduck',
            '상덕 - 다시보기':'@sangduck2_replay',
            '호요믹스':'channel/UC6pM_fjt__KO-KS61goPlGQ',},
        'Minecraft':{
            '뚜뚜형':'@%EB%9A%9C%EB%9A%9C%ED%98%95',
            '스냅제이':'@%EC%8A%A4%EB%83%85%EC%A0%9C%EC%9D%B4',
            'theysix':'@TheySix',}
            }
    
    if youtuber != '유튜브':
        webbrowser.open('https://www.youtube.com/'+youtuber_link[game][youtuber])
        if game in ('Genshin','StarRail'):
            element['quick_start_area'][8].current(0)
        elif game in ('Honkai',):
            element['quick_start_area'][3].current(0)
        elif game in ('Minecraft',):
            element['quick_start_area'][2].current(0)

def open_etc_site(game):
    if game in ('Genshin','StarRail'):
        site_name = element['quick_start_area'][9].get()
    elif game in ('Minecraft',):
        site_name = element['quick_start_area'][3].get()
    site_link={
        'Genshin':{
            '호요랩 - 전적' : 'https://act.hoyolab.com/app/community-game-records-sea/',
            '아카샤':'https://akasha.cv/artifacts',
            '페이몬 moe':'https://paimon.moe/'},
        
        'StarRail':{
            '호요랩 - 전적' : 'https://act.hoyolab.com/app/community-game-records-sea/rpg/'},
            
        'Minecraft':{
            'better_F3':'https://modrinth.com/mod/betterf3/versions',
            'fabric_api':'https://modrinth.com/mod/fabric-api/versions',
            'flashback':'https://modrinth.com/mod/flashback/versions',
            'litematica':'https://modrinth.com/mod/litematica/versions',
            'malilib':'https://modrinth.com/mod/malilib/versions',
            'no_more_useless_key':'https://modrinth.com/mod/nmuk/versions',
            'shulkerbox_tooltip':'https://modrinth.com/mod/shulkerboxtooltip/versions',
            'sodium':'https://modrinth.com/mod/sodium/versions',
            'block_entity_rendering':'https://modrinth.com/mod/beer/versions',}
            
            }
    if site_name != '기타 사이트' and site_name != '모드':
        webbrowser.open(site_link[game][site_name])
        if game in ('Genshin','StarRail'):
            element['quick_start_area'][9].current(0)
        elif game in ('Minecraft',):
            element['quick_start_area'][3].current(0)

def choose_main_display_game(game):

    destroy_element_in('quick_start_area')

    image=ImageTk.PhotoImage(Image.open(f"data\\{game}_recent_version_image.webp").resize((300, 180)))
    button=tk.Button(app,image=image,command=lambda g=game: open_game_exe(g))
    button.image=image
    button.grid(row=1,column=0,columnspan=6,pady=10)
    element['quick_start_area'].append(button)

    if game == 'Genshin':
        game_wiki=tk.Frame(app,background='#5E80FF',relief="solid")
        game_wiki.grid(row=2,columnspan=6,column=0)
        game_wiki.wiki='hoyo'
        element['quick_start_area'].append(game_wiki)

        button=tk.Button(game_wiki,text='변경 : 나무위키',background='#0DA77F',command=lambda : chang_wiki_to('namu'))
        button.grid(row=0,column=0,sticky='w',pady=5,padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='캐릭터',command=lambda : open_website(game,'character'))
        button.grid(row=0,column=2,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='무기',command=lambda : open_website(game,'weapon'))
        button.grid(row=0,column=3,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='성유물',command=lambda : open_website(game,'artifacts'))
        button.grid(row=0,column=4,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        game_tool=tk.Frame(app,relief="solid")
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        image=ImageTk.PhotoImage(Image.open(f"data\\호요랩.webp").resize((25, 25)))
        button=tk.Button(game_tool,image=image,command=lambda : webbrowser.open('https://www.hoyolab.com/home'),relief="raised")
        button.grid(row=0,column=0,padx=5,pady=5)
        button.image=image
        element['quick_start_area'].append(button)

        tk.Button(game_tool,text='월드맵(공식)',command=lambda : webbrowser.open('https://act.hoyolab.com/ys/app/interactive-map')).grid(row=0,column=1,padx=5,pady=5)
        tk.Button(game_tool,text='월드맵(비공식)',command=lambda : webbrowser.open('https://genshin-impact-map.appsample.com')).grid(row=0,column=2,padx=5)
        tk.Button(game_tool,text='리딤입력',command=lambda : webbrowser.open('https://genshin.hoyoverse.com/ko/gift')).grid(row=0,column=3,padx=5)

        combobox = ttk.Combobox(app, values=['유튜브', '원신','상덕','상덕 - 다시보기','최슬','몽키매직','호요믹스','원신 - 영어','원신 - 일본','원신 - 중국'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=0)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_youtube(game))

        element['quick_start_area'].append(combobox)

        combobox = ttk.Combobox(app, values=['기타 사이트', '호요랩 - 전적','아카샤','페이몬 moe'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=3)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_etc_site(game))
        element['quick_start_area'].append(combobox)

        today = datetime.date.today()
        if 1 < today.day <= 16:
            text = f'나선 초기화 D-{16 - today.day}'
            if 16-today.day <= 3:
                color='#ec1c24'
            else:
                color='#0ed145'
        elif today.day == 1:
            text = f'환상극 초기화 D-0'
            color='#ec1c24'
        else:
            if today.month != 12:
                next_reset = datetime.date(today.year, today.month + 1, 1)
            else:
                next_reset = datetime.date(today.year + 1, 1, 1)
            delta = (next_reset - today).days
            text = f'환상극 초기화 D-{delta}'
            if delta <= 3:
                color='#ec1c24'
            else:
                color='#0ed145'

        button=tk.Button(app,text=text,background=color)
        button.grid(row=5,column=0,padx=5,pady=5,columnspan=3)
        element['quick_start_area'].append(button)

        button=tk.Button(app,text='배너 이미지 갱신',command=get_new_Genshin_version_image)
        button.grid(row=5,column=4,padx=5,columnspan=2)
        element['quick_start_area'].append(button)

    if game == 'StarRail':
        game_wiki=tk.Frame(app,background='#5E80FF',relief="solid")
        game_wiki.grid(row=2,columnspan=6,column=0)
        game_wiki.wiki='hoyo'
        element['quick_start_area'].append(game_wiki)

        button=tk.Button(game_wiki,text='변경 : 나무위키',background='#0DA77F',command=lambda : chang_wiki_to('namu'))
        button.grid(row=0,column=0,sticky='w',pady=5,padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='캐릭터',command=lambda : open_website(game,'character'))
        button.grid(row=0,column=2,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='광추',command=lambda : open_website(game,'weapon'))
        button.grid(row=0,column=3,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        button=tk.Button(game_wiki,text='유물',command=lambda : open_website(game,'artifacts'))
        button.grid(row=0,column=4,sticky='e',padx=5)
        element['quick_start_area'].append(button)

        game_tool=tk.Frame(app,relief="solid")
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        image=ImageTk.PhotoImage(Image.open(f"data\\호요랩.webp").resize((25, 25)))
        button=tk.Button(game_tool,image=image,command=lambda : webbrowser.open('https://www.hoyolab.com/home'),relief="raised")
        button.grid(row=0,column=0,padx=5,pady=5)
        button.image=image
        element['quick_start_area'].append(button)

        tk.Button(game_tool,text='월드맵',command=lambda : webbrowser.open('https://act.hoyolab.com/sr/app/interactive-map/#/map/')).grid(row=0,column=1,padx=5,pady=5)
        tk.Button(game_tool,text='육성추천',command=lambda : webbrowser.open('https://act.hoyolab.com/sr/event/cultivation-tool/#/tools/suggestion')).grid(row=0,column=2,padx=5)
        tk.Button(game_tool,text='리딤입력',command=lambda : webbrowser.open('https://hsr.hoyoverse.com/gift?lang=ko-kr')).grid(row=0,column=3,padx=5)

        combobox = ttk.Combobox(app, values=['유튜브', '스타레일','상덕','상덕 - 다시보기','최슬','몽키매직','호요믹스','스타레일 - 영어','스타레일 - 일본','스타레일 - 중국'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=0)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_youtube(game))

        element['quick_start_area'].append(combobox)

        combobox = ttk.Combobox(app, values=['기타 사이트', '호요랩 - 전적'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=3)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_etc_site(game))
        element['quick_start_area'].append(combobox)

        today = datetime.date.today()
        events = [
            ("혼돈", datetime.date(2025, 9, 15)),
            ("허구", datetime.date(2025, 10, 14)),
            ("종말", datetime.date(2025, 9, 29)),
            ("이상중재", datetime.date(2025, 9, 24))]

        next_event_name = ''
        next_event_day = 43

        for name, start_date in events:
            delta_days = (today - start_date).days
            if delta_days % 42==0:
                days_left = 0
            else:
                days_left = 43 - delta_days % 42

            if days_left < next_event_day:
                next_event_name = name
                next_event_day = days_left

        text = f'{next_event_name} 초기화 D-{next_event_day}'
        if next_event_day <= 3:
            color = '#ec1c24' 
        else:
            color = '#0ed145'

        button=tk.Button(app,text=text,background=color)
        button.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

        button=tk.Button(app,text='배너 이미지 갱신',command=get_new_StarRail_version_image)
        button.grid(row=5,column=4,padx=5,columnspan=2)
        element['quick_start_area'].append(button)

    if game == 'Honkai':

        game_tool=tk.Frame(app,relief="solid")
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        image=ImageTk.PhotoImage(Image.open(f"data\\호요랩.webp").resize((25, 25)))
        button=tk.Button(game_tool,image=image,command=lambda : webbrowser.open('https://www.hoyolab.com/home'),relief="raised")
        button.grid(row=0,column=0,padx=5,pady=5)
        button.image=image
        element['quick_start_area'].append(button)

        tk.Button(game_tool,text='전적',command=lambda : webbrowser.open('https://act.hoyolab.com/app/community-game-records-sea/bh3/')).grid(row=0,column=1,padx=5,pady=5)
        tk.Button(game_tool,text='낙원 공략',command=lambda : webbrowser.open('https://arca.live/b/hk3rd?category=%EC%99%95%EC%84%B8%EB%82%99%ED%86%A0')).grid(row=0,column=2,padx=5)

        combobox = ttk.Combobox(game_tool, values=['유튜브', '붕괴3rd','상덕','상덕 - 다시보기','호요믹스'], state="readonly",width=15)
        combobox.grid(row=0,columnspan=3,column=3)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_youtube(game))
        element['quick_start_area'].append(combobox)

        button=tk.Button(app,text='배너 이미지 갱신',command=get_new_Honkai_version_image)
        button.grid(row=5,column=4,padx=5,columnspan=2)
        element['quick_start_area'].append(button)

    if game == 'Minecraft':
        game_tool=tk.Frame(app,relief="solid")
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        tk.Button(game_tool,text='주민 거래',command=lambda : webbrowser.open('https://minecraft.fandom.com/ko/wiki/%EA%B1%B0%EB%9E%98#%EA%B0%91%EC%98%B7_%EC%A0%9C%EC%A1%B0%EC%9D%B8')).grid(row=0,column=0,padx=5,pady=5)
        tk.Button(game_tool,text='청크 배이스',command=lambda : webbrowser.open('https://www.chunkbase.com/apps/')).grid(row=0,column=1,padx=5)
        tk.Button(game_tool,text='지도 변환',command=lambda : webbrowser.open('https://rebane2001.com/mapartcraft/')).grid(row=0,column=2,padx=5)
        tk.Button(game_tool,text='바닐라 트윅스',command=lambda : webbrowser.open('https://vanillatweaks.net/picker/resource-packs/')).grid(row=0,column=3,padx=5)
        
        tk.Button(game_tool,text='마크 폴더 열기',command=lambda : os.startfile(os.path.realpath('C:\\Users\\a9894\\AppData\\Roaming\\.minecraft')),width=25).grid(row=1,column=0,padx=5,pady=5,columnspan=4)

        combobox = ttk.Combobox(app, values=['유튜브', '뚜뚜형','스냅제이','theysix'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=0)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_youtube(game))

        element['quick_start_area'].append(combobox)

        combobox = ttk.Combobox(app, values=['모드', 'better_F3','fabric_api','flashback','litematica','malilib','no_more_useless_key','shulkerbox_tooltip','sodium','block_entity_rendering'], state="readonly",width=15)
        combobox.grid(row=4,columnspan=3,column=3)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", lambda event: open_etc_site(game))
        element['quick_start_area'].append(combobox)

    if game == 'nikke':
        game_tool=tk.Frame(app,relief="solid", )
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        tk.Button(game_tool,text='공식 유튜브',command=lambda : webbrowser.open('https://www.youtube.com/@nikkekr')).grid(row=0,column=0,padx=5,pady=5)
        tk.Button(game_tool,text='네이버 라운지',command=lambda : webbrowser.open('https://game.naver.com/lounge/nikke/home')).grid(row=0,column=1,padx=5)
        tk.Button(game_tool,text='blablalink',command=lambda : webbrowser.open('https://www.blablalink.com/?from=nikke_sns&scene=outer_game')).grid(row=0,column=2,padx=5)
        tk.Button(game_tool,text='nikke704',command=lambda : webbrowser.open('https://nikke704.oopy.io/1a34790a-0529-811e-a282-ef83d799a3f6')).grid(row=0,column=3,padx=5)
        
        tk.Button(game_tool,text='고뇨',command=lambda : webbrowser.open('https://www.youtube.com/@gonyo1')).grid(row=1,column=0,padx=5,columnspan=2)
        tk.Button(game_tool,text='순망',command=lambda : webbrowser.open('https://www.youtube.com/@sunmang14')).grid(row=1,column=2,padx=5,columnspan=2)
        
    if game == 'lol':
        game_tool=tk.Frame(app,relief="solid", )
        game_tool.grid(row=3,columnspan=6,column=0)
        element['quick_start_area'].append(game_tool)

        tk.Button(game_tool,text='opgg',command=lambda : webbrowser.open('https://op.gg/ko')).grid(row=0,column=0,padx=5,pady=5)
        tk.Button(game_tool,text='fow',command=lambda : webbrowser.open('https://www.fow.lol')).grid(row=0,column=1,padx=5)
        tk.Button(game_tool,text='lol.ps',command=lambda : webbrowser.open('https://lol.ps/')).grid(row=0,column=2,padx=5)
        tk.Button(game_tool,text='deeplol',command=lambda : webbrowser.open('https://www.deeplol.gg/')).grid(row=0,column=3,padx=5)
        tk.Button(game_tool,text='your.gg',command=lambda : webbrowser.open('https://your.gg/ko/kr/home')).grid(row=0,column=4,padx=5)
        

def main_start():
    

    game_list=('Genshin','StarRail','Honkai','Minecraft','nikke','lol')
    for i,game in enumerate(game_list):
        image=ImageTk.PhotoImage(Image.open(f"data\\{game} icon.png").resize((50, 50)))
        button=tk.Button(app,image=image,command=lambda g = game: choose_main_display_game(g))
        button.image=image
        button.grid(row=0,column=i)
        element['choose_area'].append(button)

#######################################################################################


# 처음 실행 시 창 숨기기
app.withdraw()

def quit_window():
    icon.visible = False
    icon.stop()
    app.quit()
    os._exit(os.EX_OK)

def show_window():
    app.after(0, app.deiconify)

def withdraw_window():
    app.withdraw()

main_start()
# 트레이 아이콘 이미지 로드
image = Image.open("data\\게임.ico")

# 트레이 메뉴 구성
menu = (item('Show', show_window), item('종료', quit_window))
icon = pystray.Icon("name", image, "game_assistant", menu)
icon.run_detached()

# 창 닫기 버튼을 눌렀을 때 숨기기
app.protocol('WM_DELETE_WINDOW', withdraw_window)

# Tkinter 이벤트 루프 시작
app.mainloop()
