import os

def run(**args):
    
    print "[*] In direlister module."
    files = os.listdir(".")
    
    return str(files)