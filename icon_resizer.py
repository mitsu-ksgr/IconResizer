#! /usr/bin/env python
# coding: utf-8

"""
icon_resizer.py
指定したアイコン画像から、Android/iOS用のアイコン画像を生成する。

！！！ 注意 ！！！
動作環境：
    python 2.7.3
    Pillowがインストールされている事(http://pypi.python.org/pypi/Pillow)
        $ pip install pillow

使い方：
$python icon_resizer.py src_icon_file_name.png

ソースとなるアイコン画像のサイズはなんでも大丈夫。
ただし、1024x1024若しくは最低でも512x512でないと、出力ファイルは劣化する。
"""


import sys
import os
from PIL import Image

"""-------------------------------------------------------------------
Icon Info Class
-------------------------------------------------------------------"""
class IconInfo :
    """
    アイコン情報を格納するクラス.
    ファイル名及びサイズを指定してインスタンスを生成する。
    基本的に、指定するファイル名にディレクトリ名は含ませない。
    各OS毎のディレクトリ直下に更にディレクトリを挟みたい場合は、
    ファイル名にOSディレクトリ配下に置きたいディレクトリの名前を含むパスを指定市
    create_dir4genicon()メソッドで対応するOSを判別し、
    配置したいディレクトリを生成しておく。
    """

    def __init__( self, file_name, width, height = -1 ) :
        """
        初期化メソッド。
        ファイル名、サイズを指定する。
        width, heightを分けて指定してもいいが、片方だけの指定でもいい。
        その場合、指定したサイズの辺を持つ正方形のアイコンとして設定される。
        """
        self.filename = file_name
        self.width = width
        self.height = height if height != -1 else width

    def generate( self, src_icon, dir ) :
        """
        設定されているプロパティの情報を元にアイコン画像を生成する
        """
        fpath = dir + os.sep + self.filename
        print "icon file: %-60s" % ( fpath ),

        # thumnail版：画像オブジェクト自体を書き換えるので注意！(保存ファイル名が違えば上書きされない)
        # >> 1度resize()でソースと同じサイズの画像オブジェクトを生成し、それを操作する。
        # 正方形以外はサムネイルで処理する
        if self.width == self.height :
            dst_icon = src_icon.resize( src_icon.size )
            dst_icon.thumbnail( (self.width, self.height), Image.ANTIALIAS )
            dst_icon.save( fpath )

        # 正方形以外は、リサイズで処理する（サムネイルだと強制的に正方形になってしまう）
        else :  # resize()はジャギーで死にたくなるので基本使わないようにしたほうが良い？
            src_icon.resize( (self.width, self.height) ).save( fpath )

        print "\tgenerated!"


"""-------------------------------------------------------------------
Icon Data
-------------------------------------------------------------------"""
# Directory name
# for SmartPhone
GENERATE_TOP_DIR_NAME           = "ir_gen"
GENERATE_ANDROID_DIR_NAME       = "Android"
GENERATE_IOS_DIR_NAME           = "iOS"
GENERATE_WINDOWS_PHONE_7_NAME   = "WindowsPhone7"
GENERATE_BLACK_BERRY            = "BlackBerry"
# for PC
GENERATE_MAC_OS_X               = "MacOSX"
GENERATE_WINDOWS_XP             = "WindowsXP"
GENERATE_WINDOWS_8              = "Windows8"

# for Android
icon_info_android = []
icon_info_android.append( IconInfo("drawable-ldpi/icon.png", 36 ) )
icon_info_android.append( IconInfo("drawable-mdpi/icon.png", 48 ) )
icon_info_android.append( IconInfo("drawable-hdpi/icon.png", 72 ) )
icon_info_android.append( IconInfo("drawable-xhdpi/icon.png", 96 ) )
icon_info_android.append( IconInfo("drawable-xxhdpi/icon.png", 144 ) )
icon_info_android.append( IconInfo("market_icon.png", 512 ) )

# for iOS
icon_info_ios = []
icon_info_ios.append( IconInfo( "Icon.png", 57 ) )
icon_info_ios.append( IconInfo( "Icon@2x.png", 114 ) )
icon_info_ios.append( IconInfo( "Icon-72.png", 72 ) )
icon_info_ios.append( IconInfo( "Icon-72@x2.png", 144 ) )
icon_info_ios.append( IconInfo( "Icon-60.png", 60 ) )
icon_info_ios.append( IconInfo( "Icon-60@x2.png", 120 ) )
icon_info_ios.append( IconInfo( "Icon-Small.png", 29 ) )
icon_info_ios.append( IconInfo( "Icon-Small@2x.png", 58 ) )
icon_info_ios.append( IconInfo( "Icon-Small-40.png", 40 ) )
icon_info_ios.append( IconInfo( "Icon-Small-40@2x.png", 80 ) )
icon_info_ios.append( IconInfo( "Icon-Small-50.png", 50 ) )
icon_info_ios.append( IconInfo( "Icon-Small-50@2x.png", 100 ) )
icon_info_ios.append( IconInfo( "iTunesArtwork.png", 512 ) )
icon_info_ios.append( IconInfo( "iTunesArtwork@2x.png", 1024 ) )

# for windows phone 7
icon_info_windows_phone_7 = []
icon_info_windows_phone_7.append( IconInfo( "ApplicationIcon.png", 62 ) )
icon_info_windows_phone_7.append( IconInfo( "ApplicationTileImage.png", 173 ) )
icon_info_windows_phone_7.append( IconInfo( "MarketplaceCatalog_small.png", 99 ) )
icon_info_windows_phone_7.append( IconInfo( "MarketplaceCatalog_large.png", 173 ) )
icon_info_windows_phone_7.append( IconInfo( "MarketplaceCatalog.png", 200 ) )

