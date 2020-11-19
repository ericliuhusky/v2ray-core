# Project V

[![GitHub Test Badge][1]][2] [![codecov.io][3]][4] [![GoDoc][5]][6] [![codebeat][7]][8] [![Downloads][9]][10] [![Downloads][11]][12]

[1]: https://github.com/v2fly/v2ray-core/workflows/Test/badge.svg "GitHub Test Badge"
[2]: https://github.com/v2fly/v2ray-core/actions "GitHub Actions Page"
[3]: https://codecov.io/gh/v2fly/v2ray-core/branch/master/graph/badge.svg?branch=master "Coverage Badge"
[4]: https://codecov.io/gh/v2fly/v2ray-core?branch=master "Codecov Status"
[5]: https://godoc.org/v2ray.com/core?status.svg "GoDoc Badge"
[6]: https://godoc.org/v2ray.com/core "GoDoc"
[7]: https://goreportcard.com/badge/github.com/v2fly/v2ray-core "Goreportcard Badge"
[8]: https://goreportcard.com/report/github.com/v2fly/v2ray-core "Goreportcard Result"
[9]: https://img.shields.io/github/downloads/v2ray/v2ray-core/total.svg "v2ray/v2ray-core downloads count"
[10]: https://github.com/v2ray/v2ray-core/releases "v2ray/v2ray-core release page"
[11]: https://img.shields.io/github/downloads/v2fly/v2ray-core/total.svg "v2fly/v2ray-core downloads count"
[12]: https://github.com/v2fly/v2ray-core/releases "v2fly/v2ray-core release page"

Project V is a set of network tools that help you to build your own computer network. It secures your network connections and thus protects your privacy. See [our website](https://www.v2fly.org/) for more information.

## Quick Start
服务端快速部署
1. wget https://github.com/ericliuhusky/v2ray-core/releases/download/5.3/easy.tar
2. tar xvf easy.tar
3. cd easy
4. ./v2raysev.sh
5. systemctl start v2ray
6. address:VPS.IP, port:10086, id:b831381d-6324-4d53-ad4f-8cda48b30811, alterId:0, level:0

服务端用户管理
1. wget https://github.com/ericliuhusky/v2ray-core/releases/download/5.3/v2rayum.tar
2. tar xvf v2rayum.tar
3. mv v2rayum /usr/local/bin
4. v2rayum -h查看帮助
5. v2rayum执行自动删除过期用户

客户端下载
- MacOS https://github.com/ericliuhusky/v2ray-core/releases/download/5.3/V2rayU.dmg
- Windows https://github.com/ericliuhusky/v2ray-core/releases/download/5.3/v2rayN-Core.zip
- Android https://github.com/ericliuhusky/v2ray-core/releases/download/5.3/v2rayNG_1.3.3.apk.zip

## License

[The MIT License (MIT)](https://raw.githubusercontent.com/v2fly/v2ray-core/master/LICENSE)

## Credits

This repo relies on the following third-party projects:

- In production:
  - [gorilla/websocket](https://github.com/gorilla/websocket)
  - [gRPC](https://google.golang.org/grpc)
  - [lucas-clemente/quic-go](https://github.com/lucas-clemente/quic-go)
  - [pires/go-proxyproto](https://github.com/pires/go-proxyproto)
  - [seiflotfy/cuckoofilter](https://github.com/seiflotfy/cuckoofilter)
  - [google/starlark-go](https://github.com/google/starlark-go)
- For testing only:
  - [miekg/dns](https://github.com/miekg/dns)
  - [h12w/socks](https://github.com/h12w/socks)
