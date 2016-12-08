# coding:utf-8
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers = headers)

        response = urllib2.urlopen(request)


        # if response.getCode() != 200:
        #     return None

        #print response.read()
        return response.read()

