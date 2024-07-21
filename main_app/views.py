from django.shortcuts import render


class DateTime:
    year: str
    month: str
    day: str
    hour: str
    minute: str
    second: str

    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.year}::{self.month}::{self.day} {self.hour}:{self.minute}:{self.second}'


class News:
    id: int
    title: str
    desc: str
    upload_time: DateTime
    is_checked: bool

    def __init__(self, id, title, desc, upload_time, is_checked):
        self.id = id
        self.title = title
        self.desc = desc
        self.upload_time = upload_time
        self.is_checked = is_checked


t1 = DateTime('2002', '02', '02', '10', '20', '30')
t2 = DateTime('2003', '03', '03', '11', '40', '40')
t3 = DateTime('2004', '04', '04', '12', '50', '50')

n1 = News(1, 'new 1', 'desc 1', t1, True)
n2 = News(2, 'new 2', 'desc 2', t2, True)
n3 = News(3, 'new 3', 'desc 3', t3, False)

data = {
    'news': [n1, n2, n3],
}


def index(request):
    return render(request, 'index.html', context=data)


def edu(request):
    return render(request, 'edu/index.html')
