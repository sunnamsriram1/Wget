# -*- coding: utf-8 -*-
import os

def banner():
    print("\n╔═━━━◇◆◇━━━═╗")
    print("║ 🔽 S_WGET_TOOL by Sriram 🔐")
    print("╚═━━━◇◆◇━━━═╝\n")

def menu():
    print("🛠️ Options:")
    print("1️⃣  Single File Download")
    print("2️⃣  Resume Broken Download")
    print("3️⃣  Download from URL list (list.txt)")
    print("4️⃣  Full Website Mirror")
    print("5️⃣  Authenticated Download (Basic Auth)")
    print("6️⃣  TOR Proxy Download")
    print("0️⃣  Exit\n")

def single_download():
    url = input("🌐 Enter file URL: ").strip()
    os.system(f'wget "{url}"')

def resume_download():
    url = input("🌐 Enter broken file URL: ").strip()
    os.system(f'wget -c "{url}"')

def multiple_download():
    list_file = input("📄 Enter URL list filename (default: list.txt): ").strip() or "list.txt"
    if os.path.exists(list_file):
        os.system(f'wget -i "{list_file}"')
    else:
        print("❌ File not found.")

def website_mirror():
    url = input("🌐 Website URL to mirror: ").strip()
    level = input("🔢 Max depth level (default 1): ").strip() or "1"
    cmd = f'wget --mirror --convert-links --no-parent --level={level} "{url}"'
    print("🔁 Mirroring full website...\n")
    os.system(cmd)
    print('Mirroring Full Website Complete 💯 Download')

def auth_download():
    url = input("🔒 Enter URL: ").strip()
    user = input("👤 Username: ").strip()
    pwd = input("🔑 Password: ").strip()
    os.system(f'wget --http-user="{user}" --http-password="{pwd}" "{url}"')

def tor_download():
    url = input("🧅 Enter URL to download via TOR: ").strip()
    print("🕸️ Connecting via Tor (127.0.0.1:9050)...")
    os.system(f'torsocks wget "{url}"')

def main():
    try:
        banner()
        while True:
            menu()
            choice = input("👉 Choose an option (0-6): ").strip()
            if choice == "1":
                single_download()
            elif choice == "2":
                resume_download()
            elif choice == "3":
                multiple_download()
            elif choice == "4":
                website_mirror()
            elif choice == "5":
                auth_download()
            elif choice == "6":
                tor_download()
            elif choice == "0":
                print("👋 Exiting S_WGET_TOOL.")
                break
            else:
                print("❌ Invalid option, try again.")
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    main()
                
