from django.db import models

YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate')
]

SHIRT_SIZES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
]

def do_something():
    pass

def do_something_else():
    pass

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, default='-')
    shirt_size = models.CharField(max_length=30, choices=SHIRT_SIZES)

    def baby_boomer_status(self):
        "Returns the person's baby bommer status"
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return 'Pre-Boomer'
        elif self.birth_date < datetime.date(1965, 1, 1):
            return 'Baby Boomer'
        else:
            return 'Post Boomer'

    @property
    def full_name(self):
        "Returns the person's full name"
        return '%s %s' % (self.first_name, self.last_name)


    class Meta():
        db_table = 'persons'

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', "GOLD SILVER BRONZE")
    name = models.CharField(max_length=30)
    medal = models.CharField(max_length=30, blank=True, choices=MedalType.choices)

class Fruit(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

class Car(models.Model):
    name = models.CharField(max_length=30)
    company_that_makes_it = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['name']
        db_table = 'cars'
        verbose_name_plural = "oxen"

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)

    def save(self, *args, **kargs):
        do_something()
        super().save(*args, **kargs)
        do_something_else()

class CommonInfo(models.Model):
    name = models.CharField(max_length=30, null=True, default='')
    age = models.DateField(null=True)

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta:
        db_table = 'students_info'



