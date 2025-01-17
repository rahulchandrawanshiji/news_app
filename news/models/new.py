from django.db import models
from .category import Category
import smtplib
Rating = [
    ('b', 'Bad'),   
    ('a', 'Average'),
    ('e', 'Excellent')
]
class News(models.Model):
    title=models.CharField(max_length=40)
    ne=models.CharField(max_length=300)
    allnews=models.CharField(max_length=5000,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads')
    category = models.ForeignKey(Category ,  on_delete=models.CASCADE , default=1,null=True,blank=True) 
    rating = models.CharField(max_length = 1, choices = Rating,default='',null=True,blank=True)

    def __str__(self):
        return self.title


def sendEmail(email,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('from mail','xyz')
    server.sendmail(email,'from mail',content)
    server.close()
def SendEmail(email,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('from mail','8878847682')
    server.sendmail('from mail',email,content)
    server.close()