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


path = '/home/nomythic/ScoutingWork/scouting_files'

# Grab files from tablet & delets it
subprocess.call("./grabNewScouting.sh")

# Parses csv files in scouting_files
for filename in glob.glob(os.path.join(path, '*.csv')):
	autoHighShot = 0
	autoLowShot = 0
	highShotTeleop = 0
	lowShotTeleop = 0
	teleopGears = 0
	gearsInAuto = 0
	didItClimb = 0
	matchNumber = 0
	teamNumber = 0
	comments = ""

	f = open(filename)
	csv_f = csv.reader(f)
	for row in csv_f:
		autoHighShot = row[0]
		autoLowShot = row[1]
		highShotTeleop = row[2]
		lowShotTeleop = row[3]	
		teleopGears = row[4]
		timerCount = row[5] 
		if row[6] == True:
			gearsInAuto = 1
		else:
			gearsInAuto = 0
		if row[7] == True:
			didItClimb = 1
		else:
			didItClimb = 0   
		matchNumber = row[8] 
		teamNumber = row[9] 
		comments = row[10]

		insertData = ("INSERT INTO scoutingData " "(teamNumber, matchNumber, aGearSuccess, aLowFuel, aHighFuel, tGearNumber, tLowFuel, tHighFuel, ClimbSuccess, climbTime, Comments)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		data = (teamNumber, matchNumber, gearsInAuto, autoLowShot, autoHighShot, teleopGears, lowShotTeleop, highShotTeleop, didItClimb, timerCount, comments)
		
		print('Team Number:  ', teamNumber)

		cur.execute(insertData,data)
		db.commit()
		
		print "ya goofed"	
		db.rollback()

		print "no idiots here"
		print 'Team Number: '+ teamNumber+ ' comments: '+ comments

	f.close()


# Moves csv's to backups
subprocess.call("./MoveCsv.sh")
