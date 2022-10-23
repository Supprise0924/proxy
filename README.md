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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9KFRH6aKR6YGTQGt4c3dhKSAyIiwiYWRkIjoiYXprb3JlYS5ub29iY3hrLmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5OTIyNWE5OS1iZmY0LWY5YTAtZjY3NC04YjhhMTA1ODAyODkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3hkZXZ2d3MiLCJob3N0IjoiYXprb3JlYS5ub29iY3hrLmNmIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiS1JfMTUyLjcwLjIzNS4yMDdfMTAyMWE2NzctMjMwIiwiYWRkIjoiMTUyLjcwLjIzNS4yMDciLCJwb3J0IjoiMzU0MTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIveGRldnZ3cyIsImhvc3QiOiJhemtvcmVhLm5vb2JjeGsuY2YiLCJ0bHMiOiIifQ==
    trojan://6248895b-4255-4f07-9479-d198bc1eb8db@download1hkt.windowsupdate1.com:28443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%AD%F0%9F%87%B0%20HK%207%20TG%40nodpai%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsImFkZCI6IjEzOS45OS45MS45NSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJnbGMuaHJ1cW9hdy5jbiIsInRscyI6IiJ9
    trojan://6248895b-4255-4f07-9479-d198bc1eb8db@download1hkt.windowsupdate1.com:28443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%AD%F0%9F%87%B0%20HK%207%20TG%40nodpai
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIxMjkiLCJhZGQiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6ImEuMTg5LmNuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIxMzUiLCJhZGQiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6ImEuMTg5LmNuIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:806#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-1152-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:806#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-2940-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:806#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-3808-81.90.189.41%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwNSIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiU0dfMTM5Ljk5LjkwLjEyMl8xMDIwY2JkNi0yNSIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwMyIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    trojan://6248895b-4255-4f07-9479-d198bc1eb8db@zf2.windowsupdate1.com:30040?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%AD%F0%9F%87%B0%20HK%202%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@ak1484.free.www.outline.network:811#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-23%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-264-ak1484.free.www.outline.network%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@ak1484.free.www.outline.network:811#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-23%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-1130-ak1484.free.www.outline.network
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@ak1484.free.www.outline.network:811#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-23%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-942-ak1484.free.www.outline.network
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjIwMjQiLCJhZGQiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3MGRlNDkyNC1kMWFjLTM0ODItYTQ5NC01NzdiNGNjYzliMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Fkb2JlIiwiaG9zdCI6InNob3Vlci5henpodWFuZ2FwaW5nLnR3IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjI1IiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMTI4LjEuMTM0LjEyNl8xMDIwY2JkNi01MyIsImFkZCI6IjEyOC4xLjEzNC4xMjYiLCJwb3J0IjoiNjY2NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmIzYjU3MS1jZGE4LTQwZjYtYzllNi1kYjk3NjVlYThmYWEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJzaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo4ZDE4MzRjOS00ZTIzLTQ3ZTMtODM0ZS0zNjNjYjgxYjFmZjc@agroup.node2.s.nodelist-gfwairport.download:50001#%F0%9F%87%B0%F0%9F%87%B7%20%5B10-23%5D-%F0%9F%87%B0%F0%9F%87%B7-%E9%9F%A9%E5%9B%BD-788-agroup.node2.s.nodelist-gfwairport.download
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@hk1.sanfen001.pics:443?allowInsecure=1&sni=hk1.sanfen001.pics#%F0%9F%87%AD%F0%9F%87%B0%20HK%2011%20TG%40nodpai
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1Mi54eXoiLCJhZGQiOiJ2MmtyNi50dXR1Mi54eXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU1ZTU1NjQ2LWQwYmYtM2NjZC05MjAxLThlYjZjNmVkMmQzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InYya3I2LnR1dHUyLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1Mi54eXogMiIsImFkZCI6InYya3I2LnR1dHUyLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVlNTU2NDYtZDBiZi0zY2NkLTkyMDEtOGViNmM2ZWQyZDNjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjJrcjYudHV0dTIueHl6IiwidGxzIjoidGxzIn0=
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@kr1.sanfen001.pics:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20github.com%2Ffreefq%20-%20%E6%97%A5%E6%9C%AC%20%203
    trojan://8800c518-e68a-4441-a45c-cd67855784c8@kr1.sanfen001.pics:443?allowInsecure=1&sni=kr1.sanfen001.pics#%F0%9F%87%AF%F0%9F%87%B5%20JP%204%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgZ2l0aHViLmNvbS9mcmVlZnEgLSDpn6nlm70gIDEiLCJhZGQiOiJhemtvcmVhLm5vb2JjeGsuY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk5MjI1YTk5LWJmZjQtZjlhMC1mNjc0LThiOGExMDU4MDI4OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImF6a29yZWEubm9vYmN4ay5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS1hemtvcmVhLm5vb2JjeGsuY2YiLCJhZGQiOiJhemtvcmVhLm5vb2JjeGsuY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk5MjI1YTk5LWJmZjQtZjlhMC1mNjc0LThiOGExMDU4MDI4OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImF6a29yZWEubm9vYmN4ay5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MmtyNi50dXR1NC5vbmUgMiIsImFkZCI6InYya3I2LnR1dHU0Lm9uZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVlNTU2NDYtZDBiZi0zY2NkLTkyMDEtOGViNmM2ZWQyZDNjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjJrcjYudHV0dTQub25lIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIwMDciLCJhZGQiOiJzZy1sYi52aGF4Lm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9FcnR1c2c4Ni82MzUwMTQ2MzhjMjY0LyIsImhvc3QiOiJzZy1sYi52aGF4Lm5ldCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjIyNDciLCJhZGQiOiJzZy1sYi52aGF4Lm5ldCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmVhMTY0OS00MjViLTQwOTItYmY1My0yOTc5MjE1MmM5MjUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC9FcnR1c2c4Ni82MzUwMTQ2MzhjMjY0LyIsImhvc3QiOiJ6b29tLnVzIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:809#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203809-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.203:803#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.203803-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:809#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204809-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@193.38.139.204:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-193.38.139.204806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC193.38.139.201-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@52.197.66.243:443#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-52.197.66.243443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@52.197.66.243:443#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-52.197.66.243443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLXZtZXNzLTE0Ni41Ni40MC4xMTcyNzY3NS3ooqvlopkt55u06L+eLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoiMTQ2LjU2LjQwLjExNyIsInBvcnQiOiIyNzY3NSIsInR5cGUiOiJub25lIiwiaWQiOiIwNTNjYTBmNC0wNTdlLTQ5M2QtYWQzMC01YmE1MWYwMGY1OWMiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLXZtZXNzLTE0Ni41Ni40MC4xMTcyNzY3NS3ooqvlopkt55u06L+eLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDIiLCJhZGQiOiIxNDYuNTYuNDAuMTE3IiwicG9ydCI6IjI3Njc1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA1M2NhMGY0LTA1N2UtNDkzZC1hZDMwLTViYTUxZjAwZjU5YyIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKwgIDQ4IiwiYWRkIjoiMTQ2LjU2LjQwLjExNyIsInBvcnQiOiIyNzY3NSIsInR5cGUiOiJub25lIiwiaWQiOiIwNTNjYTBmNC0wNTdlLTQ5M2QtYWQzMC01YmE1MWYwMGY1OWMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KFRH6aKR6YGTQGt4c3dhKSA1IiwiYWRkIjoiMTk1LjEyMy4yNDMuMjEiLCJwb3J0IjoiMTAwMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzlhYTg5YjgtNGY4My0xMWVkLTg4NWEtNTJhYzAwNjRmNTBhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92cG5qYW50aXQiLCJob3N0IjoiMTk1LjEyMy4yNDMuMjEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MiIsImFkZCI6IjE5NS4xMjMuMjQzLjIxIiwicG9ydCI6IjEwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc5YWE4OWI4LTRmODMtMTFlZC04ODVhLTUyYWMwMDY0ZjUwYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6IjE5NS4xMjMuMjQzLjIxIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzMCIsImFkZCI6IjE1Mi43MC4yMzUuMjA3IiwicG9ydCI6IjM1NDEyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcwZDk1MzA4LTJhNjEtNGY5My1mMTM5LTkxMDNkMDU4N2ZkOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiIxOTUuMTIzLjI0My4yMSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgODU1IiwiYWRkIjoiMTY4LjEzOC4yMDcuNjYiLCJwb3J0IjoiMjEzNjUiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTA1Zjk5YjEtZTdiYS00NWUwLWFlNGQtYjBmZmRmMGFkMjQ1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6IjE5NS4xMjMuMjQzLjIxIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.114.114.19:5601#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-754-38.114.114.19
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@172.99.190.87:3389#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-292-172.99.190.87
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@172.99.190.87:3389#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20046
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MSIsImFkZCI6IjE0MS45OC4xOS43NyIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJiODI0OGUxNi00ZjgxLTExZWQtODdlNi0wMDE2M2VkMTc4YTQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiIxNDEuOTguMTkuNzciLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.143.66.99:5001#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3696-38.143.66.99
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.64.138.145:5601#%F0%9F%87%A8%F0%9F%87%A6%20%5B10-23%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-5342-38.64.138.145
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.137.9:7306#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3776-38.75.137.9%202
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@172.99.190.61:5601#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-2186-172.99.190.61
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-406-172.99.190.39
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxNw@138.68.248.130:811#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-ss-138.68.248.130811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7%202
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@169.197.141.14:8888#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%A6%F0%9F%87%B6-%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA-5344-169.197.141.14
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.137.9:7306#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3776-38.75.137.9
    ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@38.143.66.64:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3716-38.143.66.64%202
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-384-38.68.135.18
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.137.9:7306#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-822-38.75.137.9
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-992-38.68.135.18
    ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@38.143.66.64:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-23%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-3716-38.143.66.64
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KFRH6aKR6YGTQGt4c3dhKSIsImFkZCI6IjUuMzQuMTc4LjE1NyIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJjNmE0NDM5NC00ZjgzLTExZWQtYWY5Zi1iYjI2MWVlZGM3MDIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiI1LjM0LjE3OC4xNTciLCJ0bHMiOiIifQ==
    trojan://752a9404-c729-485e-8ea5-acb3f4fc8180@hg1.leifengkeji.live:48899?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2019
    trojan://3a2c0c6c-9ee5-c05f-c951-fcd73831983e@kr05.wangxd.life:3052?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2078
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh78g5o235YWLKFRH6aKR6YGTQGt4c3dhKSIsImFkZCI6IjE5NS4xMjMuMjQ2LjEyMCIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJiM2E0MGI1ZS00ZjgyLTExZWQtOTE4ZC01MmNmMDBlNDYxYWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiIxOTUuMTIzLjI0Ni4xMjAiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDE3LjM4TWIiLCJhZGQiOiIxNTIuNzAuMjM1LjIwNyIsInBvcnQiOiIzNTQxMiIsInR5cGUiOiJub25lIiwiaWQiOiI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii92cG5qYW50aXQiLCJob3N0IjoiMTk1LjEyMy4yNDYuMTIwIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@85.208.108.60:3389#%F0%9F%87%B8%F0%9F%87%A6%20%5B10-23%5D-%F0%9F%87%A6%F0%9F%87%B6-%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AF-2590-85.208.108.60
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@85.208.108.90:8080#%F0%9F%87%B8%F0%9F%87%A6%20%5B10-23%5D-%F0%9F%87%A6%F0%9F%87%B6-%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AF-314-85.208.108.90
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.64.138.145:8080#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2039%202
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@167.88.61.50:3389#%F0%9F%87%B8%F0%9F%87%AA%20%5B10-23%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-2312-167.88.61.50
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.143.66.99:5001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2062
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.75.136.34:8080#_01
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9KFRH6aKR6YGTQGt4c3dhKSAyIiwiYWRkIjoiMTQxLjk4LjE5Ljc3IiwicG9ydCI6IjEwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4MjQ4ZTE2LTRmODEtMTFlZC04N2U2LTAwMTYzZWQxNzhhNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6IjE0MS45OC4xOS43NyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HtfCfh7EgLeazouWFsC0xNDEuOTguMTkuNzciLCJhZGQiOiIxNDEuOTguMTkuNzciLCJwb3J0IjoiMTAwMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjgyNDhlMTYtNGY4MS0xMWVkLTg3ZTYtMDAxNjNlZDE3OGE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92cG5qYW50aXQiLCJob3N0IjoiMTQxLjk4LjE5Ljc3IiwidGxzIjoiIn0=
    trojan://xxoo@138.124.183.216:443?allowInsecure=1#mianfeifq%20235%202
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.68.135.18:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2052
    ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@172.99.190.39:5003#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%20120
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@172.99.190.39:5500#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2083
    vmess://eyJ2IjoiMiIsInBzIjoi5Lqa5aSq5Zyw5Yy6IDAwMSIsImFkZCI6IjEwMy4xNTkuMTMyLjEwMiIsInBvcnQiOiIzMTM3MiIsInR5cGUiOiJub25lIiwiaWQiOiJjMTEyMzZhZi01NmE2LTQ5YjMtYzFiOS03YjU0YWMzYWNiNDIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9XzEwMjIwNjkiLCJhZGQiOiJ0aDIudnBuamFudGl0LmNvbSIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJiODI0OGUxNi00ZjgxLTExZWQtODdlNi0wMDE2M2VkMTc4YTQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZwbmphbnRpdCIsImhvc3QiOiJ0aDIudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoifCAxLjY3TWIiLCJhZGQiOiIxMDMuMTU5LjEzMi4xMDIiLCJwb3J0IjoiMzEzNzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzExMjM2YWYtNTZhNi00OWIzLWMxYjktN2I1NGFjM2FjYjQyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6InRoMi52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@93.186.201.124:803#%F0%9F%87%A9%F0%9F%87%AA%20%5B10-23%5D-%F0%9F%87%A9%F0%9F%87%AA-%E5%BE%B7%E5%9B%BD-2554-93.186.201.124
    vmess://eyJ2IjoiMiIsInBzIjoidW5rbm93biAxMTgiLCJhZGQiOiIxMDMuMTU5LjEzMi4xMDIiLCJwb3J0IjoiMzEzNzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzExMjM2YWYtNTZhNi00OWIzLWMxYjktN2I1NGFjM2FjYjQyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdnBuamFudGl0IiwiaG9zdCI6InRoMi52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@169.197.141.14:7002#ZZ_20%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Ht/Cfh7QgLee9l+mprOWwvOS6mi05NC4xNzcuOC44NyIsImFkZCI6Ijk0LjE3Ny44Ljg3IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyRjA5NDg0NS1FMkJELUVCRjctREVCNy05OTU5OTI0MzZGQUYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NwZWVkdGVzdCIsImhvc3QiOiJ2aWUubmFwc3Rlcm5ldHYuY29tIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6VWtYUnNYdlI2YnVETUcyWQ@213.183.63.221:9001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2045
    

</details>

### 所有节点
合并节点总数: `5139`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `166`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `136`
- [freefq/free](https://github.com/freefq/free), 节点数量: `13`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `300`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `6498`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `35`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `19`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `14`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `146`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `48`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `12`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `11`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `49`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `20`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `217`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `207`
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
