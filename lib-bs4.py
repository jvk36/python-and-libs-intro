from bs4 import BeautifulSoup


with open("./templates/website.html", encoding="utf-8") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)  # prints the title tag - <title>Angela's Personal Site</title>
# print(soup.title.name) # prints title name - title
# print(soup.title.string) # prints what is inside the tag - Angela's Personal Site
# print(soup.prettify())

all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)  # prints all the anchor tags as a list
for tag in all_anchor_tags:
    # print(tag.getText())  # prints each of the anchor tags.
    # print(tag.get("href"))  # prints each of the links indicated in href
    pass

para = soup.find("p")
# print(para)

# searching based on attribute
# ******** NOTICE class attribute is given as class_ as class is a reserved word.
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading) # prints the h3 tag with given class
# print(section_heading.get("class"))  # prints - heading

# CSS SELECTORS CAN BE USED TO GET TO THE TAG YOU ARE LOOKING FOR
company_url = soup.select_one("p em strong a")
all_url_tags = soup.select("a")
# print(company_url)
# print(all_url_tags)
name = soup.select_one("#name")  # print the tag with the id attribute "name"
# print(name)
headings = soup.select(".heading")
print(headings) # print a list of tags with class attribute "heading"

