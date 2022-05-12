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
        latitude = self.request.get('zipCode')
        longitude = self.request.get('zipCode')
        hr_daily = self.request.get('countryCode')
        url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&hourly=" + countrycode
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        postalLocation = data['result'][0]['postalLocation']
        state = data['result'][0]['state']
        district = data['result'][0]['district']
        province = data['result'][0]['province']

        template_values = {
            "postalLocation": postalLocation,
            "state": state,
            "district": district,
            "province": province  
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)