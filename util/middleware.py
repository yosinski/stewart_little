# Some debug middleware

from datetime import datetime
from settings import MEDIA_ROOT, MEDIA_URL
from django.db import connection

LOGGING_ROOT = MEDIA_ROOT + 'log'
LOGGING_URL  = MEDIA_URL  + 'log'



def cleanUrl(url):
    return url.replace('/', '_')



class ReqRespLogger(object):

    def process_request(self, request):
        request.timest = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        filename = '%s/%s_req_%s.html' % (LOGGING_ROOT, request.timest, cleanUrl(request.path))
        url      = '%s/%s_req_%s.html' % (LOGGING_URL,  request.timest, cleanUrl(request.path))
        try:
            ff = open(filename, 'w')
        except:
            print 'ERROR: ReqRespLogger could not open %s' % filename
            return None
        
        print >>ff, request
        ff.close()
        print 'Saved request to  %s' % url

    def process_response(self, request, response):
        try:
            timest = request.timest
        except AttributeError:
            timest = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        filename = '%s/%s_resp_%s.html' % (LOGGING_ROOT, timest, cleanUrl(request.path))
        url      = '%s/%s_resp_%s.html' % (LOGGING_URL,  timest, cleanUrl(request.path))
        try:
            ff = open(filename, 'w')
        except:
            print 'ERROR: ReqRespLogger could not open %s' % filename
            return response
        
        print >>ff, response
        ff.close()
        print 'Saved response to %s' % url
        return response



class PrintSQL(object):
    '''Prints SQL queries'''
    
    def process_response(self, request, response):
        # # Get active comparisions
        # from main.models import Comparison
        # comparisons = Comparison.objects \
        #                    .filter(user = request.user, dateDeleted = None)
        # for cmpr in comparisons:
        #     print '  ---', cmpr, cmpr.votesA, cmpr.votesB

        queries = connection.queries
        print '%d queries in %f seconds' % (len(queries),
                                            sum([float(qq['time']) for qq in queries]))
        for qq in queries:
            print '%s: %s' % (qq['time'], qq['sql'])
        return response


