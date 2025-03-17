from inventory.models import Brand

from django.db import connection, reset_queries

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

Brand.objects.create(brand_id=1, name='Nike')

Brand.objects.all()

Brand.objects.all().delete()
x = Brand.objects.all().query
Brand.objects.filter(brand_id=1)





sqlformatted = format(str(x.query))
sqlformatted = format(str(x.query), reindent=True)
print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))