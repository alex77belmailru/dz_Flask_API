class Event:
    def __init__(self, date: str, title: str, text: str, _id: str = None):
        self._id = _id
        self.date = date
        self.title = title
        self.text = text

    def __str__(self):
        return f'{self._id}|{self.date}|{self.title}|{self.text}' \
            if self._id else f'{self.date}|{self.title}|{self.text}'




