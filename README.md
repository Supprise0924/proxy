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

    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1#mianfeifq%20284
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=0#%7C43.25Mb
    trojan://6e3b4240-38f9-4321-9b3c-bc669a34b848@141.94.76.177:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20%E5%BE%B7%E5%9B%BD%20002
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAzNCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8xMTExMTEub25saW5lIiwiaG9zdCI6IndvcmtlcnMuZGV2IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifCA4LjUzTWIiLCJhZGQiOiIxMjkuMTU0LjU3LjEzNCIsInBvcnQiOiIyNjI4MiIsInR5cGUiOiJub25lIiwiaWQiOiJjYWJiZGY1ZC0zY2NhLTQ2MDUtYmExYy1jODlhN2Q1YjRjMDciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxNCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8xMTExMTEub25saW5lIiwiaG9zdCI6IndvcmtlcnMuZGV2IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBn@38.64.138.53:1035#%F0%9F%87%BA%F0%9F%87%B8%20%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.531035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@jgwxn4.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%202%20%E2%86%92%20openitsub.com
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g14.xingbayun.buzz:10001?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2019%20%E2%86%92%20openitsub.com
    trojan://0f5e6d9a-49af-4bc0-b04b-503102382144@ukt1.sshocean.net:443?allowInsecure=1#%F0%9F%87%AB%F0%9F%87%B7%20FR%203%20%E2%86%92%20openitsub.com
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1#%F0%9F%87%A6%F0%9F%87%BA%20AU%201%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgX0tSX+mfqeWbvV8xQDIyIiwiYWRkIjoibTQuNDAwMTAwMTAueHl6IiwicG9ydCI6IjM3MTIxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU3NWU0ZDkyLTEwNTYtNDRjMi04Y2FjLTc1ZWYxYzg1OWFkNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJtNC40MDAxMDAxMC54eXoiLCJ0bHMiOiJ0bHMifQ==
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@152.67.98.30:443?allowInsecure=1#%F0%9F%87%A6%F0%9F%87%BA%20%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20005
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh7cg5LyK5pyXXzEwMTQwMDYiLCJhZGQiOiJNYWhzYVByb3h5VGVsZWdyYW1DaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2dyYXBocWwiLCJob3N0IjoiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLCJ0bHMiOiIifQ==
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1#%F0%9F%87%A6%F0%9F%87%BA%20AU%202
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g10.xingbayun.buzz:10002?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g10.xingbayun.buzz#%F0%9F%87%B8%F0%9F%87%AC%20%E6%96%B0%E5%8A%A0%E5%9D%A1%28TG%E9%A2%91%E9%81%93%40kxswa%29
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g14.xingbayun.buzz:10001?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g14.xingbayun.buzz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQwMTIiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYmY0MTlkNWY1OWY3ZDAud2luZG93c3VwZGF0ZS5jb20iLCJ0bHMiOiIifQ==
    trojan://137032ae-1bdb-445d-85e0-6edd7d343afb@nice-de02.nicevpn.top:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20DE%203%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh7cg5LyK5pyXXzEwMTQwMTQiLCJhZGQiOiJNYWhzYVByb3h5VGVsZWdyYW1DaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2dyYXBocWwiLCJob3N0IjoiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQwMDMiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYmY0MTlkNWY1OWY3ZDAud2luZG93c3VwZGF0ZS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQwMzQiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYmY0MTlkNWY1OWY3ZDAud2luZG93c3VwZGF0ZS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDIxLjQ0TWIiLCJhZGQiOiIxNTIuNzAuMjQxLjE4IiwicG9ydCI6IjI2Njc2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVjZDI3NGMwLTE3NWQtNDVmNy04Mjc2LWEzZGE5Mzc4NjYzMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@138.2.45.243:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20_%E7%BE%8E%E5%9B%BD_%5B%E6%99%B4%E5%9B%AD%E7%9A%84%E5%AE%9D%E8%97%8F%E5%BA%93%5D_44
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g10.xingbayun.buzz:10002?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%209%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV85IiwiYWRkIjoiMTM4LjIuOC4yMjciLCJwb3J0IjoiNTk0NDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNmZkMDQyZmEtZTg2NC00YTk1LTg1YmMtNmY1OTBhMDNkMzRhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImFld2ZoZTV6MXBva3JrdzhiaTlnMTAueGluZ2JheXVuLmJ1enoiLCJ0bHMiOiIifQ==
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g11.xingbayun.buzz:10001?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g11.xingbayun.buzz#%F0%9F%87%B8%F0%9F%87%AC%20%E6%96%B0%E5%8A%A0%E5%9D%A1%28TG%E9%A2%91%E9%81%93%40kxswa%29%203%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV85IDIiLCJhZGQiOiIxMzguMi44LjIyNyIsInBvcnQiOiI1OTQ0MiIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmQwNDJmYS1lODY0LTRhOTUtODViYy02ZjU5MGEwM2QzNGEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYWV3ZmhlNXoxcG9rcmt3OGJpOWcxMC54aW5nYmF5dW4uYnV6eiIsInRscyI6IiJ9
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g09.xingbayun.buzz:1003?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%202%20%E2%86%92%20openitsub.com
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g11.xingbayun.buzz:10001?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g11.xingbayun.buzz#%F0%9F%87%B8%F0%9F%87%AC%20%E6%96%B0%E5%8A%A0%E5%9D%A1%20011
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@140.238.205.173:443?allowInsecure=1#AU_140.238.205.173_10157f3f-23
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@168.138.44.176:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=jgwhdlb1.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20US%20556
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g11.xingbayun.buzz:10001?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1#%F0%9F%87%AE%F0%9F%87%B3%20%E5%8D%B0%E5%BA%A6%20003
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@168.138.44.176:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2028%20%E2%86%92%20openitsub.com
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1#%F0%9F%87%AE%F0%9F%87%B3%20%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India%2FHyderabad_26
    trojan://Sp3eDVp@content-provider5.cdn-delivery.akamaicd.com:443?allowInsecure=1#%F0%9F%87%AB%F0%9F%87%B7%20FR%206%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoifDIxNy4yNU1iIiwiYWRkIjoiMTM5Ljk5LjkxLjk1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImFld2ZoZTV6MXBva3JrdzhiaTlnMTAueGluZ2JheXVuLmJ1enoiLCJ0bHMiOiIifQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%207%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@162.251.61.221:805#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-162.251.61.221805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ssr://MTgzLjIzMi4xNDEuMTE5OjU2MTphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVySzU1NjZoNlppXzVMeWY1NmVSNW9xQSZvYmZzcGFyYW09JnByb3RvcGFyYW09TlRNNU1qYzZhR3BuYW5WNU5uUTJOVFZxYW1j
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2014%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MyIsImFkZCI6IjE3MC4xODcuMjMwLjIzMSIsInBvcnQiOiI2MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiI0OTE2NjkyOS0wMjBlLTRlZjAtOTdlNy03OTg5Y2U5MmZjNjkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNzAuMTg3LjIzMC4yMzEiLCJ0bHMiOiIifQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=0#%7C59.07Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@134.195.196.143:805#%F0%9F%87%A8%F0%9F%87%A6%20_CA_%E5%8A%A0%E6%8B%BF%E5%A4%A7
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTE3MiB8MTEuOTZNYiIsImFkZCI6IjEzOC4yLjQ0LjIxMSIsInBvcnQiOiIyMDA4MSIsInR5cGUiOiJub25lIiwiaWQiOiI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImFld2ZoZTV6MXBva3JrdzhiaTlnMTAueGluZ2JheXVuLmJ1enoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgU0fjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIDUiLCJhZGQiOiJzZzAyLnhpYW9xaTk5LmNmIiwicG9ydCI6IjYzNjMyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ5MTY2OTI5LTAyMGUtNGVmMC05N2U3LTc5ODljZTkyZmM2OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InNnMDIueGlhb3FpOTkuY2YiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1zZzAyLnhpYW9xaTk5LmNmIiwiYWRkIjoic2cwMi54aWFvcWk5OS5jZiIsInBvcnQiOiI2MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiI0OTE2NjkyOS0wMjBlLTRlZjAtOTdlNy03OTg5Y2U5MmZjNjkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJzZzAyLnhpYW9xaTk5LmNmIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwOCIsImFkZCI6IjEzOC4yLjQ0LjIxMSIsInBvcnQiOiIyMDA4MSIsInR5cGUiOiJub25lIiwiaWQiOiI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImFld2ZoZTV6MXBva3JrdzhiaTlnMTAueGluZ2JheXVuLmJ1enoiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@162.251.61.221:800#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-162.251.61.221800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1zZzAyLnhpYW9xaTk5LmNmIDIiLCJhZGQiOiJzZzAyLnhpYW9xaTk5LmNmIiwicG9ydCI6IjYzNjMyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ5MTY2OTI5LTAyMGUtNGVmMC05N2U3LTc5ODljZTkyZmM2OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InNnMDIueGlhb3FpOTkuY2YiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDIyLjM0TWIiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYWV3ZmhlNXoxcG9rcmt3OGJpOWcxMC54aW5nYmF5dW4uYnV6eiIsInRscyI6IiJ9
    trojan://0f5e6d9a-49af-4bc0-b04b-503102382144@ukt1.sshocean.net:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20020
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hKFRH6aKR6YGTQGt4c3dhKSA1IiwiYWRkIjoiMTcwLjE4Ny4yMzAuMjMxIiwicG9ydCI6IjYzNjMyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ5MTY2OTI5LTAyMGUtNGVmMC05N2U3LTc5ODljZTkyZmM2OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjE3MC4xODcuMjMwLjIzMSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzAuMTg3LjIzMC4yMzEiLCJhZGQiOiIxNzAuMTg3LjIzMC4yMzEiLCJwb3J0IjoiNjM2MzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDkxNjY5MjktMDIwZS00ZWYwLTk3ZTctNzk4OWNlOTJmYzY5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTcwLjE4Ny4yMzAuMjMxIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifCA0LjU1TWIiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYWV3ZmhlNXoxcG9rcmt3OGJpOWcxMC54aW5nYmF5dW4uYnV6eiIsInRscyI6IiJ9
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@152.67.162.166:443?allowInsecure=1#%F0%9F%87%AE%F0%9F%87%B3%20%E5%8D%B0%E5%BA%A6%20001
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@152.67.162.166:443?allowInsecure=1#IN_152.67.162.166_10157f3f-72
    vmess://eyJ2IjoiMiIsInBzIjoiSlBfMTM4LjIuNDQuMjExXzEwMTU3ZjNmLTE0MyIsImFkZCI6IjEzOC4yLjQ0LjIxMSIsInBvcnQiOiIyMDA4MSIsInR5cGUiOiJub25lIiwiaWQiOiI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYWV3ZmhlNXoxcG9rcmt3OGJpOWcxMC54aW5nYmF5dW4uYnV6eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwNyIsImFkZCI6IjE1Mi43MC4yMzUuMjA3IiwicG9ydCI6IjM1NDEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcwZDk1MzA4LTJhNjEtNGY5My1mMTM5LTkxMDNkMDU4N2ZkOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhZXdmaGU1ejFwb2tya3c4Ymk5ZzEwLnhpbmdiYXl1bi5idXp6IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@195.12.49.82:812#%F0%9F%87%AC%F0%9F%87%A7%20%5B10-16%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-800-195.12.49.82
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g19.xingbayun.buzz:1001?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g19.xingbayun.buzz#%F0%9F%87%A9%F0%9F%87%AA%20%E5%BE%B7%E5%9B%BD%20004
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@195.12.49.82:812#%F0%9F%87%AC%F0%9F%87%A7%20%5B10-16%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-392-195.12.49.82
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=www.sxsy88.tk#%F0%9F%87%BA%F0%9F%87%B8%20US%20431
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@162.251.61.221:812#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-162.251.61.221812-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIaw@185.126.116.125:9098#RO_08%202%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDkvIrmnJcgIDI4IiwiYWRkIjoiYXJ2YW5jbG91ZC5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjgzMTM4MWQtNjMyNC00ZDUzLWFkNGYtOGNkYTQ4YjMwODExIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ncmFwaHFsIiwiaG9zdCI6Im1haHNhcHJveHkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivKFRH6aKR6YGTQGt4c3dhKSAyIiwiYWRkIjoiMjk2Y2FjNDMtZmY5MC00ZmQxLTk0ODUtMDY3MWMyZGM2NGE0LmNubmljLnJpcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjZjZiODlkNS1hOGE4LTQ0NzgtYTQzNS1iZGVkNjViMDY3MDUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ0bXMuZGluZ3RhbGsuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIaw@185.126.116.125:9098#RO_08%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0yOTZjYWM0My1mZjkwLTRmZDEtOTQ4NS0wNjcxYzJkYzY0YTQuY25uaWMucmlwIiwiYWRkIjoiMjk2Y2FjNDMtZmY5MC00ZmQxLTk0ODUtMDY3MWMyZGM2NGE0LmNubmljLnJpcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjZjZiODlkNS1hOGE4LTQ0NzgtYTQzNS1iZGVkNjViMDY3MDUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ0bXMuZGluZ3RhbGsuY29tIiwidGxzIjoiIn0=
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2016%20%E2%86%92%20openitsub.com%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsImFkZCI6IjEzOS45OS45MS45NSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhZXdmaGU1ejFwb2tya3c4Ymk5ZzEwLnhpbmdiYXl1bi5idXp6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMDgt5LuY6LS55o6o6I2Qc3VvLnl0L3NzcnN1YiIsImFkZCI6IjE3Mi42NC4xNTMuMjAwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzQuemh1amljbjIuY29tIiwidGxzIjoidGxzIn0=
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g25.xingbayun.buzz:10001?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g25.xingbayun.buzz#%F0%9F%87%A6%F0%9F%87%BA%20%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20001
    trojan://0f5e6d9a-49af-4bc0-b04b-503102382144@ukt1.sshocean.net:443?allowInsecure=0#%7C%202.76Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgSEsgMyDihpIgb3Blbml0c3ViLmNvbSIsImFkZCI6IjI5NmNhYzQzLWZmOTAtNGZkMS05NDg1LTA2NzFjMmRjNjRhNC5jbm5pYy5yaXAiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2Y2Yjg5ZDUtYThhOC00NDc4LWE0MzUtYmRlZDY1YjA2NzA1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidG1zLmRpbmd0YWxrLmNvbSIsInRscyI6IiJ9
    trojan://862e68d2-05f3-4253-9116-819623bb7335@aewfhe5z1pokrkw8bi9g09.xingbayun.buzz:1003?allowInsecure=1&sni=aewfhe5z1pokrkw8bi9g09.xingbayun.buzz#%F0%9F%87%B8%F0%9F%87%AC%20%E6%96%B0%E5%8A%A0%E5%9D%A1%28TG%E9%A2%91%E9%81%93%40kxswa%29%202
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs01.bolab.net:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%206%20%E2%86%92%20openitsub.com
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2021%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxMjkiLCJhZGQiOiJlcjIubXliZXN0amouY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5YzQxOWE1My05YTI5LTRjNTktOTZhNy1iMDUyZTc5ZTRjMzciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzE2NTM1MzEiLCJob3N0IjoiZXIxLm15YmVzdGpqLmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.107.226.238:2375#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-16%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-782-38.107.226.238
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTQxNTMiLCJhZGQiOiJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoiZWUuY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.63.99:8090#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.63.998090-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@167.88.63.99:2375#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.63.992375-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2096
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@38.121.43.71:8882#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2076
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@167.88.63.99:7307#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.63.997307-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.68.134.85:5600#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2039
    ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@38.68.134.85:6679#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2099
    ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.68.134.48:2375#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-15%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-942-38.68.134.48
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@167.88.62.68:5600#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.62.685600-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@167.88.62.68:8881#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.62.688881-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@167.88.62.68:8000#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.62.688000-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@169.197.143.232:7307#ZZ_21

</details>

### 所有节点
合并节点总数: `4001`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `74`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `152`
- [freefq/free](https://github.com/freefq/free), 节点数量: `41`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4162`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `77`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `34`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `12`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `209`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `170`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `38`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `42`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `39`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `33`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `219`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `233`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `292`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `33`

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
