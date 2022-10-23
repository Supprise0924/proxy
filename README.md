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
高速节点数量: `92`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwNCIsImFkZCI6IjEzOS45OS45MS45NSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan%2FOsaka_9
    vmess://eyJ2IjoiMiIsInBzIjoiU0dfMTM5Ljk5LjkwLjEyMl8xMDIwY2JkNi0yNSIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwNSIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIyMzkiLCJhZGQiOiIxNDYuNTYuMTMzLjEyIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcwZGU0OTI0LWQxYWMtMzQ4Mi1hNDk0LTU3N2I0Y2NjOWIxZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYWRvYmUiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzEudjItcmF5LmNvbSIsImFkZCI6InNnMS52Mi1yYXkuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY5OGY1NWNjLWQ3NGEtNGM5MC1iZjY5LTk3M2IzYjY3Njc0ZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZmFzdHNzaC9nYWZzZzY1Zy82MzUwNDVkYzMwZWU2LyIsImhvc3QiOiJoa2cxMnMxMS1pbi1mMTQuMWUxMDAubmV0IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5Lit5Zu9LXZtZXNzLTguMjE0LjMzLjE1ODgwLeiiq+WimS3nm7Tov54t6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMiIsImFkZCI6IjguMjE0LjMzLjE1OCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjYjgxZTZhYi0xZDgzLTRhYzEtZjBhZC1hZTVjMmE3YzI5ZWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNDYuNTYuMTMzLjEyIiwiYWRkIjoiMTQ2LjU2LjEzMy4xMiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:806#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-3808-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:806#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-6072-81.90.189.41
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIzMTYiLCJhZGQiOiI1MS43OS4xNTYuMjIzIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMxZDAxMjI1LTJlNmYtNDlmYS04MzNlLWVkZjdjYjFmODAzMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvSkFHT0FOU1NILyIsImhvc3QiOiJuYW1hdmEuaXIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwNiIsImFkZCI6InNnOC52bWVzLnh5eiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjMWQwMTIyNS0yZTZmLTQ5ZmEtODMzZS1lZGY3Y2IxZjgwMzAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL0pBR09BTlNTSC8iLCJob3N0Ijoic2c4LnZtZXMueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIxMjkiLCJhZGQiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6ImEuMTg5LmNuIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@ak1484.free.www.outline.network:811#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-23%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-1130-ak1484.free.www.outline.network
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@ak1484.free.www.outline.network:811#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-23%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-264-ak1484.free.www.outline.network
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjMuOTEuMTAwLjI0M18xMDIwY2JkNi0xMDUgMiIsImFkZCI6IjIzLjkxLjEwMC4yNDMiLCJwb3J0IjoiMzA4NjIiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2IwZjQ0ZTQtZGQxMS00MjlkLWM4MGYtNjE1YjEwNTk1ZGI5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvYWRvYmUiLCJob3N0IjoiYS4xODkuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzgudm1lcy54eXoiLCJhZGQiOiJzZzgudm1lcy54eXoiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzFkMDEyMjUtMmU2Zi00OWZhLTgzM2UtZWRmN2NiMWY4MDMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9KQUdPQU5TU0gvIiwiaG9zdCI6Im5hbWF2YS5pciIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjI1IiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9KQUdPQU5TU0gvIiwiaG9zdCI6Im5hbWF2YS5pciIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIzMTIiLCJhZGQiOiJzZzgudm1lcy54eXoiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzFkMDEyMjUtMmU2Zi00OWZhLTgzM2UtZWRmN2NiMWY4MDMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9KQUdPQU5TU0gvIiwiaG9zdCI6Im5hbWF2YS5pciIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS01MS43OS4xNTYuMjIzIiwiYWRkIjoiNTEuNzkuMTU2LjIyMyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjMWQwMTIyNS0yZTZmLTQ5ZmEtODMzZS1lZGY3Y2IxZjgwMzAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL0pBR09BTlNTSC8iLCJob3N0IjoibmFtYXZhLmlyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMTI4LjEuMTM0LjEyNl8xMDIwY2JkNi01MyIsImFkZCI6IjEyOC4xLjEzNC4xMjYiLCJwb3J0IjoiNjY2NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmIzYjU3MS1jZGE4LTQwZjYtYzllNi1kYjk3NjVlYThmYWEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9KQUdPQU5TU0gvIiwiaG9zdCI6Im5hbWF2YS5pciIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpiNDczZGRiYy01N2I0LTQxZjQtOTVkYS05NDlkNDI2N2U0M2I@ea1.bafang.vip:10023#%F0%9F%87%AD%F0%9F%87%B0%20%E9%A6%99%E6%B8%AF01%7CSS%E7%9B%B4%E8%BF%9E%7Cx2
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1NC5vbmUiLCJhZGQiOiJ2MmtyNi50dXR1NC5vbmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU1ZTU1NjQ2LWQwYmYtM2NjZC05MjAxLThlYjZjNmVkMmQzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InYya3I2LnR1dHU0Lm9uZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKwgIDMgMiIsImFkZCI6InYya3I2LnR1dHU0Lm9uZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVlNTU2NDYtZDBiZi0zY2NkLTkyMDEtOGViNmM2ZWQyZDNjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjJrcjYudHV0dTQub25lIiwidGxzIjoidGxzIn0=
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@hk1.sanfen001.pics:443?allowInsecure=1&sni=hk1.sanfen001.pics#%F0%9F%87%AD%F0%9F%87%B0%20HK%2011%20TG%40nodpai
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1Mi54eXoiLCJhZGQiOiJ2MmtyNi50dXR1Mi54eXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU1ZTU1NjQ2LWQwYmYtM2NjZC05MjAxLThlYjZjNmVkMmQzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InYya3I2LnR1dHUyLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1Mi54eXogMiIsImFkZCI6InYya3I2LnR1dHUyLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVlNTU2NDYtZDBiZi0zY2NkLTkyMDEtOGViNmM2ZWQyZDNjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii90dSIsImhvc3QiOiJ2MmtyNi50dXR1Mi54eXoiLCJ0bHMiOiJ0bHMifQ==
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@kr1.sanfen001.pics:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20github.com%2Ffreefq%20-%20%E6%97%A5%E6%9C%AC%20%203
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@kr1.sanfen001.pics:443?allowInsecure=1&sni=kr1.sanfen001.pics#%F0%9F%87%AF%F0%9F%87%B5%20JP%204%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDpn6nlm73pppblsJRBbWF6b27mlbDmja7kuK3lv4MgMSIsImFkZCI6IjU0LjE4MC4xMDEuNiIsInBvcnQiOiIxMTExMSIsInR5cGUiOiJub25lIiwiaWQiOiI3NTJhOTQwNC1jNzI5LTQ4NWUtOGVhNS1hY2IzZjRmYzgxODAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS01NC4xODAuMTAxLjYiLCJhZGQiOiI1NC4xODAuMTAxLjYiLCJwb3J0IjoiMTExMTEiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzUyYTk0MDQtYzcyOS00ODVlLThlYTUtYWNiM2Y0ZmM4MTgwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDpn6nlm73pppblsJRBbWF6b27mlbDmja7kuK3lv4MgMSAyIiwiYWRkIjoiNTQuMTgwLjEwMS42IiwicG9ydCI6IjExMTExIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc1MmE5NDA0LWM3MjktNDg1ZS04ZWE1LWFjYjNmNGZjODE4MCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDpn6nlm73pppblsJRBbWF6b27mlbDmja7kuK3lv4MgNCIsImFkZCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInBvcnQiOiIxMTExMSIsInR5cGUiOiJub25lIiwiaWQiOiI3NTJhOTQwNC1jNzI5LTQ4NWUtOGVhNS1hY2IzZjRmYzgxODAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2bTE1LmxlaWZlbmdrZWppLmxpdmUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIxMzQiLCJhZGQiOiJ2bTE1LmxlaWZlbmdrZWppLmxpdmUiLCJwb3J0IjoiMTExMTEiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzUyYTk0MDQtYzcyOS00ODVlLThlYTUtYWNiM2Y0ZmM4MTgwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoidm0xNS5sZWlmZW5na2VqaS5saXZlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDpn6nlm73pppblsJRBbWF6b27mlbDmja7kuK3lv4MgNCAyIiwiYWRkIjoidm0xNS5sZWlmZW5na2VqaS5saXZlIiwicG9ydCI6IjExMTExIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc1MmE5NDA0LWM3MjktNDg1ZS04ZWE1LWFjYjNmNGZjODE4MCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjIwMDQiLCJhZGQiOiIxNjUuMTU0LjI1My42MyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjMzOGE1OWQtOWM1Yy00ZTgzLWEyZDAtN2EzNzg4ODRjOTY5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjIwMTUiLCJhZGQiOiIxNjUuMTU0LjI1My42MyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjBhMWUzZDEtOWZiMC00ZjA5LThiYzktYjc1ZWMzMWExODU4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjIwMDIiLCJhZGQiOiIxNjUuMTU0LjI0NC4yOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjMzOGE1OWQtOWM1Yy00ZTgzLWEyZDAtN2EzNzg4ODRjOTY5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjIwMDciLCJhZGQiOiIxNjUuMTU0LjI0NC4yOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTE0NGRlMzgtYTg4MS00ZDQ1LTg1MmItNTllYjVjMzhmN2E4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InZtMTUubGVpZmVuZ2tlamkubGl2ZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKzkuJzkuqxMaW5vZGXmlbDmja7kuK3lv4MgMTMiLCJhZGQiOiJ2ZGUxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2ZGUxLjBiYWQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDmtZnmsZ/nnIHlj7Dlt57luILnp7vliqggMjMiLCJhZGQiOiJrd2RvZC0xMDU2LXYyLTEuaGtnLXIta2NkLWUuYXAuY2poaC5iZWF1dHkiLCJwb3J0IjoiMjk5ODgiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2FhYzYyODUtNTExYy00YTA3LWI2ZGItZWRmYmRjZmUzODg5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsImhvc3QiOiJzMy5jamhoLmJlYXV0eSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTI5LjE1OS40MS4yMzNfMTAyMTgwYjUtNjkiLCJhZGQiOiIxMjkuMTU5LjQxLjIzMyIsInBvcnQiOiIzMjU4NiIsInR5cGUiOiJub25lIiwiaWQiOiIzNDFhOTE4Mi1jNDIzLTQ5OWMtYzQ2ZS1kMTc4MzhiMjkwMzciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsImhvc3QiOiJzMy5jamhoLmJlYXV0eSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyOCAyIiwiYWRkIjoiMTUyLjY5LjE5Ny42MCIsInBvcnQiOiIxMDY5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImFjOGUyNmZlLTgxNTAtNGI2MC1hZTY0LTgyZmM3N2ViYTJjZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2plNXgzcEJOMXZlejNOUXVkTmtCIiwiaG9zdCI6InMzLmNqaGguYmVhdXR5IiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.114.114.19:5601#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3744-38.114.114.19
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbveWKoOWIqeemj+WwvOS6muW3nua0m+adieefti00MS4yMTYuMTc3LjIzNCIsImFkZCI6IjQxLjIxNi4xNzcuMjM0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZmZWExNjQ5LTQyNWItNDA5Mi1iZjUzLTI5NzkyMTUyYzkyNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Noa2l0L0Fyc2hhbTg1MjMxLzYzNDdkMDgwMjJiOTEvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.137.9:7306#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3776-38.75.137.9
    ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@38.143.66.64:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3716-38.143.66.64
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-1178-172.99.190.39
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202%202
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-384-38.68.135.18
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-480-38.68.135.18
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIyMzMxIiwiYWRkIjoidXNhNC52cG5qYW50aXQuY29tIiwicG9ydCI6IjEwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM2YTQ0Mzk0LTRmODMtMTFlZC1hZjlmLWJiMjYxZWVkYzcwMiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6InVzYTQudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgZ2l0aHViLmNvbS9mcmVlZnEgLSDliqDmi7/lpKcgIDciLCJhZGQiOiIxNjUuMTU0LjI0NC4yOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjhjM2ZiZmUtOWY2NS00ODYxLWI4MjQtZjAwNDlhYTU1ODEwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6InVzYTQudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDE2IiwiYWRkIjoidm1zLXNlcnZpY2UuY2xvdWQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjlmYzdiZjc4LTQ1OTYtNDUxOC1hZjFmLWM2NDkwM2I2OTAzOSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InZtcy1zZXJ2aWNlLmNsb3VkIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggQFNTUlNVQi3nvo7lm71WMDMt5LuY6LS55o6o6I2QZGxqLnRmL3NzcnN1YiIsImFkZCI6Ind3dy5kaWdpdGFsb2NlYW4uY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY0NWZjNGU3LWUzYTMtNGU4Mi04YWJkLTJkNzEzMjQ4OTRjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCJob3N0Ijoic3Nyc3ViLnYwMi5hc3VrYS5idXp6IiwidGxzIjoiIn0=
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@hk1.sanfen001.pics:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%201
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@hk1.sanfen001.pics:443?allowInsecure=1&sni=hk1.sanfen001.pics#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20002
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIwNTAiLCJhZGQiOiIyMy4yMjQuMTAxLjEwMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTQ2YmE1ZGYtNTc3MS00ODczLWEzY2ItODkyMzc4NTI2MTQ3IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZm9vdGVycyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIxNTYyIiwiYWRkIjoiMjMuMjI0LjEwMS4xMDIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk0NmJhNWRmLTU3NzEtNDg3My1hM2NiLTg5MjM3ODUyNjE0NyIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiL2Zvb3RlcnMiLCJob3N0Ijoid3d3Ljc2MTI2NDQ5Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIxMDI4IiwiYWRkIjoiMTA0LjI1LjUyLjE4NyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGNkYjAxNmYtZjE0ZS0zMGIzLTk3ZDYtNDUzYzc0MWE1YzgwIiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii95NDc1IiwiaG9zdCI6IjEwNC4yNS41Mi4xODciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIxMDQxIiwiYWRkIjoiMTA0LjI1LjUyLjE4NyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGNkYjAxNmYtZjE0ZS0zMGIzLTk3ZDYtNDUzYzc0MWE1YzgwIiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii95NDc1IiwiaG9zdCI6ImZyZWUuZnJsaS54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjIwMDMiLCJhZGQiOiJhb3Auc3NmcmVlLnJ1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmUwMWY2Ni00MzM0LTExZWQtYTExYi0wMDAwMTcwMjIwMDgiLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nZXR3ZWF0aGVyIiwiaG9zdCI6ImFvcC5zc2ZyZWUucnUiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDI1LjcyTWIiLCJhZGQiOiIxNjguMTM4LjIwNy42NiIsInBvcnQiOiIyMTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiI5MDVmOTliMS1lN2JhLTQ1ZTAtYWU0ZC1iMGZmZGYwYWQyNDUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9nZXR3ZWF0aGVyIiwiaG9zdCI6ImFvcC5zc2ZyZWUucnUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDQxLjA3TWIiLCJhZGQiOiIxMzkuOTkuOTAuMTIyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvZ2V0d2VhdGhlciIsImhvc3QiOiJhb3Auc3NmcmVlLnJ1IiwidGxzIjoiIn0=
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=0#%7C20.25Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cg5be06KW/IDAwMyIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=0#%7C20.25Mb%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMTQiLCJhZGQiOiJzZy1hdGhhLnYyLXJheS5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWZjMzI5NzMtYTE1ZS00MDRjLWIxZjctNzA3MTg3ZjdmZDZlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9mYXN0c3NoL2Ftcm96aTg3LzYzNTA0MTZlYzMzMGIvIiwiaG9zdCI6Inpvb20udXMiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6kg5Y2w5bqm5bC86KW/5LqaXzEwMjIwMTQgMiIsImFkZCI6InNnLWF0aGEudjItcmF5LmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI1ZmMzMjk3My1hMTVlLTQwNGMtYjFmNy03MDcxODdmN2ZkNmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Zhc3Rzc2gvYW1yb3ppODcvNjM1MDQxNmVjMzMwYi8iLCJob3N0Ijoiem9vbS51cyIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2039
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.114.114.19:5601#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2070
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeasp+ebny1zZy1hdGhhLnYyLXJheS5jb20iLCJhZGQiOiJzZy1hdGhhLnYyLXJheS5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWZjMzI5NzMtYTE1ZS00MDRjLWIxZjctNzA3MTg3ZjdmZDZlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9mYXN0c3NoL2Ftcm96aTg3LzYzNTA0MTZlYzMzMGIvIiwiaG9zdCI6Inpvb20udXMiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDExLjc2TWIiLCJhZGQiOiI4LjIxNC4zMy4xNTgiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2I4MWU2YWItMWQ4My00YWMxLWYwYWQtYWU1YzJhN2MyOWVmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsvCfh74gTVlfMjAyLjU5LjEwLjExNl8xMDIxODBiNS05MyIsImFkZCI6IjIwMi41OS4xMC4xMTYiLCJwb3J0IjoiMzEzNzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2FiNzkzNzAtZjEzNS00NDViLWQ0ODAtYWFhMGQ2OWJiMTA4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@169.197.141.14:7002#ZZ_20%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@217.138.193.10:803#%F0%9F%87%AC%F0%9F%87%A7%20%5B10-23%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-268-217.138.193.10
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2077%202
    ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.143.66.99:8118#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%20107
    vmess://eyJ2IjoiMiIsInBzIjoifCAxLjY3TWIiLCJhZGQiOiIxMDMuMTU5LjEzMi4xMDIiLCJwb3J0IjoiMzEzNzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzExMjM2YWYtNTZhNi00OWIzLWMxYjktN2I1NGFjM2FjYjQyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.143.66.99:8118#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2099%202
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIaw@185.126.116.125:9098#RO_08
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2052
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2079%202
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@169.197.141.14:7002#ZZ_20
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@93.186.201.124:803#%F0%9F%87%A9%F0%9F%87%AA%20%5B10-22%5D-%F0%9F%87%A9%F0%9F%87%AA-%E5%BE%B7%E5%9B%BD-2900-93.186.201.124
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2083
    

</details>

### 所有节点
合并节点总数: `4982`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `166`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `133`
- [freefq/free](https://github.com/freefq/free), 节点数量: `25`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `6498`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `88`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `19`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `14`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `155`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `48`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `23`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `11`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `77`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `20`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `217`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `190`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `269`
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
