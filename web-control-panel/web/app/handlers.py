import webapp2

import templates
import led_abstractions


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_variables = {
            'message': "Hello World"
        }
        templates.render('home', template_variables, self)


class LedHandler(webapp2.RequestHandler):
    def get(self, led_number):
        template_variables = {
            'led_number': led_number
        }
        templates.render('forms/led_form', template_variables, self)

    def post(self, led_number):
        red = self.request.get('red', 0)
        green = self.request.get('green', 0)
        blue = self.request.get('blue', 0)
        brightness = self.request.get('brightness', 1)

        led_abstractions.set_led(led_number, red, green, blue, brightness)
        led_abstractions.apply_changes()

        self.response.write("SET LED " + led_number)


class NotFoundHandler(webapp2.RequestHandler):
    def get(self, route):
        self.error(404)
        template_variables = {
            'message': "404 - Page Not Found"
        }
        templates.render('404', template_variables, self)
