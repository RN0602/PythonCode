import concurrent.futures


class ParallelProcessExecutor:
    '''複数プロセスの制御'''
    
    def __init__(self, func_args_lst):
        '''コンストラクタ'''
        self.executor = concurrent.futures.ProcessPoolExecutor()
        self.func_args_lst = func_args_lst
        self.results:list = []
    
    def __del__(self):
        '''デストラクタ'''
        self.executor.shutdown(wait=True)
        self.results = None
    
    def execute(self):
        '''複数プロセスの実行'''
        with self.executor:
            
            #各プロセスをプールに登録
            future_results = {self.executor.submit(func, *args): args for func, args in self.func_args_lst}
            
            for future in concurrent.futures.as_completed(future_results):
                try:
                    #各プロセスが終了するまで待機        
                    result = future.result()
                except Exception:
                    #他プロセスのキャンセル
                    for f in future_results:
                        f.cancel()
                    break
                else:
                    #各プロセスの戻り値を格納
                    self.results.append(result)
        
        return self.results
