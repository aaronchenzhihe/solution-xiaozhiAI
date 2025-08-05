from misc import PWM_V2
import utime
from machine import Pin
import sys_bus

lcd=Pin(Pin.GPIO39, Pin.OUT, Pin.PULL_DISABLE, 0)
# 初始化PWM
pwms = [PWM_V2(pwm_v2, 50.0, 10) for pwm_v2 in [PWM_V2.PWM0, PWM_V2.PWM1, PWM_V2.PWM2, PWM_V2.PWM3]]

# def pmw_go():
    


def led_handler(topic,msg):
    if msg == "open":
        lcd.write(1)
        print("111")
    elif msg == "close":
        lcd.write(0)
        print("000")



def pwm_handler(topic,msg):
    if msg == "go":
        print("正转90°")
    elif msg == "back":
        print("反转90°")
    elif msg == "stop":
        print("停止")
    



sys_bus.subscribe("dev_led",led_handler)
sys_bus.subscribe("act",pwm_handler)









#角度 = (脉宽 - 0.5ms) × (180° / (2.5ms - 0.5ms))  = (脉宽 - 0.5ms) × 90°/ms
     

current_angles = [0, 0, 0, 0]





