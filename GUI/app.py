from gui.base_frame import BaseFrame
import tkinter as tk
from gui.const_gui import (
    APP_TITLE,
    APP_SIZE_WIDTH,
    APP_SIZE_HEIGHT,
)

class Application(tk.Tk):
    '''
    トップレベルウィンドウ
    ・tk.Tkを継承
    '''
    
    def __init__(self):
        '''コンストラクタ'''
        tk.Tk.__init__(self)
        
        #タイトル設定
        self.title(APP_TITLE)
        
        #拡大ボタン無効化
        self.resizable(0,0)
        
        #中央配置
        pc_screen_height = self.winfo_screenheight()
        pc_screen_width = self.winfo_screenwidth()
        width = int(pc_screen_width/2 - APP_SIZE_WIDTH/2)
        height = int(pc_screen_height/2 - APP_SIZE_HEIGHT/2)
        self.geometry(f'{APP_SIZE_WIDTH}x{APP_SIZE_HEIGHT}+{width}+{height}')
        
        #Screen配置
        BaseFrame(self).grid()

    