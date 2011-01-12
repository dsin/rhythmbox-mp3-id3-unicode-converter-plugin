import rb, rhythmdb, urllib
from Id3UnicodeConfigureDialog import Id3UnicodeConfigureDialog

def detect_charset(s, default_charset='tis-620'):
        print 'default charset : %s' % default_charset
        charsets = (default_charset, 'utf-8')
        for charset in charsets:
                try:
                        return unicode(s.encode('iso-8859-1'), charset)
                except:
                        continue   
        print 'use default charset'             
        return s

class Id3UnicodePlugin (rb.Plugin):
    def __init__(self):
        rb.Plugin.__init__(self)
    def activate(self, shell):
        self.shell = shell
        self.db = shell.props.db
        self.db.connect("entry_added", self.on_entry_added)

        builder_file = self.find_file("id3unicode-prefs.ui")
        self.id3_configure_dialog = Id3UnicodeConfigureDialog(builder_file)

        self.modified_entry = False

    def on_entry_added(self, _tree, entry):
        self.type_song = self.db.entry_type_get_by_name("song")
        type=entry.get_entry_type()
        if type==self.type_song:
         if not self.modified_entry :
                 song_location = urllib.unquote(self.db.entry_get(entry, rhythmdb.PROP_LOCATION))

                 try:
                         urllib.urlopen(song_location)
                 except :
                         print "file not found : %s" % song_location
                         return

                 title = self.db.entry_get(entry, rhythmdb.PROP_TITLE)
                 artist = self.db.entry_get(entry, rhythmdb.PROP_ARTIST)
                 album = self.db.entry_get(entry, rhythmdb.PROP_ALBUM)
                 genre = self.db.entry_get(entry, rhythmdb.PROP_GENRE)
                 print "%s %s %s %s" % (title, artist, album, genre)

                 self.db.entry_delete(entry)
                 self.db.commit()
                 
                 entry_new = self.db.entry_new(self.type_song, song_location)
                 self.db.set(entry_new, rhythmdb.PROP_TITLE, detect_charset(title, self.id3_configure_dialog.get_prefs()))
                 print 'set title'
                 self.db.set(entry_new, rhythmdb.PROP_ARTIST, detect_charset(artist, self.id3_configure_dialog.get_prefs()))
                 print 'set artist'
                 self.db.set(entry_new, rhythmdb.PROP_ALBUM, detect_charset(album, self.id3_configure_dialog.get_prefs()))
                 print 'set album'
                 self.db.set(entry_new, rhythmdb.PROP_GENRE, detect_charset(genre, self.id3_configure_dialog.get_prefs()))
                 print 'set genre'
                 self.db.commit()
                 self.modified_entry = True
         else :
                 self.modified_entry = False

    def create_configure_dialog(self, dialog=None):
        if not dialog:
                self.id3_configure_dialog.create_builder()
                dialog = self.id3_configure_dialog.get_dialog()
                dialog.present()
        return dialog
