import speedtest as s

check = s.Speedtest()

download_speed = round(check.download()/(1000**2),2)
upload_speed = round(check.upload()/(1000**2),2)

print('''Results:\nDownload speed : {down} Mbps
Upload speed : {up} Mbps'''.format(down=download_speed, up=upload_speed))
