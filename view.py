import os, cherrypy, sys, re, smtplib, string
from Tkinter import Image
from jinja2 import Template, Environment, FileSystemLoader
from datetime import date
from operator import attrgetter
from email.mime.text import MIMEText

reload(sys)
sys.setdefaultencoding("utf-8")


from pymongo import MongoClient

class dex():
    def dexKey(self, pkmn):
        return pkmn.dex_number

    def __init__(self):
        cherrypy.engine.subscribe('start', self.start)
        cherrypy.engine.subscribe('stop', self.stop)



    def start(self):
        self.client = MongoClient("mongodb://majoridiocy:nick2693@107.170.240.186:27017")
        self.db = self.client.dex
        #self.db.dex.delete_many({})
        print(self.db.pkmn.count({}))

    def stop(self):
        self.client.close()

    @cherrypy.expose
    def default(self, type, page):
        if str(type).lower() == "move":
            c = self.db.moves.find({"name":str(page).lower().replace(" ", "-")})
            for x in c:
                return setup.env.get_template("move.html").render(move=x)
            return "Move %s Not Found" % page
        elif str(type).lower() == "pokemon" or "pkmn":
            try:
                #IS NUMBER
                num = int(page)
                c = self.db.pkmn.find({"dex":str(num)})
                for x in c:
                    return setup.env.get_template("pkmn.html").render(pkmn=x)
            except ValueError:
                #IS NAME
                c =self.db.pkmn.find({"name":str(page).lower()})
                for x in c:
                    return setup.env.get_template("pkmn.html").render(pkmn=x)
        else:
            return "Not Found"


    @cherrypy.expose
    def index(self):
        return setup.env.get_template("index_page.html").render()

class calc():
    @cherrypy.expose
    def index(self):
        return setup.env.get_template("calc_page.html").render()

