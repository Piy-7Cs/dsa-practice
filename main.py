

data = {"data":[{"node":{"id":32281,"title":"Naruto","main_picture":{"medium":"https://cdn.myanimelist.net/images/anime/5/87048.webp","large":"https://cdn.myanimelist.net/images/anime/5/87048l.webp"}}},
{"node":{"id":54857,"title":"one piece","main_picture":{"medium":"https://cdn.myanimelist.net/images/anime/1706/144725.jpg","large":"https://cdn.myanimelist.net/images/anime/1706/144725l.jpg"}}},
{"node":{"id":59978,"title":"Sousou no Frieren 2nd Season","main_picture":{"medium":"https://cdn.myanimelist.net/images/anime/1921/154528.jpg","large":"https://cdn.myanimelist.net/images/anime/1921/154528l.jpg"}}}],
"paging":{}}




arr = list(data.get("data"))

def get_titles(arr):
    item = arr.get("node")
    title = item.get("title")
    return title
    

x = map(get_titles, arr)

titles = ', '.join(str(element) for element in x)


print(list(x))
print(titles)

