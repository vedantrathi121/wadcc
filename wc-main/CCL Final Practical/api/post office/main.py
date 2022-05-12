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
        pincode = self.request.get('zipCode')
        url = "https://api.postalpincode.in/pincode/" + pincode
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        postOffice = data[0]['PostOffice'][0]['Name']
        branchType = data[0]['PostOffice'][0]['BranchType']
        circle = data[0]['PostOffice'][0]['Circle']
        district = data[0]['PostOffice'][0]['District']

        template_values = {
            "postOffice": postOffice,
            "branchType": branchType,
            "circle": circle, 
            "district": district
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)