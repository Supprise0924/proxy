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
高速节点数量: `100`
<details>
  <summary>展开复制节点</summary>

    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwMDciLAogICJhZGQiOiAiMTQxLjEwMS4xMTQuMTUwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxMzgiLAogICJhZGQiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwb3J0IjogNTU1NTUsCiAgImlkIjogImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4xOTUuMTcxIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIxMDIiLAogICJhZGQiOiAic2hvcGlmeS5jb20iLAogICJwb3J0IjogMjA4NiwKICAiaWQiOiAiZGM4YjY0ZGItZWI2ZC00YmRmLTk4YjItMzE2MTUzMTliZWE4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2bi5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicGF0aCI6ICIvYXJpZXMiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAwNSIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwMjUiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNjEiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=golang.protocolbuffer.com#%E7%BE%8E%E5%9B%BD%20019
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=jd101.8faka.tk#mianfeifq%2B215
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=n2.gladns.com#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20037
    trojan://1bacde9b-3a1a-43eb-b091-287824dc91d3@kr1.api-aws.com:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%E6%97%A5%E6%9C%AC%20006
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C340.96Mb
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@168.138.43.89:443?allowInsecure=1&sni=sni=huayun.xyz#%F0%9F%87%AF%F0%9F%87%B5_JP_%E6%97%A5%E6%9C%AC_2
    trojan://2fecc75c-3acc-3bb8-b30e-cd1159b4ed15@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=gbo02.vsvideo.shop#%E6%96%B0%E5%8A%A0%E5%9D%A1%20003
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@168.138.43.89:443?allowInsecure=1&sni=golang.protocolbuffer.com#JP%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjQ0IiwKICAiYWRkIjogIlBMLm5leGl0YWxseS54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI1NGM2YzgyMy00OTU3LTRjNmMtYjEwYy0zNTliYzUxZjdjYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIlBMLm5leGl0YWxseS54eXoiLAogICJwYXRoIjogIi9hNTRlMjg0Y2I2LyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=1009jp.tfzhc.top#v2rayfree.eu.org%20-%20%E6%96%B0%E5%8A%A0%E5%9D%A1DigitalOcean%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2019
    trojan://2fecc75c-3acc-3bb8-b30e-cd1159b4ed15@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=ip153740813.mobgslb.tbcache.com#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://2fecc75c-3acc-3bb8-b30e-cd1159b4ed15@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=jd2.8faka.tk#%F0%9F%87%B8%F0%9F%87%AC%2BSG%2B9%2BTG%3A%40nodpai
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=jgwdj3.gaox.ml#%E6%96%B0%E5%8A%A0%E5%9D%A1%20003
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=n2.gladns.com#github.com/freefq%20-%20%E6%96%B0%E5%8A%A0%E5%9D%A1DigitalOcean%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2023
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMzA2IiwKICAiYWRkIjogIlBMLm5leGl0YWxseS54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI1NGM2YzgyMy00OTU3LTRjNmMtYjEwYy0zNTliYzUxZjdjYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIlBMLm5leGl0YWxseS54eXoiLAogICJwYXRoIjogIi9hNTRlMjg0Y2I2LyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://2fecc75c-3acc-3bb8-b30e-cd1159b4ed15@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=n2.gladns.com#%F0%9F%87%B8%F0%9F%87%AC%E7%99%BD%E5%AB%96-0034
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US%20%7C340.96Mb
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=1009jp.tfzhc.top#v2rayfree.eu.org%20-%20%E6%96%B0%E5%8A%A0%E5%9D%A1DigitalOcean%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2019
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDI1OSIsCiAgImFkZCI6ICIxMzkuOTkuOTAuMTIyIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MC4xMjIiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://ZFYOpKqD8uEClpZ2ya83cyCDalwSOYz3F3eCxnBD4eSXNSR5R0aAATj7I3x69g@18.163.249.175:443?allowInsecure=1&sni=golang.protocolbuffer.com#%E7%BE%8E%E5%9B%BD%20017
    trojan://469eb2d7-c86c-3484-ba85-4f26f0645b9b@do-sg-01.vvsoga.net:1234?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%F0%9F%87%B8%F0%9F%87%AC%20Relay_%F0%9F%87%B8%F0%9F%87%ACSG%20%7C521.88Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI0NjMiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIa0AxODUuMTI2LjExNi4xMjU6OTA5OA==#%F0%9F%87%B7%F0%9F%87%B4RO_08
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAidjJyYXlmcmVlLmV1Lm9yZyAtIOaWsOWKoOWdoU9WSCAyMCIsCiAgImFkZCI6ICJzZy1vdmgxLnYyLXJheS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImE5NDgxNjAwLWVmMzYtNDAyYS1hMGU1LTU1NDdiZmQ3Yjg3YyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicGF0aCI6ICIvZmFzdHNzaC9mZ2hoaC82MzQxOTdjNGNkZjgxLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDI1OSIsCiAgImFkZCI6ICIxMzkuOTkuOTAuMTIyIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MC4xMjIiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDIxMiIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjQ0IiwKICAiYWRkIjogIlBMLm5leGl0YWxseS54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI1NGM2YzgyMy00OTU3LTRjNmMtYjEwYy0zNTliYzUxZjdjYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIlBMLm5leGl0YWxseS54eXoiLAogICJwYXRoIjogIi9hNTRlMjg0Y2I2LyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAwNSIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggMTAiLAogICJhZGQiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1&sni=ip153740813.mobgslb.tbcache.com#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@129.146.190.42:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD_8
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDI5MSIsCiAgImFkZCI6ICIxMzguMi44LjIyNyIsCiAgInBvcnQiOiA1OTQ0MiwKICAiaWQiOiAiNmZkMDQyZmEtZTg2NC00YTk1LTg1YmMtNmY1OTBhMDNkMzRhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuOC4yMjciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDIxMiIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwMjUiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNzYiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMua2Fwb2suYnV6eiIsCiAgInBhdGgiOiAiL1NDUC05MTQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7At6aaZ5rivLWZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAiYWRkIjogImZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjc0ZjExYzYtZjY5Yi00MGI5LTg5NjYtZjM5ZTA2ZTk3YmU3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJmdWxsYWNjZXNzdG9ob25na29uZ25ldC5henVyZXdlYnNpdGVzLm5ldCIsCiAgInBhdGgiOiAiL3dzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0fjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiYTk0ODE2MDAtZWYzNi00MDJhLWEwZTUtNTU0N2JmZDdiODdjIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy1vdmgxLnYyLXJheS5jb20iLAogICJwYXRoIjogIi9mYXN0c3NoL2ZnaGhoLzYzNDE5N2M0Y2RmODEvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNDUiLAogICJhZGQiOiAiOC4yMDkuMjIwLjM0IiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI3NDc1OGYwNi1mNGI5LTRlZjEtYTg2Yy1mMGEwY2M4MjEwOWYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImx1eC5qdXN0dS5tbCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNDUiLAogICJhZGQiOiAiOC4yMDkuMjIwLjM0IiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI3NDc1OGYwNi1mNGI5LTRlZjEtYTg2Yy1mMGEwY2M4MjEwOWYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImx1eC5qdXN0dS5tbCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=jd101.8faka.tk#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20038
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIwNDEiLAogICJhZGQiOiAiZnVsbGFjY2Vzc3RvaG9uZ2tvbmduZXQuYXp1cmV3ZWJzaXRlcy5uZXQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyNzRmMTFjNi1mNjliLTQwYjktODk2Ni1mMzllMDZlOTdiZTciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAicGF0aCI6ICIvd3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1LjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogImZ1bGxhY2Nlc3N0b2tvcmVhbm5ldHN1Ym5vZGUxLmF6dXJld2Vic2l0ZXMubmV0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjc0ZjExYzYtZjY5Yi00MGI5LTg5NjYtZjM5ZTA2ZTk3YmU3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJmdWxsYWNjZXNzdG9rb3JlYW5uZXRzdWJub2RlMS5henVyZXdlYnNpdGVzLm5ldCIsCiAgInBhdGgiOiAiL3dzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://54080134-2cba-4535-8599-95650bd9aa54@jgwhdlb2.gaox.ml:443?allowInsecure=1&sni=924hk02.tfzhc.top#%F0%9F%87%AE%F0%9F%87%B3%20_IN_%E5%8D%B0%E5%BA%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDMiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5rC45LmF5YWN6LS55pu05pawIiwKICAiYWRkIjogIjM4LjU0LjMzLjc3IiwKICAicG9ydCI6IDUzMjU3LAogICJpZCI6ICI4MDg3OTNmYS0wOWUxLTQzMTgtYjBmNi02MzFlNDFmMmRlNDgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjM4LjU0LjMzLjc3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://54080134-2cba-4535-8599-95650bd9aa54@jgwhdlb2.gaox.ml:443?allowInsecure=1&sni=924hk02.tfzhc.top#%F0%9F%87%AE%F0%9F%87%B3%20_IN_%E5%8D%B0%E5%BA%A6
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India/Hyderabad_26
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwMTQiLAogICJhZGQiOiAiMTcyLjY0LjE1NC4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://123456@trojan-ctb-sg01.globalssh.xyz:443?allowInsecure=1&sni=jd2.8faka.tk#%F0%9F%87%A9%F0%9F%87%AA%2BDE%2B22
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNzUiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMua2Fwb2suYnV6eiIsCiAgInBhdGgiOiAiL1NDUC05MTQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD_9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hIDAwMSIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTI3LjAuMC4xIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODEy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A812-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI2OTciLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1LjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogImZ1bGxhY2Nlc3N0b2tvcmVhbm5ldHN1Ym5vZGUxLmF6dXJld2Vic2l0ZXMubmV0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjc0ZjExYzYtZjY5Yi00MGI5LTg5NjYtZjM5ZTA2ZTk3YmU3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJmdWxsYWNjZXNzdG9rb3JlYW5uZXRzdWJub2RlMS5henVyZXdlYnNpdGVzLm5ldCIsCiAgInBhdGgiOiAiL3dzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://xxoo@194.156.99.39:443?allowInsecure=1&sni=ip153740813.mobgslb.tbcache.com#%F0%9F%87%B7%F0%9F%87%BA%20RU%201%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDMzIiwKICAiYWRkIjogIjE3Mi42NC4xNTUuMjAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTgwMzBhZmQtODEyYS00YWZlLWE3NjYtOWM3NmZmM2VkZGQ0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzQuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73ljY7nm5vpob9Db2dlbnTpgJrkv6Hlhazlj7ggMjAiLAogICJhZGQiOiAiMzguNTQuMzMuNzciLAogICJwb3J0IjogNTMyNTcsCiAgImlkIjogIjgwODc5M2ZhLTA5ZTEtNDMxOC1iMGY2LTYzMWU0MWYyZGU0OCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMzguNTQuMzMuNzciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%AF%F0%9F%87%B5_JP_%E6%97%A5%E6%9C%AC_4
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=924hk02.tfzhc.top#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%F0%9F%87%AF%F0%9F%87%B5%20Relay_%F0%9F%87%AF%F0%9F%87%B5JP%20%7C11.90Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDI0IiwKICAiYWRkIjogImVlLm9wcG8ucXVlc3QiLAogICJwb3J0IjogODAsCiAgImlkIjogImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZWUub3Bwby5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI2OTYiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy5wcnByLmxpbmsiLAogICJwYXRoIjogIi9UZWxlZ3JhbS9TaGFyZUNlbnRyZVByby9ta25uaXgiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlDjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogIjguMjA5LjIyMC4zNCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiNzQ3NThmMDYtZjRiOS00ZWYxLWE4NmMtZjBhMGNjODIxMDlmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsdXguanVzdHUubWwiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIa0AxODUuMTI2LjExNi4xMjU6OTA5OA==#%F0%9F%87%B7%F0%9F%87%B4RO_08
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=sni=huayun.xyz#%F0%9F%87%AF%F0%9F%87%B5_JP_%E6%97%A5%E6%9C%AC_3
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%E6%97%A5%E6%9C%AC%20005
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwMTciLAogICJhZGQiOiAiMTk4LjQxLjIxMi4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=ukt1.sshocean.net#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%AF%F0%9F%87%B5_JP_%E6%97%A5%E6%9C%AC_3
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=ip153740813.mobgslb.tbcache.com#%F0%9F%87%AF%F0%9F%87%B5%20JP%206%20%E2%86%92%20openitsub.com

</details>

### 所有节点
合并节点总数: `5384`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `195`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `136`
- [freefq/free](https://github.com/freefq/free), 节点数量: `32`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3166`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `115`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `4`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `27`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `3`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `128`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `125`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `29`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `29`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `200`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `30`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `193`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `166`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `270`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `14`

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
