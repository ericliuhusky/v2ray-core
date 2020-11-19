#!/bin/sh
# v2ray linux服务器一键安装配置部署脚本

# 切换到当前目录
cd "$(dirname $0)"
# 下载v2ray-linux-64
wget https://github.com/ericliuhusky/v2ray-core/releases/download/v1.0.0/v2ray-linux-64.tar
# 解压
tar xvf v2ray-linux-64.tar
# 删除压缩包
rm v2ray-linux-64.tar

# 切换到v2ray目录
cd v2ray-linux-64

# 写入快速开始配置文件
echo '{
    "inbounds": [
        {
            "port": 10086,
            "protocol": "vmess",
            "settings": {
                "clients": [
                    {
                        "id": "b831381d-6324-4d53-ad4f-8cda48b30811"
                    }
                ]
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom"
        }
    ]
}' > config.json

# 把可执行程序v2ray移到/usr/local/bin
mv v2ray /usr/local/bin
# 把配置文件移动到/usr/local/etc/v2ray
if ! test -d /usr/local/etc/v2ray
then
mkdir /usr/local/etc/v2ray
fi
mv config.json /usr/local/etc/v2ray
# 把system service控制台服务描述文件移动到/usr/lib/systemd/system
mv systemd/system/v2ray.service /usr/lib/systemd/system
# 同步重新加载描述文件
systemctl daemon-reload