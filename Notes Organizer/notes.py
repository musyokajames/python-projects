class Notes():
    def __init__(self,title,content,category):
        self.title = title
        self.content = content
        self.category = category
    
    def __str__(self):
        return f"----------\nTITLE:{self.title}\nCONTENT:{self.content}\n"