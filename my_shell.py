from shop.models import Item, Purchase
from django.utils import timezone

i = Item(name="Notebook Lennovo", price=1500)
i.save()
i1 = Item(name="Notebook Asus", price=1000)
i1.save()
i2 = Item(name="Notebook Acer", price=800)
i2.save()
i3 = Item(name="TV Samsung", price=2000)
i3.save()
i4 = Item(name="Iphone 13", price=1500)
i4.save()


i.purchase_set.create(name="Попов Сергей Владимирович", age=41, data_purchase=timezone.now())
i.purchase_set.create(name="Иванов Андрей Иванович", age=39, data_purchase=timezone.now())
i1.purchase_set.create(name="Иванов Сергей Иванович", age=39, data_purchase=timezone.now())
i2.purchase_set.create(name="Иванов Иван Иванович", age=39, data_purchase=timezone.now())
i3.purchase_set.create(name="Петров Серегей Иванович", age=39, data_purchase=timezone.now())
i4.purchase_set.create(name="Петров Владимир Иванович", age=39, data_purchase=timezone.now())
i1.purchase_set.create(name="Петров Иван Иванович", age=39, data_purchase=timezone.now())
i2.purchase_set.create(name="Сидоров Тимур Владимирович", age=39, data_purchase=timezone.now())
i3.purchase_set.create(name="Сидоров Владимир Владимирович", age=39, data_purchase=timezone.now())
i1.purchase_set.create(name="Сидоров Иван Владимирович", age=39, data_purchase=timezone.now())



