import vlc
import pafy
import urllib.request

url = "/Your video link goes here/" #Links can be added through commits. Files will be made through file streaming to get the link for each video
video = pafy.new(url)
best = video.getbest()
playurl = best.url
ins = vlc.Instance()
player = ins.media_player_new()

code = urllib.request.urlopen(url).getcode()
if str(code).startswith('2') or str(code).startswith('3'):
    print('The video is working')
else:
    print('The video is broken or unavailable')

Media = ins.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()

good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
while str(player.get_state()) in good_states:
    print('The video is playing. Current state = {}'.format(player.get_state()))

print('The video is not playing. Current state = {}'.format(player.get_state()))
player.stop()
