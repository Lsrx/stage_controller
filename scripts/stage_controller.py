#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from nav_msgs.msg import *
import random
import math

laser = LaserScan()
odometry = Odometry()

def odometry_callback(data):
    global odometry
    odometry = data
def laser_callback(data):
    global laser
    laser = data

if __name__ == "__main__":
    rospy.init_node("stage_controller_node", anonymous=False)
    rospy.Subscriber("/base_pose_ground_truth", Odometry, odometry_callback)
    rospy.Subscriber("/base_scan", LaserScan, laser_callback)

    target_x = -0.5
    target_y = -0.5
    min_distance = 0.4

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(5) # 10hz
    velocity = Twist()
    while not rospy.is_shutdown():
        x = odometry.pose.pose.position.x
        y = odometry.pose.pose.position.y
        
        # Verifica se chegou ao alvo, se a distancia for menor que a minima distancia, para o robô
        distance = math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
        if distance <= min_distance:
            rospy.loginfo("Alvo alcançado! Parando o movimento.")
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0
            pub.publish(velocity)
            break
        rospy.loginfo("Where I am: X: %s, Y: %s", x, y)
        
        #verifica o tamnho da lista e maior que 0  e se a minima distancia é maior que 0.5
        if len(laser.ranges) > 0 and min(laser.ranges) > 0.5:
            velocity.linear.x = random.uniform(0.0, 0.5)
            velocity.angular.z = random.uniform(-1.0, 1.0) * random.uniform(0.0, 0.5)
            rospy.loginfo("Navegando...")
        
        #se nao gira, ou seja, encontrou parede 
        else:
            velocity.linear.x = 0.0
            velocity.angular.z = 0.50
            rospy.loginfo("Girando")
        pub.publish(velocity)
        r.sleep()
