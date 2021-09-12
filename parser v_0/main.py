import cianparser

data = cianparser.parse(offer="sale", accommodation="flat", location="Москва", rooms="all", start_page=1, end_page=2)

print(data[0])