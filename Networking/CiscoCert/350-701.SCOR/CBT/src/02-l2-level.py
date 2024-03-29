#!/usr/bin/env python3


class MainPage(webapp.RequestHandler):
    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(template.render(path, context))

    def get(self):
        self.render_template("index.html")


application = webapp.WSGIApplication([(".*", MainPage)], debug=False)
