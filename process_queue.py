#!/usr/bin/env python3
import os
import time
import threading

class second_thread:
    def dosomthing(self, orig,delll):
        print('second thread')
        time.sleep(5)
        print('second thread 2')
        print(orig)
        print (delll)

def run_dw_comm(dw_item):
    dw_pars = dw_item.split(":")
    if len(dw_pars) > 1:
        sync_comm = 'python synccloud.py ' + dw_pars[0] + ' ' + dw_pars[1]
        print(sync_comm)
        os.system(sync_comm)
        time.sleep(1)
        st = second_thread()
        thread = threading.Thread(target=st.dosomthing,args=(['bye bye','get sine']))
        thread.daemon = True
        thread.start()



def process_queue():
    file_name = 'dw_queue'
    while True:
        file_object = open(file_name,'r')
        dw_list = file_object.readlines()
        if len(dw_list) > 0:
            dw_item = dw_list[0]
            dw_list.remove(dw_item)
            file_object.close()
            file_object = open(file_name,'w')
            file_object.writelines(dw_list)
            file_object.close()
            run_dw_comm(dw_item)  
        else:
            time.sleep(300)

process_queue()