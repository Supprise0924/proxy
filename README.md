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
高速节点数量: `93`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzExMDIwNTMiLCJhZGQiOiJhZWFkanBhZXMwMS54bi0tejRxNDhsY3ZwLmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiIzZTgyMGViMC0zZjA2LTQzMzctYTRmYy0wYzNjN2MwZDNiNGQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2ltYWdlcyIsImhvc3QiOiJzaG91dGluZ3RvdXRpYW8zLjEwMDEwLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDIyNjQiLCJhZGQiOiI4LjIxOS41OC41OCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTE2NDZmOWEtYjRlOS00YWNhLWJmZTMtODg5MmIzZTU4ZmU3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9yYXkiLCJob3N0IjoibGczMC5jZmNkbjMueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDIyODkiLCJhZGQiOiI4LjIxOS4xMjEuMTkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkxNjQ2ZjlhLWI0ZTktNGFjYS1iZmUzLTg4OTJiM2U1OGZlNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcmF5IiwiaG9zdCI6ImxnMzAuY2ZjZG4zLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDIyOTAiLCJhZGQiOiI4LjIxOS4xNzMuMTA4IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MTY0NmY5YS1iNGU5LTRhY2EtYmZlMy04ODkyYjNlNThmZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzMwLmNmY2RuMy54eXoiLCJ0bHMiOiJ0bHMifQ==
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@jgwcc3.gaox.ml:443?allowInsecure=0#%F0%9F%87%B0%F0%9F%87%B7%20%5B11-02%5D-%F0%9F%87%B0%F0%9F%87%B7-%E9%9F%A9%E5%9B%BD%E6%98%A5%E5%B7%9D-254-jgwcc3.gaox.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDIwMDIiLCJhZGQiOiIxNS4yMzUuMTQ3LjE4NiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9FcnR1c2c4Ni82MzUwMTQ2MzhjMjY0LyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjOWRhYTYxNi0zZDY3LTQwNzgtOWZhNS0yOWVmYTRiMzE4ZTI@xjp.paolujichang.com:81#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-144-xjp.paolujichang.com
    trojan://0dd659b8-a536-4e5b-aa42-db4a61a04847@13.251.63.10:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-658-13.251.63.10
    trojan://16c267c7-9734-4703-b3fb-5a23c2ab7fda@43.198.12.229:28443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-178-43.198.12.229
    trojan://16c8c162-71ef-4d19-8a8e-c690aeb998d7@tr-jp.sy-fly.net:12888?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-070-tr-jp.sy-fly.net
    trojan://275d9aa8-b271-43d1-b1cf-1f3e6e881047@zf1.windowsupdate1.com:50010?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-4094-zf1.windowsupdate1.com
    trojan://27d01290-3763-11ed-90db-1239d0255272@sg1-trojan.bonds.id:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-398-sg1-trojan.bonds.id
    trojan://28bccca2-43d2-47f8-bd63-b1361ce7d362@kh.iamnotagoodman.com:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-394-kh.iamnotagoodman.com
    trojan://2f95d996-e911-4b1b-82b1-1d86bf2c517d@23.100.91.117:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-046-23.100.91.117
    trojan://35b65b31-174e-4007-ad65-8eae6d7b8c41@tw01.henet.top:30000?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE%E8%8A%B1%E8%8E%B2%E5%8E%BF-008-tw01.henet.top
    trojan://36ebef7d1b1d6205fd0c55f28800e674@45.66.134.219:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-4036-45.66.134.219
    trojan://423b4a2b-987f-46a7-9222-776839117b3a@31.72img.xyz:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-660-31.72img.xyz
    trojan://4c7985e0-79e8-11eb-b8d3-1239d0255272@103.253.24.216:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-648-103.253.24.216
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-3376-43.229.153.148
    trojan://6c8b18adb11737af@211.72.35.152:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-696-211.72.35.152
    trojan://6c8b18adb11737af@211.72.35.155:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-694-211.72.35.155
    trojan://6c8b18adb11737af@211.72.35.158:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-692-211.72.35.158
    trojan://6c8b18adb11737af@60.249.3.125:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-324-60.249.3.125
    trojan://6c8b18adb11737af@60.249.3.226:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-690-60.249.3.226
    trojan://6c8b18adb11737af@60.249.3.228:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-078-60.249.3.228
    trojan://6c8b18adb11737af@60.249.3.230:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-688-60.249.3.230
    trojan://6d8d2ced-54da-4e79-bfae-2ed55345b954@23.100.91.146:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-552-23.100.91.146
    trojan://6d8d2ced-54da-4e79-bfae-2ed55345b954@23.100.91.61:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-003-23.100.91.61
    trojan://750a29bf-0a40-437f-b120-38de74ae7eaf@141.147.191.85:28443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC%E4%B8%9C%E4%BA%AC-4044-141.147.191.85
    trojan://750a29bf-0a40-437f-b120-38de74ae7eaf@210.0.158.220:28443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-3808-210.0.158.220
    trojan://7a9a3bb7-43b4YWVzLTI1Ni1nY206eHBRd3lWNFc1RmRBNk5NQU5KSng3M1VT@2.58.242.43:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-3980-2.58.242.43
    trojan://7b06d22a8a7c764f@211.72.35.156:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-180-211.72.35.156
    trojan://7b06d22a8a7c764f@60.249.3.229:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-684-60.249.3.229
    trojan://7b06d22a8a7c764f@60.249.3.231:3389?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-682-60.249.3.231
    trojan://7x42LetRa0@106.180.225.69:1443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-158-106.180.225.69
    trojan://9010950e-8e09-486a-bf96-3b0cf22097b4@sg1.sanfen001.pics:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-674-sg1.sanfen001.pics
    trojan://94a08db5-db61-487a-b208-c66445f32737@1024sg99.tfzhc.top:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-3360-1024sg99.tfzhc.top
    trojan://9c48615a-d5e7-366c-907f-19a105b17451@211.72.174.126:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-076-211.72.174.126
    trojan://9c822f05-cfdc-479a-9534-60f3d4127435@jgwcc2.gaox.ml:443?allowInsecure=0#%F0%9F%87%B0%F0%9F%87%B7%20%5B11-02%5D-%F0%9F%87%B0%F0%9F%87%B7-%E9%9F%A9%E5%9B%BD%E6%98%A5%E5%B7%9D-3798-jgwcc2.gaox.ml
    trojan://A5gRXcqzaSY2lN87FaDxx34Ka33ROYj9eSZFIDCueEyl8ySBn0TpwC3OCApDZ6@121.78.213.3:443?allowInsecure=0#%F0%9F%87%B0%F0%9F%87%B7%20%5B11-02%5D-%F0%9F%87%B0%F0%9F%87%B7-%E9%9F%A9%E5%9B%BD-570-121.78.213.3
    trojan://ED177480-E516-11EA-8B44-BBC4E882BA0B@tw01.balala2016.xyz:20261?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE%E6%96%B0%E7%AB%B9%E5%B8%82-3984-tw01.balala2016.xyz
    trojan://H5sVBuzPFUgVTdY8Ry@pro-tw1-4.nigirocloud.com:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-02%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-700-pro-tw1-4.nigirocloud.com
    trojan://ZDAAFTxBNu5j9pl3Re834a3xSXwOZYeIlE30Dp86qc7yYgKaDCaROCSSnz2FCy@47.52.101.237:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-524-47.52.101.237
    trojan://ZlYZ0KxC8uxngp736aR34y3TaFwFOC95DO2XR8yeeAD3cESNDSCBqAYIjpaSlz@219.76.13.175:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-02%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-538-219.76.13.175
    trojan://affae2e0-e84b-11ec-b09f-1239d0255272@trojan1.udpgw.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-220-jgwhdlb2.gaox.ml
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjOWRhYTYxNi0zZDY3LTQwNzgtOWZhNS0yOWVmYTRiMzE4ZTI@jjs.paolujichang.com:81#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3096-jjs.paolujichang.com
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@134.195.196.19:443#%F0%9F%87%A8%F0%9F%87%A6%20%5B11-02%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7%E8%92%99%E7%89%B9%E5%88%A9%E5%B0%94-148-134.195.196.19
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.91.106.51:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3094-38.91.106.51
    ss://YWVzLTI1Ni1nY206ZTRGQ1dyZ3BramkzUVk@169.197.141.39:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%A6%F0%9F%87%B6-%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA-140-169.197.141.39
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.33.88.190:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.33.88.190
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.79.79.37:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.79.79.37
    ssr://Z3p5ZC0wMS5jY3RlbGVzY29wZS54eXo6NDE5OTk6YXV0aF9hZXMxMjhfbWQ1OmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDphRWRyVVRZNU1UVjBSQS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9OEotSHV2Q2ZoN2dnTGVlLWp1V2J2UzFuZW5sa0xUQXhMbU5qZEdWc1pYTmpiM0JsTG5oNWVnJm9iZnNwYXJhbT1ZV3BoZUM1dGFXTnliM052Wm5RdVkyOXQmcHJvdG9wYXJhbT1NVEkwT1RFMU9rbFVlVEpEYkhoUlJGWQ
    trojan://%21str111111@www.cjf0423.cf:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-182-www.cjf0423.cf
    trojan://0f253dfd-ab4c-414e-84c0-cb0c5a279899@jp01.awcloud.top:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-040-jp01.awcloud.top
    trojan://0f76f49a-f531-4707-8622-2f8e88c38624@us02.henet.top:30000?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3366-us02.henet.top
    trojan://176196e4-7cf7-4561-87a9-21a1b4e344be@ap.liangyuandian.top:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-4046-ap.liangyuandian.top
    trojan://26e219f2-5c2a-356c-9767-9fd681cc0134@165.154.235.186:24567?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20%5B11-02%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-312-165.154.235.186
    trojan://28bccca2-43d2-47f8-bd63-b1361ce7d362@de.iamnotagoodman.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3382-de.iamnotagoodman.com
    trojan://2f95d996-e911-4b1b-82b1-1d86bf2c517d@dl-hk2.efpan.one:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-4034-dl-hk2.efpan.one
    trojan://38239dd0-902b-11eb-afc1-1239d0255272@us-trojan.bonds.id:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD%E5%BC%97%E5%90%89%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%96%87%E7%89%B9%E5%B1%B1%E5%86%9C%E5%9C%BA-3270-us-trojan.bonds.id
    trojan://3d6e81e4-c6df-32ad-a808-e83d4fd1ca1a@azhj001.xibai6.top:20716?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-562-azhj001.xibai6.top
    trojan://4V4kxVXmcg5Yn2DqF2@ty1-1.nigirocloud.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-680-ty1-1.nigirocloud.com
    trojan://4f8c0e41-dbdb-40f1-99cb-2c2a0b909b52@jp.iamnotagoodman.com:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3782-jp.iamnotagoodman.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpzejdqMQ@sg4-ss.sshstores.net:8388#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3132-sg4-ss.sshstores.net
    trojan://54f4dd9a-6a6c-4c84-b328-4a51da70793e@625us.ok365.cyou:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20%5B11-02%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-604-625us.ok365.cyou
    trojan://640e3ef0-9c44-49a8-98f6-0895b11eecd6@t03.ssrsub.com.xyz:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-360-t03.ssrsub.com.xyz
    trojan://67960bfb-00de-4a6b-9a7a-e74fc9e8b158@149.56.141.11:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20%5B11-02%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-4016-149.56.141.11
    trojan://6A30qqSh8W@45.136.14.70:15410?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-02%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-592-45.136.14.70
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9XzExMDIwNjUiLCJhZGQiOiI4LjIwOS43Mi45IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MTY0NmY5YS1iNGU5LTRhY2EtYmZlMy04ODkyYjNlNThmZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzMwLmNmY2RuMy54eXoiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9XzExMDIwNzAiLCJhZGQiOiI4LjIwOS4xMDQuMjMwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MTY0NmY5YS1iNGU5LTRhY2EtYmZlMy04ODkyYjNlNThmZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzMwLmNmY2RuMy54eXoiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@167.88.63.59:443#%F0%9F%87%B8%F0%9F%87%AA%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-260-167.88.63.59
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9XzExMDIwNjYiLCJhZGQiOiI4LjIwOS4xMTguNDYiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkxNjQ2ZjlhLWI0ZTktNGFjYS1iZmUzLTg4OTJiM2U1OGZlNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcmF5IiwiaG9zdCI6ImxnMzAuY2ZjZG4zLnh5eiIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@37.120.147.230:443#%F0%9F%87%B7%F0%9F%87%B4%20%5B11-02%5D-%F0%9F%87%B7%F0%9F%87%B4-%E7%BD%97%E9%A9%AC%E5%B0%BC%E4%BA%9A-3092-37.120.147.230
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@167.88.61.119:443#%F0%9F%87%B8%F0%9F%87%AA%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-3040-167.88.61.119
    ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@85.208.108.62:443#%F0%9F%87%B8%F0%9F%87%A6%20%5B11-02%5D-%F0%9F%87%A6%F0%9F%87%B6-%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AF-3126-85.208.108.62
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA2NSIsImFkZCI6IjE5OC4yNDQuMTQ4LjIxNCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTE2NDZmOWEtYjRlOS00YWNhLWJmZTMtODg5MmIzZTU4ZmU3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9yYXkiLCJob3N0IjoiMTk4LjI0NC4xNDguMjE0IiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206YjFkYzM0NGZkM2Mz@193.107.23.250:443#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-02%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-3016-193.107.23.250
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA2NCIsImFkZCI6IjE3Mi42Ny4xOTYuMCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGRiOTllOTYtM2VlMy00MTljLWIxZmItODU2OTc1ODAxMzgwIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcmF5IiwiaG9zdCI6IjE3Mi42Ny4xOTYuMCIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@167.88.63.44:443#%F0%9F%87%B8%F0%9F%87%AA%20%5B11-02%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-3038-167.88.63.44
    ss://YWVzLTI1Ni1nY206OG42cHdBY3JydjJwajZ0RlkycDNUYlE2@82.102.26.117:33992#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2063
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@62.210.222.195:443#%F0%9F%87%AB%F0%9F%87%B7%20%5B11-02%5D-%F0%9F%87%AB%F0%9F%87%B7-%E6%B3%95%E5%9B%BD-015-62.210.222.195
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA2MiIsImFkZCI6IjEwNC4xOS43Ljg0IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0Y2RiMDE2Zi1mMTRlLTMwYjMtOTdkNi00NTNjNzQxYTVjODAiLCJhaWQiOiIxIiwibmV0Ijoid3MiLCJwYXRoIjoiL3k0NzUiLCJob3N0IjoiMTA0LjE5LjcuODQiLCJ0bHMiOiJ0bHMifQ==
    ssr://MTQ2LjE5LjE5Ni4xNDY6NDEwMDU6YXV0aF9hZXMxMjhfc2hhMTpjaGFjaGEyMC1pZXRmOnRsczEuMl90aWNrZXRfYXV0aDplVkJMY21WNFdHRldUVUZZUm1abGVnLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcV9DZmg3Y2dMZWF6bGVXYnZTMHhORFl1TVRrdU1UazJMakUwTmcmb2Jmc3BhcmFtPU1HVmpOVFF5T0RBNE5DNWtiM2R1Ykc5aFpDNTNhVzVrYjNkemRYQmtZWFJsTG1OdmJRJnByb3RvcGFyYW09TWpnd09EUTZhMlkwTjFobQ
    ssr://MTQuMTUyLjkyLjc3OjEyMTI3OmF1dGhfYWVzMTI4X3NoYTE6YWVzLTI1Ni1jZmI6aHR0cF9zaW1wbGU6TmpoNFpHZDFPV1Y1YVdZLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz01Ym1fNUxpYzU1eUI1TGljNkk2ZTViaUNMVEUwTGpFMU1pNDVNaTQzTncmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPU5qQXdOemMzT2pFMU5GUTRZZw
    ssr://MTQuMTUyLjkyLjcyOjEyMTI3OmF1dGhfYWVzMTI4X3NoYTE6YWVzLTI1Ni1jZmI6aHR0cF9zaW1wbGU6TmpoNFpHZDFPV1Y1YVdZLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz01Ym1fNUxpYzU1eUI1TGljNkk2ZTViaUNMVEUwTGpFMU1pNDVNaTQzTWcmb2Jmc3BhcmFtPVRVZFpkMDlVYXpKTlJFRXpUbnBqZFdScVNYcGFhbVIxVkZSQiZwcm90b3BhcmFtPU5qQXdOemMzT2pFMU5GUTRZZw
    ssr://MTQuMTUyLjkyLjgxOjEyMTI3OmF1dGhfYWVzMTI4X3NoYTE6YWVzLTI1Ni1jZmI6aHR0cF9zaW1wbGU6TmpoNFpHZDFPV1Y1YVdZLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz01Ym1fNUxpYzU1eUI1TGljNkk2ZTViaUNMVEUwTGpFMU1pNDVNaTQ0TVEmb2Jmc3BhcmFtPU1HWXdPVGsyTURBM056Y3Vkakl6WmpkdUpRJnByb3RvcGFyYW09TmpBd056YzNPakUxTkZRNEpTVQ
    ssr://ZGctaGstbm9kZTAyLmxpbmt0aGluay5hcHA6MTIwMjU6b3JpZ2luOm5vbmU6aHR0cF9wb3N0OlpUVnZjR3AxVEVSRlVRLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcmZDZmg3QWdZV1JwZkRBM01ETjJJQzBnWkdjdGFHc3RibTlrWlRBeSZvYmZzcGFyYW09WVdwaGVDNXRhV055YjNOdlpuUXVZMjl0JnByb3RvcGFyYW09
    ssr://MjIzLjE2Ny4xNTkuMzQ6NTYxOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9OEotSHFQQ2ZoN01nTGVTNGl1YTF0LVc0Z2kweU1qTXVNVFkzTGpFMU9TNHpOQSZvYmZzcGFyYW09JnByb3RvcGFyYW09TlRNNU1qUTZhR3BuYW5WNU5uUTJOVFZxYW1j
    ssr://NDIuMTU3LjE5NS4yNDE6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNalF4Jm9iZnNwYXJhbT1UVWRaZDA5VWF6Sk5SRUV6VG5wamRXUnFTWHBhYW1SMVZGUkImcHJvdG9wYXJhbT1OakF3TnpjM09qRTFORlE0WWc
    ssr://NDIuMTU3LjE5NS4yNDQ6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNalEwJm9iZnNwYXJhbT1UVWRaZDA5VWF6Sk5SRUV6VG5wamRXUnFTWHBhYW1SMVZGUkJQUSZwcm90b3BhcmFtPU5qQXdOemMzT2pFMU5GUTRZZw
    ssr://NDIuMTU3LjE5NS4yNDU6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNalExJm9iZnNwYXJhbT1NR1l3T1RrMk1EQTNOemN1ZGpJelpqZHVUVEEmcHJvdG9wYXJhbT1OakF3TnpjM09qRTFORlE0WWc
    ss://YWVzLTI1Ni1jZmI6Y2Ruc3NyLnNzcnN1Yi5jb20@cdnssr.ssrsub.com:443#%F0%9F%87%BF%F0%9F%87%A6%20-%E5%8D%97%E9%9D%9E%E8%B1%AA%E7%99%BB%E7%9C%81%E7%BA%A6%E7%BF%B0%E5%86%85%E6%96%AF%E5%A0%A1-cdnssr.ssrsub.com
    

</details>

### 所有节点
合并节点总数: `2335`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `83`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `138`
- [freefq/free](https://github.com/freefq/free), 节点数量: `27`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `527`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3206`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `18`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `56`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `17`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `44`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `237`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `18`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `26`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `28`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `16`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `312`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `191`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `266`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `21`

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
- [阿伟云](https://awcloud.cc/#/register?code=8C18uZwl)
  - 最低月付 1¥ 起, 9.99¥100G
  - 无带宽速率限制，有流媒体解锁，香港 BGP 中继线路

## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

## 星标统计
[![Star History Chart](https://api.star-history.com/svg?repos=alanbobs999/TopFreeProxies&type=Date)](https://star-history.com/#alanbobs999/TopFreeProxies&Date)
