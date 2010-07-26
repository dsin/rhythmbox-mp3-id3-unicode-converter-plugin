import rb, rhythmdb

def detect_charset(s):
        charsets = ('tis-620', 'utf-8')
        for charset in charsets:
                try:
                        return unicode(s.encode('iso-8859-1'), charset)
                except:
                        continue                
        return s

class Id3UnicodePlugin (rb.Plugin):
    def __init__(self):
        rb.Plugin.__init__(self)
    def activate(self, shell):
        self.shell = shell
        self.db = shell.props.db
        self.db.connect("entry_added", self.on_entry_added)

    def on_entry_added(self, _tree, entry):
        self.type_song = self.db.entry_type_get_by_name("song")
        type=entry.get_entry_type()
        if type==self.type_song:
         title = self.db.entry_get(entry, rhythmdb.PROP_TITLE)
         artist = self.db.entry_get(entry, rhythmdb.PROP_ARTIST)
         album = self.db.entry_get(entry, rhythmdb.PROP_ALBUM)
         genre = self.db.entry_get(entry, rhythmdb.PROP_GENRE)

         self.db.set(entry, rhythmdb.PROP_TITLE, detect_charset(title))
         self.db.set(entry, rhythmdb.PROP_ARTIST, detect_charset(artist))
         self.db.set(entry, rhythmdb.PROP_ALBUM, detect_charset(album))
         self.db.set(entry, rhythmdb.PROP_GENRE, detect_charset(genre))