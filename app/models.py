from django.db import models

class Csv(models.Model):
    fid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=True)
    file_csv=models.FileField(upload_to='csv_file/')

    class Meta:
        db_table='Csv'

class Num(models.Model):
    content=models.CharField(max_length=250,blank=True)
    finame=models.CharField(max_length=50,blank=True)

    class Meta:
        db_table='Num'

class Report(models.Model):
    num=models.CharField(max_length=50,blank=True)
    msg=models.CharField(max_length=250,blank=True)
    date=models.CharField(max_length=50,blank=True)
    status=models.CharField(max_length=50,blank=True)
    pin=models.CharField(max_length=50,blank=True)
    port=models.CharField(max_length=50,blank=True)

    class Meta:
        db_table='Report' 

class Sim(models.Model):
    pin=models.CharField(max_length=50,blank=True)
    port=models.CharField(max_length=50,blank=True)

    class Meta:
        db_table='Sim'

class Device(models.Model):
    port=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=100,blank=True)
    pin=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=100,blank=True)
    imei=models.CharField(max_length=100,blank=True)
    signal=models.CharField(max_length=100,blank=True)
    report=models.CharField(max_length=100,blank=True)

    class Meta:
        db_table='Device'

class Spin(models.Model):
    port=models.CharField(max_length=50,blank=True)
    sim=models.CharField(max_length=50,blank=True)

    class Meta:
        db_table='Spin'

class  Numupdate(models.Model):
    name=models.CharField(max_length=100,blank=True)
    mobile=models.CharField(max_length=50,blank=True)

    class Meta:
        db_table='Numupdate'