# for BlackBerry
icon_info_black_berry = []
icon_info_black_berry.append( IconInfo( "icon.png", 48 ) )

# for Mac OS X
icon_info_mac_os_x = []
icon_info_mac_os_x.append( IconInfo( "icon_16x16.png", 16 ) )
icon_info_mac_os_x.append( IconInfo( "icon_16x16@2x.png", 32 ) )
icon_info_mac_os_x.append( IconInfo( "icon_32x32.png", 32 ) )
icon_info_mac_os_x.append( IconInfo( "icon_32x32@2x.png", 64 ) )
icon_info_mac_os_x.append( IconInfo( "icon_128x128.png", 128 ) )
icon_info_mac_os_x.append( IconInfo( "icon_128x128@2x.png", 256 ) )
icon_info_mac_os_x.append( IconInfo( "icon_256x256.png", 256 ) )
icon_info_mac_os_x.append( IconInfo( "icon_256x256@2x.png", 512 ) )
icon_info_mac_os_x.append( IconInfo( "icon_512x512.png", 512 ) )
icon_info_mac_os_x.append( IconInfo( "icon_512x512@2x.png", 1024 ) )

# for Windows XP
icon_info_windows_xp = []
icon_info_windows_xp.append( IconInfo( "icon48x48.png", 48 ) )
icon_info_windows_xp.append( IconInfo( "icon32x32.png", 32 ) )
icon_info_windows_xp.append( IconInfo( "icon24x24.png", 24 ) )
icon_info_windows_xp.append( IconInfo( "icon16x16.png", 16 ) )

# for Windows 8
icon_info_windows_8 = []
icon_info_windows_8.append( IconInfo( "icon620x300.png", 620, 300 ) )
icon_info_windows_8.append( IconInfo( "icon310x150.png", 310, 150 ) )
icon_info_windows_8.append( IconInfo( "icon150x150.png", 150, 150 ) )
icon_info_windows_8.append( IconInfo( "icon50x50.png", 50, 50 ) )
icon_info_windows_8.append( IconInfo( "icon30x30.png", 30, 30 ) )


# all icon info (要らないやつはコメントアウトして追加しないようにすればいい。)
icon_infos = []
icon_infos.append( (GENERATE_ANDROID_DIR_NAME, icon_info_android) )
icon_infos.append( (GENERATE_IOS_DIR_NAME, icon_info_ios) )
#icon_infos.append( (GENERATE_WINDOWS_PHONE_7_NAME, icon_info_windows_phone_7) )
#icon_infos.append( (GENERATE_BLACK_BERRY, icon_info_black_berry ) )
#icon_infos.append( (GENERATE_MAC_OS_X, icon_info_mac_os_x ) )
#icon_infos.append( (GENERATE_WINDOWS_XP, icon_info_windows_xp ) )
#icon_infos.append( (GENERATE_WINDOWS_8, icon_info_windows_8 ) )


"""-------------------------------------------------------------------
Methods
-------------------------------------------------------------------"""

def create_dir4genicon( dir_path ) :
    """
    生成したアイコンを格納するディレクトリを作成する。
    OS毎に、更にディレクトリを追加したい場合は、ここで個別に作成する。
    """
    if  os.path.exists( dir_path ) : return

    # ディレクトリを生成
    os.mkdir( dir_path )
    print "mkdir :" + dir_path

    # Androidの場合は、各解像度用のディレクトリも生成する
    if GENERATE_ANDROID_DIR_NAME in dir_path :
        os.mkdir( dir_path + os.sep + "drawable-ldpi" )
        os.mkdir( dir_path + os.sep + "drawable-mdpi" )
        os.mkdir( dir_path + os.sep + "drawable-hdpi" )
        os.mkdir( dir_path + os.sep + "drawable-xhdpi" )
        os.mkdir( dir_path + os.sep + "drawable-xxhdpi" )
        print "mkdir : drawable directories."


"""-------------------------------------------------------------------
Entry Point. argv = [bg_thin_converter.py, src_icon_file.png
-------------------------------------------------------------------"""
if __name__ != "__main__" : exit()

# 引数エラー
if len(sys.argv) < 2 :
    print "argment error: icon_resizer needs src icon file."
    print "$ python icon_resizer.py SRC_ICON_FILE_NAME.png"
    exit()

src_file_name = sys.argv[1]     # 引数を受け取る

# 引数チェック(png以外は弾く)
if not ".png" in src_file_name :
    print "src file error: src file must be png format."
    print "input file name [", src_file_name, "]"
    exit()


# 生成ファイルの出力先ディレクトリを生成
top_dir_path = os.curdir + os.sep + GENERATE_TOP_DIR_NAME
if not os.path.exists( top_dir_path ) :
    os.mkdir( top_dir_path )
    print "mkdir :" + top_dir_path

# アイコンのソースイメージを生成
src_icon = Image.open( src_file_name )
print "-" * 30
print "src file name : " + src_file_name
print "         size : " + str(src_icon.size[0]) + "x" + str(src_icon.size[1])
print "-" * 30

# アイコンを生成するß
for infos in icon_infos :
    print "type : " + infos[0]
    gen_path = top_dir_path + os.sep + infos[0]

    # アイコン格納用ディレクトリを作成する
    create_dir4genicon( gen_path )

    # アイコンを生成する
    for icon in infos[1] : icon.generate( src_icon, gen_path )

    print ""    # 改行



