import numpy as np
import cv2 as cv

# 定义一个函数，用于初始化和绘制静态图形
def draw_static_shapes():
    img = np.zeros((512, 512, 3), np.uint8)
    # 绘制一条蓝色的直线，起点为(0, 0)，终点为(511, 511)，线宽为5
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    # 绘制一个绿色的矩形，左上角为(384, 0)，右下角为(510, 128)，线宽为3
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    # 绘制一个红色的圆，圆心为(447, 63)，半径为63，填充颜色
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    # 绘制一个白色的椭圆，中心为(256, 256)，长轴为100，短轴为50，起始角度为0，结束角度为180，填充颜色
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

    # 定义一个多边形的顶点数组
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # 重塑顶点数组的形状
    pts = pts.reshape((-1, 1, 2))
    # 绘制一个黄色的多边形
    cv.polylines(img, [pts], True, (0, 255, 255))

    # 在图像上绘制白色的文本“OpenCV”，位置为(10, 500)，字体为HERSHEY_SIMPLEX，字体大小为4，颜色为白色，线宽为2，线型为LINE_AA
    cv.putText(img, 'OpenCV', (10, 500), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv.LINE_AA)

    # 返回绘制后的图像
    return img

# 鼠标回调函数
def draw_dynamic_shapes(event, x, y, flags, param):
    global ix, iy, drawing, mode, thickness
    # 如果鼠标左键按下
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 如果鼠标移动
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(param, (ix, iy), (x, y), (0, 255, 0), thickness)
            else:
                cv.circle(param, (x, y), thickness, (0, 0, 255), -1)
    # 如果鼠标左键抬起
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(param, (ix, iy), (x, y), (0, 255, 0), thickness)
        else:
            cv.circle(param, (x, y), thickness, (0, 0, 255), -1)

# 主程序
def main():
    global drawing, mode, ix, iy, thickness
    drawing = False  # 如果 True 是鼠标按下
    mode = True  # 如果 True，画矩形，按下‘m’切换到曲线
    ix, iy = -1, -1
    thickness = 5  # 初始化笔触粗细

    # 初始化静态图像
    static_img = draw_static_shapes()

    # 初始化动态图像
    dynamic_img = np.zeros((512, 512, 3), np.uint8)

    # 创建两个窗口
    cv.namedWindow('Static Image')
    cv.namedWindow('Dynamic Image')
    cv.setMouseCallback('Dynamic Image', draw_dynamic_shapes, param=dynamic_img)

    while True:
        # 显示静态图像
        cv.imshow('Static Image', static_img)
        # 显示动态图像
        cv.imshow('Dynamic Image', dynamic_img)

        # 按下 'm' 切换模式
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        # 按下 '+' 增加笔触粗细
        elif k == ord('+'):
            thickness += 1
            print(f"Pen thickness increased to {thickness}")
        # 按下 '-' 减少笔触粗细
        elif k == ord('-'):
            thickness = max(1, thickness - 1)  # 确保笔触粗细不小于 1
            print(f"Pen thickness decreased to {thickness}")
        # 按下 'q' 退出程序
        elif k == ord('q'):
            break

    # 关闭所有 OpenCV 窗口
    cv.destroyAllWindows()

# 运行主程序
if __name__ == "__main__":
    main()