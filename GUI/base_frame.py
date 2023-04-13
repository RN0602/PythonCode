from gui.preview_frame import PreviewFrame
from gui.input_item_frame import InpuItemFrame
from gui.button_frame import ButtonFrame
import tkinter as tk
from gui.const_gui import (
    APP_SIZE_WIDTH,
    APP_SIZE_HEIGHT,
    BASE_FRAME_BG
)


class BaseFrame(tk.Frame):
    '''
    ベースフレーム
    ・tk.Frameを継承
    '''
    
    def __init__(self, master):
        '''コンストラクタ'''
        tk.Frame.__init__(
            self,
            width = APP_SIZE_WIDTH,
            height = APP_SIZE_HEIGHT,
            borderwidth = 1,
            relief = tk.GROOVE,
            bg = BASE_FRAME_BG,
        )
        self.app = master
        
        #フレームサイズ固定化
        self.grid_propagate(False)
        
        #子フレームの作成及び配置
        self._create_frame()
        self._frame_place()
    
    def _create_frame(self):
        '''子フレームの作成'''
        self.preview_frame = PreviewFrame(self)
        self.input_item_frame = InpuItemFrame(self, self.preview_frame)
        self.button_frame = ButtonFrame(self, self.input_item_frame, self.preview_frame, self.app)
    
    def _frame_place(self):
        '''子フレームの配置'''
        self.input_item_frame.grid(row=0, column=0, padx=20, pady=15)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), sticky=tk.W)
        self.preview_frame.grid(row=0, column=1, rowspan=2, pady=(20,0))
