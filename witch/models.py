from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    main_text = models.TextField()
    additional_texts = models.TextField(blank=True)


class AdditionalText(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = models.TextField()


class Comment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    text = models.TextField()


class Certificate(models.Model):
    image = models.ImageField(upload_to='certificates/')
