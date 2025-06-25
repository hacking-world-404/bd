#------------- IMPORT ------------#
from os import system as c
import marshal
import base64
import zlib
try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('clear')
#__________________[ COLOUR ]__________________#
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print(f' HEY SIR WELCOME TO HACKING WORLD...... ')
os.system('espeak -a 300 " HI SIR WELCOME TO HACKING WORLD "')
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#---------------- LOGO -----------#
os.system('espeak -a 300 "  WELCOME,  TO,    HACKING WORLD  V I P,  TOOLS"')
print ("jone my teligerm channel ")
logo=''' 
 ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▄▖
▐▌ ▐▌ █    █  ▐▌▗▞▘     ▝▚▞▘ ▐▌   
▐▛▀▜▌ █    █  ▐▛▚▖       ▐▌  ▐▌   
▐▌ ▐▌ █  ▗▄█▄▖▐▌ ▐▌    ▗▞▘▝▚▖▝▚▄▄▖                                                                                            
'''#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
    print(40*'-')
    print(' TIK TOK : HACKING WORLD ')
    print(' GITHUB  : HACKING WORLD 404')
    print ('WHATSAPP : 01846390932')
    print(40*'-')
#----------- MAIN FUNCTION ------------#
def main():
    clear()
    print(' [A] DIAMOND TOP UP BD ')
    print(' [0] EXIT TERMINAL ')
    print(40*'-')
    option=input(' [?] CHOICE MENU : ')
    if option in ['a','A']:
        marshal_enc()
    elif option in ['b','B']:
        base64_enc()
    elif option in ['c','C']:
        zlib_enc()
    elif option in ['d','D']:
        cython_executable()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    os.system('espeak -a 300 "  ENTER,  YOUR,    FREE FIRE  UID , "')
    file=input(' ENTER YOUR FREE FIRE  UID : ')    
    os.system('espeak -a 300 "  Plasse use Android version 13 and try Again."')
    filex=input('Plasse use Android version 13 and try Again...')   
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write(run_code)
    out_put.close()
    print(40*'-')
    print(' [✓✓]Plasse use Android version 13 and try Again...')
    print(' [✓✓]Plasse use Android version 13 and try Again..√'+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    os.system('espeak -a 300 "  ENTER,  YOUR,    FREE FIRE UID "')
    input_file=input(' ENTER FREE FIRE UID : ')
    os.system('espeak -a 300 "  This tool is paid, and its price is 999 bdt Taka"')
    output_file=input(' This tool is paid, and its price is 999 Taka.: ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√:/')
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√: '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    os.system('espeak -a 300 "  ENTER,  YOUR,    BAN FREE FIRE UID, "')
    src=input(' ENTER BAN FREE FIRE UID : ')
    os.system('espeak -a 300 "  This tool is paid, and its price is 999 bdt Taka"')
    exit('  :/')
    save_file=input(' This tool is paid, and its price is 999 Taka.√>>: ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√:/')
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√: '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
    clear()
    file=input(' ENTER SOURCE FILE PATH : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√:")')
    save=file[:-3]
    print(' [✓✓] This tool is paid, and its price is 999 Taka.√√: '+save)
#----------------- END --------------#
main()