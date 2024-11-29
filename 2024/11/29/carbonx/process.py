import os

# 获取当前文件夹路径
current_folder = os.getcwd()

# 遍历当前文件夹下所有 .jpg 文件
for filename in os.listdir(current_folder):
    if filename.endswith(".jpg"):
        # 使用 "_" 分割文件名并获取最后一部分
        new_name = filename.split("_")[-1]

        # 构造旧文件的完整路径和新文件的完整路径
        old_path = os.path.join(current_folder, filename)
        new_path = os.path.join(current_folder, new_name)

        # 重命名文件
        os.rename(old_path, new_path)

        print(f'Renamed: {filename} -> {new_name}')

for i in range(22):
    name = "0" + str(i) if i < 10 else str(i)
    print("{%asset_image "+name+".jpg%}")