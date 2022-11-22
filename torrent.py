import sys
import time
import libtorrent as lt
#Create torrent
file = lt.file_storage()
lt.add_files(fs, "./prac.txt")
creat= lt.create_torrent(fs)
t.add_tracker("udp://tracker.openbittorrent.com:80/announce", 0)
t.set_creator('libtorrent %s' % lt.version)
t.set_comment("test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()    
file = open("myfile.torrent", "wb")
file.write(lt.bencode(torrent))
file.close()
#-------
session = lt.session()
session.listen_on(6881, 6891)
ja = session.add_torrent({'ti': lt.torrent_info('mytorrent.torrent'), 'save_path': '.', 'seed_mode': True}) 
print("Total size: ") + str(ja.status().total_wanted)
print("Name: ") + ja.name()   
while True:
    status = ja.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
      'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
      (status.progress * 100, status.download_rate / 1000, status.upload_rate / 1000, status.num_peers, state_str[status.state]))
    sys.stdout.flush()

    time.sleep(1)


