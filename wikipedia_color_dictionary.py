wikipedia_color_urls = ['https://en.m.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F', 'https://en.m.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M', 'https://en.m.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z']

color_dict = {}
for url in wikipedia_color_urls:
    request = requests.get(url)
    color_soup = BeautifulSoup(request.content, 'html')
    table = color_soup.find('tbody')
    rows = table.find_all('tr')[1:]
    for row in rows:
        color_dict[clean_string(row.find('th').text)] = row.find('td').text.strip()
    
    
with open('data/color_dict.json','w') as file:
    json.dump(color_dict, file)