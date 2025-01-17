from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email=email)   
        except:
            return False 
    @staticmethod
    def get_customer_by_password(password):
        try:
            return Customer.objects.filter(password=password)   
        except:
            return False 
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
