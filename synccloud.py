#!/usr/bin/env python3
import os
import sys
import rarfile
import threading
import time

class post_download:
	def delete_files(self,dw_path):
		del_com = 'rm -rf ' + dw_path
		print(del_com)
		os.system(del_com)

	def move_files(self,dw_path,dest,filerar):
		#if unrar_status:
		failure = 1
		files = os.listdir(dw_path)
		print('unrar ok')
		for file in files:
			print(file)
			if os.path.isdir(dw_path + file): #not file.endswith('.rar') and not file.endswith('.txt'):
				print(dw_path + file)
				filename = file.replace(" ","\ ")
				mv_com = 'mv ' + dw_path + filename + ' ' + dest + ' --verbose'
				print(mv_com)
				failure = os.system(mv_com)
		return failure


	def unrar_files(self,dw_path, dest):
		print(dw_path)
		print(dest)
		passw = 'www.compucalitv.com'
		files = os.listdir(dw_path)
		unrar_status = False
		#filename = ''
		failure = 0
		for file in files:
			if 'part01.rar' in file.lower() or 'part1.rar' in file.lower():
				print(dw_path + file)
				rf = rarfile.RarFile(dw_path + file)
				rf.extractall(dw_path,None,passw)
				unrar_status=True
				#filename = file[:5]
				failure = failure + self.move_files(dw_path,dest,'')
				#break

		#if unrar_status == False:
		for file in files:
			if file.endswith('.rar') and 'part' not in file.lower():
				print(dw_path + file)
				rf = rarfile.RarFile(dw_path + file)
				rf.extractall(dw_path,None,passw)
				unrar_status=True
				#filename = file[:5]
				#break
				failure = failure + self.move_files(dw_path,dest,file)

		if failure == 0:
		    self.delete_files(dw_path)

def download_files(orig, dest):
    print(orig)
    print(dest)
    dw_path = 'downloads/' + orig + '/'
    dw_com = 'rclone sync remfichier:' + orig + ' ' + dw_path + ' --bwlimit=1M -P'
    print(dw_com)
    time.sleep(3)
    os.system(dw_com)
    pd = post_download()
    thread = threading.Thread(target=pd.unrar_files,args=([dw_path,dest]))
    thread.daemon = True
    thread.start()
    print('download ok')
    #unrar_files(dw_path, dest + orig)



download_files(sys.argv[1], sys.argv[2])
