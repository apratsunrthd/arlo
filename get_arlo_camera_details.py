from arlo import Arlo
import json
import re

USERNAME = 'apratsunrthd@gmail.com'
PASSWORD = 'qU89g$M$^%Vr'



def pp(data):
    print(json.dumps(data, indent=4, sort_keys=True))

try:
    arlo = Arlo(USERNAME, PASSWORD, 'gmail.credentials')
    
    devices = arlo.GetDevices()
    for i, device in enumerate(devices):
        for key in ['deviceId', 'parentId', 'uniqueId', 'userId', 'xCloudId']:
            if key in device:
                device[key] = re.sub(r'[0-9A-Za-z]', r'X', device.get(key))

        for key in ['deviceName', 'presignedFullFrameSnapshotUrl', 'presignedLastImageUrl', 'presignedSnapshotUrl']:
            device[key] = ""

        device['owner']['ownerId'] = re.sub(r'[0-9A-Za-z]', r'X', device['owner']['ownerId'])
        device['owner']['firstName'] = ""
        device['owner']['lastName'] = ""
        
        devices[i] = device

    pp(devices)
except Exception as e:
    print(e)