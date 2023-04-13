from queue import Queue
import threading


class CloseableQueue(Queue):
    '''Queueを継承したクラス'''
    
    #クラス変数
    SENTINEL = object()
    
    def close(self):
        '''反復処理の停止'''
        self.put(self.SENTINEL)
        
    def __iter__(self):
        '''反復処理'''
        while True:
            #取得
            item = self.get()
            try:
                #停止
                if item is self.SENTINEL:
                    return
                
                #ジェネレータで呼び出し元へ返す
                yield item
            finally:
                #作業進捗を通知
                self.task_done()
    
    def execute(self):
        '''タスクを実行'''
        for func, *args in self:
            threading.Thread(target=func, args=(*args,)).start()

