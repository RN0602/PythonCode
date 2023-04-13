from gui.const_gui import *
import tkinter as tk

class PreviewFrame(tk.LabelFrame):
    '''
    Previewのラベルフレーム
    ・tk.LabelFrameを継承
    '''

    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, width=300, height=380,
                               text=LABEL_FRAME_TAG, relief=tk.GROOVE,
                               labelanchor='nw', bg='lavender'
                               )
        
        #フレームサイズの固定化
        self.grid_propagate(False)
        
        #子フレーム作成及び配置
        self.disp_frame = self.PreviewDisplayFrame(self)
        self.disp_frame.grid(padx=(10,10), pady=4)
    
    class PreviewDisplayFrame(tk.Frame):
        '''
        入力値を表示するフレーム
        ・InnnerClass
        ・tk.Frameを継承
        '''
        
        def __init__(self, master):
            tk.Frame.__init__(self, master, width=275, height=345,
                            relief=tk.GROOVE, bg=PREVIW_FRAME_BG, padx=10)
            
            #フレームサイズの固定化
            self.grid_propagate(False)

            #ウィジェット作成及び配置
            self._create_widget(self)
            self._place_widget()
        
        #ウィジェット作成
        def _create_widget(self, master):
            
            #ラベル
            self.label_regist_person = tk.Label(
                master, text=P_REGIST_PERSON, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_document_number = tk.Label(
                master, text=P_DOCUMENT_NUMBER, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_soft_version = tk.Label(
                master, text=P_SOFT_VERSION, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_svsoft_version = tk.Label(
                master, text=P_SVSOFT_VERSION, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_result_path = tk.Label(
                master, text=P_RESULT_PATH, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_usb_path = tk.Label(
                master, text=P_USB_PATH, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_control_number = tk.Label(
                master, text=P_CONTROL_NUMBER, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_evaluation_content = tk.Label(
                master, text=P_EVALUATION_CONTENTS, bg=PREVIW_FRAME_BG, 
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_type = tk.Label(
                master, text=P_TYPE, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_robot = tk.Label(
                master, text=P_ROBOT,bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_controller = tk.Label(
                master, text=P_CONTROLLER, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_applicate = tk.Label(
                master, text=P_APPLICATE, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_client = tk.Label(
                master, text=P_CUSTOMER, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            self.label_sheet_name = tk.Label(
                master, text=P_SHEET_NAME, bg=PREVIW_FRAME_BG,
                fg=PREVIW_FRAME_FG, width=12, anchor=tk.W, font=('Times New ike', 9)
            )
            
            #入力ボックス
            self.input_regist_person = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG, width=22, font=('Times New ike', 9)
            )
            self.input_document_number = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG, width=22, font=('Times New ike', 9)
            )
            self.input_soft_version = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_svsoft_version = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_result_path = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG, width=22, font=('Times New ike', 9)
            )
            self.input_usb_path = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG, width=22, font=('Times New ike', 9)
            )
            self.input_control_number = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_evaluation_content = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG, width=22, wraplength=145, font=('Times New ike', 9)
            )
            self.input_type = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_robot = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_controller = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_applicate = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_client = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
            self.input_sheet_name = tk.Label(
                master, text='', bg=PREVIW_FRAME_BG, fg=PREVIW_FRAME_FG,  width=22, font=('Times New ike', 9)
            )
                
        def _place_widget(self):
            '''ウィジェット配置'''
            self.label_regist_person.grid(row=0, column=0, pady=2)
            self.label_document_number.grid(row=1, column=0, pady=2)
            self.label_soft_version.grid(row=2, column=0, pady=2)
            self.label_svsoft_version.grid(row=3, column=0, pady=2)
            self.label_result_path.grid(row=4, column=0, pady=2)
            self.label_usb_path.grid(row=5, column=0, pady=2)
            self.label_control_number.grid(row=6, column=0, pady=2)
            self.label_evaluation_content.grid(row=7, column=0, pady=2)
            self.label_type.grid(row=8, column=0, pady=2)
            self.label_robot.grid(row=9, column=0, pady=2)
            self.label_controller.grid(row=10, column=0, pady=2)
            self.label_applicate.grid(row=11, column=0, pady=2)
            self.label_client.grid(row=12, column=0, pady=2)
            self.label_sheet_name.grid(row=13, column=0, pady=2)
            
            self.input_widgets = [
                self.input_regist_person,
                self.input_document_number,
                self.input_soft_version,
                self.input_svsoft_version,
                self.input_result_path,
                self.input_usb_path,
                self.input_control_number,
                self.input_evaluation_content,
                self.input_type,
                self.input_robot,
                self.input_controller,
                self.input_applicate,
                self.input_client,
                self.input_sheet_name,
            ]

            #ラベル配置
            for key, input in enumerate(self.input_widgets):
                input.grid(row=key, column=1)
            
        def display_value_clear(self):
            '''表示値をクリア'''
            for entry in self.input_widgets:
                entry.config(text='')
            