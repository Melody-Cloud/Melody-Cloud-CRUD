from models import Artist, Album, Song, Tag

# Artists
# https://data.whicdn.com/images/310209005/large.jpg
peep = Artist(name='Lil Peep', artistDescription="Gustav Åhr (November 1, 1996 – November 15, 2017), better known by his stage name Lil Peep, was an American rapper and singer from Long Beach, Long Island, New York")
peep.save()

tha_kid = Artist(name='Th@ Kid', artistDescription="Elmo Kennedy O'Connor (born January 11th, 1994), better known as “Bones” (formerly known as “Th@ Kid”), is an underground rapper from Muir Beach, CA. He is one of the four members of the “Seshollowaterboyz” and has actively released music under several other aliases, such as: surrenderdorthy, OREGONTRAIL")
tha_kid.save()

john_denver = Artist(name='John Denver', artistDescription="American singer-songwriter, record producer, actor, activist, and humanitarian, whose greatest commercial success was as a solo singer.")
john_denver.save()


# Albums
crybaby = Album(artistId=peep, albumName='Crybaby', albumDescription='Crybaby is a mixtape by LiL PEEP, released at the 10th of June, 2016. It features GOTHBOICLIQUE members WICCA PHASE SPRINGS ETERNAL, Cold Hart, and Lil Tracy.')
crybaby.save()
# Songs
crybaby_song = Song(artistId=peep, albumId=crybaby, name='Crybaby', musicSrcUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/Crybaby.mp3', waveformImgUrl='https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/Crybaby.mp3.png', amountOfPlays=12131, amountOfLikes=1001, description='First song')
crybaby_song.save()
# Tags
rap_tag = Tag(songId=crybaby_song, songTag='Rap')
crybaby_tag = Tag(songId=crybaby_song, songTag='Crybaby')

rap_tag.save()
crybaby_tag.save()
