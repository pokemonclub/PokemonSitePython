import jinja2

def init():
    global env
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["public/html"]))
    global header
    header = env.get_template("header.html")
    global pkmnpage
    pkmnpage = env.get_template("pokemon.html")
    global navbar
    navbar = env.get_template("navbar.html")

def renderHeader(title="Website", desc=""):
    return header.render(title=title, desc=desc)
