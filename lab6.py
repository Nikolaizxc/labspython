class book:
    def __init__(self, name, pages, time_for_page, pics):
        self.name = name
        self.pages = pages
        self.time = time_for_page
        self.pics = pics
    
    def count_time(self):
        return self.pages * self.time
    
        


class encychlopedya(book):
    def __init__(self, name, pages, time_for_page, pics, articles):
        super().__init__(name, pages, time_for_page, pics)
        self.articles = articles
    def count_avg_articles(self):
        if self.pages > 0:

            return self.articles//self.pages
        else:
            return "artichley net!"


class phone_numbers_holder(book):
    def __init__(self, name, pages, time_for_page, pics, numbers):
        super().__init__(name, pages, time_for_page, pics)
        self.numbers = numbers
    def count_numbers(self):
        return self.numbers
    def count_avg_numbers(self):
        if self.pages > 0:

            return self.numbers//self.pages
        else:
            return "nymerov net!"

    def __add__(self, obj):
        if isinstance(obj, int):
            amount = obj
        
            return phone_numbers_holder(self.name, self.pages, self.time, self.pics, self.numbers+amount)
        elif isinstance(obj, phone_numbers_holder):
            return phone_numbers_holder(f"{self.name}, {obj.name}", self.pages+obj.pages, self.time+obj.time, self.pics+obj.pics, self.numbers+obj.numbers)

ph_h = phone_numbers_holder("tele", 67, 11, 12, 522)
ph_h2 = phone_numbers_holder("phones", 67, 11, 12, 50)
ph_h+=ph_h2
print(ph_h.name)
