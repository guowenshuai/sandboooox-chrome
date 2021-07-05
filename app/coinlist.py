from util import LocalConfig
import json, base64

def loadLocalAccounts():
    config = LocalConfig().config
    b64_str = config.get('coinlist', 'local', fallback="")
    localAccounts = json.loads(b642str(b64_str))
    return list(localAccounts.values())

def saveLocalAccount(line):
    if not line or "email"  not in line:
        return
    config = LocalConfig().config
    b64_str = config.get('coinlist', 'local', fallback="")
    localAccounts = json.loads(b642str(b64_str))
    # localAccounts.append(line)
    localAccounts[line['email']] = line
    config['coinlist']['local'] = str2b64(json.dumps(localAccounts))
    LocalConfig().save(config)

def str2b64(real_str):
    print(real_str.encode())
    return base64.b64encode(real_str.encode()).decode()

def b642str(b64_str):
    if len(b64_str) == 0:
        return "{}"
    return base64.b64decode(b64_str).decode()

def exportLocalAccount():
    config = LocalConfig().config
    b64_str = config.get('coinlist', 'local', fallback="")  
    return b64_str  

def importLocalAccount(b64_str):
    try:
        localAccounts = json.loads(b642str(b64_str))
    except Exception as e:
        return False
    else:
        config = LocalConfig().config
        config['coinlist']['local'] = b64_str
        LocalConfig().save(config)
    return True

