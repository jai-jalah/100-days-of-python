# from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # tags = [print(tag.getText()) for tag in all_anchor_tags]
# # tags = [print(tag.get("href")) for tag in all_anchor_tags]

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))

# name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# print(headings)