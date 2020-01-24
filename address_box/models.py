from django.db import models
TYPES = (
    (1, 'private'),
    (2, 'professional'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    description = models.TextField(null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Email(models.Model):
    email = models.CharField(max_length=64, unique=True)
    type = models.IntegerField(choices=TYPES)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.email)


class Group(models.Model):
    name = models.CharField(max_length=32)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return '{}'.format(self.name)