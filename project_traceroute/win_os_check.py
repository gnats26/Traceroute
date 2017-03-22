import platform


if platform.system() == "Windows":
    command = "tracert"


if platform.system() == "Linux":
    command = "traceroute"

