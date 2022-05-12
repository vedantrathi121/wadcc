import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        name = self.request.get('name')
        url = "http://universities.hipolabs.com/search?name=" + name
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        name = data[0]['name']
        website = data[0]['web_pages'][0]

        template_values = {
            "name": name,
            "website": website
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)