from libs.plm import plm
import time

while(True):
    time.sleep(1)
    for call in plm.handle_list:
        call[0]()