from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):  # классы и модели называть в единственном числе
    # это док стринг
    """ Таблица "Товар"

    id
    Название товара
    Ссылка на товар
    Цена товара
    Дава и время создания записи
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)  # в поле будет записывать время и дата создание записи

    # для описания это будет выводиться в первую очередь
    def __str__(self):
        return self.title


class WishList(models.Model):
    """ Таблица "Лист Желаемых подарков"
    
    id
    owner -
    products - ManyToMany
    is_hidden - bool - кто может видеть этот виш лист
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product) # создает промежуточную таблицу для реляционной бд
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
