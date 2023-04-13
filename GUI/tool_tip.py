import tkinter as tk


class ToolTip:
    '''ツールチップクラス'''
    
    def __init__(self, widget:tk.Widget, text:str):
        self.widget = widget
        self.text = text
        self.id = None 
        self.tw = None 
        
        #イベントドリブン定義
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Motion>', self.motion)
        self.widget.bind('<Leave>', self.leave)
        
    def enter(self, event):
        '''マウスカーソルがウィジェットに入ったとき'''
        self.schedule()

    def leave(self, event):
        '''マウスカーソルがウィジェットから抜けたとき'''
        self.unschedule()
        self.id = self.widget.after(500, self.hideTooltip)
        
    def motion(self, event):
        '''マウスカーソルがウィジェット上を移動中のとき'''
        self.unschedule()
        self.schedule()
    
    def schedule(self):
        '''ToolTipの表示を制御'''
        if self.tw:
            return
        self.unschedule()
        #500msec後にツールチップを表示しidを受け取る
        self.id = self.widget.after(500, self.showTooltip)
    
    def unschedule(self):
        '''ToolTipの表示を制御'''
        id = self.id
        self.id = None
        if id:
            #after関数の発生待ちをキャンセル
            self.widget.after_cancel(id)
            
    def showTooltip(self):
        '''ToolTip表示'''
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
        
        #マウスカーソルの現在位置を取得
        x, y = self.widget.winfo_pointerxy()
        
        #サブウィンドウ作成
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        
        #サブウィンドウの作成位置を定義
        self.tw.geometry(f'+{x+10}+{y+10}')
        
        #サブウィンドウにラベル表示
        label = tk.Label(self.tw, text=self.text, background='lightyellow',
                         relief='solid', borderwidth=1, justify='left')
        label.pack(ipadx=10)
    
    def hideTooltip(self):
        '''ToolTip削除'''
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()       
        