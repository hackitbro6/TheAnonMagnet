
from torrentp import TorrentDownloader
x =  ${{ github.event.inputs.link }}
torrent_file = TorrentDownloader(x , '.')
torrent_file.start_download()
