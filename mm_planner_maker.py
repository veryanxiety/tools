import time,datetime
year=2022
m=[31,28,31,30,31,30,31,31,30,31,30,31]
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

def print_node(text,bg_color=-1,color=-1,position=-1,is_terminal=True):
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

def print_tnode():
    f.write('</node>\n')

def print_icon(name):
    f.write('<icon BUILTIN="'+name+'"/>')
    
def print_annotation():
    print_node('Annotations',-1,-1,-1,False)
    
    print_node('Weekdays',-1,-1,0,False)
    for i in range(len(wd)):
        print_node(wd[i],i,-1,-1,True)
    print_tnode()
    
    print_node('Actions',-1,-1,1,False)
    for i in range(len(actions)):
        print_node(actions[i],-1,-1,-1,False)
        print_icon(actions_icons[i])
        print_tnode()        
    print_tnode()
    
    print_node('Priority',-1,-1,0,False)
    for i in range(len(priority)):
        print_node(priority[i],-1,-1,-1,False)
        print_icon(priority_icons[i])
        print_tnode()
    print_tnode()
    
    print_node('Results',-1,-1,1,False)
    for i in range(len(results)):
        print_node(results[i],-1,-1,-1,False)
        print_icon(results_icons[i])
        print_tnode()
    print_tnode()
    
    print_tnode()
    

f=open("C:\\Users\\me\\Documents\\2022_AK.mm",'w')
f.write('<map version="1.0.1">\n')
print_node(str(year),-1,-1,-1,False)
print_node('Plans',-1,-1,0,True)
print_node('Events',-1,-1,1,True)
for month in range(12):
    print_node(str((month+1)/10)+str((month+1)%10),-1,-1,int(month/6),False)
    print_node('Plans',-1,-1,-1,True)
    print_node('Events',-1,-1,-1,True)
    for i in range(m[month]):
        print_node(str((i+1)/10)+str((i+1)%10),datetime.date(year,month+1,i+1).weekday(),-1,-1,True)
    print_tnode()
print_annotation()
print_tnode()
f.write('</map>')
f.close()