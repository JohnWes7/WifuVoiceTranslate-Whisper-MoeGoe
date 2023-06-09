import threading
import time

class input_thread(threading.Thread):
    def __init__(self, threadname, keylist : list[str]) -> None:
        super().__init__(name='线程' + threadname)

        self.keydict = {}
        for i in keylist:
            self.keydict[i] = False
        # print(self.keydict)

        self.stop_flag = False

    
    def run(self) -> None:
        while not self.stop_flag:
            uinp = input()
            # print(uinp)

            for i in self.keydict.keys():
                if uinp == i:
                    self.keydict[i] = not self.keydict[i]

            print(self.keydict)
            time.sleep(0.1)
    
    def stop(self):
        self.stop_flag = True
    
    def get(self, key):
        return self.keydict.get(key)


if __name__ == "__main__":

    keylist = ["", "q"]
    inp_thr = input_thread("inputA", keylist)
    inp_thr.start()
    while True:
        is_recording = False

        while inp_thr.get(keylist[0]) and not inp_thr.get(keylist[1]):
            if is_recording == False:
                is_recording = True
                print("开始录制")
            
            print("录制中")

        if is_recording and inp_thr.get(keylist[0]) == False:
            print("录制结束")
            print("开始储存")
        
        if inp_thr.get(keylist[1]):
            break
        
        time.sleep(0.1)
    
    inp_thr.stop()
    print("done")
    

