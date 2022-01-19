from datetime import datetime

connected_devices = {
    "000000000000": {
        "first_seen": datetime.now(),
        "last_seen": datetime.now(),
        "number_of_flashes": 0,
    },
    "BCDDC29E8A3B": {
        "first_seen": datetime.now(),
        "last_seen": datetime.now(),
        "number_of_flashes": 0,
    }
}


print(connected_devices)

for device in connected_devices:
    print(connected_devices[device]['last_seen'])

# Lambda function in sort Lifted from
# https://stackoverflow.com/questions/54768089/iterate-through-a-sorted-nested-dictionary-in-python
for device in sorted(connected_devices, key=lambda x: connected_devices[x]['last_seen'], reverse=True):
    # print(device)
    # I'm not quite sure why I need
    device_date = connected_devices[device]['last_seen'].date()
    device_hour = connected_devices[device]['last_seen'].hour
    device_minute = connected_devices[device]['last_seen'].minute
    device_second = connected_devices[device]['last_seen'].second
    # print(device_date, device_hour, device_minute, device_second)
    print(f"[{device_date}] {device_hour}:{device_minute}:{device_second}")

