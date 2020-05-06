import speedtest as s
from tqdm import tqdm
import time



check = s.Speedtest()

download_speed = round(check.download()/(1000**2),2)
upload_speed = round(check.upload()/(1000**2),2)

print('''Results:\nDownload speed : {down} Mbps
Upload speed : {up} Mbps'''.format(down=download_speed, up=upload_speed))
