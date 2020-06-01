from requests_html import HTMLSession


class Novel:
    def __init__(self,name,author,category,status,link) -> None:
        self.name = name
        self.author = author
        self.category = category
        self.status = status
        self.link = link

    def __repr__(self):
        return f"{self.name} is written by {self.author} with link {self.link}. Category is {self.category} and status is {self.status}"

if __name__ == "__main__":
    s = HTMLSession()
    base_url = "https://www.xbiquge.cc/modules/article/search.php?searchkey=%BF%EC%B4%A9"
    r = s.get(url = base_url)
    if r.status_code == 200:
        lis = r.html.xpath("//div[@class = 'novelslistss']/li")
        novel_list = []
        for li in lis:
            name = li.xpath("//span[@class='s2']/a/text()")[0]
            author = li.xpath("//span[@class='s4']/text()")[0]
            category = li.xpath("//span[@class='s1']/text()")[0]
            status = li.xpath("//span[@class='s7']/text()")[0]
            link = li.xpath("//span[@class='s2']/a/@href")[0]
            current_novel = Novel(name,author,category,status,link)
            novel_list.append(current_novel)

        print(novel_list)

        # xpath和css selector两种
