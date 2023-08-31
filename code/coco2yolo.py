# 开发人：吴兆波
# 开发时间：2023/8/27 31
# 处理同一个数据集下多个json文件时，仅运行一次class_txt即可
import json
import os
import cv2

"存储标签与预测框到txt文件中"
def json_txt(json_path, txt_path):
    json_path = "C:\\Users\\wuzha\\Desktop\\HRSC2016-MS\\test.json"
    txt_path = "C:\\Users\\wuzha\\Desktop\\test_annotations/"
    path_root_images = "C:\\Users\\wuzha\\Desktop\\HRSC2016-MS\\AllImages/"
    # 生成存放txt文件的路径
    if not os.path.exists(txt_path):
        os.mkdir(txt_path)
    # 读取json文件
    with open(json_path, 'r') as f:
        dict = json.load(f)
    # 得到images和annotations信息
    images_value = dict.get("images")  # 得到某个键下对应的值
    annotations_value = dict.get("annotations")  # 得到某个键下对应的值
    # 使用images下的图像名的id创建txt文件
    list=[]  # 将文件名存储在list中
    for i in images_value:
        open(txt_path + os.path.splitext(str(i.get("file_name")))[0] + '.txt', 'w')
        list.append(i.get("file_name"))


    # 将id对应图片的bbox写入txt文件中
    for i in range(len(list)):
        for j in annotations_value:
            if j.get("image_id") == i:
                # bbox标签归一化处理
                k = j.get('bbox')
                w = images_value[i].get("width")
                h = images_value[i].get("height")
                x_c = round((k[0] + round(k[2]/2, 6))/w, 6)
                y_c = round((k[1] + round(k[3]/2, 6))/h, 6)
                w_ = round(k[2]/w, 6)
                h_ = round(k[3]/h, 6)
                new_list = [x_c, y_c, w_, h_]
                with open(txt_path + os.path.splitext(str(images_value[i].get("file_name")))[0] + '.txt', 'a') as file1:  # 写入txt文件中
                    print(j.get("category_id"), new_list[0], new_list[1], new_list[2], new_list[3], file=file1)
                '''path_img = os.path.join(path_root_images, images_value[i].get("file_name"))
                img = cv2.imread(path_img)
                img_tmp = img.copy()
                x1 = int((x_c - w_/2) * w)
                y1 = int((y_c - h_/2) * h)
                x2 = int((x_c + w_/2) * w)
                y2 = int((y_c + h_/2) * h)
                cv2.rectangle(img_tmp, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cv2.imshow("show", img_tmp)
                cv2.waitKey(0)'''


"将id对应的标签存储在class.txt中"
'''def class_txt(json_path, class_txt_path):
    json_path = "C:\\Users\\wuzha\\Desktop\\HRSC2016-MS\\train.json"
    class_txt_path = "C:\\Users\\wuzha\\Desktop\\code_paper\\categories.txt"
    with open(json_path, 'r') as f:
        dict = json.load(f)
    # 得到categories下对应的信息
    categories_value = dict.get("categories")  # 得到某个键下对应的值
    # 将每个类别id与类别写入txt文件中
    with open(class_txt_path, 'a') as file0:
        for i in categories_value:
            print(i.get("id"), i.get('name'), file=file0)'''


json_txt("a", "b")
'''class_txt("a", "b")'''
