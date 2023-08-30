from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(months=1)