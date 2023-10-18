import pyshark

capture = pyshark.LiveCapture(display_filter='ip.addr == 192.168.1.5')
capture.set_debug()

capture.sniff(timeout=50)

for packet in capture:
    print(packet.ip.src)

capture.close()
# for packet in capture.sniff_continuously(packet_count=5):
#     print('Just arrived:', packet)
