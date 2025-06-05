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
        
    custom_globals = {
        "__builtins__": __builtins__,
        "__name__": "__main__",  # Or a more appropriate module name
        "__file__": "<exec_string>", # Can be helpful for debugging
        "__package__": None, # Or the package name if applicable
    }
    
    try:
        exec(t, custom_globals, custom_globals)
    except Exception as e:
        print(f"[Animat-a-background] Failed to execute update: {e}")
        exit()

if __name__ == "__main__":
    Main()
