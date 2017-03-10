import jinja2

def init():
    global env
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["public/html", "public/css", "public/txt"]))
    global header
    header = env.get_template("header.html")
    global pkmnpage
    pkmnpage = env.get_template("pkmn.html")

def renderHeader(title="Website", desc=""):
    return header.render(title=title, desc=desc)
