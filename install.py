#! usr/bin/python2
####################################################################
#                               Color
B = "\033[34m"; Y = "\033[33m"; G = "\033[32m"; W = "\033[0m";R = "\033[31m";C = "\033[36m"
###################################################################
#                           Import Module
import sys , time , os , json , subprocess , commands
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
except ImportError:
    os.system('pip2 install requests')
    # print (B+"\n["+W+"="+B+"] "+G+"install requirements module success, run kembali\n")
    os.system('python2 '+sys.argv[0])
    sys.exit()
####################################################################
#                             Function
def execute(cmd):
    os.system(cmd)
def terminal_clear():
    os.system('clear')
def install(pkg):
    terminal_clear()
    print (Y+"INSTALL PKG... "+pkg+R+'\nexecute: '+Y+'pkg install '+pkg+' -y\n'+G)
    os.system('pkg install '+pkg+' -y')
def rename(awal,akhir):
    os.system('cd && mv '+awal+' '+akhir)
def move(awal,akhir):
    os.system('cd && mv '+awal+' '+akhir)
def buat_pintasan(awal,akhir):
    os.system('cd && ln -s '+awal+' '+akhir)
def mkdir(name):
    os.system('cd && mkdir '+name)
def wget(link):
    os.system('cd && wget '+link)
def unzip(link):
    os.system('cd && unzip '+link)
def rm(link):
    os.system('cd && rm '+link)
def rmrf(link):
    os.system('cd && rm -rf '+link)
def copy(awal,akhir):
    os.system('cd && cp '+awal+' '+akhir)
def git(link,rename):
    os.system('cd && git clone '+ link + " " + rename)

def kill_process(process):
    os.system("ps | grep "+process+" | killall -9 "+process)

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def get_info():
    t0 = time.time()
    try:
        print("Get info from database...")
        response = requests_retry_session().get("https://p34c3-khyrein.linuxploit.com/ngodingyuk/info/",timeout=5,headers={'User-Agent': 'Mozilla/5.0'})
        return json.loads(response.text)
    except Exception as x:
        print('It failed :( ' + x.__class__.__name__ + ', status:' + str(response.status_code) + '\ncontent:\n' + response.text)
        sys.exit()
    else:
        print('It eventually worked ' + response.status_code)
        sys.exit()
    finally:
        t1 = time.time()
        print('Time Took: ' + str(round(t1 - t0, 2)) + ' seconds')
        time.sleep(2)
def cek_local_info():
    nama_file = ""
    if sys.argv[0] == "install.py":
        nama_file = "info.json"
    else:
        nama_file = "../.ngodingyuk/info.json"
    with open(nama_file) as json_file:
        data = json.load(json_file)
        return data
def start_server():
    execute("nohup apachectl -k start                        > ~/.ngoding-debug/apache2.log          2>&1 &")
    execute("nohup php -S 0.0.0.0:8001 -t ~/.blackicecoder/  > ~/.ngoding-debug/blackicecoder.log    2>&1 &")
    execute("nohup php -S 0.0.0.0:8002 -t ~/.phpmyadmin/     > ~/.ngoding-debug/phpmyadmin.log       2>&1 &")
    execute("nohup php -S 0.0.0.0:8004 -t ~/.ngoding-debug/  > ~/.ngoding-debug/ngoding-debug.log    2>&1 &")
    execute("nohup mysqld_safe                               > ~/.ngoding-debug/mysqld_safe.log      2>&1 &")

def stop_server():
    kill_process("php")
    kill_process("mysqld_safe")
    kill_process("mariadbd")
    execute("nohup apachectl -k stop > ~/.ngoding-debug/apache2.log 2>&1 &")

