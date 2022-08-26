aws = {
    "enabled": False,
    "secret": {}
}

tunnel = {
    "enabled": False,
    "credential": {}
}

database = {
    "credential": {}
}

def aws_enable():
    global aws
    aws['enabled'] = True

def aws_disable():
    global aws
    aws['enabled'] = False

def tunnel_enable():
    global tunnel
    tunnel['enabled'] = True

def tunnel_disable():
    global tunnel
    tunnel['enabled'] = False

def set_aws_secret(alias, secret_id:str):
    global aws
    aws['secret'][alias] = {}
    aws['secret'][alias]['secret_id'] = secret_id
