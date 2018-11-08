import random
from models import Artist, Album, Song, Tag
import lorem

# Artists
# https://data.whicdn.com/images/310209005/large.jpg
peep = Artist(name='Lil Peep', artistDescription="Gustav Åhr (November 1, 1996 – November 15, 2017), better known by his stage name Lil Peep, was an American rapper and singer from Long Beach, Long Island, New York", artistImageUrl="https://data.whicdn.com/images/310209005/large.jpg")
peep.save()


tha_kid = Artist(name='Th@ Kid', artistDescription="Elmo Kennedy O'Connor (born January 11th, 1994), better known as “Bones” (formerly known as “Th@ Kid”), is an underground rapper from Muir Beach, CA. He is one of the four members of the “Seshollowaterboyz” and has actively released music under several other aliases, such as: surrenderdorthy, OREGONTRAIL", artistImageUrl="https://kidfromthe6ix.files.wordpress.com/2014/12/b3zhyc5cmaavwim-large.png")
tha_kid.save()

# john_denver = Artist(name='John Denver', artistDescription="American singer-songwriter, record producer, actor, activist, and humanitarian, whose greatest commercial success was as a solo singer.")
# john_denver.save()


# Albums
crybaby = Album(artistId=peep, albumName='Crybaby', albumDescription='Crybaby is a mixtape by LiL PEEP, released at the 10th of June, 2016. It features GOTHBOICLIQUE members WICCA PHASE SPRINGS ETERNAL, Cold Hart, and Lil Tracy.')
crybaby.save()
# Songs
crybaby_song = Song(artistId=peep, albumId=crybaby, name='Crybaby', musicSrc='https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/Crybaby.mp3', waveformImgUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/Crybaby.mp3.png', amountOfPlays=random.randint(10000, 100000), amountOfLikes=random.randint(1000, 10000), description='First song in the album', lyrics=lorem.text())
crybaby_song.save()

liljeep_song = Song(artistId=peep, albumId=crybaby, name='Lil Jeep', musicSrc='https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/LilJeep.mp3', waveformImgUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/LilJeep.mp3.png', amountOfPlays=random.randint(10000, 100000), amountOfLikes=random.randint(1000, 10000), description='Second song in the album', lyrics=lorem.text())
liljeep_song.save()

yesterday_song = Song(artistId=peep, albumId=crybaby, name='Yesterday', musicSrc='https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/Yesterday.mp3', waveformImgUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/Yesterday.mp3.png', amountOfPlays=random.randint(10000, 100000), amountOfLikes=random.randint(1000, 10000), description='Third song in the album', lyrics=lorem.text())
yesterday_song.save()

aid_song = Song(artistId=peep, albumId=crybaby, name='Absolute', musicSrc='https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/AbsoluteInDoubt.mp3', waveformImgUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/AbsoluteInDoubt.mp3.png', amountOfPlays=random.randint(10000, 100000), amountOfLikes=random.randint(1000, 10000), description='Fourth song in the album', lyrics=lorem.text())
aid_song.save()
# Tags
rap_tag = Tag(songId=crybaby_song, songTag='Rap')
sad_tag = Tag(songId=crybaby_song, songTag='Sad')

rap_tag.save()

rap_tag = Tag(songId=liljeep_song, songTag='Rap')
rap_tag.save()
chill_tag = Tag(songId=liljeep_song, songTag='Chill')
chill_tag.save()

tag = Tag(songId=yesterday_song, songTag='Rock')
tag.save()
tag = Tag(songId=yesterday_song, songTag='Dynamic')
tag.save()

rap_tag = Tag(songId=aid_song, songTag='Dynamic')
rap_tag.save()

sad_tag = Tag(songId=aid_song, songTag='Sad')
sad_tag.save()
