from django.shortcuts import render
from django.http import HttpResponse
from practice.models import Car, Manufacturer, Person, Group, Membership
from datetime import date

# Create your views here.

def index(request):
    return HttpResponse('Lool')


def create_model (request):
    # ringo = Person.objects.create(
    #     first_name="Ringo",
    #     last_name="Starr",
    #     shirt_size="M"
    # )

    # paul = Person.objects.create(
    #     first_name="Paul",
    #     last_name="McCartney",
    #     shirt_size='M'
    # )

    # beatles = Group.objects.create(name="The Beatles")

    # m1 = Membership(
    #     person = ringo,
    #     group = beatles,
    #     date_joined = date(1999, 1, 1),
    #     invite_reason = "Needed a new Drummer"
    # )
    # m1.save()

    # print(beatles.members.all())
    # print(ringo.group_set.all())

    # m2 = Membership.objects.create(
    #     person = paul,
    #     group = beatles,
    #     date_joined = date(1998, 3, 9),
    #     invite_reason = "Wanted to form a band"
    # )
    # print(beatles.members.all())
    datas = Group.objects.filter(members__first_name__startswith="Paul")

    person = Person.objects.filter(
            first_name__startswith="Paul"
        ).first()
    print(Person._meta.get_fields())
    return HttpResponse("Done")






