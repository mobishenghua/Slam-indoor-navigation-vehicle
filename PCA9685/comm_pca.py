#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from ackermann_msgs.msg import AckermannDriveStamped
from adafruit_servokit import ServoKit

flag_move = 0
servokit = ServoKit(channels=16, address=0x40)

def set_throttle_steer(data):

    global flag_move

    throttle = data.drive.speed
    steer = data.drive.steering_angle

    servokit.servo[0].angle = steer
    servokit.continuous_servo[1].throttle = throttle

def servo_commands():

    rospy.init_node('servo_commands', anonymous=True)

    rospy.Subscriber("/ackermann_cmd_mux/output", AckermannDriveStamped, set_throttle_steer)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        servo_commands()
    except rospy.ROSInterruptException:
        pass