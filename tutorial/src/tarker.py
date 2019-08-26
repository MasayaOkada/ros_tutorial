#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('talker')					# ROSの最初におこなう作業　talkerというノードができる
pub = rospy.Publisher('chatter', String, queue_size = 10)	# chatterという名前でstd_msgs/String型のpublishをつくる
								# queue_sizeはバッファーの格納
rate = rospy.Rate(10)						# 10Hz

while not rospy.is_shutdown():					# Ctrl+cされるまで続ける
	hello_str = String()					# StringのメッセージをStringクラスからつくる
	hello_str.data = "hello world %s" % rospy.get_time()	# hello_strの内容を書き込む
	pub.publish(hello_str.data)				# hello_strをpublish
	rate.sleep()						# 10Hzを実現するために必要な時間をsleep
