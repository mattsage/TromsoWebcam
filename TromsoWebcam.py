import urllib 
import time
import datetime
import os
#from pushbullet.pushbullet import PushBullet

#apiKey = "apikey"
#p = PushBullet(apiKey)
#devices = p.getDevices()

count = 0

while count < 48: #48 due to photo every 30 mins e.g. 30*48/60 = 24 hours
  #Grab Photos from University of Tromso, SkyCam and AmiHotel
	urllib.urlretrieve("http://weather.cs.uit.no/wcam0_snapshots/wcam0_latest_small.jpg", "file.jpg")
	urllib.urlretrieve("http://polaris.nipr.ac.jp/~acaurora/aurora/Tromso/latest.jpg", "file2.jpg")
	urllib.urlretrieve("http://www.amihotel.no/webcamera/broadcast.jpg", "file3.jpg")
	
  #convert names to Date Stamp
	os.rename("file.jpg", time.strftime("uni_%Y%m%d%H%M.jpg"))
	os.rename("file2.jpg", time.strftime("sky_%Y%m%d%H%M.jpg"))
	os.rename("file3.jpg", time.strftime("amihotel_%Y%m%d%H%M.jpg"))

	count = count + 1 #Increase count
	print ("%d photos taken") % count
	time.sleep( 1800 ) #sleep for 1800 seconds (30 mins)

else:
	os.system("convert -delay 10 -loop 0 uni_*.jpg uni_%Y%m%d.gif")
	os.system("convert -delay 10 -loop 0 sky_*.jpg sky_%Y%m%d.gif")
	os.system("convert -delay 10 -loop 0 amihotel_*.jpg amihotel_%Y%m%d.gif")
	# p.pushNote(devices[0]["iden"], 'Pi Timelapse Complete', 'Shutting Down')
   	#os.system("sudo shutdown -h now")
	print ("Time Lapse Complete")
