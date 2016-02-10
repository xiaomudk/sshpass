# ssh自动登录脚本

> ssh登陆不能在命令行中指定密码，sshpass正好解决了这个问题，它允许你用 -p 参数指定明文密码，然后直接登录远程服务器。 它支持密码从命令行,环境变量中读取。

<br />
**安装依赖库**
```
easy_install pexpect
或者
pip install pexpect
```

<br />
**sshpass用法:**
```
   sshpass 参数 SSH命令(ssh，sftp，scp等)。
    参数:
        -p password    //将参数password作为密码(key passphrase也是使用这个参数)。
        -e        //将环境变量SSHPASS作为密码。

```

*对于第1次连接主机出现的`Are you sure you want to continue connecting (yes/no)` 会自动输入`yes`。*

### 比如:
```
sshpass -p '123456' ssh root@192.168.56.102 "uptime"
sshpass -p '123456789' ssh -i ~/host_key root@192.168.56.102 "uptime"
sshpass -p'123456' rsync -av /tmp/abc.txt -e \'ssh -i ~/host_key -p22\' root@192.168.56.102:/tmp
```