import os
link = os.environ["VAR"]
from torrentp import TorrentDownloader
x =  (link)
torrent_file = TorrentDownloader(x , '.')
torrent_file.start_download()
