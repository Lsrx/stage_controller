# Lucas Silva - 157138
# Codigo construido a partir do fornecido como base da Misaki

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

    # Inicializando variaveis

    alvo_x = -0.5
    alvo_y = -0.5
    min_distancia = 0.4
    distancia = 0
    velocity.linear.x = 0
    velocity.angular.z = 0

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(5) # 10hz
    velocity = Twist()
    while not rospy.is_shutdown():
        x = odometry.pose.pose.position.x
        y = odometry.pose.pose.position.y
        
        rospy.loginfo("As coordenadas atuais do robo sao: X: %s, Y: %s", x, y)

	# Calcula distancia linear ate o alvo

        distancia = math.sqrt((x - alvo_x) ** 2 + (y - alvo_y) ** 2)

	# Se a distância for menor que a tolerância para o robo por ter alcancado o objetivo

        if distancia <= min_distancia:
            rospy.loginfo("O robo chegou ao objetivo.")
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0
            pub.publish(velocity)
            break
        
	# Verifica se o comprimeiro dos ranges do laser são maiores que zero e se a distancia é maior que 0.5

        if len(laser.ranges) > 0 and min(laser.ranges) > 0.5:
            velocity.linear.x = random.uniform(0.0, 0.5)
            velocity.angular.z = random.uniform(-1.0, 1.0) * random.uniform(0.0, 0.5)
            rospy.loginfo("Indo ao objetivo")
        
        # Caso seja menor significa que encontrou um obstaculo com colisao imimente, portanto performa uma rotacao ate os ranges se adequarem 

        else:
            velocity.linear.x = 0.0
            velocity.angular.z = 0.50
            rospy.loginfo("Girando")
        pub.publish(velocity)
        r.sleep()
