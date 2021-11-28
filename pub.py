
#!/usr/bin/python3

import rospy
from std_msgs.msg import Float64MultiArray
from time import sleep

if __name__ == '__main__':

    rospy.init_node("Give_Commands")
    x = rospy.Publisher("/trpy", Float64MultiArray, queue_size=10)
    
    msg = Float64MultiArray()
    msg.data = [60, 0, 0, 0]

    current = rospy.Time.now()
    dur = rospy.Duration(1)

    while(rospy.Time.now() < current + dur):

        print("Going Up")
        x.publish(msg)

    msg = Float64MultiArray()
    msg.data = [50.0, 0, 0, 0]

    current = rospy.Time.now()

    while(rospy.Time.now() < current + dur):
        print("Hovering")
        x.publish(msg)

    
