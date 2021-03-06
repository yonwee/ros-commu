#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CameraInfo
from ssd.msg import ClassifiedObjectArray

from ssd_wrapper import SSD, ClassificationResult

ssd = SSD(use_gpu=True)

latest_image_data = None
latest_camera_info = None
bridge = CvBridge()

publisher = None


def init_publisher():
    global publisher
    publisher = rospy.Publisher('ssd_node/classification_result', ClassifiedObjectArray, queue_size=5)


def callback(data):
    global latest_image_data
    latest_image_data = data


def camera_info_callback(data):
    global latest_camera_info
    latest_camera_info = data


def init_listener():
    rospy.Subscriber("/cv_camera/image_raw", Image, callback)
    rospy.Subscriber("/cv_camera/camera_info", CameraInfo, camera_info_callback)

    while not rospy.is_shutdown():
        if latest_image_data is not None and latest_camera_info is not None:
            cv_image = bridge.imgmsg_to_cv2(latest_image_data, "bgr8")

            objects = ssd.classify_image(cv_image)  # type: list[ClassificationResult]

            msg = ClassifiedObjectArray()
            msg.objects = []
            msg.image = latest_image_data
            msg.camera_info = latest_camera_info

            obj_count = {}

            for obj in objects:
                count = obj_count.get(obj.label_name, 0)

                msg.objects.append(obj.to_msg(count))

                obj_count[obj.label_name] = count + 1

            publisher.publish(msg)

            #save_opencv_image(cv_image, '/home/maurice/catkin_ws/src/ssd/src/raw.png')

            #image_boxed = draw_bounding_boxes(cv_image, objects)
            #display_opencv_image(image_boxed)

            #save_opencv_image(cv_image, '/home/maurice/catkin_ws/src/ssd/src/boxed{}.png'.format(image_number))
            #image_number += 1




if __name__ == '__main__':
    rospy.init_node('ssd_classifier')
    init_publisher()
    init_listener()