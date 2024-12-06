import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_paginate


try:
    for page in lazy_paginator(10):
        for user in page:
            print(user)
        break
except BrokenPipeError:
    sys.stderr.close()