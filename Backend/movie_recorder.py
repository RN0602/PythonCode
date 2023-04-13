import threading
from datetime import datetime
import cv2
import gc


class MovieRecorder:
    '''Webカメラ制御'''
    
    #定数
    DISPOSE_INTERVAL = 10    #sec
    MOVIE_FILE_EXTS = '.mp4'
    MOVIE_FILE_DATE_FORMAT = '%Y%m%d%H%M%S'
    MOVIE_TITLE = 'Video Capture'
    
    def __init__(self, camera_num:int, recording_time, fps, frame_width, frame_height):
        '''コンストラクタ'''
        self.camera = cv2.VideoCapture(camera_num)
        self.fps = fps
        self.resolution = (frame_width, frame_height)
        self._set_setting(fps, frame_width, frame_height)
        self.recording_time = recording_time
        self.save_flg = False
        self.frame_lst = list()
        self.is_connected = True
    
    def _get_setting(self):
        '''Webカメラから設定を取得'''
        fps = int(self.camera.get(cv2.CAP_PROP_FPS))                # カメラのFPS
        w = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))          # カメラの横幅
        h = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))         # カメラの縦幅
        return fps, w, h
    
    def _set_setting(self, fps:int, width:int, height:int):
        '''Webカメラの設定'''
        self.camera.set(cv2.CAP_PROP_FPS, fps)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
    def execute(self, save_file_name:str):
        '''映像出力及び録画'''
        gc_cnt = 0
        movie_save_cnt = 0
        
        #カメラが接続されているか確認
        if not self.camera.isOpened():
            self.is_connected = False
            return
        
        while True:
            #フレームを取得
            ret, frame = self.camera.read()
            gc_cnt += 1
            
            #途中でフレームが取得できなくなった場合
            if not ret: return
            
            #一定時間経過後にgcを実行
            if gc_cnt > self.fps * self.DISPOSE_INTERVAL:
                gc_cnt = 0
                self.dispose()
            
            #フレームリストに格納し要素が一定以上であれば古いフレームは捨てる
            self.frame_lst.append(frame)
            if len(self.frame_lst) > self.fps * self.recording_time:
                self.frame_lst.pop(0)
                self.dispose()
            
            #セーブ処理
            if self.save_flg:
                movie_save_cnt += 1
                #指定秒数経過後にセーブを実行
                if movie_save_cnt > self.fps * self.recording_time / 2:
                    movie_save_cnt = 0
                    self.save_flg = False
                    movie_file_name = save_file_name + datetime.now().strftime(self.MOVIE_FILE_DATE_FORMAT) + self.MOVIE_FILE_EXTS
                    threading.Thread(target=self._save, args=(movie_file_name,)).start()
                    
            #映像に出力
            cv2.imshow(self.MOVIE_TITLE, frame)
            cv2.waitKey(1)

    def _save(self, filename:str):
        '''動画をMP4形式で保存'''
        #保存するフレームがあるか確認
        if not self.frame_lst:
            raise Exception
        
        #圧縮処理の形式を指定
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        video_writer = cv2.VideoWriter(
            filename, fourcc, self.fps, self.resolution
        )
        
        #フレームを一括保存
        for frame in self.frame_lst:
            video_writer.write(frame)
        video_writer.release()
    
    def release(self):    
        #カメラを解放
        self.camera.release()
        cv2.destroyAllWindows()
        self.dispose()
    
    def movie_save(self):
        self.save_flg = True
    
    def dispose(self):
        gc.collect()
