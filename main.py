import pywifi
import time


def get_wifi_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(5)

    scan_results = iface.scan_results()
    names = [result.ssid for result in scan_results]
    return names


def save_networks_to_file(names, filename):
    existing_names = set()

    try:
        with open(filename, "r") as file:
            existing_names = set(line.strip() for line in file)
    except FileNotFoundError:
        pass

    with open(filename, "a") as file:
        for ssid in names:
            if ssid not in existing_names:
                file.write(ssid + "\n")
                existing_names.add(ssid)


if __name__ == "__main__":
    while True:
        names = get_wifi_networks()
        output_file = "wifi_networks.txt"

        print(names)

        save_networks_to_file(names, output_file)
        print(f"SSID names saved to {output_file}")
        time.sleep(10)
