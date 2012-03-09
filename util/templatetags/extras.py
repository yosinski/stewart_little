from datetime import datetime, timedelta
import repoze.timeago

from django import template
from django.forms.fields import CheckboxInput
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat



register = template.Library()



@register.filter
def yearsFloor(td):
    if isinstance(td, basestring) or isinstance(td, datetime):
        #print type(td)
        #print 'td is "%s"' % td
        return u'ERROR'

    #if td < -td:
    #    return u'~ yearsFloor error! ~'

    days = td.days + td.seconds / 86400.0

    age = int(days/365.25)

    return '%d' % age



@register.filter
def humanjoin(elements):
    if isinstance(elements, basestring):
        return elements

    length = len(elements)
    if length == 0:
        return u''
    elif length == 1:
        return elements[0]
    elif length == 2:
        return string_concat(elements[0],
                             ' ', _('and'), ' ',
                             elements[1])
    else:
        return string_concat(', '.join(elements[0:-1]),
                             ', ', _('and'), ' ',
                             elements[-1])



def humanjoinNonFilter(elements):
    if isinstance(elements, basestring):
        return elements

    length = len(elements)
    if length == 0:
        return u''
    elif length == 1:
        return elements[0]
    elif length == 2:
        return string_concat(elements[0],
                             ' ', _('and'), ' ',
                             elements[1])
    else:
        # Ugly hack to make string_concat do ', '.join()
        temp = []
        [temp.extend([xx, ', ']) for xx in elements[0:-1]]
        temp.append(_('and'))
        temp.append(' ')
        temp.append(elements[-1])

        print 'temp is', temp
        
        return string_concat(*temp)



@register.filter
def padTo2(st):
    if not isinstance(st, basestring):
        st = str(st)
    #print 'st is', st
    if len(st) < 2:
        st = (' ' * (2-len(st))) + st
    return st



@register.filter
def padTo2(st):
    if not isinstance(st, basestring):
        st = str(st)
    #print 'st is', st
    if len(st) < 2:
        st = (' ' * (2-len(st))) + st
    return st



def subtract(value, arg):
    '''Subtracts arg from value.  Works with ints.'''
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except:
            return value

subtract.is_safe = False
register.filter(subtract)


@register.filter
def prependPlus(value):
    '''Prepend a plus sign if value is greater than 0.'''
    try:
        val = float(value)
    except ValueError:
        # if can't be converted to number
        return value

    value = str(value)
    if val > 0.0:
        return '+' + value
    else:
        return value


@register.filter
def negZeroPos(value):
    '''returns "negative", "zero", or "positive" depending on the value.'''
    try:
        val = float(value)
    except:
        return ''

    if val > 0:
        return 'positive'
    elif val == 0:
        return 'zero'
    else:
        return 'negative'



# If you aren't using UTC time everywhere, this line can be used
# to customize repoze.timeago:
repoze.timeago._NOW = datetime.now

@register.filter(name='elapsed')
def elapsed(timestamp):
    """
    This filter accepts a datetime and computes an elapsed time from "now".
    The elapsed time is displayed as a "humanized" string.
    Examples:
        1 minute ago
        5 minutes ago
        1 hour ago
        10 hours ago
        1 day ago
        7 days ago

    """
    return repoze.timeago.get_elapsed(timestamp)
elapsed.is_safe = True



@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, CheckboxInput)