def findThisProcess( process_name ):
    ps     = subprocess.Popen("ps -eaf | grep '"+process_name+"' | grep -v grep | wc -l", shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return int(output)

####################################################################
#                              Initial
jangan_kosong = True
select_menu = 0
pilih_new_project = 0

info = get_info() # dapatkan info dari database
####################################################################
#                        Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#                            Setup Style
def banner():
    date = time.asctime()
    terminal_clear()
    print (Y+"\n0{==========================================================}0")
    print (  Y+"|                  "+date+"                  |")
    print (  Y+"| "+G+"                          ___                         __  "+Y+" |")
    print (  Y+"| "+G+"   ____  ____ _____  ____/ (_)___  ____ ___  ____  __/ /__"+Y+" |")
    print (  Y+"| "+G+"  / __ \/ __ `/ __ \/ __  / / __ \/ __ `/ / / / / / / //_/"+Y+" |")
    print (  Y+"| "+G+" / / / / /_/ / /_/ / /_/ / / / / / /_/ / /_/ / /_/ / ,<"+Y+"    |")
    print (  Y+"| "+G+"/_/ /_/\__, /\____/\__,_/_/_/ /_/\__, /\__, /\__,_/_/|_| "+Y+"  |")
    print (  Y+"| "+G+"      /____/                    /____//____/"+Y+"               |")
    print (  Y+"|                                                            |")
    print (  Y+"| "+R+"version: "+W+cek_local_info()['version']+"            "+W+" Author : Jefri Herdi Triyanto"+Y+"   |")
    print (  Y+"|                                                            |")

def menu():
    print (  Y+"0{========================="+W+" MENU "+Y+"===========================}0")
    if jangan_kosong == False:
        print (  R+"   ~> tolong jangan mengkosongkan pilihan!")
    print (  Y+"   "+B+"["+R+"+"+B+"] "+W+"pilih menu yang ingin di eksekusi :")

    if select_menu == 0: # pilihan home
        # reset variable pointer
        pilih_new_project = 0
        if cek_local_info()['version'] == info['version']:
            if findThisProcess("php")==0 and findThisProcess("mysqld_safe")==0 and findThisProcess("mariadbd")==0 :
                print (  Y+"   ["+W+"1"+Y+"] "+C+"start server!")
            else:
                print (  Y+"   ["+W+"1"+Y+"] "+C+"stop server!")
            print (  Y+"   ["+W+"2"+Y+"] "+C+"new project (*)")
            print (  Y+"   ["+W+"3"+Y+"] "+C+"open project (*)")
            print (  Y+"   ["+W+"4"+Y+"] "+C+"delete project (*)")
            print (  Y+"   ["+W+"5"+Y+"] "+C+"uninstall (?)")
        else:
            print (  Y+"   ["+W+"1"+Y+"] "+C+"update! ("+G+info['version']+B+")")
        
        print (  Y+"   ["+W+"9"+Y+"] "+C+"What's New!")
        print (  Y+"   ["+W+"0"+Y+"] "+C+"Exit!")
    elif select_menu == 2: # pilihan new project
        x=0
        for p in info['new_project']:
            x=x+1
            print (  Y+"   ["+W+str(x)+Y+"] "+C+p['name'])
        print (  Y+"   ["+W+"0"+Y+"] "+C+"Back!")
    
    print (  Y+"0{==========================================================}0")

def bye():
    terminal_clear()
    print (Y+"\n0{==========================================================}0")
    print (  Y+"|                                                            |")
    print (  Y+"| "+G+"           ____  ___   ___  ____  ______   _______   "+Y+"      |")
    print (  Y+"| "+G+"          / ___|/ _ \ / _ \|  _ \| __ ) \ / / ____|  "+Y+"      |")
    print (  Y+"| "+G+"         | |  _| | | | | | | | | |  _ \\\\ V /|  _|  "+Y+"        |")
    print (  Y+"| "+G+"         | |_| | |_| | |_| | |_| | |_) || | | |___   "+Y+"      |")
    print (  Y+"| "+G+"          \____|\___/ \___/|____/|____/ |_| |_____|  "+Y+"      |")
    print (  Y+"|                                                            |")
    print (  Y+"0{==========================================================}0")
####################################################################
#                            Setup Loop
if sys.argv[0] == "install.py":
    banner()
    ## INSTALL PKG
    # WAJIB
    install("wget")
    install("zip")
    install("php")
    install("mariadb")
    install("apache2")
    # TAMBAHAN, (if development => SKIP)
    # install("nodejs") # cek lagi nama pkg nya
    
    ## BUAT FOLDER
    # wajib
    buat_pintasan("/data/data/com.termux/files/usr/share/apache2/default-site/htdocs","ngodingyuk/public_html")
    mkdir(".ngoding-debug")
    mkdir(".ngodingyuk")
    # tambahan (Node.JS) (if development => SKIP)
    mkdir("ngodingyuk/project")
    mkdir("ngodingyuk/project/reactjs")
    mkdir("ngodingyuk/project/react-native")
    
    
    ## INSTALL PHPMYADMIN
    wget("https://files.phpmyadmin.net/phpMyAdmin/"+info['phpmyadmin']+"/phpMyAdmin-"+info['phpmyadmin']+"-all-languages.zip")
    unzip("phpMyAdmin-"+info['phpmyadmin']+"-all-languages.zip")
    rm("phpMyAdmin-"+info['phpmyadmin']+"-all-languages.zip")
    rename("phpMyAdmin-"+info['phpmyadmin']+"-all-languages",".phpmyadmin")
    copy("ngodingyuk/config.inc.php",".ngodingyuk/config.inc.php")
    move("ngodingyuk/config.inc.php",".phpmyadmin/config.inc.php")
    
    
    ## INSTALL BLACKICEcoder
    git("https://github.com/jefripunza/BLACKICEcoder.git",".blackicecoder")
    
    
    ## FINISHING
    move("ngodingyuk/info.json",".ngodingyuk/info.json")
    rmrf("ngodingyuk/.git")
    rename("ngodingyuk/install.py","ngodingyuk/start.py")
    
    execute("cd && python2 ngodingyuk/start.py")
    
    sys.exit()
else:
    while True:
        try:
            banner()
            menu()
            pilihan_str = raw_input(B+"["+W+"?"+B+"]"+G+" Pilih"+Y+" : "+W)
            if pilihan_str != "":
                pilihan_str = int(pilihan_str)
                # execute
                if select_menu == 0: # menu ========================================================
                    if pilihan_str == 0: # exit
                        terminal_clear()
                        bye()
                        sys.exit()
                    elif pilihan_str == 1: # start server | stop server | update
                        select_menu = 1
                    elif pilihan_str == 2: # new project
                        select_menu = 2
                    elif pilihan_str == 3: # open project
                        select_menu = 3
                    else:
                        select_menu = 0
                elif select_menu == 1: # (run) start server | stop server | update =================
                    if cek_local_info()['version'] == info['version']:
                        if findThisProcess("php")==0 and findThisProcess("mysqld_safe")==0 and findThisProcess("mariadbd")==0 :
                            # if start server
                            start_server()
                        else:
                            # if stop server
                            stop_server()
                    # else:
                        # if update
                    select_menu = 0 # setelah selesai start server | stop server | update, auto back
                elif select_menu == 2: # new project ~> pilih project ==============================
                    if pilihan_str == 0: # back
                        select_menu = 0
                elif select_menu == 3: # open project ~> pilih project ==============================
                    if pilihan_str == 0: # back
                        select_menu = 0
                jangan_kosong = True
            else:
                jangan_kosong = False
        except KeyboardInterrupt:
            terminal_clear()
            bye()
            sys.exit()
        except Exception as x:
            print('x: ' + str(x))
            print('Err: ' + x.__class__.__name__)
            sys.exit()
