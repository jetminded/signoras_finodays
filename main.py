from bs4 import BeautifulSoup
import requests
result = []
for j in range(1, 55):
    url = f"https://www.cian.ru/cat.php?deal_type=sale&demolished_in_moscow_programm=0&engine_version=2&object_type%5B0%5D=1&offer_type=flat&p={j}&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1"
    page = requests.get(url)
    print('Page status:', page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_offers = soup.find_all('a', class_='_93444fe79c--link--39cNw')
    for offer in all_offers:
        try:
            offer_page = requests.get(offer.get('href'))
            offer_soup = BeautifulSoup(offer_page.text, 'html.parser')
            # обязательная группа фичей
            total_square = offer_soup('div', class_='a10a3f92e9--info-value--18c8R')[0].text.split()[0]
            kitchen_square = offer_soup('div', class_='a10a3f92e9--info-value--18c8R')[2].text.split()[0]
            floor = offer_soup('div', class_='a10a3f92e9--info-value--18c8R')[3].text.split()[0]
            amount_of_floors = offer_soup('div', class_='a10a3f92e9--info-value--18c8R')[3].text.split()[2]
            year_of_building = offer_soup('div', class_='a10a3f92e9--info-value--18c8R')[4].text.split()[0]
            price = offer_soup('span', itemprop='price')[0].get('content')
            underground_station = offer_soup('a', class_='a10a3f92e9--underground_link--AzxRC')[0].text
            time_to_walk = offer_soup('span', class_='a10a3f92e9--underground_time--1fKft')[0].text.split()[1]
            # допольнительная группа фичей
            i = 0
            side_info = offer_soup('span', class_='a10a3f92e9--name--3bt8k')
            height = -1
            renovation = -1
            wall_material = -1
            view = -1
            amount_of_balcony = -1
            for info in side_info:
                if info.text == 'Высота потолков':
                    height = offer_soup('span', class_='a10a3f92e9--value--3Ftu5')[i].text.split()[0]
                if info.text == 'Ремонт':
                    renovation = offer_soup('span', class_='a10a3f92e9--value--3Ftu5')[i].text
                if info.text == 'Материал стен':
                    wall_material = offer_soup('span', class_='a10a3f92e9--value--3Ftu5')[i].text
                if info.text == 'Вид из окон':
                    view = offer_soup('span', class_='a10a3f92e9--value--3Ftu5')[i].text
                if info.text == 'Балкон/лоджия':
                    amount_of_balcony = offer_soup('span', class_='a10a3f92e9--value--3Ftu5')[i].text.split()[0]
                i += 1
            flat = {}
            flat['underground_station'] = underground_station
            flat['time_to_walk'] = time_to_walk
            flat['price'] = price
            flat['total_square'] = total_square
            flat['kitchen_square'] = kitchen_square
            flat['floor'] = floor
            flat['amount_of_floors'] = amount_of_floors
            flat['year_of_building'] = year_of_building
            flat['height'] = height
            flat['renovation'] = renovation
            flat['wall_material'] = wall_material
            flat['view'] = view
            flat['amount_of_balcony'] = amount_of_balcony
            result.append(flat)
        except:
            print('lol')
print(result)
print(len(result))

