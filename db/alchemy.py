from multiprocessing.sharedctypes import synchronized
from struct import Struct
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://root:tiger@localhost:5432/example_db' #ссылка на базу данных
engine = create_engine(db_url, echo=False) #переменная при использовании которой создается подключение к базе
Base = declarative_base() #создаем обьект для работы с базой

class User(Base): #создаем класс через который будем обращаться к столбцам
    __tablename__ = 'users'

    #прописываем столбцы которые у нас будут в таблице
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    fullname = Column(String(100))
    nickname = Column(String(100))

    def __repr__(self) -> str:
        return f"<User: {self.name}, {self.fullname}, {self.nickname}>"

#cоздаем таблицу в базе данных
Base.metadata.create_all(engine)

#создаем обьект для создания сессии подключения к базе данных
Session = sessionmaker(bind=engine)

#создаем экземпляр класса Session при помощи него будем общатся с базой
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='Kruelty875')

#добавляем обьект в сессию
session.add(ed_user)

#добавляем обьекты из сессии в базу
session.commit()

#добавим в сессию сразу много обьектов
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flinstone', nickname='freddy')
    ])

""" поменяем nickname в обьекте ed_user,
    однако так как предыдущий обьекит уже записан
    у нас будет записан новый обьект
    ed_user = User(name='ed', fullname='Ed Jones', nickname='eddie')
"""
ed_user.nickname = 'eddie' 

#посмотрим какие обьекты были изменены в сессии
session.dirty

#посмотрим какие новые обьекты были добавлены в сессию
session.new

#наконец добавляем обьекты в базу фиксируя транзакцию
session.commit()

#посмотри все обьекты в таблицу users
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname, instance.nickname)

#посмотрим конкретные обьекты в таблице
for name, fullname in session.query(User.name, User.fullname):
    if name == 'wendy' and fullname == 'Wendy Williams':
        print(name, fullname)

#посмотрим конкретный обьект таблицы средствами SQLAlchemy
for name in session.query(User.name).filter_by(name='fred'):
    print(name)

#давайте посмотрим какой никнейм у Mary Contrary
for nickname in session.query(User.nickname).filter_by(fullname='Mary Contrary'):
    print(nickname)

#ещё один вариант просмотра конкретного обьекта таблицы с более гибкими настройками
for nickname in session.query(User.nickname).filter(User.fullname=='Mary Contrary'):
    print(nickname)

#посморим конкретный столбец в таблице
for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

#сделаем срез по id и посмотрим содержимое
for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

#мария решила поменять никнейм во имя луны, сразу же и проверим поменялся ли
for new in session.query(User).filter(User.fullname=='Mary Contrary'):
    new.nickname = 'Tirend'
    session.commit()
    for new in session.query(User).filter(User.fullname=='Mary Contrary'):
        print(new.nickname)

#удалить строку из таблицы
data = session.query(User).filter(User.name == 'fred')
data.delete()
session.commit()