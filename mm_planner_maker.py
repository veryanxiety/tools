import datetime
import time

year=2023
m=[31,28,31,30,31,30,31,31,30,31,30,31]
if not(year % 4) and (not(year % 400) or (year % 100)):
    m[1] += 1
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
actions=["&#x41a;&#x440;&#x430;&#x441;&#x43e;&#x442;&#x430;/&#x437;&#x434;&#x43e;&#x440;&#x43e;&#x432;&#x44c;&#x435;","&#x420;&#x430;&#x431;&#x43e;&#x442;&#x430;/&#x443;&#x447;&#x435;&#x431;&#x430;",
"&#x424;&#x438;&#x43d;&#x430;&#x43d;&#x441;&#x44b;","&#x41e;&#x431;&#x449;&#x435;&#x43d;&#x438;&#x435;","&#x411;&#x44b;&#x442;/&#x445;&#x43e;&#x437;&#x44f;&#x439;&#x441;&#x442;&#x432;&#x43e;","&#x421;&#x430;&#x43c;&#x43e;&#x440;&#x430;&#x437;&#x432;&#x438;&#x442;&#x438;&#x435;",
"&#x412;&#x43f;&#x435;&#x447;&#x430;&#x442;&#x43b;&#x435;&#x43d;&#x438;&#x44f;"]
actions_icons=["full-1","full-2","full-3","full-4","full-5","full-6","full-7"]
priority=['HIGH','NORMAL','LOW']
priority_icons=["up","forward","down"]
results=['DONE','PAUSE','FAIL']
results_icons=["button_ok","hourglass","button_cancel"]

current_mtime = lambda: int(round(time.time() * 1000))
ids= lambda: int(round(time.time() * 1000*1000)%1e10)
bgcolors=["#ccffff","#ccffcc","#6699ff","#cccccc","#ffffcc","#ffcccc","#ff99ff"]
colors=[]

def print_node(f, text,bg_color=-1,color=-1,position=-1,is_terminal=True):
    w='<node '
    if bg_color>=0:
        w=w+'BACKGROUND_COLOR="'+bgcolors[bg_color]+'" '
    if color>=0:
        w=w+'COLOR="'+colors[color]+'"'
    w=w+'CREATED="'+str(current_mtime())+'" '
    w=w+'ID="ID_'+str(ids())+'" '
    w=w+'MODIFIED="'+str(current_mtime())+'" '
    if position==0:
        w=w+'POSITION="left" '
    elif position==1:
        w=w+'POSITION="right" '
    w=w+'TEXT="'+text+'"'
    if is_terminal:
        w=w+'/'
    w=w+'>'
    f.write(w+'\n')

def print_tnode(f):
    f.write('</node>\n')

def print_icon(f, name):
    f.write('<icon BUILTIN="'+name+'"/>')
    
def print_annotation(f):
    print_node(f, 'Annotations',-1,-1,-1,False)
    
    print_node(f, 'Weekdays',-1,-1,0,False)
    for i in range(len(wd)):
        print_node(f, wd[i],i,-1,-1,True)
    print_tnode(f)
    
    print_node(f, 'Actions',-1,-1,1,False)
    for i in range(len(actions)):
        print_node(f, actions[i],-1,-1,-1,False)
        print_icon(f, actions_icons[i])
        print_tnode(f)        
    print_tnode(f)
    
    print_node(f, 'Priority',-1,-1,0,False)
    for i in range(len(priority)):
        print_node(f, priority[i],-1,-1,-1,False)
        print_icon(f, priority_icons[i])
        print_tnode(f)
    print_tnode(f)
    
    print_node(f, 'Results',-1,-1,1,False)
    for i in range(len(results)):
        print_node(f, results[i],-1,-1,-1,False)
        print_icon(f, results_icons[i])
        print_tnode(f)
    print_tnode(f)
    
    print_tnode(f)
    

with open("2023_AK.mm",'w') as f:
    f.write('<map version="1.0.1">\n')
    print_node(f, str(year),-1,-1,-1,False)
    print_node(f, 'Plans',-1,-1,0,True)
    print_node(f, 'Events',-1,-1,1,True)
    for month in range(12):
        print_node(f, str((month+1)//10)+str((month+1)%10),-1,-1,int(month//6),False)
        print_node(f, 'Plans',-1,-1,-1,True)
        print_node(f, 'Events',-1,-1,-1,True)
        for i in range(m[month]):
            print_node(f, str((i+1)//10)+str((i+1)%10),datetime.date(year,month+1,i+1).weekday(),-1,-1,True)
        print_tnode(f)
    print_annotation(f)
    print_tnode(f)
    f.write('</map>')
