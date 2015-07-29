import webapp2
from handlers import *

app = webapp2.WSGIApplication([
    ('/', mainHandler.MainPage),
    ('/account', accountHandler.AccountHandler),
    ('/payment', paymentHandler.PaymentHandler)
], debug=True)