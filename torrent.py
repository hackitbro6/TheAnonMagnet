import os

input_variable = os.environ['MAIN_LINK']

from torrentp import TorrentDownloader
x =  (MAIN_LINK)
torrent_file = TorrentDownloader(x , '.')
torrent_file.start_download()
