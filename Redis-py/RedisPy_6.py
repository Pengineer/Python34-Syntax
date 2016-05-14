# Redis持久化

'''
 Redis的持久化有两种方式，一种方法叫做快照（snapshotting），它可以将某一时刻的数据都写入硬盘；另一种方法叫
 只追加文件（append-only file, AOF）它会在执行写命令时，将被执行的写命令复制到硬盘里。这两种持久化的方法可
 以同时使用。
 '''

'''
 创建快照的方法：
 （1）客户端发送BGSAVE命令，其底层是通过调用fork创建一个子进程，因此在创建快照的过程中父进程仍然可以处理命令请求；
 （2）客户端发送SAVE命令，这种情况下Redis不再处理其他命令。SAVE命令用得少，除非内存吃紧。
 （3）设置SAVE配置选项，Redis自动进行快照的创建。
 （4）关闭服务器时，Redis会先执行SAVE命令，然后关闭服务器。
 （5）在Redis服务器连接另一个Redis服务器，并向对方发送SYNC命令来开始一次复制操作的时候，如果主服务器目前没有执行
      BGSAVE或则并非刚刚执行，那么主服务器就会执行BGSAVE命令。
'''

def process_logs(conn, path, callback):
    current_file, offset = conn.mget('progress:file', 'progress:position')
    pipe = conn.pipeline()

    def update_process():  # 通过使用闭包来减少重复代码
        pipe.mset({'progress:file':fname, 'progress:position':offset})
        pipe.execute()

    for fname in sorted(os.listdir(path)):
        if fname < current_file:
            continue

        inp = open(os.path.join(path, fname), 'rb')
        if fname == current_file:
            inp.seek(int(offset, 10))
        else:
            offset = 0

        current_file = None

        for lno, line in enumerate(inp):
            callback(pipe, line)
            offset += int(offset) + len(line)
            if not (lno+1) % 1000:
                update_progress()
            update_progress()
            inp.close()

'''
 通过创建快照来保存数据的缺点就是随着Redis占用内存的增多fork子进程的时间就会增加，从而导致系统停顿。
 AOF持久化会将被执行的写命令写入到AOF文件的末尾。AOF的缺点是随着Redis的运行，AOF文件的体积会越来越大，大的AOF文件
 也意味着较长时间的Redis恢复。
'''



