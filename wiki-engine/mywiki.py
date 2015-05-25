import webapp2

# pip
import markdown

# my lib
import path
import reader 



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        data = reader.read_md(path.md_path + "home.md")
        for line in data:
            html = markdown.markdown(line)
            self.response.write(html)

class git_md(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        data = reader.read_md(path.md_path + "git.md")
        for line in data:
            html = markdown.markdown(line)
            self.response.write(html)
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/git', git_md),
], debug=True)

