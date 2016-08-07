import webapp2

import handlers

ROUTES = [
    ('/', handlers.HomeHandler),
    ('/led/(.*)', handlers.LedHandler),
    ('/(.*)', handlers.NotFoundHandler),
]
