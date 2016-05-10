# os模块与os.path模块

'''
 因为os模块的存在，使得Python不用关注底层操作系统的异构性。
 os模块中关于文件/目录常用的函数如下：
 getcwd()：返回当前工作目录
 chdir(path)：改变工作目录
 listdir(path='.')：列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
 mkdir(path)：创建单层目录，如该目录已存在抛出异常
 mkdirs(path)：递归创建多层目录，如该目录已存在抛出异常，注意：'E"\\a\\b'和'E:\\a\\c'并不会冲突
 remove(path)：删除文件
 rmdir(path)：删除单层目录，如该目录非空则抛出异常
 removedirs(path)：递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
 rename(old, new)：将文件old重命名为new
 system(command)：运行系统的shell命令

 以下是支持路劲操作中常用到的一些定义，支持所有平台
 os.curdir：指代当前目录（'.'）
 os.pardir：指代上一级目录（'..'）
 os.sep：输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
 os.linesep：当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
 os.name：指代当前使用的操作系统（包括：'posix', 'nt', 'mac', 'os2', 'ce', 'java'）

os.path模块中关于路径常用的函数使用方法
basename(path)：去掉目录路径，单独返回文件名
dirname(path)：去掉文件名，单独返回目录路径
join(path1[,path2[,...]])：将path1，怕他会2各部分组合成一个路径名
split(path)：分割文件名与路径，返回（f_path, f_name）元组。如果完全使用目录，他也会将最后一个目录作为温佳明分离，且不会判断文件或则目录是否存在
splitext(path)：分离文件名与扩展名，返回（f_name, f_extension）元组
getsize(file)：返回指定文件的尺寸，单位是字节
getatime(file)：返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getctime(file)：返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getmtime(file)：返回指定文件的最新修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
exists(path)：判断指定路径（目录或文件）是否存在
isabs(path)：判断指定路径是否为绝对路径
isdir(path)：判断指定路径是否存在且时一个目录
isfile(path)：判断指定路径是否存在且时一个文件
islink(path)：判断指定路径是否存在且时一个符号链接
ismount(path)：判断指定路径是否存在且时一个挂载点
samefile(path1, patj2)：判断path1和path2两个路径是够执行同一个文件
'''
