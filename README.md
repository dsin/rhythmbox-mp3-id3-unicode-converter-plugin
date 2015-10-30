Rhythmbox MP3 ID3 Unicode Convertor ( Rhythmbox Plugin ) BETA
==========

Deprecated
-------------------------
This project is no longer support by developer.

Introduction
-------------------------
This is Rhythmbox(https://wiki.gnome.org/Apps/Rhythmbox) Plugin that convert unreadable id3 tag to readable utf-8 id3 tag on-the-fly.

Which languages are supported right now ?
-------------------------
tis-620 : Thai language ( ภาษาไทย )
windows-1250 (https://en.wikipedia.org/wiki/Windows-1250) : Central European and Eastern European languages that use Latin script, such as Polish, Czech, Slovak, Hungarian, Slovene, Bosnian, Croatian, Serbian, Romanian and Albanian. It may also be used with the German language
and others in the future

How it works
-------------------------
When you add your song to Rhythmbox's library, ID3 Unicode automatically converts the metadata of the song to UTF-8 and save back to the song and show the readable playlist. It's very natural and easy if we use Rhythmbox as a main music player. We just do the same way that we did.

Installation
-------------------------
1. extract id3unicode to `~/.gnome2/rhythmbox/plugins/`

If there are no plugins folder, just create it.

2. start Rhythmbox and enable "ID3 Unicode" at Edit > Plugins

3. enjoy your music

In ubuntu 10.10, the folder will be at `~/.local/share/rhythmbox` ? Thank you very much to supersasho (http://dsin.blogspot.com/2010/07/ubuntu-rhythmbox.html#c7062056600238517089) for this suggestion.

More encoding ?
-------------------------
Other than supporting encoding, this plugin can also convert other id3 metadata encoding.

You can simply add it to variable called 'charsets' by yourself.

However, please notify me about any other encoding, so that I can add it to the trunk. Then the other who face the same encoding problem do not need to do that again.

Thanks

Report a bug
-------------------------
This is a free software, so feel free to edit it. If you find a bug or any suggestion, please send it to myblog (http://dsin.blogspot.com/2010/07/ubuntu-rhythmbox.html)

What is New ?
-------------------------
Version v.2
ID3 is not overwritten anymore
We didn't override ID3 in your song anymore. The plugin just read the right encoding and display the readable one in the playlist.

Encoding Preferences
We added configure ui. You can choose the encoding from the preferences of the plugin.
