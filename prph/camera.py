# coding:utf-8
'''
python想操作摄像头，
VideoCapture是windows特有的，
linux要用opencv才行。
'''
import time
import cv2
import numpy as np
"""
函数名：cv2.VideoCapture()
功  能：通过摄像头捕获实时图像数据
返回值：有
参数一：摄像头代号，0为默认摄像头，笔记本内建摄像头一般为 0
       或者填写视频名称直接加载本地视频文件
"""
def camera():
    cap = cv2.VideoCapture(0)#创建一个 VideoCapture 对象
    #filepath = '../image/'
    pngname = time.strftime('%Y%m%d-%H%M%S')+'.png'
    filepath = 'image/'+pngname   #必须在当前文件夹下新建image文件夹
   
    while(1):
        # get a frame
        ret, frame = cap.read()
        #  窗口显示，显示名为 Capture
        cv2.imshow("capture", frame)
        #每帧数据延时 1ms，延时不能为 0，否则读取的结果会是静态帧
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(filepath, frame)
            
            break

    cap.release()#释放摄像头
    cv2.destroyAllWindows()#删除建立的全部窗口
    return filepath


if __name__=='__main__':
  camera()
