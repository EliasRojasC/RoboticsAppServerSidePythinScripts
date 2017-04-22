import subprocess
import csv
import glob
import os
import MySQLdb

# Connect to database
db= MySQLdb.connect(host="localhost",
	                user="root",
	                passwd="2491",
	                db='nomythic-scouting')
cur = db.cursor()


path = '/home/nomythic/RoboticsAppServerSidePythonScripts-master/scouting_files'

# Grab files from tablet & delets it
subprocess.call("./grabNewScouting.sh")

# Parses csv files in scouting_files
for filename in glob.glob(os.path.join(path, '*.csv')):
	autoFuelPoints = 0
	teleopFuelPoints = 0
	lowShotTeleop = 0
	teleopGears = 0
	gearsInAuto = 0
	didItClimb = 0
	matchNumber = 0
	teamNumber = 0
	comments = ""
	sliderMeme = 0
	gearPickerUper = 0

	f = open(filename)
	csv_f = csv.reader(f)
	for row in csv_f:
		autoFuelPoints = row[0]
		teleopFuelPoints = row[1]
		teleopGears = row[2]
		timerCount = row[3] 
		if row[4] == " true":
			gearsInAuto = 1
		else:
			gearsInAuto = 0
		if row[5] == " true":
			didItClimb = 1
		else:
			didItClimb = 0   
		matchNumber = row[6] 
		teamNumber = row[7] 
		comments = row[8]
		sliderMeme = row[9]
		if row [10] == " true":
			gearPickerUper = 1
		else:
			gearPickerUper =0

		insertData = ("INSERT INTO scoutingData " "(teamNumber, matchNumber, aGearSuccess, aAllFuel, tGearNumber, tAllFuel, ClimbSuccess, climbTime, Comments, defense, pickUpGear)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		data = (teamNumber, matchNumber, gearsInAuto, autoFuelPoints, teleopGears, teleopFuelPoints, didItClimb, timerCount, comments, sliderMeme, gearPickerUper)
		
		print('Team Number:  ', teamNumber,' gearsInAuto ', gearsInAuto)

		cur.execute(insertData,data)
		db.commit()
		
		print "ya goofed"	
		db.rollback()

		print "no idiots here"
		print 'Team Number: '+ teamNumber+ ' comments: '+ comments

	f.close()


# Moves csv's  to backups
subprocess.call("./MoveCsv.sh")