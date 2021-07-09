import subprocess

out1 = []
out2 = {}

def get_wifi_names():
    data = subprocess.check_output("netsh wlan show profiles", shell=True, universal_newlines=True).split('\n')
    for i in data:
        if 'All User Profile' in i:
            out1.append(i.replace('All User Profile     : ',''))
    return out1

def get_wifi_pass(arg):

    for i in arg:
        data2 = subprocess.check_output("netsh wlan show profiles {} key=clear".format(i), shell=True, universal_newlines=True).split('\n')

        for y in data2:
            if "SSID name" in y:
                reps_y = y.replace('SSID name              : ','')
                out2[reps_y]= "None"

            if "Key Content" in y:
                repk = y.replace('Key Content            : ','')
                out2[reps_y] = repk
            else:
                pass
            
    return out2

def check(args):
    for key in out2.copy():   #if not use .copy(), then dict size is changing and getting iteration error
        if  out2[key] == "None":
            out2.pop(key)
    return out2


get_wifi_names()
get_wifi_pass(out1)
check(out2)

with open('Wifi-Find.txt','w') as f:
    f.write("     Wifi-Name             {:<60}\n".format('Password'))
    f.write('\n')
    for key in out2:
        f.write("{:<20} : {:<50} ".format(key, out2[key]))
        f.write('\n')




        
