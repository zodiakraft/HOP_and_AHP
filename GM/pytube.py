import pafy

url = 'https://www.youtube.com/watch?v=37vhxQQukdE'

v = pafy.new(url)
streams = v.streams

available_streams = {}
count = 1

for stream in streams:
    available_streams[count] = stream
    print(f'{count}: {stream}')
    count += 1

stream_count = int(input())
d = streams[stream_count - 1].download(filepath = 'C:\\Users\\UpuHa\\Downloads\\pytube-master')
print('OK')
