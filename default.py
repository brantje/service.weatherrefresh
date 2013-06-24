import xbmc
import xbmcaddon
import time
__addon__      = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')


while True: 
	line1 = "Weather updated"
	thetime = 5000  #in miliseconds
	#xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, thetime, __icon__))
	xbmc.executebuiltin('Weather.Refresh')
	time.sleep( 900 )