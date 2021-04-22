def openMethod(filename):
    """open 方法读取txt文件"""
    data = []
    file = open(filename,'r')
    file_data = file.readlines() # 读取所有行
    # from row in file_data:
