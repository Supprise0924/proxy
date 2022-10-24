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
高速节点数量: `94`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIwMDUiLCJhZGQiOiJzZzE1My5oa2FhMC50ayIsInBvcnQiOiIxNDM1OCIsInR5cGUiOiJub25lIiwiaWQiOiJiYmY0MjNkOC02Yjc4LTQxNmEtOGYxMi0yNTQ2ZTFhZjg3ZWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2hrYWEwIiwiaG9zdCI6InNnMTUzLmhrYWEwLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiS1JfMTUyLjcwLjIzNS4yMDdfMTAyMWE2NzctOTgiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9oa2FhMCIsImhvc3QiOiJzZzE1My5oa2FhMC50ayIsInRscyI6IiJ9
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan%2FOsaka_9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag5Lit6L2sIPCfh63wn4ewIEhLIDE1IFRHQG5vZHBhaSIsImFkZCI6ImhrMDEueG5pdW5pdTg4OC54eXoiLCJwb3J0IjoiMzAxMDQiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmEzYjQ4MzMtYmUyZS0zYmMyLTljYWEtYzM1YWYxNDlkZTZkIiwiYWlkIjoiMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImhrMDEueG5pdW5pdTg4OC54eXoiLCJ0bHMiOiIifQ==
    trojan://ZFYOpKqD8uEClpZ2ya83cyCDalwSOYz3F3eCxnBD4eSXNSR5R0aAATj7I3x69g@219.76.13.180:443?allowInsecure=1&sni=golang.protocolbuffer.com#%F0%9F%87%AD%F0%9F%87%B0%20HK%201%20%E2%86%92%20openitsub.com
    trojan://ZlYZ0KxC8uxngp736aR34y3TaFwFOC95DO2XR8yeeAD3cESNDSCBqAYIjpaSlz@219.76.13.175:443?allowInsecure=1&sni=python.protocolbuffer.com#%F0%9F%87%AD%F0%9F%87%B0%20HK%202%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoiU0dfMTM5Ljk5LjkwLjEyMl8xMDIwY2JkNi0xNiIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoicHl0aG9uLnByb3RvY29sYnVmZmVyLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5Lit5Zu9LXZtZXNzLTguMjE0LjMzLjE1ODgwLeiiq+WimS3nm7Tov54t6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMiIsImFkZCI6IjguMjE0LjMzLjE1OCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjYjgxZTZhYi0xZDgzLTRhYzEtZjBhZC1hZTVjMmE3YzI5ZWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5Lit5Zu9LXZtZXNzLTguMjE0LjMzLjE1ODgwLeiiq+WimS3nm7Tov54t6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliaciLCJhZGQiOiI4LjIxNC4zMy4xNTgiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2I4MWU2YWItMWQ4My00YWMxLWYwYWQtYWU1YzJhN2MyOWVmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://ZFYOpKqD8uEClpZ2ya83cyCDalwSOYz3F3eCxnBD4eSXNSR5R0aAATj7I3x69g@219.76.13.180:443?allowInsecure=1&sni=golang.protocolbuffer.com#%F0%9F%87%B8%F0%9F%87%AC%20SG%2028%20TG%40airproxies
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5Lit5Zu9LXZtZXNzLTguMjE0LjMzLjE1ODgwLeiiq+WimS3nm7Tov54t6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMyIsImFkZCI6IjguMjE0LjMzLjE1OCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjYjgxZTZhYi0xZDgzLTRhYzEtZjBhZC1hZTVjMmE3YzI5ZWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://41b87c2c-7dce-3a3d-85e7-9c00b5bea867@azhj001.xibai6.top:20770?allowInsecure=1&sni=ssl.ssl12.xyz#%F0%9F%87%A8%F0%9F%87%B3%20TW%2010%20TG%40airproxies
    trojan://d45e6245-926b-4283-8c72-91e229d6c5f5@kr1.sanfen001.pics:443?allowInsecure=1&sni=kr1.sanfen001.pics#%F0%9F%87%B0%F0%9F%87%B7%20KR%201%20TG%40airproxies
    trojan://d45e6245-926b-4283-8c72-91e229d6c5f5@kr2.sanfen001.pics:443?allowInsecure=1&sni=kr1.sanfen001.pics#%F0%9F%87%B0%F0%9F%87%B7%20KR%204%20TG%40airproxies
    trojan://d45e6245-926b-4283-8c72-91e229d6c5f5@kr1.sanfen001.pics:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%203%20%E2%86%92%20openitsub.com%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIzMTYiLCJhZGQiOiI1MS43OS4xNTYuMjIzIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMxZDAxMjI1LTJlNmYtNDlmYS04MzNlLWVkZjdjYjFmODAzMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvSkFHT0FOU1NILyIsImhvc3QiOiJuYW1hdmEuaXIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIzMTIiLCJhZGQiOiJzZzgudm1lcy54eXoiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzFkMDEyMjUtMmU2Zi00OWZhLTgzM2UtZWRmN2NiMWY4MDMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9KQUdPQU5TU0gvIiwiaG9zdCI6Im5hbWF2YS5pciIsInRscyI6IiJ9
    trojan://84773125-8f79-481c-a80b-e1f4aad86850@kr1.api-aws.com:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%204%20%E2%86%92%20openitsub.com
    trojan://d45e6245-926b-4283-8c72-91e229d6c5f5@hk1.sanfen001.pics:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%201%20%E2%86%92%20openitsub.com
    trojan://d45e6245-926b-4283-8c72-91e229d6c5f5@hk1.sanfen001.pics:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20github.com%2Ffreefq%20-%20%E6%97%A5%E6%9C%AC%20%2011
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIwMjQiLCJhZGQiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6InNob3Vlci5henpodWFuZ2FwaW5nLnR3IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjI0IiwiYWRkIjoiMTI4LjEuMTM0LjEyNiIsInBvcnQiOiI2NjY2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdmYjNiNTcxLWNkYTgtNDBmNi1jOWU2LWRiOTc2NWVhOGZhYSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6InNob3Vlci5henpodWFuZ2FwaW5nLnR3IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMTI4LjEuMTM0LjEyNl8xMDIwY2JkNi01MyIsImFkZCI6IjEyOC4xLjEzNC4xMjYiLCJwb3J0IjoiNjY2NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmIzYjU3MS1jZGE4LTQwZjYtYzllNi1kYjk3NjVlYThmYWEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysIDAwNCIsImFkZCI6IjE3Mi4xMDUuMjM1LjE2MyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKzkuJzkuqxMaW5vZGXmlbDmja7kuK3lv4MgMTUiLCJhZGQiOiJhZWFkanBhZXMwMS54bi0tejRxNDhsY3ZwLmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI5NDY3M2UxOS0xMWZhLTQzNzAtODU4My05ODllOWViMWE3MTAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJzaG91dGluZ3RvdXRpYW8zLjEwMDEwLmNvbSIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:809#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203809-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:803#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203803-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:809#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204809-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjIwMDMiLCJhZGQiOiIxNjUuMTU0LjI0My4xNjEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImUxM2E5YzQyLTU0ZDYtNGZlMS05NTc4LTBjYTNiZmMxNzEyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJzaG91dGluZ3RvdXRpYW8zLjEwMDEwLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjIwMDEiLCJhZGQiOiIxNjUuMTU0LjI0My4xNjEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImYzMzhhNTlkLTljNWMtNGU4My1hMmQwLTdhMzc4ODg0Yzk2OSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJzaG91dGluZ3RvdXRpYW8zLjEwMDEwLmNvbSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@52.197.66.243:443#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-52.197.66.243443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@52.197.66.243:443#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-52.197.66.243443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@52.197.66.243:443#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-52.197.66.243443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLXZtZXNzLTE0Ni41Ni40MC4xMTcyNzY3NS3ooqvlopkt55u06L+eLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoiMTQ2LjU2LjQwLjExNyIsInBvcnQiOiIyNzY3NSIsInR5cGUiOiJub25lIiwiaWQiOiIwNTNjYTBmNC0wNTdlLTQ5M2QtYWQzMC01YmE1MWYwMGY1OWMiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLXZtZXNzLTE0Ni41Ni40MC4xMTcyNzY3NS3ooqvlopkt55u06L+eLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDIiLCJhZGQiOiIxNDYuNTYuNDAuMTE3IiwicG9ydCI6IjI3Njc1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA1M2NhMGY0LTA1N2UtNDkzZC1hZDMwLTViYTUxZjAwZjU5YyIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLXZtZXNzLTE0Ni41Ni40MC4xMTcyNzY3NS3ooqvlopkt55u06L+eLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDMiLCJhZGQiOiIxNDYuNTYuNDAuMTE3IiwicG9ydCI6IjI3Njc1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA1M2NhMGY0LTA1N2UtNDkzZC1hZDMwLTViYTUxZjAwZjU5YyIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg576O5Zu9LXZtZXNzLWNhLjAxMTIyMzMueHl6ODQ0My3ooqvlopkt5Lit6L2sMTk5Ljg3LjIxMC4xODYt6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliaciLCJhZGQiOiJjYS4wMTEyMjMzLnh5eiIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMzMDAwZTlkLWJlZTctNGZkYi1iMzEyLWRkMDcwMzBmMzI1ZCIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaG9tZSIsImhvc3QiOiJjYS4wMTEyMjMzLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg576O5Zu9LXZtZXNzLWNhLjAxMTIyMzMueHl6ODQ0My3ooqvlopkt5Lit6L2sMTk5Ljg3LjIxMC4xODYt6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMiIsImFkZCI6ImNhLjAxMTIyMzMueHl6IiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzMwMDBlOWQtYmVlNy00ZmRiLWIzMTItZGQwNzAzMGYzMjVkIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ob21lIiwiaG9zdCI6ImNhLjAxMTIyMzMueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg576O5Zu9LXZtZXNzLWNhLjAxMTIyMzMueHl6ODQ0My3ooqvlopkt5Lit6L2sMTk5Ljg3LjIxMC4xODYt6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMyIsImFkZCI6ImNhLjAxMTIyMzMueHl6IiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzMwMDBlOWQtYmVlNy00ZmRiLWIzMTItZGQwNzAzMGYzMjVkIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ob21lIiwiaG9zdCI6ImNhLjAxMTIyMzMueHl6IiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-24%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3742-104.243.25.95
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=www.sxsy88.tk#%F0%9F%87%BA%F0%9F%87%B8%20US%20431
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=www.sxsy88.tk#%F0%9F%87%BA%F0%9F%87%B8%20US%20431%202
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.63.99:8090#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-167.88.63.998090-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://91a3db80-baf5-3f35-8c0e-b6483aefa1fd@us.dogintnode.com:443?allowInsecure=1&sni=us.dogintnode.com#%F0%9F%87%BA%F0%9F%87%B8%20US-208.115.243.55-017
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=0#US_107.181.161.163_102227c4-255
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://ZlYZ0KxC8uxngp736aR34y3TaFwFOC95DO2XR8yeeAD3cESNDSCBqAYIjpaSlz@219.76.13.175:443?allowInsecure=1&sni=python.protocolbuffer.com#US3
    trojan://ZFYOpKqD8uEClpZ2ya83cyCDalwSOYz3F3eCxnBD4eSXNSR5R0aAATj7I3x69g@219.76.13.175:443?allowInsecure=1&sni=golang.protocolbuffer.com#US5
    trojan://F3CSSRxD8uljgF73IAn34C3aE9wSqAzZDp5ZOCpxDBRacNYelOYayKTe826Xy0@219.76.13.180:443?allowInsecure=1&sni=stutter.freetrade.link#US6
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgZ2l0aHViLmNvbS9mcmVlZnEgLSDliqDmi7/lpKcgIDYiLCJhZGQiOiIxNjUuMTU0LjI0My4xNjEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcxMDhlNzk2LTU1ZGItNDBmOS1hZTAwLTAwMTUzYTQ1N2VhOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJzdHV0dGVyLmZyZWV0cmFkZS5saW5rIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIxMDczIiwiYWRkIjoiaGsxdmRmLW5vZGUuYWlxaWNoZTEyMy5jb20iLCJwb3J0IjoiODE4OSIsInR5cGUiOiJub25lIiwiaWQiOiJhOTA1OTdjMS1iYWIzLTQyMTctYWQ2Zi0wODM4Njc1Yzg2MzgiLCJhaWQiOiIxMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InN0dXR0ZXIuZnJlZXRyYWRlLmxpbmsiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNTQ0IiwiYWRkIjoiMTY4LjEzOC4yMDEuMjA4IiwicG9ydCI6IjEwMzI4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImJmODQ3YmY3LTBiYTUtNDg4NS1iZDJiLWRhNGQ3N2FmYmRhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJzdHV0dGVyLmZyZWV0cmFkZS5saW5rIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIxMDk2IiwiYWRkIjoiMTcyLjY3LjczLjIxMyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjcxZTM3ODQtZjE3MS00MDM1LTk4N2EtZGYwZmY0YjRjZDYxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jZWF0dndzIiwiaG9zdCI6IjEuNzMxODA4LnRrIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0OSIsImFkZCI6IjUuMzQuMTc4LjE1NyIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJjNmE0NDM5NC00ZjgzLTExZWQtYWY5Zi1iYjI2MWVlZGM3MDIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiI1LjM0LjE3OC4xNTciLCJ0bHMiOiIifQ==
    trojan://752a9404-c729-485e-8ea5-acb3f4fc8180@tr5.leifengkeji.live:4444?allowInsecure=1&sni=tr5.leifengkeji.live#%F0%9F%87%BA%F0%9F%87%B8%20US-69.165.74.232-153
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20openitsub.com%202
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@jgwcc3.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2018
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOayueeuoeegtOino+i1hOa6kOWQmzIuMCkgMzkiLCJhZGQiOiIxNzIuNjcuMTk2LjAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRkYjk5ZTk2LTNlZTMtNDE5Yy1iMWZiLTg1Njk3NTgwMTM4MCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcmF5IiwiaG9zdCI6ImxvY2FsaG9zdGVyLm1sIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDE3IiwiYWRkIjoibWluZzIua2l3aXJlaWNoLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMThlNWY0MGYtYmRhNi00YzE1LTkzMzQtZTg3Y2RhNjA0N2FmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoibWluZzIua2l3aXJlaWNoLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjE2LjI0LjU3LjI1M18xMDIzZDIzMy0yMDIiLCJhZGQiOiJ4eHJlbmRlcnh4Lm9ucmVuZGVyLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjBkOTVkNzktMDM1NS00NTkzLWE2NjktOTMzYzI5Y2Y5ZTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoieHhyZW5kZXJ4eC5vbnJlbmRlci5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDlt54gMTIiLCJhZGQiOiJ4eHJlbmRlcnh4Lm9ucmVuZGVyLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjBkOTVkNzktMDM1NS00NTkzLWE2NjktOTMzYzI5Y2Y5ZTY0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoieHhyZW5kZXJ4eC5vbnJlbmRlci5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh78g5o235YWLXzEwMjIwMDciLCJhZGQiOiJjejEudnBuamFudGl0LmNvbSIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJiM2E0MGI1ZS00ZjgyLTExZWQtOTE4ZC01MmNmMDBlNDYxYWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiJjejEudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDEwLjEwTWIiLCJhZGQiOiJubC52Mi1yYXkuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImJiOTdlZTBhLTZkNTctNDBjMC1hNDQ2LTQ1Yjc4YzMwMzYwMyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZmFzdHNzaC9oa2d6czAxLzYzMTVkNDA3NjU3ZjYvIiwiaG9zdCI6Im5sLnYyLXJheS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDE3LjM4TWIiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9mYXN0c3NoL2hrZ3pzMDEvNjMxNWQ0MDc2NTdmNi8iLCJob3N0IjoibmwudjItcmF5LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cg5be06KW/IDAwMyIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Zhc3Rzc2gvaGtnenMwMS82MzE1ZDQwNzY1N2Y2LyIsImhvc3QiOiJubC52Mi1yYXkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifDEwNS40Mk1iIiwiYWRkIjoiMTM5Ljk5LjkxLjk1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvZmFzdHNzaC9oa2d6czAxLzYzMTVkNDA3NjU3ZjYvIiwiaG9zdCI6Im5sLnYyLXJheS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDljJfkuqzluILlvq7ova8o5Lit5Zu9KeaciemZkOWFrOWPuCAzIDIiLCJhZGQiOiJoazAxLnhuaXVuaXU4ODgueHl6IiwicG9ydCI6IjMwMTA0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjJhM2I0ODMzLWJlMmUtM2JjMi05Y2FhLWMzNWFmMTQ5ZGU2ZCIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Zhc3Rzc2gvaGtnenMwMS82MzE1ZDQwNzY1N2Y2LyIsImhvc3QiOiJubC52Mi1yYXkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDljJfkuqzluILlvq7ova8o5Lit5Zu9KeaciemZkOWFrOWPuCAzIiwiYWRkIjoiaGswMS54bml1bml1ODg4Lnh5eiIsInBvcnQiOiIzMDEwNCIsInR5cGUiOiJub25lIiwiaWQiOiIyYTNiNDgzMy1iZTJlLTNiYzItOWNhYS1jMzVhZjE0OWRlNmQiLCJhaWQiOiIyIiwibmV0IjoidGNwIiwicGF0aCI6Ii9mYXN0c3NoL2hrZ3pzMDEvNjMxNWQ0MDc2NTdmNi8iLCJob3N0IjoibmwudjItcmF5LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Lit5Zu9XzEwMjI2MDMiLCJhZGQiOiJjZi43MzE4MDgudGsiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjgxOTRmNzI0LWQ2NDgtNGViOC05OGQyLTAwMTMxMzZlNzlmMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYnhmYnZ3cyIsImhvc3QiOiJoNTUyOC4xODA4LmNmIiwidGxzIjoidGxzIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#_%E6%B2%B9%E7%AE%A1%EF%BC%9A%E5%85%A8%E7%BD%91%E6%9C%80%E5%BC%BA%E7%99%BD%E5%AB%96%2034
    trojan://idc117okt@idc1.vpn-akcelluler.my.id:443?allowInsecure=1&sni=idc1.vpn-akcelluler.my.id#%E4%BA%9A%E5%A4%AA%E5%9C%B0%E5%8C%BA%20003
    vmess://eyJ2IjoiMiIsInBzIjoi5Lqa5rSyKOayueeuoeegtOino+i1hOa6kOWQmzIuMCkgOSIsImFkZCI6IjIxMS43Mi4zNS4xMTAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY2ZDdiMDcyLWRlMDAtNDVkYy05ZTI0LTQ5ZjhjZjQzNTMwZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbGlub2QiLCJob3N0IjoibGluZG8uY25hYmMuZXUub3JnIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.75.136.21:5001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2016
    ss://YWVzLTI1Ni1jZmI6cDl6NUJWQURIMllGczNNTg@213.183.59.218:9040#%F0%9F%87%B3%F0%9F%87%B1%20%5B10-24%5D-%F0%9F%87%B3%F0%9F%87%B1-%E8%8D%B7%E5%85%B0-1738-213.183.59.218
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMDciLCJhZGQiOiJpZC1sYi52aGF4Lm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9BcnNoYW04NTIzMS82MzQ3ZDA4MDIyYjkxLyIsImhvc3QiOiJ6b29tLnVzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifDQxLjA3TWIiLCJhZGQiOiIxMzkuOTkuOTAuMTIyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvc3Noa2l0L0Fyc2hhbTg1MjMxLzYzNDdkMDgwMjJiOTEvIiwiaG9zdCI6Inpvb20udXMiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMDEiLCJhZGQiOiJpZC1sYi52aGF4Lm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9BcnNoYW04NTIzMS82MzQ3ZDA4MDIyYjkxLyIsImhvc3QiOiJpZC1sYi52aGF4Lm5ldCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMDgiLCJhZGQiOiJpZC1sYi52aGF4Lm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9Ib3NlZWUxNy82MzQ3ZDczZjM3NzYyLyIsImhvc3QiOiJ6b29tLnVzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMTUiLCJhZGQiOiI0MS4yMTYuMTc3LjIzNCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9BcnNoYW04NTIzMS82MzQ3ZDA4MDIyYjkxLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://idc117okt@103.176.78.153:443?allowInsecure=1#%E4%BA%9A%E5%A4%AA%E5%9C%B0%E5%8C%BA%20002
    trojan://idc117okt@103.176.78.153:443?allowInsecure=1#ID_103.176.78.153_10223ad5-134
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMTUgMiIsImFkZCI6IjQxLjIxNi4xNzcuMjM0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZmZWExNjQ5LTQyNWItNDA5Mi1iZjUzLTI5NzkyMTUyYzkyNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Noa2l0L0Fyc2hhbTg1MjMxLzYzNDdkMDgwMjJiOTEvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%20102%202
    ss://YWVzLTI1Ni1jZmI6VWtYUnNYdlI2YnVETUcyWQ@213.183.63.221:9001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2057
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2088
    

</details>

### 所有节点
合并节点总数: `4792`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `133`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `122`
- [freefq/free](https://github.com/freefq/free), 节点数量: `16`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `44`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `6498`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `41`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `39`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `27`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `159`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `102`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `15`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `14`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `49`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `25`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `217`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `181`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `277`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `20`

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
