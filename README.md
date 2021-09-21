# DemonCord-Music

## Setting it up with repl.it

Open <a href="https://repl.it/~">repl.it</a> and click on create new repl and then selcet Java in languages section and write any name and create.

Then go to shell and type `git clone https://github.com/DemonKingSwarn/DemonCord-Music.git`.

Then again go to  shell and type `chmod u+X install.sh` 

then type `./install.sh` in the shell itself, it will download the required .jar file for the bot.

After that open the `config.txt` file and put your bot's token and your user id at their respective places, also make sure to change the prefix.

and then run the repl, you will get the web url which you need to paste in `stay_alive.py`.

Then to run the bot type `chmod u+x run.sh` in shell and then `./run.sh`.

To make it 24/7, copy the web url and go to  <a  href="https://uptimerobot.com">uptimerobot</a> and create a new https monitor and paste that url there and click create. 

If your bot isn't in the server already then you will get the invite url in `nohup.out` file.

## Features
  * Easy to run (just make sure Java is installed, and run!)
  * Fast loading of songs
  * No external keys needed (besides a Discord Bot token)
  * Smooth playback
  * Server-specific setup for the "DJ" role that can moderate the music
  * Clean and beautiful menus
  * Supports many sites, including Youtube, Soundcloud, and more
  * Supports many online radio/streams
  * Supports local files
  * Playlist support (both web/youtube, and local)

## Supported sources and formats
DemonCord Music supports all sources and formats supported by [lavaplayer](https://github.com/sedmelluq/lavaplayer#supported-formats):
### Sources
  * YouTube
  * SoundCloud
  * Bandcamp
  * Vimeo
  * Twitch streams
  * Local files
  * HTTP URLs
### Formats
  * MP3
  * FLAC
  * WAV
  * Matroska/WebM (AAC, Opus or Vorbis codecs)
  * MP4/M4A (AAC codec)
  * OGG streams (Opus, Vorbis and FLAC codecs)
  * AAC streams
  * Stream playlists (M3U and PLS)

## Editing
This bot (and the source code here) might not be easy to edit for inexperienced programmers. The main purpose of having the source public is to show the capabilities of the libraries, to allow others to understand how the bot works, and to allow those knowledgeable about java, JDA, and Discord bot development to contribute. There are many requirements and dependencies required to edit and compile it, and there will not be support provided for people looking to make changes on their own. Instead, consider making a feature request (see the above section). If you choose to make edits, please do so in accordance with the Apache 2.0 License.
 
