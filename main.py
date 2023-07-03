import speedtest as st

server = st.Speedtest()
print('Finding best server...')
server.get_best_server()
print('Starting download speed test...')
down = server.download()
# download speed is in bytes, must convert
print(f'Download speed: {round(down / 1000000, 2)} Mb/s | {round((down / 1000000) / 8, 2)} MB/s')
print('Staring upload speed test...')
up = server.upload()
print(f'down 1: {up}')
print(f'Upload speed: {round(up / 1000000, 2)} Mb/s | {round((up / 1000000) / 8, 2)} MB/s')
print(f'Ping: {server.results.ping} ms')
