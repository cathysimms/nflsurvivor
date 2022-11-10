from application import db
from application.models import Teams, Games, Users, Picks

db.drop_all()
db.create_all()


cardinals = Teams(team_name = 'Cardinals', team_city='Arizona')
falcons = Teams(team_name = 'Falcons', team_city='Atlanta')
ravens = Teams(team_name = 'Ravens', team_city='Baltimore')
bills = Teams(team_name = 'Bills', team_city='Buffalo')
bengals = Teams(team_name = 'Bengals', team_city='Cincinnati')
browns = Teams(team_name = 'Browns', team_city='Cleveland')
panthers = Teams(team_name = 'Panthers', team_city='Carolina')
bears = Teams(team_name = 'Bears', team_city='Chicago')
cowboys = Teams(team_name = 'Cowboys', team_city='Dallas')
broncos = Teams(team_name = 'Broncos', team_city='Denver')
lions = Teams(team_name = 'Lions', team_city='Detroit')
packers = Teams(team_name = 'Packers', team_city='Green Bay')
texans = Teams(team_name = 'Texans', team_city='Heuston')
colts = Teams(team_name = 'Colts', team_city='Indianapolis')
jaguars = Teams(team_name = 'Jaguars', team_city='Jacksonville')
chiefs = Teams(team_name = 'Chiefs', team_city='Kansas City')
raiders = Teams(team_name = 'Raiders', team_city='Las Vegas')
chargers = Teams(team_name = 'Chargers', team_city='Los Angeles')
rams = Teams(team_name = 'Rams', team_city='Los Angeles')
dolphins = Teams(team_name = 'Dolphins', team_city='Miami')
vikings = Teams(team_name = 'Vikings', team_city='Minnesota')
patriots = Teams(team_name = 'Patriots', team_city='New England')
saints = Teams(team_name = 'Saints', team_city='New Orleans')
giants = Teams(team_name = 'Giants', team_city='New York')
jets = Teams(team_name = 'Jets', team_city='New York')
eagles = Teams(team_name = 'Eagles', team_city='Philadelphia')
steelers = Teams(team_name = 'Steelers', team_city='Pittsburgh')
niners = Teams(team_name = '49ers', team_city='San Francisco')
seahawks = Teams(team_name = 'Seahawks', team_city='Seattle')
buccaneers = Teams(team_name = 'Buccaneers', team_city='Tampa Bay')
titans = Teams(team_name = 'Titans', team_city='Tennessee')
commanders = Teams(team_name = 'Commanders', team_city='Washington')



teams = [cardinals,falcons,ravens,bills,bengals,browns,panthers,bears,cowboys,broncos,lions,packers,texans,colts,jaguars,chiefs,raiders,chargers,rams,dolphins,vikings,patriots,saints,giants,jets,eagles,steelers,niners,seahawks,buccaneers,titans,commanders]
for team in teams:
    db.session.add(team)
db.session.commit()

games = []
#week 1
games.append(Games(home_team = rams.id , away_team = bills.id, week_no = 1))
# liosea1 = Games(home_team = lions , away_team = eagles, week_no = 1)
# beanin1 = Games(home_team =  bears, away_team = niners , week_no = 1)
# benste1 = Games(home_team = bengals , away_team = steelers, week_no = 1)
# dolpat1 = Games(home_team = dolphins , away_team = patriots, week_no = 1)
# panbrw1 = Games(home_team =  panthers, away_team = browns, week_no = 1)
# texcol1 = Games(home_team =  texans, away_team = colts, week_no = 1)
# comjag1 = Games(home_team = commanders , away_team = jaguars, week_no = 1)
# falsai1 = Games(home_team = falcons , away_team = saints , week_no = 1)
# jetrav1 = Games(home_team = jets , away_team = ravens, week_no = 1)
# vikpac1 = Games(home_team =  vikings, away_team = packers, week_no = 1)
# titgia1 = Games(home_team = titans , away_team = giants, week_no = 1)
# charai1 = Games(home_team = chargers , away_team = raiders, week_no = 1)
# carchi1 = Games(home_team = cardinals , away_team = chiefs, week_no = 1)
# cowbuc1 = Games(home_team =  cowboys, away_team = buccaneers, week_no = 1)
# seabro1 = Games(home_team =  seahawks, away_team = broncos, week_no = 1)

# #week2
# chicha2 = Games(home_team = chiefs, away_team = chargers, week_no = 2)
# stepat2 = Games(home_team = steelers, away_team = patriots, week_no = 2)
# giapan2 = Games(home_team = giants, away_team = panthers, week_no = 2)
# brwjet2 = Games(home_team = browns, away_team = jets, week_no = 2)
# jagcol2 = Games(home_team = jaguars, away_team = colts, week_no = 2)
# ravdol2 = Games(home_team = ravens, away_team = dolphins, week_no = 2)
# saibuc2 = Games(home_team = saints, away_team = buccaneers, week_no = 2)
# liocom2 = Games(home_team = lions, away_team = commanders, week_no = 2)
# ramfal2 = Games(home_team = rams, away_team = falcons , week_no = 2)
# ninsea2 = Games(home_team = niners, away_team = seahawks , week_no = 2)
# raicar2 = Games(home_team = raiders, away_team = cardinals, week_no = 2)
# brotex2 = Games(home_team = broncos, away_team = texans, week_no = 2)
# cowben2 = Games(home_team = cowboys, away_team = bengals, week_no = 2)
# pacbea2 = Games(home_team = packers, away_team = bears, week_no = 2)
# biltit2 = Games(home_team = bills, away_team = titans, week_no = 2)
# eagvik2 = Games(home_team = eagles, away_team = vikings , week_no = 2)

#week3
#chicha2 = Games(home_team = , away_team = , week_no = 3)

for game in games:
    db.session.add(game)
db.session.commit()