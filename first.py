from plexapi.server import PlexServer

baseurl = 'plex server ip'
token='plex token'
plex = PlexServer(baseurl, token)

movies = plex.library.section('Ταινίες')
for movie in movies.all():
    movie = movie.reload()
    for subtitle in movie.subtitleStreams():
     if subtitle.languageCode=="gre" and subtitle.selected==True and not "(Ελληνικά)" in movie.title:
         test = {'title.value': movie.title+" (Ελληνικά)"}
         movie.edit(**test)
         movie.reload






