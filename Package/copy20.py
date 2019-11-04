import shutil
import os

# shutil.copy(来源路径， 目标路径)
# 返回值为目标路径
# 拷贝同时可以给目标重新命名 
result1 = shutil.copy("/python/Package/20.py", "/python/Package/Userpackage/copy20.py")
print(result1)


# shutil.copy2(来源路径，目标路径) 
# 同样是复制文件，保留元数据（文件信息）
# 返回目标路径
# copy和copy2 的唯一区别在于copy2复制文件时尽量保留元数据


# shutil.copyfile(源路径， 目标路径)  将文件中的内容复制到另一个文件当中
# 返回值为目标路径
# help(shutil.copyfile)
result2 = shutil.copyfile('./20.py', './copy20.py')
print(result2)
print(os.getcwd())