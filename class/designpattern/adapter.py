#
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-15 16:53:49
# @LastEditors: llseng
# @LastEditTime: 2021-04-15 17:38:27
#

from abc import ABCMeta, abstractmethod

class MediaPlayer( metaclass=ABCMeta ):
    """
    媒体播放器接口
    """
    @abstractmethod
    def play( self, audioType, fileName ):
        pass
    
class AdvancedMediaPlayer( metaclass=ABCMeta ):
    """
    高级媒体播放器接口
    """
    @abstractmethod
    def playVlc( self, fileName ):
        pass

    @abstractmethod
    def playMp4( self, fileName ):
        pass

class VlcPlayer( AdvancedMediaPlayer ):
    """
    Vlc播放器
    """
    def playVlc( self, fileName ):
        print( "Playing Vlc file. file: ", fileName )
    
    def playMp4( self, fileName ):
        # print( "Playing Mp4 file. file: ", fileName )
        pass

class Mp4Player( AdvancedMediaPlayer ):
    """
    Mp4播放器
    """
    def playVlc( self, fileName ):
        # print( "Playing Vlc file. file: ", fileName )
        pass
    
    def playMp4( self, fileName ):
        print( "Playing Mp4 file. file: ", fileName )

class MediaAdapter( MediaPlayer ):
    """
    媒体适配器
    """
    def __init__(self, audioType):
        self._advMediaPlayer = None
        if audioType == "vlc":
            self._advMediaPlayer = VlcPlayer()
        elif audioType == "mp4":
            self._advMediaPlayer = Mp4Player()
        super().__init__()
    def play(self, audioType, fileName):
        if audioType == "vlc":
            self._advMediaPlayer.playVlc( fileName )
        elif audioType == "mp4":
            self._advMediaPlayer.playMp4( fileName )

class AudioPlayer( MediaPlayer ):
    """
    实体类
    """
    def play(self, audioType, fileName):
        if audioType == "mp3":
            print( "Playing Mp3 file. file: ", fileName )
        elif audioType == "mp4" or audioType == "vlc":
            adpter = MediaAdapter(audioType)
            adpter.play(audioType, fileName)
        else:
            print("Invalid media.", audioType, "format not supported")


if __name__ == "__main__":
    player = AudioPlayer()
    
    player.play( "vlc", "vvvvv.vlc" )
    player.play( "mp3", "wwwww.mp3" )
    player.play( "mp4", "mmmmm.mp4" )
    player.play( "avi", "aaaaa.avi" )
