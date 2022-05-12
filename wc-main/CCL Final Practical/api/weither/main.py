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
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')
        hr_daily = self.request.get('hr_daily')
        if hr_daily=='hourly':
            hr_daily='hourly=temperature_2m,relativehumidity_2m'
            url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&" + hr_daily
            #hourly=temperature_2m,relativehumidity_2m" + "&daily=sunrise,sunset&timezone=Asia%2FSingapore"
            data = urllib.urlopen(url).read()
            data = json.loads(data)
            temparature = data['hourly']['relativehumidity_2m'][0]
            humidity = data['hourly']['temperature_2m'][0]
            # sunset = data['daily']['sunset'][0].split('T')[1]
            template_values = {
            "temparature": temparature,
            "humidity": humidity
            }
            path = os.path.join(os.path.dirname(__file__), 'results.html')
            self.response.out.write(template.render(path, template_values))
        elif hr_daily=='daily':
            hr_daily= 'daily=sunrise,sunset&timezone=Asia%2FSingapore'
            url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&" + hr_daily
            #hourly=temperature_2m,relativehumidity_2m" + "&daily=sunrise,sunset&timezone=Asia%2FSingapore"
            data = urllib.urlopen(url).read()
            data = json.loads(data)
            sunrise = data['daily']['sunrise'][0].split('T')[1]
            sunset = data['daily']['sunset'][0].split('T')[1]
            # sunset = data['daily']['sunset'][0].split('T')[1]
            template_values = {
            "sunrise": sunrise,
            "sunset": sunset  
            }
            path = os.path.join(os.path.dirname(__file__), 'results2.html')
            self.response.out.write(template.render(path, template_values))
        else:
            hr_daily='hourly=temperature_2m,relativehumidity_2m&daily=sunrise,sunset&timezone=Asia%2FSingapore'
            url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&" + hr_daily
            #hourly=temperature_2m,relativehumidity_2m" + "&daily=sunrise,sunset&timezone=Asia%2FSingapore"
            data = urllib.urlopen(url).read()
            data = json.loads(data)
            temparature = data['hourly']['relativehumidity_2m'][0]
            humidity = data['hourly']['temperature_2m'][0]
            sunrise = data['daily']['sunrise'][0].split('T')[1]
            sunset = data['daily']['sunset'][0].split('T')[1]
            template_values = {
            "temparature": temparature,
            "humidity": humidity,
            "sunrise": sunrise,
            "sunset": sunset
            }
            path = os.path.join(os.path.dirname(__file__), 'results3.html')
            self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)