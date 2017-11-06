#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class RezultatHandler(BaseHandler):
    def post(self):
        city_first = self.request.get("01_vnos")
        city_second = self.request.get("02_vnos")
        city_third = self.request.get("03_vnos")
        city_fourth = self.request.get("04_vnos")
        city_fifth = self.request.get("05_vnos")
        city_sixth = self.request.get("06_vnos")
        city_seventh = self.request.get("07_vnos")
        city_eighth = self.request.get("08_vnos")
        city_nineth = self.request.get("09_vnos")

        if len(city_first) == 0:
            return self.write("There is no guess.\n")
        elif city_first.lower == "paris" or "pariz":
            return self.write("You are right, 01_city is Paris.\n")
        elif city_first.lower is not "paris" or "pariz":
            return self.write("Mistake, 01_city is not %s.\n" % city_first)

        if len(city_second) == 0:
            return self.write("There is no guess.\n")
        elif city_second.lower == "kijev":
            return self.write("You are right, 02_city is Kijev.\n")
        elif city_second.lower is not "kijev":
            return self.write("Nope, 02_city is not %s.\n" % city_second)

        if len(city_third) == 0:
            return self.write("There is no guess.\n")
        elif city_third.lower == "budapest":
            return self.write("You are right, 03_city is Budapest.\n")
        elif city_third.lower is not "budapest":
            return self.write("Nope, 03_city is not %s.\n" % city_third)

        if len(city_fourth) == 0:
            return self.write("There is no guess.\n")
        elif city_fourth.lower == "ljubljana":
            return self.write("You are right, 04_city is Ljubljana\n")
        elif city_fourth.lower is not "ljubljana":
            return self.write("You dont have luck, 04_city is not %s.\n" % city_fourth)

        if len(city_fifth) == 0:
            return self.write("There is no guess.\n")
        elif city_fifth.lower == "tokio":
            return self.write("You are right, 05_city is Tokio.\n")
        elif city_fifth.lower is not "tokio":
            return self.write("No, 05_city is not %s.\n" % city_fifth)

        if len(city_sixth) == 0:
            return self.write("There is no guess.\n")
        elif city_sixth.lower == "new dheli":
            return self.write("You are right, 06_city is New Dheli.\n")
        elif city_sixth.lower is not "new dheli":
            return self.write("Sadly, 06_city is not %s.\n" % city_sixth)

        if len(city_seventh) == 0:
            return ("There is no guess.\n")
        elif city_seventh.lower == "sidney":
            return ("You are right, 07_city is Sidney.\n")
        elif city_seventh.lower is not "sidney":
            return ("Nope, 07_city is not %s.\n" % city_seventh)

        if len(city_eight) == 0:
            return ("There is no guess.\n")
        elif city_eighth.lower == "kairo" or "cairo":
            return ("You are right, 08_city is Cairo.\n")
        elif city_eighth.lower is not "kairo" or "cairo":
            return ("Mistake, 08_city is not %s.\n" % city_eighth)

        if len(city_ninth) == 0:
            return ("There is no guess.\n")
        elif city_nineth.lower == "sarajevo":
            return ("You are right, 09_city is Sarajevo.\n")
        elif city_nineth.lower is not "sarajevo":
            return ("Nein, 09_city is not %s.\n" % city_nineth)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', RezultatHandler),
], debug=True)
