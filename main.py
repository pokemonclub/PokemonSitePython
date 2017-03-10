import cherrypy
import setup, os, sys

if "__main__" == __name__:
    setup.init()
    conf = {
        '/':{
            'tools.sessions.on':True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir': './public'
        }
    }

    cherrypy.tree.mount(view.main(), "/", conf)
    cherrypy.tree.mount(view.dex(), "/dex", conf)
    cherrypy.tree.mount(view.calc(), "/calc", conf)
    cherrypy.tree.mount(view.gym_leaders(), "/gyms", conf)

    if len(sys.argv) > 1:
        if sys.argv[1] == "True":
            cherrypy.config.update({
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 80,

        })

    cherrypy.engine.start()
    cherrypy.engine.block()
