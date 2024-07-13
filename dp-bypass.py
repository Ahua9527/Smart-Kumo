import kumo_config
import requests

def get_vars_from_kumo_config():
    return {
        "address": kumo_config.address,
        "view1_in": kumo_config.view1_in,
        "view2_in": kumo_config.view2_in,
        "view3_in": kumo_config.view3_in,
        "view4_in": kumo_config.view4_in,
        "Monitor_1": kumo_config.Monitor_1,
        "Monitor_2": kumo_config.Monitor_2,
        "Monitor_3": kumo_config.Monitor_3,
        "Monitor_4": kumo_config.Monitor_4,
        "Monitor_5": kumo_config.Monitor_5,
        "Monitor_6": kumo_config.Monitor_6,
        "Monitor_7": kumo_config.Monitor_7,
        "Monitor_8": kumo_config.Monitor_8,
        "Monitor_9": kumo_config.Monitor_9,
    }

# 获取 KUMO 设备的配置信息
kumo_config = get_vars_from_kumo_config()

# 查询 view1_in 连接位置
url = f"http://{kumo_config['address']}/config?action=get&paramid=eParamID_XPT_Destination{kumo_config['view1_in']}_Status"
response = requests.get(url)
if response.status_code == 200:
    camera_1 = response.json().get("value", "未知")
    print("view1_in 连接到输入端口:", camera_1)
else:
    print("查询 view1_in 连接位置失败:", response.status_code)

# 查询 view2_in 连接位置
url = f"http://{kumo_config['address']}/config?action=get&paramid=eParamID_XPT_Destination{kumo_config['view2_in']}_Status"
response = requests.get(url)
if response.status_code == 200:
    camera_2 = response.json().get("value", "未知")
    print("view2_in 连接到输入端口:", camera_2)
else:
    print("查询 view2_in 连接位置失败:", response.status_code)

# 查询 view3_in 连接位置
url = f"http://{kumo_config['address']}/config?action=get&paramid=eParamID_XPT_Destination{kumo_config['view3_in']}_Status"
response = requests.get(url)
if response.status_code == 200:
    camera_3 = response.json().get("value", "未知")
    print("view3_in 连接到输入端口:", camera_3)
else:
    print("查询 view3_in 连接位置失败:", response.status_code)

# 查询 view4_in 连接位置
url = f"http://{kumo_config['address']}/config?action=get&paramid=eParamID_XPT_Destination{kumo_config['view4_in']}_Status"
response = requests.get(url)
if response.status_code == 200:
    camera_4 = response.json().get("value", "未知")
    print("view4_in 连接到输入端口:", camera_4)
else:
    print("查询 view4_in 连接位置失败:", response.status_code)

# 处理 Monitor_5、Monitor_6、Monitor_7、Monitor_8
for monitor_num in range(5, 9):
    monitor_key = f"Monitor_{monitor_num}"
    url = f"http://{kumo_config['address']}/config?action=get&paramid=eParamID_XPT_Destination{kumo_config[monitor_key]}_Status"
    response = requests.get(url)
    if response.status_code == 200:
        monitor_connection = response.json().get("value", "未知")
        print(f"{monitor_key} 当前连接到输入端口:", monitor_connection)
        if monitor_connection in ['5', '6', '7', '8']:
            camera_num = int(monitor_connection) - 4
            print(f"{monitor_key} 当前连接到输入端口 {monitor_connection}，将其连接到 camera_{camera_num}")
            url = f"http://{kumo_config['address']}/config?action=set&paramid=eParamID_XPT_Destination{kumo_config[monitor_key]}_Status&value={globals()[f'camera_{camera_num}']}"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"已将 {monitor_key} 连接到 camera_{camera_num}")
            else:
                print("连接失败:", response.status_code)
        else:
            print(f"{monitor_key} 未连接到有效的输入端口，无需执行连接操作")
    else:
        print(f"查询 {monitor_key} 连接位置失败:", response.status_code)