class gym_leaders():
    @cherrypy.expose
    def index(self):
        gym_leaders=[
            {'name': 'Claire', 'name_lower': 'claire', 'pokemon': [
                {'name' : 'Jolteon', 'src': '/static/sprites/135.gif', 'kdr' : 'unknown'},
                {'name' : 'Rotom-W', 'src': '/static/sprites/479-wash.gif', 'kdr' : 'unknown'},
                {'name' : 'Eelektross', 'src': '/static/sprites/604.gif', 'kdr' : 'unknown'},
                {'name' : 'Galvantula', 'src': '/static/sprites/596.gif', 'kdr' : 'unknown'},
                {'name' : 'Electivire', 'src': '/static/sprites/466.gif', 'kdr' : 'unknown'},
                {'name' : 'Magnezone', 'src': '/static/sprites/462.gif', 'kdr' : 'unknown'},
                {'name' : 'Heliolisk', 'src': '/static/sprites/695.gif', 'kdr' : 'unknown'},
                {'name' : 'Manectric', 'src': '/static/sprites/310.gif', 'kdr' : 'unknown'},
                {'name' : 'Zapdos', 'src': '/static/sprites/145.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Shayda', 'name_lower': 'shayda', 'pokemon': [
                {'name' : 'Charizard', 'src': '/static/sprites/6-mega-y.gif', 'kdr' : 'unknown'},
                {'name' : 'Gliscor', 'src': '/static/sprites/472.gif', 'kdr' : 'unknown'},
                {'name' : 'Togekiss', 'src': '/static/sprites/468.gif', 'kdr' : 'unknown'},
                {'name' : 'Hawlucha', 'src': '/static/sprites/701.gif', 'kdr' : 'unknown'},
                {'name' : 'Gyarados', 'src': '/static/sprites/130.gif', 'kdr' : 'unknown'},
                {'name' : 'Talonflame', 'src': '/static/sprites/663.gif', 'kdr' : 'unknown'},
                {'name' : 'Dragonite', 'src': '/static/sprites/149.gif', 'kdr' : 'unknown'},
                {'name' : 'Skarmory', 'src': '/static/sprites/227.gif', 'kdr' : 'unknown'},
                {'name' : 'Zapdos', 'src': '/static/sprites/145.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Jason', 'name_lower': 'jason', 'pokemon': [
                {'name' : 'Salamence', 'src': '/static/sprites/373.gif', 'kdr' : 'unknown'},
                {'name' : 'Garchomp', 'src': '/static/sprites/445-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Hydreigon', 'src': '/static/sprites/635.gif', 'kdr' : 'unknown'},
                {'name' : 'Goodra', 'src': '/static/sprites/706.gif', 'kdr' : 'unknown'},
                {'name' : 'Altaria', 'src': '/static/sprites/334-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Dragonite', 'src': '/static/sprites/149.gif', 'kdr' : 'unknown'},
                {'name' : 'Dragalge', 'src': '/static/sprites/691.gif', 'kdr' : 'unknown'},
                {'name' : 'Tyrantrum', 'src': '/static/sprites/697.gif', 'kdr' : 'unknown'},
                {'name' : 'Kyurem-B', 'src': '/static/sprites/646-black.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Chris', 'name_lower': 'chris', 'pokemon': [
                {'name' : 'Absol', 'src': '/static/sprites/359-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Umbreon', 'src': '/static/sprites/197.gif', 'kdr' : 'unknown'},
                {'name' : 'Hydreigon', 'src': '/static/sprites/635.gif', 'kdr' : 'unknown'},
                {'name' : 'Weavile', 'src': '/static/sprites/461.gif', 'kdr' : 'unknown'},
                {'name' : 'Sableye', 'src': '/static/sprites/302-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Mandibuzz', 'src': '/static/sprites/630.gif', 'kdr' : 'unknown'},
                {'name' : 'Drapion', 'src': '/static/sprites/452.gif', 'kdr' : 'unknown'},
                {'name' : 'Tyranitar', 'src': '/static/sprites/248.gif', 'kdr' : 'unknown'},
                {'name' : 'Bisharp', 'src': '/static/sprites/625.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Bops', 'name_lower': 'bops', 'pokemon': [
                {'name' : 'Pinsir', 'src': '/static/sprites/127-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Heracross', 'src': '/static/sprites/214-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Volcarona', 'src': '/static/sprites/637.gif', 'kdr' : 'unknown'},
                {'name' : 'Galvantula', 'src': '/static/sprites/596.gif', 'kdr' : 'unknown'},
                {'name' : 'Armaldo', 'src': '/static/sprites/348.gif', 'kdr' : 'unknown'},
                {'name' : 'Scolipede', 'src': '/static/sprites/545.gif', 'kdr' : 'unknown'},
                {'name' : 'Scizor', 'src': '/static/sprites/212-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Yanmega', 'src': '/static/sprites/469.gif', 'kdr' : 'unknown'},
                {'name' : 'Crustle', 'src': '/static/sprites/558.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Kevin', 'name_lower': 'kevin', 'pokemon': [
                {'name' : 'Scrafty', 'src': '/static/sprites/560.gif', 'kdr' : 'unknown'},
                {'name' : 'Medicham', 'src': '/static/sprites/308-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Emboar', 'src': '/static/sprites/500.gif', 'kdr' : 'unknown'},
                {'name' : 'Hawlucha', 'src': '/static/sprites/701.gif', 'kdr' : 'unknown'},
                {'name' : 'Breloom', 'src': '/static/sprites/286.gif', 'kdr' : 'unknown'},
                {'name' : 'Machamp', 'src': '/static/sprites/68.gif', 'kdr' : 'unknown'},
                {'name' : 'Lucario', 'src': '/static/sprites/448.gif', 'kdr' : 'unknown'},
                {'name' : 'Infernape', 'src': '/static/sprites/392.gif', 'kdr' : 'unknown'},
                {'name' : 'Keldeo', 'src': '/static/sprites/647.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Alex', 'name_lower': 'alex', 'pokemon': [
                {'name' : 'Munchlax', 'src': '/static/sprites/446.gif', 'kdr' : 'unknown'},
                {'name' : 'Dunsparce', 'src': '/static/sprites/206.gif', 'kdr' : 'unknown'},
                {'name' : 'Audino', 'src': '/static/sprites/531.gif', 'kdr' : 'unknown'},
                {'name' : 'Porygon-Z', 'src': '/static/sprites/474.gif', 'kdr' : 'unknown'},
                {'name' : 'Tauros', 'src': '/static/sprites/128.gif', 'kdr' : 'unknown'},
                {'name' : 'Minccino', 'src': '/static/sprites/572.gif', 'kdr' : 'unknown'},
                {'name' : 'Kecleon', 'src': '/static/sprites/352.gif', 'kdr' : 'unknown'},
                {'name' : 'Exploud', 'src': '/static/sprites/295.gif', 'kdr' : 'unknown'},
                {'name' : 'Furfrou', 'src': '/static/sprites/676.gif', 'kdr' : 'unknown'}
            ]},
            {'name': 'Patrick', 'name_lower': 'patrick', 'pokemon': [
                {'name' : 'Ludicolo', 'src': '/static/sprites/272.gif', 'kdr' : 'unknown'},
                {'name' : 'Whimsicott', 'src': '/static/sprites/547.gif', 'kdr' : 'unknown'},
                {'name' : 'Ferrothorn', 'src': '/static/sprites/598.gif', 'kdr' : 'unknown'},
                {'name' : 'Serperior', 'src': '/static/sprites/497.gif', 'kdr' : 'unknown'},
                {'name' : 'Breloom', 'src': '/static/sprites/286.gif', 'kdr' : 'unknown'},
                {'name' : 'Leavanny', 'src': '/static/sprites/542.gif', 'kdr' : 'unknown'},
                {'name' : 'Venusaur', 'src': '/static/sprites/3-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Sceptile', 'src': '/static/sprites/254-mega.gif', 'kdr' : 'unknown'},
                {'name' : 'Celebi', 'src': '/static/sprites/251.gif', 'kdr' : 'unknown'}
            ]},
        ]

        output = setup.env.get_template("gym_leaders.html").render(gym_leaders=gym_leaders)
        return output


    @cherrypy.expose
    def challenge_claire(self, input_name_claire=None, input_email_claire=None, input_team_claire=None, input_format_claire=None):
        email_check = r'[^@]+@[^@]+\.[^@]+'
        team_check = r'\w+, \w+, \w+, \w+, \w+, \w+'
        if(input_name_claire == '' or input_email_claire == '' or input_team_claire == '' or input_format_claire == ''):
            output = 'Form completed with missing fields, press back and complete the form'
        elif (input_email_claire == re.search(email_check, input_email_claire)):
            output = 'The email you have entered is invalid! Please try again'
        elif (input_team_claire == re.search(team_check, input_team_claire)):
            output = 'The team you typed is invalid. Please remember to add commas! Press back to edit your form'
        else:
            email = MIMEText('Hello Claire! You have received a challenge from ' + input_name_claire + '. They have requested a battle on ' + input_format_claire + ' using ' + input_team_claire + '. If you need to, you can contact your challenger here: ' + input_email_claire)
            email['Subject'] = '[Challenge!]'
            email['From'] = 'pokemonpres@gmail.com'
            email['To'] = 'claire_koperwas@yahoo.com'#claire_koperwas@yahoo.com
            s = smtplib.SMTP('mail.sjsupokemon.club')
            s.login('admin@sjsupokemon.club', 'nick2693')
            s.sendmail(input_email_claire, ['claire_koperwas@yahoo.com'], email.as_string())
            s.quit()
            input = {}
            input['name'] = input_name_claire
            input['email'] = input_email_claire
            input['team'] = input_team_claire
            input['format'] = input_format_claire
            input['gym_leader'] = 'Claire'
            input['gym_desc'] = 'You have challenged the Electric type gym leader, Claire!!!'
            #with open('/static/gyms/challenges.txt', 'a') as save_file:
            #    save_file.write(input['gym_leader'] + ' challenged by ' + input['name'] + ' on ' + input['format'] + ' with ' + input['team'])
            output = setup.env.get_template("challenge.html").render(input=input)
            return output

class tournament():

    def __init__(self, name, date, first, second, third, prize="", challonge=""):
        self.name = name
        self.date_obj = date
        self.date = date.strftime("%d %B %Y")
        self.first = first
        self.second = second
        self.third = third
        self.prize = prize
        self.challonge = challonge

class regulation():

    def __init__(self, title, link, active):
        self.title = title
        self.link = link
        self.active = active

class officer():

    def __init__(self, name, position):
        self.name = name
        self.position = position

class main():

    tourneys = [tournament("Monotype", date(2015,11,20), "Nick Boyd", "Rianna \"the Bops\" Nandan", "Ty Garcia", challonge="http://challonge.com/sjsumonotypefall2015"),
                tournament("Cute", date(2016, 3, 18), "Shayda Sophia", "Javier Ayala", "Brenna Botzheim"),
                tournament("NU", date(2016, 3, 4), "Javier Ayala", "Claude Michel", "Will Giallo", challonge="http://challonge.com/sjsunuspring2016"),
                tournament("Gen 1", date(2016, 2, 26), "Manuel Saucedo", "Javier Ayala", "Will Giallo"),
                tournament("Team Battle", date(2016, 2, 19), "Shayda Sophia and Alex Vargas", "Tad Mikasa and Rianna \"the Bops\" Nandan", "Will Giallo and Joe Giallo"),
                tournament("OU", date(2016, 2, 5), "Javier Ayala", "Tad Mikasa", "Ty Garcia"),
                tournament("Halloween", date(2015, 10, 30), "Javier Ayala", "Tad Mikasa", "Chris Ngai"),
                tournament("Little Cup", date(2015, 10, 16), "Nick Boyd", "Shayda Sophia", "Will Giallo and Alex Vargas - tied"),
                tournament("Draft", date(2015, 10, 2), "Yair", "Tad Mikasa", "Chris Ngai"),
                tournament("Monochrome", date(2015, 9, 18), "Eduardo", "Javier Ayala", "Alex Nguyen"),
                tournament("OU", date(2015, 9, 4), "Javier Ayala", "Chris Ngai", "Shayda Sophia"),
                tournament("OU", date(2015, 4, 24), "Jason Yan", "Khalia Flores", "NA"),
                tournament("VGC", date(2015, 4, 8), "Sergio Camacho", "Javier Ayala", "Jason Yan"),
                tournament("Little Cup", date(2015, 3, 13), "Shayda Sophia", "Tad Mikasa", "Jose Madrid"),
                tournament("Never Used", date(2015, 2, 25), "Jose Madrid", "Jason Yan", "James Escoto"),
                tournament("OU Draft", date(2016, 4, 22), "Chris Ngai", "Tad Mikasa", "Ty Garcia", challonge="http://challonge.com/2016SpringDraftTournament"),
                tournament("Monotype", date(2016, 5, 6), "Rianna \"the Bops\" Nandan", "Shayda Sophia", "Alex Vargas", challonge="http://challonge.com/2016springmonotypetourney"),
                tournament("OU", date(2016, 6, 9), "Tad Mikasa", "Raymond", "Joe Giallo", challonge="http://challonge.com/SJSUOUTOURNEY2016FALL"),
                tournament("Teambuilder", date(2016, 6, 23), "Shashwath", "Jordan", "Javier Ayala", challonge="http://challonge.com/TBTSJSUF2016"),
                tournament("Draft", date(2016, 10, 14), "Will Giallo", "Chris Ngai", "Nick Boyd", challonge="http://challonge.com/DraftTourneyF2016"),
                tournament("Halloween", date(2016, 10, 28), "Raymond", "Tad Mikasa", "Rianna \"the Bops\" Nandan", challonge="http://challonge.com/HALLOWTOURNEYF2016"),
                tournament("Find a Friend", date(2016, 11, 4), "Will and Shayda", "Tad and Mitchell", "Sean and Claude", challonge="http://challonge.com/TT2016F"),
                tournament("Monotype", date(2016, 12, 2), "Rianna \"the Bops\" Nandan", "Nick Boyd", "Yair Aragundi", challonge="http://challonge.com/MonotypeFall16"),
                tournament("Team Rocket", date(2017, 2, 3), "Nick Boyd", "Will Giallo", "Ed Martinez", challonge="http://challonge.com/SJSUTR2017")
            ]
    regulations = [
        regulation("Club Tournament Regulations","https://docs.google.com/document/d/1d5JiFS_6BsYqIfMRnN7J20UPxzovNyXQ179j2T9YVAo/edit", False),
        regulation("Contest Tournament","https://docs.google.com/document/d/1q15GqdMIj3aiA3s64VkQRVKDJdbry0dsh2YZKelb9-w/edit", False),
        regulation("Favorite Pokemon","https://docs.google.com/document/d/1Oi0WhzGesphmcFN4FWQk3DlJ_i-x3mFZZkVdVatRvUY/edit", False),
        regulation("Generation 1 Tournament","https://docs.google.com/document/d/1asPIVJJLAUJJiKZlfovNGp2ehuDs6oCmmeJPLhWHY4s/edit", False),
        regulation("Gym Regulations","https://docs.google.com/document/d/1Je7YDFOZtfAMwj9iELk-ZcIArCQJhAHKByBCUE3LpP8/edit", False),
        regulation("Halloween","https://docs.google.com/document/d/1kdOmbO2ed2YTkEWv-oe2aD2rwAo8_nDSpQfgplIk11Q/edit", False),
        regulation("Little Cup","https://docs.google.com/document/d/1sNPHsBBkmCBHNQLbrE-WLu5uuDwA5Oyhmx1jOtJuBbA/edit", True),
        regulation("Monochrome","https://docs.google.com/document/d/1MnnYwcmwCZFYDc8qf3UPaj0jVnhD3KL0PWoVMHKAZMA/edit", False),
        regulation("Monotype","https://docs.google.com/document/d/1ulhvToTeYAy1GK7jaNPlTNUXa0mrdtygj-FVAzwTWbc/edit", True),
        regulation("Never Used","https://docs.google.com/document/d/1t2TIuIz8kkz1UFA50STbpuc72n7OTxB5QyCEgK0dJI8/edit", False),
        regulation("Not Fully Evolved (NFE)","https://docs.google.com/document/d/16WUmQfOOjksfjkBVevBS6zxz-WQMPxaMDuFM2I60yBE/edit", False),
        regulation("Over Used","https://docs.google.com/document/d/1mxHoxztFC5nWjzU5sLomVmFZQwlAuMvnmReiOkP_9UM/edit", False),
        regulation("OU Draft","https://docs.google.com/document/d/1T3W_VsrZBEPngOdFnJU531By72sBjATPef9AJI8EqXs/edit", False),
        regulation("Point Buy","https://docs.google.com/document/d/1lA4bK2z5ehU4_DO4AIOXAg_KCDmZQhADB3qD9CIvUnA/edit", True),
        regulation("Saint Patrick's Day","https://docs.google.com/document/d/1_rzUVCSVMF6zN453l3auAjTzqyM1_xTijDxDn_bYFpA/edit", True),
        regulation("Steal Yo Pokes","https://docs.google.com/document/d/1ZG0CCfdZwnkK6p_ZYIM5b1Xj0k8-9G2vjd0VgxspGjo/edit", False),
        regulation("Team Battle","https://docs.google.com/document/d/108gnHE_Gacj8aEkdSt4mY-PZ8TWHTXd3OgxQKuD2hJY/edit", False),
        regulation("Team Builder","https://docs.google.com/document/d/13gWOnTRv6mcjoqAslxa7VeBM2vB-F7GO71SIeMkHTwQ/edit", False),
        regulation("Team Rocket","https://docs.google.com/document/d/1ZG0CCfdZwnkK6p_ZYIM5b1Xj0k8-9G2vjd0VgxspGjo/edit", True),
        regulation("Tier Rotation","https://docs.google.com/document/d/1VDKwWH9FjWv3UZbCMwIKAl7WNDnhSH1r0g5KxEymAxY/edit", False),
        regulation("Ubers","https://docs.google.com/document/d/1o7C7RdxOGGt6tnWpyowq78-1ILPYIHmScMluaPHizxo/edit", False),
        regulation("VGC","https://docs.google.com/document/d/1czvrFG9eMvloleFIT8Pn0X_mPWgTRZi4SRsPfecjjeY/edit", True)
    ]
    for reg in regulations:
        if not reg.active:
            regulations.remove(reg)
    for reg in regulations:
        if not reg.active:
            regulations.remove(reg)
    for reg in regulations:
        if not reg.active:
            regulations.remove(reg)


    officers = [
        ["Spring 2017: Another New Game", officer("Khaila Zherine Flores", "President"), officer("William Giallo", "Vice President"), officer("Jason Yan", "Treasurer"), officer("Kevin Nguyen", "Secretary"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Social Media Manager"),officer("Patrick Rettinhouse", "Intern")],
        ["Fall 2016: Steeling the Sun", officer("Khaila Zherine Flores", "President"),officer("William Giallo", "Vice President"),officer("Jason Yan", "Treasurer"),officer("Shayda Sophia", "Secretary"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Rianna Nandan", "Historian"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Media Manager")],
        ["Spring 2016: Dawn of the Pokemon League", officer("Khaila Zherine Flores", "President"),officer("William Giallo", "Vice President"),officer("Jose Madrid", "Treasurer"),officer("Shayda Sophia", "Secretary"),officer("Alex Nguyen", "Publicist"),officer("Roxas Nick", "Publicist"),officer("Nick Boyd", "Web Master"),officer("Claire Koperwas", "Jr. Web Master"),officer("Javier Ayala-Mora", "Historian"),officer("Tad Mikasa", "Event Coordinator"),officer("Eduardo Martinez", "Media Manager")],
        ["Fall 2015: The Great Expansion", officer("Khaila Zherine Flores", "President"), officer("James Escoto", "President"), officer("Jose Madrid", "Treasurer"), officer("Shayda Sophia", "Secretary"),officer("Alex Nguyen", "Publicist"), officer("Nick Boyd", "Web Master"), officer("Jason Yan", "Jr. Web Master"), officer("Javier Ayala-Mora", "Historian"), officer("Tad Mikasa", "Event Coordinator")],
        ["Spring 2015: New Game", officer("Khaila Zherine Flores", "President"), officer("James Escoto", "President"), officer("Jose Madrid", "Treasurer"), officer("Nick Boyd", "Secretary"), officer("Alex Nguyen", "Publicist")]
    ]

    @cherrypy.expose
    def index(self):
        challonge_link = ""
        for x in sorted(self.tourneys, key=lambda date: date.date_obj, reverse=True):
            if x.challonge != "":
                challonge_link = x.challonge
                break
        return setup.env.get_template("sjsupkmnclub.html").render(tournaments=sorted(self.tourneys, key=lambda date: date.date_obj, reverse=True), regulations=sorted(self.regulations), officers=self.officers, c_link=challonge_link)
