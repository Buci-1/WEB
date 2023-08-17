由于网络限制，一些服务器通常需要使用代理才能连接外网，

那么我们使用docker pull 镜像时同样需要配置代理。

1. 在服务器上添加如下目录

```bash
mkdir /etc/systemd/system/docker.service.d
```

2. 创建如下文件，并配置你的代理服务器

```
$ vim /etc/systemd/system/docker.service.d/http_proxy.conf 
[Service] 
Environment="HTTP_PROXY=代理ip:port" 
Environment="HTTPS_PROXY=代理ip:port"
```

3. 重启docker

```
sudo systemctl daemon-reload

sudo systemctl restart docker
```

4. 检查代理配置

   sudo docker info

```
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: 172.30.23.110:10088
 HTTPS Proxy: 172.30.23.110:10088
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Registry Mirrors:
  https://registry.docker-cn.com/
  http://hub-mirror.c.163.com/
  https://docker.mirrors.ustc.edu.cn/
 Live Restore Enabled: false
```
