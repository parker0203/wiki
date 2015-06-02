import webapp2

# pip
import markdown
import markdown2

# my lib
import path
import reader 

amateur_header = reader.read_file_to_string(path.template_path + "amateur-header.html")
amateur_header += reader.read_file_to_string(path.css_path + "github.css")
amateur_header += reader.read_file_to_string(path.template_path+ "amateur-mid.html")

amateur_footer = reader.read_file_to_string(path.template_path + "amateur-footer.html")

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        data = reader.read_file_to_string_list(path.md_path + "home.md")
        for line in data:
            html = markdown.markdown(line)
            self.response.write(html)

class git_md(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        self.response.write(amateur_header)
        md_parse = reader.read_file_to_string(path.md_path + "git.md")
        
        md_html = markdown2.markdown(md_parse, extras={'fenced-code-blocks': {'cssclass': 'github'}}) # this  github css does not do anything right now
        self.response.write(md_html)
        self.response.write(amateur_footer)
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/git', git_md),
], debug=True)

