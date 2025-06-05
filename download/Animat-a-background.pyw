# [
# 
# Script made by CrazyH2 (https://github.com/crazyh2)
# © Copyright 2025 CrazyH2. All rights reserved.
# 
# ]

def Main():
    print("[Animat-a-background] Running...")
    
    try:
        import urllib.request
    except:
        print("[Animat-a-background] Failed to import urlib.request")
        exit()
        
    try:
        r = urllib.request.urlopen('https://raw.githubusercontent.com/CrazyH2/Animat-a-background/refs/heads/main/versions/latest.py')
    except:
        print("[Animat-a-background] Failed to fetch python update")
        exit()

    try:
        t = r.read()
    except:
        print("[Animat-a-background] Failed to parse python update")
        exit()
        
    exec(t)

if __name__ == "__main__":
    Main()
