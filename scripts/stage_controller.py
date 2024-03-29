# Lucas Silva - 157138
# Codigo construido a partir do fornecido como base da Misaki
#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from nav_msgs.msg import *
import random
import math

# Inicialização das variáveis globais
laser = LaserScan()
odometry = Odometry()
velocity = Twist()  # Inicialize a variável velocity

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

    # Inicializando variáveis
    alvo_x = 2
    alvo_y = 2.5
    min_distancia = 0.3
    distancia = 0

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(5)  # 10hz

    while not rospy.is_shutdown():
        x = odometry.pose.pose.position.x
        y = odometry.pose.pose.position.y

        rospy.loginfo("As coordenadas atuais do robo sao: X: %s, Y: %s", x, y)

        # Calcula distância linear até o alvo
        distancia = math.sqrt((x - alvo_x) ** 2 + (y - alvo_y) ** 2)

        # Se a distância for menor que a tolerância, o robô chegou ao objetivo
        if distancia <= min_distancia:
            rospy.loginfo("O robo chegou ao objetivo.")
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0
            pub.publish(velocity)
            break

        # Verifica se o comprimento dos ranges do laser são maiores que zero e se a distância é maior que 0.5
        if len(laser.ranges) > 0 and min(laser.ranges) > 0.5:
            velocity.linear.x = random.uniform(0.0, 0.5)
            velocity.angular.z = random.uniform(-1.0, 1.0) * random.uniform(0.0, 0.5)
            rospy.loginfo("Indo ao objetivo")

        # Caso contrário, significa que encontrou um obstáculo com colisão iminente, portanto realiza uma rotação até os ranges se adequarem
        else:
            velocity.linear.x = 0.0
            velocity.angular.z = 0.50  # Ajuste a velocidade angular
            rospy.loginfo("Girando")

        pub.publish(velocity)
        r.sleep()
