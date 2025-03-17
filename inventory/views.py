from django.http import HttpResponse
from django.db.utils import IntegrityError
from .models import Brand


def new(request):
    try:

        b = Brand.objects.create(brand_id=5, name="Sketchers")
        print(f"brand name:{b.name}, brand ID:{b.brand_id}")
    except IntegrityError:
        print("Log: The object already exists")
        return HttpResponse("The object already exists")

    return HttpResponse("Brand successfully created.")
