import matplotlib.pyplot as plt
import numpy as np

column = ['epoch', 'train_GIOU_loss', 'train_obj_loss', 'train_cls_loss', 'total', 'target', 'img_size', 'precision',
          'recall', 'MAP@0.5', 'F1', 'val_GIOU_loss', 'val_obj_loss', 'val_cls_loss']


def plot_result(result, title, ylabel):
    ind = column.index(title)  # 获取索引
    plt.figure(figsize=(10, 8), dpi=100)
    plt.title(title)
    plt.plot(result[:, 0], result[:, ind], color="#800080", linewidth=2.5, label=title)
    plt.xlabel('epoch')

    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


def result2matrix(result_dir, epoch_num):
    data = np.genfromtxt(result_dir)
    result = data[0:epoch_num + 1, 2:15]  # 获取数据
    print(f"\n一共{len(result)}个epochs的结果")
    epoch = np.arange(len(result))  # 生成epoch序号
    epoch = epoch.reshape(len(result), 1)
    result = np.hstack((epoch, result))  # 新添一列epoch
    return result


def plot_yolov5_curves(txt_dir):
    output = result2matrix(txt_dir, epoch_num=300)
    plot_result(output, 'train_GIOU_loss', 'loss')
    plot_result(output, 'train_obj_loss', 'loss')
    plot_result(output, 'train_cls_loss', 'loss')
    plot_result(output, 'val_GIOU_loss', 'loss')
    plot_result(output, 'val_obj_loss', 'loss')
    plot_result(output, 'val_cls_loss', 'loss')
    plot_result(output, 'total', 'loss')
    plot_result(output, 'precision', 'value')
    plot_result(output, 'recall', 'value')
    plot_result(output, 'MAP@0.5', 'value')
    plot_result(output, 'F1', 'value')


'''
一共11个图，可根据自己要求拓展
'''
if __name__ == '__main__':
    result_dir = "C:/pythonx/yolo/yolov5-fire/runs/train/exp2/results.csv"
    plot_yolov5_curves(result_dir)


