from util import LocalConfig
import json

def loadLocalAccounts():
    config = LocalConfig().config
    localAccounts = json.loads(config.get('coinlist', 'local', fallback="[]"))
    return localAccounts

def saveLocalAccount(line):
    if not line or "email"  not in line:
        return
    config = LocalConfig().config
    localAccounts = json.loads(config.get('coinlist', 'local', fallback="[]"))
    localAccounts.append(line)
    config['coinlist']['local'] =  json.dumps(localAccounts)
    LocalConfig().save(config)