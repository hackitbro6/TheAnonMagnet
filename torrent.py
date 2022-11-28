import os
input_variable = os.environ['INPUT_STORE']

from torrentp import TorrentDownloader
x =  (input_variable)
torrent_file = TorrentDownloader(x , '.')
torrent_file.start_download()
