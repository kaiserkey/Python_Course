from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, days=1, hours=10)

print(now)

