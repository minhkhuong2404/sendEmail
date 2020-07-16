import sys

from bs4 import BeautifulSoup
import requests


def NCT():
    BXH_top = ""
    BXH_top_100 = ""
    sys.stdout = open("NCT.txt", "w")
    URL = "https://www.nhaccuatui.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    BXH = soup.find('ul', class_="notifi new_header")
    BXH_links = BXH.findAll('li')
    for link in BXH_links:
        BXH_link = link.find('a')['href']
        try:
            if BXH_link.split('.')[2] == "com/bai-hat/top-20":
                BXH_top = BXH_link
            elif BXH_link.split('.')[2] == "com/top100/top-100-nhac-tre":
                BXH_top_100 = BXH_link
        except IndexError:
            continue

    BXH_page = requests.get(BXH_top)
    soup2 = BeautifulSoup(BXH_page.content, 'html.parser')
    list_of_top_songs = soup2.find('ul', class_="list_show_chart")
    top_songs = list_of_top_songs.findAll('li')
    print("Top 20 bai hat trong tuan\n")
    for top_song in top_songs:
        link = top_song.find('a')['href']
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        lyrics_container = soup.find("p", class_="pd_lyric trans")

        title = top_song.find('h3', class_="h3")
        print("Title: " + title.text + " by"),
        list_singers = soup.find("div", class_="name_title")
        singers = list_singers.find("h2", class_="name-singer")
        singers_in_song = singers.findAll('a')
        singer_song = ""

        for singer in singers_in_song:
            singer_song += singer.text.strip() + ', '

        correct_singer_song = singer_song.rstrip(', ')
        print(correct_singer_song)
        print(link + '\n')

        print("Lyrics: " + title.text)
        print(lyrics_container.text.strip() + '\n')

    BXH_100_page = requests.get(BXH_top_100)
    soup3 = BeautifulSoup(BXH_100_page.content, 'html.parser')
    list_of_top_100_songs = soup3.find('ul', class_="list_show_chart")
    top_100_songs = list_of_top_100_songs.findAll('li')
    print("Top 100 bai hat\n")
    for top_100_song in top_100_songs:
        link = top_100_song.find('a')['href']
        title = top_100_song.find('h3', class_="h3")
        print("Title: " + title.text)
        print(link + '\n')


if __name__ == '__main__':
    NCT()
