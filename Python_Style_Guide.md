### Follow <a href="https://www.python.org/dev/peps/pep-0008/">PEP 8.</a><br>
#### Import Statements

We expand on PEP 8‘s suggestions for import statements. These greatly improve one’s ability to ascertain what is and isn’t available in a given file.

Import one module per import statement:
```
import os
import sys
```
not:
```
import os, sys
```
Separate imports into groups with a line of whitespace: standard library; (if a web app) Django or other framework; third-party; and local imports:
```
import os
import sys

from django.conf import settings
import pyquery

from myapp import models, views
```
Alphabetize your imports; it will make your code easier to scan. See how terrible this is:
```
import cows
import kittens
import bears
```
A simple sort:
```
import bears
import cows
import kittens
```
Imports on top, from imports below:
```
import x
import y
import z
from bears import pandas
from xylophone import bar
from zoos import lions
```
That’s loads easier to read than:
```
from bears import pandas
import x
from xylophone import bar
import y
import z
from zoos import lions
```

Lastly, when importing things into your namespace from a package use an alphabetized CONSTANT, Class, var order:

from models import DATE, TIME, Dog, Kitteh, upload_pets

If possible though, it may be easier to import the entire package, especially for methods as it help answers the question, “where did you come from?”

Bad:
```
from foo import you


def my_code():
    you()  # wait, is this defined in this file?
```
Good:
```
import foo


def my_code():
    foo.you()  # oh you...
```

Good, using hanging indent. Note that the next line is lined up with the previous line delimiter:
```
log.msg('Something long log message and some vars: {0}, {1}'
        .format(variable_a, variable_b))
```
```
accounts = PaymentAccounts.objects.filter(
    accounts__provider__type=2,
    something_else=True
)
accounts = (PaymentAccounts.objects
    .filter(accounts__provider__type=2)
    .exclude(something_else=False)
)
```
