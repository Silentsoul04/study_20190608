#!/usr/bin/python3
import os

path_test = r'D:\xiaozhan_git\study_20190608\day22\day22-time.py'
print(os.path.basename('/root/runoob.txt'))         # 返回文件名 runoob.txt
print(os.path.dirname('/root/abc/runoob.txt'))          # 返回目录路径 /root/abc
print(os.path.split('/root/runoob.txt'))             # 分割文件名与路径 ('/root', 'runoob.txt')
print(os.path.join('root', 'test', 'runoob.txt'))    # 将目录和文件名合成一个路径root\test\runoob.txt
print(os.path.isfile(path_test))    # True

print(os.getcwd())     # D:\xiaozhan_git\study_20190608\day22

# os.chdir()   os.system()   os.popen().read()
# os.mkdir()    os.remove()

# os 常用方法
# os.remove() 删除文件
# os.rename() 重命名文件
# os.walk() 生成目录树下的所有文件名
# os.chdir() 改变目录
# os.mkdir/makedirs 创建目录/多层目录
# os.rmdir/removedirs 删除目录/多层目录
# os.listdir() 列出指定目录的文件
# os.getcwd() 取得当前工作目录
# os.chmod() 改变目录权限
# os.path.basename() 去掉目录路径，返回文件名
# os.path.dirname() 去掉文件名，返回目录路径
# os.path.join() 将分离的各部分组合成一个路径名
# os.path.split() 返回( dirname(), basename())元组
# os.path.splitext() 返回 (filename, extension) 元组
# os.path.getatime\ctime\mtime 分别返回最近访问、创建、修改时间
# os.path.getsize() 返回文件大小
# os.path.exists() 是否存在
# os.path.isabs() 是否为绝对路径
# os.path.isdir() 是否为目录
# os.path.isfile() 是否为文件