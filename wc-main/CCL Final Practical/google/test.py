import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.write("Hello World")
        
        # name = 'xyz'
        # seat = 'ddd'
        # dept = 'Information Technology'
        # for i in range (1,6):
        #     self.response.write(name + " " + seat + " " + dept + "<br />")
        #     self.response.write(name)
        #     self.response.write(seat)
        #     self.response.write(dept)
        #     self.response.write('<br />')

        # seat = 'xdd'
        # dept = 'Information Technology'
        # i=0
        # while i<10 :
        #     self.response.write("Seat No: " + seat + " Department: " + dept + "<br />")
        #     self.response.write(seat)
        #     self.response.write(dept)
        #     self.response.write('<br />')
        #     i+=1        

        # num = 5
        # for i in range (1,11):
        #     self.response.write(num) 
        #     self.response.write(' x ')
        #     self.response.write(i)
        #     self.response.write(' = ')
        #     self.response.write(num*i)
        #     self.response.write('<br />')

        # num = 10
        # for i in range (1,11):
        #     self.response.write(num) 
        #     self.response.write(' x ')
        #     self.response.write(i)
        #     self.response.write(' = ')
        #     self.response.write(num*i)
        #     self.response.write('<br />')

        i1=0
        i2=1
        self.response.write(i1)
        self.response.write(" ")
        self.response.write(i2)
        self.response.write(" ")
        for i in range(1,7):
            self.response.write(i1+i2)
            self.response.write(" ")
            temp = i2
            i2 = i1 + i2
            i1 = temp
        # for i in range(1,7):
        #     self.response.write(i1+i2)
        #     self.response.write(" ")
        #     temp = i1 + i2
        #     i1 = i2
        #     i2 = temp



app = webapp2.WSGIApplication({('/', MainPage),}, debug=True)    


