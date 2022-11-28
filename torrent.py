
from torrentp import TorrentDownloader
x =  ${{ github.event.inputs.Token }}
torrent_file = TorrentDownloader(x , '.')
torrent_file.start_download()
