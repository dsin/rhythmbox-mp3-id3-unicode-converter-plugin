import gobject, gtk
import gconf
from os import system, path

class Id3UnicodeConfigureDialog (object):
	def __init__(self, builder_file):
		gconf_keys = {'id3_encoding': "/apps/rhythmbox/plugins/id3unicode/id3_encoding"}

		self.gconf = gconf.client_get_default()
		self.gconf_keys = gconf_keys

		self.builder_file = builder_file

	def create_builder(self):
		builder = gtk.Builder()
		builder.add_from_file(self.builder_file)
		builder.connect_signals({"rb_id3_unicode_encoding_toggled_cb" : self.encoding_toggled})

		self.dialog = builder.get_object("preferences_dialog")
		self.dialog.connect("response", self.dialog_response)

		# set fields from gconf
		id3_encoding = self.get_prefs()
		if id3_encoding is None:
			id3_encoding = 'tis-620'
		builder.get_object("tis_620").set_active(id3_encoding == "tis-620")
		builder.get_object("windows_1250").set_active(id3_encoding == "windows-1250")

	def encoding_toggled(self, button):
			print "encoding radiobutton toggled: " + button.get_label()
			id3_encoding = {"tis-620": "tis-620", "windows-1250": "windows-1250"}
			if button.get_active():
					self.gconf.set_string(self.gconf_keys['id3_encoding'], id3_encoding[button.get_label()])

	def dialog_response(self, dialog, response):
			print 'response!'
			self.dialog.hide()

	def get_dialog (self):
		return self.dialog
	
	def get_prefs (self):
		id3_encoding = gconf.client_get_default().get_string(self.gconf_keys['id3_encoding'])

		print "id3_encoding: " + id3_encoding
		return id3_encoding

