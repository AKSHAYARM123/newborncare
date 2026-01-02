from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=100)

class panchayath(models.Model):
    place=models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)
    contact= models.BigIntegerField()
    email= models.CharField(max_length=100)


class ward(models.Model):
    PANCHAYATH=models.ForeignKey(panchayath,on_delete=models.CASCADE)
    wardnumder=models.BigIntegerField()

class ashaworker(models.Model):
    LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
    image=models.CharField(max_length=200)
    name=models.CharField(max_length=30)
    WARD=models.ForeignKey(ward,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    regno=models.CharField(max_length=100)


class expert(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
    image = models.FileField()
    gender=models.CharField(max_length=100)

class mother(models.Model):
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post=models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
    image = models.FileField()
    WARD=models.ForeignKey(ward,on_delete=models.CASCADE)



class child(models.Model):
    name = models.CharField(max_length=100)
    weight=models.IntegerField()
    PARENT=models.ForeignKey(mother, on_delete=models.CASCADE)
    age = models.BigIntegerField()

class vaccination(models.Model):
    ashaworkerid = models.ForeignKey(ashaworker,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    desc = models.CharField(max_length=100)
    place = models.CharField(max_length=100)



class reminder(models.Model):
    time = models.TimeField()
    PARENT = models.ForeignKey(mother, on_delete=models.CASCADE)
    desc = models.CharField(max_length=10)

class shedule(models.Model):
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    EXPERT=models.ForeignKey(expert, on_delete=models.CASCADE)

class food(models.Model):
    category = models.CharField(max_length=100)
    foodname = models.CharField(max_length=100)
    quantity= models.BigIntegerField()
    ashaworkerid = models.ForeignKey(ashaworker,on_delete=models.CASCADE)



class foodallocation(models.Model):
    FOOD = models.ForeignKey(food, on_delete=models.CASCADE)
    date = models.DateField()
    parent = models.ForeignKey(mother,on_delete=models.CASCADE)
    day=models.CharField(max_length=100)

class booking(models.Model):
    PARENT = models.ForeignKey(mother, on_delete=models.CASCADE)
    SHEDULE = models.ForeignKey(shedule, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)


class prescription(models.Model):
    BOOKING = models.ForeignKey(booking, on_delete=models.CASCADE)
    file = models.FileField()


class  childvaccinationdetails(models.Model):
    CHILDID= models.ForeignKey(child, on_delete=models.CASCADE)
    VACCINATIONID=models.ForeignKey(vaccination, on_delete=models.CASCADE)
    date = models.DateField()

































