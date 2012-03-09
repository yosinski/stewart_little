import string
import random

randChars  = '%s%s' % (string.ascii_letters, string.digits)

def randomString(length = 10):
    return ''.join(random.choice(randChars) for ii in xrange(length))
