import webapp2

# pip
import markdown
import markdown2

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
        line2 = ""
        for line in data:
            line2 += line
            line2 += "\r"
        
        #html = markdown.markdown(line2)
        html = markdown2.markdown_path(path.md_path + "git.md", extras=["fenced-code-blocks"])
        self.response.write(html)
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/git', git_md),
], debug=True)

