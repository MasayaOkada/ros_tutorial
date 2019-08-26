#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(message):						# callback関数でmessageという引数をとる
	rospy.loginfo("I heard %s", message.data)		# 文字列を表示する

rospy.init_node('listener')					
sub = rospy.Subscriber('chatter', String, callback)		# std_msgs/String型のpublishをsubscribeしてcallbackを実行
rospy.spin()							# 無限ループして受信を待ち続ける
