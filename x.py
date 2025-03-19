from inventory.models import Brand, Category, Product, ProductInventory, ProductType

from django.db import connection, reset_queries

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

Brand.objects.create(brand_id=1, name="Nike")
Category.objects.create(name="Shoes", slug="shoes")
Product.objects.create(
    id=1,
    web_id=1,
    slug="airmax",
    name="Airmax",
    description="mens running shoes",
    is_active=True,
)
ProductType.objects.create(name="shoe")
ProductInventory.objects.create(
    sku="123",
    upc="123",
    product_type_id=1,
    product_id=1,
    brand_id=1,
    retail_price="10.00",
    store_price="10.00",
    sale_price="10.00",
    weight="100",
)
Brand.objects.all()

Brand.objects.all().delete()
x = Brand.objects.all().query
Brand.objects.filter(brand_id=1)


sqlformatted = format(str(x.query))
sqlformatted = format(str(x.query), reindent=True)
print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))

# create()- api or function for interacting with db to insert records
# errors
"""
IntegrityError
"""

# save()

"""
You can only read or write
how to read 1:M
how to write 1:M
how to read M:M with join table
how to write M:M with join table 
map save() and create() to serializer methods
"""
