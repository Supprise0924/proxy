# TopFreeProxies
[![GitHub Workflow Status](https://github.com/alanbobs999/topfreeproxies/actions/workflows/get-proxies.yml/badge.svg)](https://github.com/alanbobs999/TopFreeProxies/actions/workflows/get-proxies.yml) 

![Watchers](https://img.shields.io/github/watchers/alanbobs999/topfreeproxies) ![Stars](https://img.shields.io/github/stars/alanbobs999/topfreeproxies) ![Forks](https://img.shields.io/github/forks/alanbobs999/topfreeproxies) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=alanbobs999.topfreeproxies) ![LICENSE](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)

[仓库介绍](https://github.com/alanbobs999/TopFreeProxies#仓库介绍) | [使用方法](https://github.com/alanbobs999/TopFreeProxies#使用方法) | [节点信息](https://github.com/alanbobs999/TopFreeProxies#节点信息) | [软件推荐](https://github.com/alanbobs999/TopFreeProxies#客户端选择) | [机场推荐](https://github.com/alanbobs999/TopFreeProxies#机场推荐) | [仓库声明](https://github.com/alanbobs999/TopFreeProxies#仓库声明)

## 仓库介绍
本仓库自动化功能全部基于 `GitHub Actions` 实现，如有需要可以自行 Fork 实现个性化需求，功能配置在 `./utils/config.ini` 配置文件中。

对网络上各免费节点池及博主分享的节点进行测速筛选出较为稳定高速的节点，再导入到仓库中进行分享记录。所筛选的节点链接在仓库 `./sub/sub_list.json` 文件中，其中大部分为其他 `GitHub` 仓库链接，如果大家有好的订阅链接欢迎提交 PR ，这些链接包含的所有节点会合并在仓库 `./sub/sub_merge.txt` 中。

测速筛选后的节点订阅文件在仓库根目录 `Eterniy`(Base64) 和 `Eternity.yaml`(Clash)。同时在仓库的 `./update` 中保留了原始节点链接的的记录。

订阅转换使用 [subconverter](https://github.com/tindy2013/subconverter) 实现，测速功能使用 [LiteSpeedTest](https://github.com/xxf098/LiteSpeedTest) 在 `GitHub Actions` 环境下实现，所以美国节点较多，不能很好代表国内网络环境下节点可用性，目前正在解决这一问题。

虽然是测速筛选过后的节点，但仍然会出现部分节点不可用的情况，遇到这种情况建议选择`Clash`, `Shadowrocket`之类能自动切换低延迟节点的客户端。

## 使用方法
将以下订阅链接导入相应客户端即可。链接中大部分为 SS 协议节点，少量 Vmess, Trojan ,SSR 协议节点，建议选择协议支持完整的客户端。

- [多协议Base64编码](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity)
- [Clash](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yaml)

另有国内加速链接：

- [多协议Base64编码](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity)
- [Clash](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity.yaml)

>`Clash`链接所使用的配置在仓库`./update/provider/`中，有相应配置文件和以国家分类的`proxy-provider`。
>
>需要其它配置可使用订阅转换工具自行转换。
>自用在线订阅转换网址：[sub-web-modify](https://sub.v1.mk/)

## 节点信息
### 高速节点
高速节点数量: `96`
<details>
  <summary>展开复制节点</summary>

    ssr://c3Yuc3NyZnJlZTcueHl6OjQ0MDAyOmF1dGhfY2hhaW5fYTpub25lOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9OEotSHNQQ2ZoN2NnNlotcDVadTlJREF3TXlBeSZvYmZzcGFyYW09JnByb3RvcGFyYW09
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:803#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203803-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ssr://Y2xhc2g2LTEuc3NyZnJlZTYueHl6OjQ0MDA0OmF1dGhfY2hhaW5fYTpub25lOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TWk0MU9YeExVbmR0ZERFd01UTTNOQSZvYmZzcGFyYW09JnByb3RvcGFyYW09
    ssr://MTIxLjAuOTcuNDc6NDQwMDQ6YXV0aF9jaGFpbl9hOm5vbmU6dGxzMS4yX3RpY2tldF9hdXRoOlpHOXVaM1JoYVhkaGJtY3VZMjl0Lz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz1NaTQzTm54TFVuZHRkREV3TVRNM055QXkmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPQ
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@38.121.43.71:8882#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%20128
    trojan://67960bfb-00de-4a6b-9a7a-e74fc9e8b158@cat1.sshocean.net:443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20001
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxMzQwIiwiYWRkIjoidW51czAxLmFqZGtqYWxqZGoueHl6IiwicG9ydCI6IjEwODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTVlOWZkYTEtZGM0OC0zYmJkLThhMTUtZTY1Mjg4ODJlYTNiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii82IiwiaG9zdCI6ImxpdmUuYmlsaWJpbGkuY29tIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQwMzIiLCJhZGQiOiJ1bnVzMDEuYWpka2phbGpkai54eXoiLCJwb3J0IjoiMTA4MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NWU5ZmRhMS1kYzQ4LTNiYmQtOGExNS1lNjUyODg4MmVhM2IiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzYiLCJob3N0IjoidW51czAxLmFqZGtqYWxqZGoueHl6IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:809#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203809-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://67960bfb-00de-4a6b-9a7a-e74fc9e8b158@cat1.sshocean.net:443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%A6%20CA%201%20%E2%86%92%20openitsub.com%202
    trojan://xxoo@138.124.183.216:443?allowInsecure=1#NO%201%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ssr://Y2xhc2g2LTMuc3NyZnJlZTYueHl6OjQ0MDA0OmF1dGhfY2hhaW5fYTpub25lOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TWk0eE5IeExVbmR0ZERFd01UTTBNdyZvYmZzcGFyYW09JnByb3RvcGFyYW09
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxMzI2IiwiYWRkIjoidW51czAxLmFqZGtqYWxqZGoueHl6IiwicG9ydCI6IjEwODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTVlOWZkYTEtZGM0OC0zYmJkLThhMTUtZTY1Mjg4ODJlYTNiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii82IiwiaG9zdCI6InVudXMwMS5hamRramFsamRqLnh5eiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.68.135.19:8119#%F0%9F%87%BA%F0%9F%87%B8%20%5B09-26%5D%7Copenrunner%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FDallas_39%202
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@169.197.143.232:7307#ZZ_21%202
    ssr://Y2xhc2g2LTMuc3NyZnJlZTYueHl6OjQ0MDA0OmF1dGhfY2hhaW5fYTpub25lOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TWk0eE5IeExVbmR0ZERFd01UTTBNeUF5Jm9iZnNwYXJhbT0mcHJvdG9wYXJhbT0
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsImFkZCI6IjEzOS45OS45MS45NSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://6e3b4240-38f9-4321-9b3c-bc669a34b848@141.94.76.177:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20DE%201%20%E2%86%92%20openitsub.com%202
    ssr://Y2xhc2g0LTIuc3NyZnJlZTQueHl6OjEyMzQ1OmF1dGhfY2hhaW5fYTpub25lOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9OEotSHNQQ2ZoN2NnNlotcDVadTlJREF3TWcmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPQ
    trojan://xxoo@138.124.183.216:443?allowInsecure=1#US_138.124.183.216_10157f3f-37
    trojan://6e3b4240-38f9-4321-9b3c-bc669a34b848@141.94.76.177:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20DE%201%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@172.99.190.39:5003#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2039
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwMSIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifDIyLjg2TWIiLCJhZGQiOiIxNjguMTM4LjIwNy42NiIsInBvcnQiOiIyMTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiI5MDVmOTliMS1lN2JhLTQ1ZTAtYWU0ZC1iMGZmZGYwYWQyNDUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxNCIsImFkZCI6IjEzOC4yLjQ0LjIxMSIsInBvcnQiOiIyMDA4MSIsInR5cGUiOiJub25lIiwiaWQiOiI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwNyAzIiwiYWRkIjoiMTUyLjcwLjIzNS4yMDciLCJwb3J0IjoiMzU0MTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjIzLjIyNS41Ny4yMjIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@169.197.141.14:7002#ZZ_20
    trojan://xxoo@138.124.183.226:443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%AD%20%E7%91%9E%E5%A3%AB%20002
    ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.143.66.99:8118#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2092
    vmess://eyJ2IjoiMiIsInBzIjoi55m95auWLTAzNCIsImFkZCI6IjEyOS4xNTQuNTcuMTM0IiwicG9ydCI6IjI2MjgyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNhYmJkZjVkLTNjY2EtNDYwNS1iYTFjLWM4OWE3ZDViNGMwNyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2075
    vmess://eyJ2IjoiMiIsInBzIjoifCA3LjI5TWIiLCJhZGQiOiIxODUuMjI1LjY5LjEzNCIsInBvcnQiOiI0NTA4MSIsInR5cGUiOiJub25lIiwiaWQiOiIzYzNiZmQ3NS1kYzMwLTRlNzYtODk0MC00N2UxMTM3ZTIxZjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTkzLjEyMi4xMTcuNTIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    trojan://67960bfb-00de-4a6b-9a7a-e74fc9e8b158@149.56.141.11:443?allowInsecure=1#CA_149.56.141.11_1016451d-109%202
    vmess://eyJ2IjoiMiIsInBzIjoi5Lqa5aSq5Zyw5Yy6IDAwMSIsImFkZCI6IjEwMy4xNTkuMTMyLjEwMiIsInBvcnQiOiIzMTM3MiIsInR5cGUiOiJub25lIiwiaWQiOiJjMTEyMzZhZi01NmE2LTQ5YjMtYzFiOS03YjU0YWMzYWNiNDIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%202%20%E2%86%92%20openitsub.com
    trojan://xxoo@138.124.183.222:443?allowInsecure=1#NO%202%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi5Lqa5aSq5Zyw5Yy6IDAwMSAyIiwiYWRkIjoiMTAzLjE1OS4xMzIuMTAyIiwicG9ydCI6IjMxMzcyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMxMTIzNmFmLTU2YTYtNDliMy1jMWI5LTdiNTRhYzNhY2I0MiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgQ07jgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIDUyIiwiYWRkIjoiNDMuMTU1Ljk2LjE1MSIsInBvcnQiOiI0Njk0NSIsInR5cGUiOiJub25lIiwiaWQiOiIzNzBhNWRmNC0wYWMwLTRlM2QtYWIxYy0yMTg4OTFjOWU2MzgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://xxoo@138.124.183.226:443?allowInsecure=1#mianfeifq%20209
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#GB_07%202
    ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.107.226.238:2375#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-538-38.107.226.238
    vmess://eyJ2IjoiMiIsInBzIjoifDE2Ljc4TWIiLCJhZGQiOiIxMDMuMTU5LjEzMi4xMDIiLCJwb3J0IjoiMzEzNzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzExMjM2YWYtNTZhNi00OWIzLWMxYjktN2I1NGFjM2FjYjQyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2011%202
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2020%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQwMDUiLCJhZGQiOiJ0YW9iYW8uYmFiYXpodWppLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmE0OTE4ZGUtYWRjZS00YzRlLWFhMDAtODhhNDIyN2NmNmVhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kaWRpIiwiaG9zdCI6InRhb2Jhby5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2085
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#GB_07
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cg5be06KW/IDAwMSIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%20116%202
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#GB_07%202%202
    trojan://xxoo@138.124.183.222:443?allowInsecure=1#NO%201%20%E2%86%92%20openitsub.com%202
    trojan://xxoo@138.124.183.222:443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%AD%20%E7%91%9E%E5%A3%AB%20001
    vmess://eyJ2IjoiMiIsInBzIjoifCA4LjQxTWIiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMjMuMjI1LjU3LjIyMiIsInRscyI6IiJ9
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20027
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2023%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxMDk5IiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMjlhLnJ1aTc3LmNvbSIsInBvcnQiOiI1MjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiIwZjFkZjNmYi00ZGM1LTQ1NTgtOWJkZS00ZjcwM2M4NjRhNzgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9jZWF0dndzIiwiaG9zdCI6IjEuNzMxODA4LnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMiIsImFkZCI6IjE1Mi43MC4yMzUuMjA3IiwicG9ydCI6IjM1NDEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcwZDk1MzA4LTJhNjEtNGY5My1mMTM5LTkxMDNkMDU4N2ZkOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIyMy4yMjUuNTcuMjIyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxNDE4IiwiYWRkIjoidGFvYmFvLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjJhNDkxOGRlLWFkY2UtNGM0ZS1hYTAwLTg4YTQyMjdjZjZlYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGlkaSIsImhvc3QiOiJ0YW9iYW8uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNTg5IiwiYWRkIjoiMTY4LjEzOC4yMDcuNjYiLCJwb3J0IjoiMjEzNjUiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTA1Zjk5YjEtZTdiYS00NWUwLWFlNGQtYjBmZmRmMGFkMjQ1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDkvIrmnJcgIDI4IiwiYWRkIjoiYXJ2YW5jbG91ZC5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjgzMTM4MWQtNjMyNC00ZDUzLWFkNGYtOGNkYTQ4YjMwODExIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ncmFwaHFsIiwiaG9zdCI6Im1haHNhcHJveHkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xOC4xNDMuMTU5LjE3MyIsImFkZCI6IjE4LjE0My4xNTkuMTczIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIxZDg5OTlmZC05MDQ1LTQwZGYtODNlOC0xOTA3MjE5MTM0MTIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgU0fjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIDMiLCJhZGQiOiIxOC4xNDMuMTU5LjE3MyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMWQ4OTk5ZmQtOTA0NS00MGRmLTgzZTgtMTkwNzIxOTEzNDEyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://6e3b4240-38f9-4321-9b3c-bc669a34b848@141.94.76.177:443?allowInsecure=1#_TG%E9%A2%91%E9%81%93%40baipiaoeverything_4
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDEuMTAxLjExNC4zMyIsImFkZCI6IjE0MS4xMDEuMTE0LjMzIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJlNWE4OGNlMi1mYzFiLTQ1ZDEtOWM1Zi01NTM3MjFkMjgwMDQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJ2MnJheTEuemh1amljbjIub3JnIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxMzMiLCJhZGQiOiJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoiZWUuY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9
    trojan://origin@188.40.251.19:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20DE%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91%203
    trojan://Sp3eDVp@content-provider24.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=content-provider24.cdn-delivery.akamaicd.com#%F0%9F%87%B3%F0%9F%87%B1%20NL%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxNTMiLCJhZGQiOiJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoiZWUuY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@jgwcc3.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh7cg5LyK5pyXXzEwMTQwMDgiLCJhZGQiOiJvamplLWxhb3dhbmcuYXBwcy5pci10aHItYXQxLmFydmFuLnJ1biIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjExMmI2MzItZmI2Yy00NzgxLWJiNDItZDRkMzEwYWE1MzJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9sYW93YW5nIiwiaG9zdCI6Im9qamUtbGFvd2FuZy5hcHBzLmlyLXRoci1hdDEuYXJ2YW4ucnVuIiwidGxzIjoidGxzIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzEwOTIgfCA0LjE1TWIiLCJhZGQiOiJ1czZiMzEtbm9kZS5haXFpY2hlMTIzLmNvbSIsInBvcnQiOiI4MTkwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImE5MDU5N2MxLWJhYjMtNDIxNy1hZDZmLTA4Mzg2NzVjODY1MyIsImFpZCI6IjEwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXM2YjMxLW5vZGUuYWlxaWNoZTEyMy5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiX0NOX3dtdCgxMC4xMylfMjMiLCJhZGQiOiJ1czZiMzEtbm9kZS5haXFpY2hlMTIzLmNvbSIsInBvcnQiOiI4MTkwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImE5MDU5N2MxLWJhYjMtNDIxNy1hZDZmLTA4Mzg2NzVjODY1MyIsImFpZCI6IjEwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXM2YjMxLW5vZGUuYWlxaWNoZTEyMy5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwNyAyIiwiYWRkIjoidXM2YjMxLW5vZGUuYWlxaWNoZTEyMy5jb20iLCJwb3J0IjoiODE5MCIsInR5cGUiOiJub25lIiwiaWQiOiJhOTA1OTdjMS1iYWIzLTQyMTctYWQ2Zi0wODM4Njc1Yzg2NTMiLCJhaWQiOiIxMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InVzNmIzMS1ub2RlLmFpcWljaGUxMjMuY29tIiwidGxzIjoidGxzIn0=
    trojan://P9qGW38zz7@nice-jp03.tiktokcdn.buzz:43857?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%201%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.75.136.34:8080#_01%202
    trojan://P9qGW38zz7@nice-jp03.tiktokcdn.buzz:43857?allowInsecure=0#%7C45.31Mb
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMTQ3NjAiLCJhZGQiOiIxNDEuMTAxLjExNC4zMyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVhODhjZTItZmMxYi00NWQxLTljNWYtNTUzNzIxZDI4MDA0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoidjJyYXkxLnpodWppY24yLm9yZyIsInRscyI6InRscyJ9
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91%2015
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1#US_107.181.161.163_1016451d-200
    trojan://f2117e99-9b6e-47fd-b0a9-634a0b15b998@146.56.189.146:443?allowInsecure=1#%F0%9F%87%B0%F0%9F%87%B7%20KR%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cg5be06KW/IDAwMiAyIiwiYWRkIjoiMTY4LjEzOC4yMDEuMjA4IiwicG9ydCI6IjEwMzI4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJmODQ3YmY3LTBiYTUtNDg4NS1iZDJiLWRhNGQ3N2FmYmRhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgfCA2LjU0TWIiLCJhZGQiOiIxNjguMTM4LjIwMS4yMDgiLCJwb3J0IjoiMTAzMjgiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmY4NDdiZjctMGJhNS00ODg1LWJkMmItZGE0ZDc3YWZiZGE4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNDE1IiwiYWRkIjoiMTY4LjEzOC4yMDEuMjA4IiwicG9ydCI6IjEwMzI4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJmODQ3YmY3LTBiYTUtNDg4NS1iZDJiLWRhNGQ3N2FmYmRhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQ0MTciLCJhZGQiOiIxNzIuNjQuMTU1LjMwIiwicG9ydCI6IjIwNTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGFmYzZjZGYtNGYwYS00NzI1LWE0NGMtNWRhY2RjMmIyNzg0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiaGF4ZXUyLnppa2tjYy5nYSIsInRscyI6InRscyJ9
    trojan://P9qGW38zz7@nice-jp03.tiktokcdn.buzz:43857?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%20002
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbveWKoOWIqeemj+WwvOS6muW3nuehheiwty00My4xNTUuOTYuMTUxIDIiLCJhZGQiOiI0My4xNTUuOTYuMTUxIiwicG9ydCI6IjQ2OTQ1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjM3MGE1ZGY0LTBhYzAtNGUzZC1hYjFjLTIxODg5MWM5ZTYzOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91%2010
    trojan://f2117e99-9b6e-47fd-b0a9-634a0b15b998@jgw2.gaox.ml:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20github.com%2Ffreefq%20-%20%E6%97%A5%E6%9C%AC%20%202%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Lit5Zu9XzEwMTQ1NDcgMiIsImFkZCI6ImZvcmV2ZXJCLmxpdXN1Y2Z3c3Rsc25vZGUueHl6IiwicG9ydCI6IjUyMTYiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjM5NDY4YmQtMTU2My00MWMwLWJmNTItNzQzNDc0MjEzMGEyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saXVsaXN1YW5zdWFuIiwiaG9zdCI6ImZvcmV2ZXJCLmxpdXN1Y2Z3c3Rsc25vZGUueHl6IiwidGxzIjoiIn0=

</details>

### 所有节点
合并节点总数: `4153`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `219`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `152`
- [freefq/free](https://github.com/freefq/free), 节点数量: `41`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4162`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `83`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `34`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `12`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `162`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `145`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `38`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `42`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `128`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `33`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `226`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `229`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `324`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `32`

## 客户端选择
### 主流桌面客户端
|                            MacOS                             |                            Linux                             |                           Windows                            | 简易描述                                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :------------------------------------------------- |
| [CFW](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [CFW](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [CFW(Clash For Windows)](https://github.com/Fndroid/clash_for_windows_pkg/releases) | SS, SSR, Trojan, Vmess, VLESS协议支持，策略分流能力强。            |
|     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      |     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      |     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      | SS, SSR, Trojan, Vmess, VLESS, Trojan-Go协议支持（需安装相关插件）。 |
|                              ×                               |                              ×                               |      [V2rayN](https://github.com/2dust/v2rayN/releases)      | SS, Trojan, Vmess, VLESS协议支持，有测速，测延迟功能，支持订阅，二维码，剪贴板导入及手动配置。                 |
|                              ×                               |                              ×                               |    [WinXray](https://github.com/TheMRLL/winxray/releases)    | SS, SSR, Trojan, Vmess, VLESS协议支持，支持自动连接最快节点。            |
|                              ×                               |                              ×                               | [Shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases) | SS协议支持， SS 专用客户端。                                       |
|                              ×                               |                              ×                               | [ShadowsocksR-windows](https://github.com/HMBSbige/ShadowsocksR-Windows/releases) | SSR协议支持，SSR 专用客户端。                                      |
|                [Surge](https://nssurge.com/)                 |                              ×                               |                              ×                               | SS, Trojan, Vmess协议支持，著名网络调试工具，策略分流能力强大，需付费。                        |
|   [ClashX](https://github.com/yichengchen/clashX/releases)   |                              ×                               |                              ×                               | SS, SSR, Trojan, Vmess协议支持，占用资源较少。                   |
|      [V2rayU](https://github.com/yanue/V2rayU/releases)      |                              ×                               |                              ×                               | SS, Trojan, Vmess协议支持，支持订阅，二维码，剪贴板导入，手动配置，二维码分享，与 V2RayN 类似。                        |

### 主流移动客户端
|                          iOS/iPadOS                          |                           Android                            | 简易描述                                                     |
| :----------------------------------------------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | [Shadowrocket](https://play.google.com/store/apps/details?id=com.v2cross.proxy) | SS, SSR, Trojan, Vmess, VLESS协议支持，iOS端需在非国区 App Store 购买，美区售价 $2.99；安卓端非与 iOS 端同一作者，不支持 SSR 协议，免费且内置免费节点。 |
|                [Surge](https://nssurge.com/)                 |                              ×                               | SS, Trojan, Vmess协议支持，iOS 端著名网络调试工具，需付费。                                  |
| [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620) |                              ×                               | SS, SSR, Trojan, Vmess协议支持，需在非国区AppStore购买，美区售价$4.99。 |
| [Potatso Lite](https://apps.apple.com/us/app/potatso-lite/id1239860606) |                              ×                               | SS, SSR协议支持，需在非国区AppStore购买，免费。              |
|                              ×                               | [Surfboard](https://play.google.com/store/apps/details?id=com.getsurfboard) | SS, SSR, Vmess协议支持，安卓端网络调试软件，兼容 Surge 2 配置。 |
|                              ×                               | [CFA(Clash For Android)](https://github.com/Kr328/ClashForAndroid/releases) | SS, SSR, Trojan, Vmess协议支持。                             |
|                              ×                               |  [SagerNet](https://github.com/SagerNet/SagerNet/releases)   | SS, SSR, Trojan, Vmess, VLESS协议支持。                      |
|                              ×                               | [Shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases) | SS协议支持，安卓专用 SS 客户端。                                                 |
|                              ×                               | [ShadowsocksR-android](https://github.com/HMBSbige/ShadowsocksR-Android/releases) | SSR协议支持，安卓专用 SSR 客户端。                                                |
|                              ×                               |     [V2rayNG](https://github.com/2dust/v2rayNG/releases)     | SS, Trojan, Vmess, VLESS协议支持，v2ray 内核。                           |

## 机场推荐
免费节点失效太快，推荐一些性价比高的机场应急使用。
- [魔戒.net](https://www.mojie.cyou/#/register?code=sAbl0qtT)
  - 按量计费机场, 1¥10G, 10¥130G
  - 所有套餐均是一样的节点与一样的服务，所有套餐流量永不过期，用完为止，不限制客户端数量，最高可提供 2Gbps 峰值
- [大迅云](https://daxun.club/#/register?code=JPmAFPav)
  - 最低月付 5¥50G, 12¥200G, 购买 12¥ 及以上套餐免费领取奈飞 + 迪士尼 Plus 共享号
  - 原生IP负载均衡，流媒体解锁晚高峰油管秒开，主打性价比，有试用
- [阿伟云](https://awslcn.xyz/#/register?code=8C18uZwl)
  - 最低月付 1¥ 起, 9.99¥100G
  - 无带宽速率限制，有流媒体解锁，香港 BGP 中继线路

## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

## 星标统计
[![Star History Chart](https://api.star-history.com/svg?repos=alanbobs999/TopFreeProxies&type=Date)](https://star-history.com/#alanbobs999/TopFreeProxies&Date)
