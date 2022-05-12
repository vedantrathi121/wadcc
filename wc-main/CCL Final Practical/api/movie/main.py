import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = []
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        filmId = self.request.get('filmId')
        url = "https://ghibliapi.herokuapp.com/films/" + filmId
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        title = data['title']
        director = data['director']
        producer = data['producer']
        releaseDate = data['release_date']

        template_values = {
            "title": title,
            "director": director,
            "producer": producer,
            "releaseDate": releaseDate  
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)