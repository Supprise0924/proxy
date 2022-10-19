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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzAyLnhpYW9xaTk5LmNmIiwiYWRkIjoic2cwMi54aWFvcWk5OS5jZiIsInBvcnQiOiI2MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiI0OTE2NjkyOS0wMjBlLTRlZjAtOTdlNy03OTg5Y2U5MmZjNjkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJzZzAyLnhpYW9xaTk5LmNmIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgX1NHX+aWsOWKoOWdoSA0IiwiYWRkIjoic2cwMi54aWFvcWk5OS5jZiIsInBvcnQiOiI2MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiI0OTE2NjkyOS0wMjBlLTRlZjAtOTdlNy03OTg5Y2U5MmZjNjkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJzZzAyLnhpYW9xaTk5LmNmIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-230-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.49:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-800-81.90.189.49%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-338-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.49:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-1088-81.90.189.49
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.41:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-406-81.90.189.41
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@81.90.189.49:801#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-800-81.90.189.49
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgxODMiLCJhZGQiOiIxOTQuMjMzLjgxLjEyNSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjZWI4YTkyMS1lYzcyLTQ4MDQtYWU5Mi1jYmQzMDlmMmYyMTMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZtZXNzIiwiaG9zdCI6InNnLXYuc3NobWF4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwMiIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii92bWVzcyIsImhvc3QiOiJzZy12LnNzaG1heC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgX0hLX+mmmea4ryAyIiwiYWRkIjoiMTY1LjE1NC4yNDQuMjkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImExNDRkZTM4LWE4ODEtNGQ0NS04NTJiLTU5ZWI1YzM4ZjdhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3ZtZXNzIiwiaG9zdCI6InNnLXYuc3NobWF4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg54uu5Z+OMnx0Z+mikemBk0ByaXBhb2ppZWRpYW4iLCJhZGQiOiIxNjUuMTU0LjI0NC4yOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTE0NGRlMzgtYTg4MS00ZDQ1LTg1MmItNTllYjVjMzhmN2E4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdm1lc3MiLCJob3N0Ijoic2ctdi5zc2htYXgueHl6IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://DigitalOcean@digitalocean.kinhproxy.com:443?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20github.com%2Ffreefq%20-%20%E6%96%B0%E5%8A%A0%E5%9D%A1DigitalOcean%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2016
    trojan://DigitalOcean@digitalocean.kinhproxy.com:443?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://DigitalOcean@139.59.227.109:443?allowInsecure=1#SG_139.59.227.109_10187dd0-203%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysMyIsImFkZCI6InpmLjY2MjI3OC54eXoiLCJwb3J0IjoiNDQxOTUiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjQ0ZGFmYzktYTYyYi00OGNlLWI4MzItNzY1NWQ1NDk3NGVhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InpmLjY2MjI3OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysMiIsImFkZCI6InpmLjY2MjI3OC54eXoiLCJwb3J0IjoiMTE0MzMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjQ0ZGFmYzktYTYyYi00OGNlLWI4MzItNzY1NWQ1NDk3NGVhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InpmLjY2MjI3OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgxODUiLCJhZGQiOiJzZy12LnNzaG1heC54eXoiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTE0N2YxYjMtZDBkNC00Y2E4LTljZTktMzhkM2MyNGQ3OTUwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92bWVzcyIsImhvc3QiOiJzZy12LnNzaG1heC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysNCIsImFkZCI6InpmLjY2MjI3OC54eXoiLCJwb3J0IjoiMTE0MzMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjQ0ZGFmYzktYTYyYi00OGNlLWI4MzItNzY1NWQ1NDk3NGVhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdm1lc3MiLCJob3N0Ijoic2ctdi5zc2htYXgueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgxODUgMiIsImFkZCI6InNnLXYuc3NobWF4Lnh5eiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJhMTQ3ZjFiMy1kMGQ0LTRjYTgtOWNlOS0zOGQzYzI0ZDc5NTAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZtZXNzIiwiaG9zdCI6InNnLXYuc3NobWF4Lnh5eiIsInRscyI6IiJ9
    ssr://MTMuMjE1LjE3OS4xNTY6MzIwMDE6b3JpZ2luOmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpNMmN3WkVoc1MwMUYvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPVUwZGZNVE11TWpFMUxqRTNPUzR4TlRaZk1UQXhPRGRrWkRBdEpRJm9iZnNwYXJhbT0mcHJvdG9wYXJhbT0
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTgwNDIiLCJhZGQiOiJjZi43MzE4MDgudGsiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjgxOTRmNzI0LWQ2NDgtNGViOC05OGQyLTAwMTMxMzZlNzlmMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYnhmYnZ3cyIsImhvc3QiOiJoNTUyOC4xODA4LmNmIiwidGxzIjoidGxzIn0=
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1#HK_103.177.248.160_10187dd0-3300
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjE3IiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjE3IDIiLCJhZGQiOiIyMy45MS4xMDAuMjQzIiwicG9ydCI6IjMwODYyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjNiMGY0NGU0LWRkMTEtNDI5ZC1jODBmLTYxNWIxMDU5NWRiOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://5f97472b-b910-32fd-bbd2-403f0c6c5ae0@3.sg.zz.xxxxx.x-t-fuckword.network:36679?allowInsecure=0&sni=3.sg.ld.xxxxx.x-t-fuckword.link#%F0%9F%87%AD%F0%9F%87%B0%20%E9%A6%99%E6%B8%AF%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%206
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysKOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIiwiYWRkIjoiMTQ2LjU2LjE4Ny4xMyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI1NjIzOThjOC1jYjdmLTQ4NTAtOTBlYi0yZmQxN2RjY2IxM2EiLCJhaWQiOiIxIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206Q1VuZFNabllzUEtjdTZLajhUSFZNQkhE@89.187.162.184:39772#%F0%9F%87%B8%F0%9F%87%AC%20%5B10-19%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-360-89.187.162.184
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@118.107.244.112:8091#%F0%9F%87%AD%F0%9F%87%B0%20%E9%A6%99%E6%B8%AF%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%205
    ssr://anAtYW00OC02LmVxbm9kZS5uZXQ6ODA4MTpvcmlnaW46YWVzLTI1Ni1jZmI6dGxzMS4yX3RpY2tldF9hdXRoOlpVRnZhMkpoUkU0Mi8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9U2xCZk5USXVNVGszTGpFMk1pNDRPVjh4TURFNE4yUmtNQzB5SlEmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPQ
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.85.3.149:800#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.85.3.149:800#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-19%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-358-45.85.3.149
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.85.3.149:800#%F0%9F%87%AF%F0%9F%87%B5%20%5B10-19%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-358-45.85.3.149%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKwgIDI1IiwiYWRkIjoic2hvdWVyLmF6emh1YW5nYXBpbmcudHciLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzBkZTQ5MjQtZDFhYy0zNDgyLWE0OTQtNTc3YjRjY2M5YjFkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hZG9iZSIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeaXpeacrC1zaG91ZXIuYXp6aHVhbmdhcGluZy50dyIsImFkZCI6InNob3Vlci5henpodWFuZ2FwaW5nLnR3IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcwZGU0OTI0LWQxYWMtMzQ4Mi1hNDk0LTU3N2I0Y2NjOWIxZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYWRvYmUiLCJob3N0IjoiYS4xODkuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMTgwMDQiLCJhZGQiOiIzLjM2LjY2LjExMyIsInBvcnQiOiIxNTIzNiIsInR5cGUiOiJub25lIiwiaWQiOiI3NDhhZGJlNy1kZGZkLTQwYTQtYTNlMy03MzY3M2Q4ZTAxODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NjdHYxMy9oZC5tM3U4IiwiaG9zdCI6IjMuMzYuNjYuMTEzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMTgwODUiLCJhZGQiOiIzLjM2LjY2LjExMyIsInBvcnQiOiIxNTIzNiIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjdlODBkMi04MTE1LTQ1OTctOTJlMC1mODVmM2JjOTcyZmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NjdHYxMy9oZC5tM3U4IiwiaG9zdCI6IjMuMzYuNjYuMTEzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDmtZnmsZ/nnIHlj7Dlt57luILnp7vliqggMzAiLCJhZGQiOiJlY2R5ZC0xMDQ5LXYyLTcuaGtnLXIta2NkLWMuYXAuY2poaC5iZWF1dHkiLCJwb3J0IjoiMjk5MzgiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2FhYzYyODUtNTExYy00YTA3LWI2ZGItZWRmYmRjZmUzODg5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsImhvc3QiOiJzMy5jamhoLmJlYXV0eSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDmtZnmsZ/nnIHlj7Dlt57luILnp7vliqggMzAgMiIsImFkZCI6ImVjZHlkLTEwNDktdjItNy5oa2ctci1rY2QtYy5hcC5jamhoLmJlYXV0eSIsInBvcnQiOiIyOTkzOCIsInR5cGUiOiJub25lIiwiaWQiOiJjYWFjNjI4NS01MTFjLTRhMDctYjZkYi1lZGZiZGNmZTM4ODkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2plNXgzcEJOMXZlejNOUXVkTmtCIiwiaG9zdCI6InMzLmNqaGguYmVhdXR5IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgwMDQiLCJhZGQiOiI1NC4xNTEuMTcyLjIwOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzcxMzA3YWMtYjc1OC00NGRlLWE0Y2YtZTMxODlkOTFjZDRjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvamU1eDNwQk4xdmV6M05RdWROa0IiLCJob3N0IjoiczMuY2poaC5iZWF1dHkiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgwMjQiLCJhZGQiOiI1NC4xNTEuMTcyLjIwOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjBhMWUzZDEtOWZiMC00ZjA5LThiYzktYjc1ZWMzMWExODU4IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvamU1eDNwQk4xdmV6M05RdWROa0IiLCJob3N0IjoiczMuY2poaC5iZWF1dHkiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMTgwMDMiLCJhZGQiOiJhenNndHIua2N0cjIwMzguaWN1IiwicG9ydCI6IjU4ODg4IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg4OTM5MjcyLTc5MGEtNDQxZi1iMTJiLThjZTUzMWFjYTgxMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imxpbm9kZXRyMDMua2FvY2hhbmdvbmxpbmUub25saW5lIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTgxNDI4IiwiYWRkIjoiMTcyLjY0LjE1My4yMDEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI4ZGFkNjljLWM5ZDYtNDdjNS1hZDA1LWM2NmFmYjg3Y2NiZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImNsYXNoMy50cnVtcDIwMjMub3JnIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzIuNjQuMTU1LjIwMSIsImFkZCI6IjE3Mi42NC4xNTUuMjAxIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyOGRhZDY5Yy1jOWQ2LTQ3YzUtYWQwNS1jNjZhZmI4N2NjYmQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJjbGFzaDMudHJ1bXAyMDIzLm9yZyIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTAiLCJhZGQiOiIxMzguMi4xNS4yMyIsInBvcnQiOiI0NjM3MCIsInR5cGUiOiJub25lIiwiaWQiOiI5OTgxNTFlNS0wYmM1LTQzNzctZTM5MC1jNDFiYjI2ZmRkMGMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoiY2xhc2gzLnRydW1wMjAyMy5vcmciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxOSIsImFkZCI6IjEzOC4yLjE1LjIzIiwicG9ydCI6IjQ2MzcwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk5ODE1MWU1LTBiYzUtNDM3Ny1lMzkwLWM0MWJiMjZmZGQwYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJjbGFzaDMudHJ1bXAyMDIzLm9yZyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1hemhrdHJhbnNmZXIua2N6ejIwMzgub25saW5lIiwiYWRkIjoiYXpoa3RyYW5zZmVyLmtjenoyMDM4Lm9ubGluZSIsInBvcnQiOiIxMjg5OCIsInR5cGUiOiJub25lIiwiaWQiOiI4ODkzOTI3Mi03OTBhLTQ0MWYtYjEyYi04Y2U1MzFhY2E4MTAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJhenQwNi5rY3RyMjAzOC5pY3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTgxNDI5IiwiYWRkIjoiMTcyLjY0LjE1NS4yMDEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI4ZGFkNjljLWM5ZDYtNDdjNS1hZDA1LWM2NmFmYjg3Y2NiZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImNsYXNoMy50cnVtcDIwMjMub3JnIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTgxNTE1IiwiYWRkIjoiYXpoa3RyYW5zZmVyLmtjenoyMDM4Lm9ubGluZSIsInBvcnQiOiIxMjg5OCIsInR5cGUiOiJub25lIiwiaWQiOiI4ODkzOTI3Mi03OTBhLTQ0MWYtYjEyYi04Y2U1MzFhY2E4MTAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJhenQwNi5rY3RyMjAzOC5pY3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1hemhrdHJhbnNmZXIua2N6ejIwMzgub25saW5lIDIiLCJhZGQiOiJhemhrdHJhbnNmZXIua2N6ejIwMzgub25saW5lIiwicG9ydCI6IjEyODk4IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg4OTM5MjcyLTc5MGEtNDQxZi1iMTJiLThjZTUzMWFjYTgxMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImF6dDA2LmtjdHIyMDM4LmljdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgZ2l0aHViLmNvbS9mcmVlZnEgLSDliqDmi7/lpKcgIDEzIiwiYWRkIjoiMTY1LjE1NC4yNDMuMTYxIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhMTQ0ZGUzOC1hODgxLTRkNDUtODUyYi01OWViNWMzOGY3YTgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYXp0MDYua2N0cjIwMzguaWN1IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgLeWKoOaLv+Wkpy0xNjUuMTU0LjI0My4xNjEiLCJhZGQiOiIxNjUuMTU0LjI0My4xNjEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImExNDRkZTM4LWE4ODEtNGQ0NS04NTJiLTU5ZWI1YzM4ZjdhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhenQwNi5rY3RyMjAzOC5pY3UiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgZ2l0aHViLmNvbS9mcmVlZnEgLSDliqDmi7/lpKcgIDYiLCJhZGQiOiIxNjUuMTU0LjI0My4xNjEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImExNDRkZTM4LWE4ODEtNGQ0NS04NTJiLTU5ZWI1YzM4ZjdhOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhenQwNi5rY3RyMjAzOC5pY3UiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgLeWKoOaLv+Wkpy0xNjUuMTU0LjI0NC44MiIsImFkZCI6IjE2NS4xNTQuMjQ0LjgyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhMTQ0ZGUzOC1hODgxLTRkNDUtODUyYi01OWViNWMzOGY3YTgiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6YgZ2l0aHViLmNvbS9mcmVlZnEgLSDliqDmi7/lpKcgIDkiLCJhZGQiOiIxNjUuMTU0LjI0NC44MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTE0NGRlMzgtYTg4MS00ZDQ1LTg1MmItNTllYjVjMzhmN2E4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%20619
    trojan://88939272-790a-441f-b12b-8ce531aca810@polo01.kctr2038.icu:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6DDOSing%20Network%2019
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMTg4ODMiLCJhZGQiOiIxNzIuNjQuMTU1LjMwIiwicG9ydCI6IjIwNTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGFmYzZjZGYtNGYwYS00NzI1LWE0NGMtNWRhY2RjMmIyNzg0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiaGF4ZXUyLnppa2tjYy5nYSIsInRscyI6InRscyJ9
    trojan://xxoo@138.124.183.216:443?allowInsecure=1#US_138.124.183.216_10187dd0-85%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggQFNTUlNVQi3nvo7lm71WMDMt5LuY6LS55o6o6I2QZGxqLnRmL3NzcnN1YiIsImFkZCI6Ind3dy5kaWdpdGFsb2NlYW4uY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY0NWZjNGU3LWUzYTMtNGU4Mi04YWJkLTJkNzEzMjQ4OTRjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCJob3N0Ijoic3Nyc3ViLnYwMi5hc3VrYS5idXp6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDExIiwiYWRkIjoiMTcyLjY0LjE1My4xMDIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImJlZDNkODc2LTJkMjYtNGQ0ZC1iNzg5LTMwNjM0MzhlZTc3NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNsYXNoMi50cnVtcDIwMjMudXMiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzIuNjQuMTUzLjEwMiIsImFkZCI6IjE3Mi42NC4xNTMuMTAyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJiZWQzZDg3Ni0yZDI2LTRkNGQtYjc4OS0zMDYzNDM4ZWU3NzQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNzIuNjQuMTUzLjEwMiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVM0IiwiYWRkIjoiMjIxLjE4MS4xODUuMTcxIiwicG9ydCI6IjkwMzgiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmNjMTUzMjYtY2QwZi0zNGRhLWJiZmItZjhjZGM5YjcxZWIyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjE3Mi42NC4xNTMuMTAyIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@167.88.63.28:7307#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2049
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.63.28:8090#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2044
    ss://YWVzLTI1Ni1nY206Q1RLOEdYRlFnS1lRRXJyZ2hQSmZaNnRr@209.216.92.212:47121#%F0%9F%87%BA%F0%9F%87%B8%20%5B10-19%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-884-209.216.92.212ss%2F%2FY2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5N09uREVaWUdqYTQ%40178.18.244.2443%23%F0%9F%87%A9%F0%9F%87%AA%20github.com%2Ffreefq%20-%20%E5%BE%B7%E5%9B%BD%20%2012
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1#%E7%99%BD%E5%AB%96-021
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HpvCfh7og5r6z5aSn5Yip5LqaIDAwNiIsImFkZCI6InZtNC5sZWlmZW5na2VqaS5saXZlIiwicG9ydCI6IjExMTExIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc1MmE5NDA0LWM3MjktNDg1ZS04ZWE1LWFjYjNmNGZjODE4MCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InZtNC5sZWlmZW5na2VqaS5saXZlIiwidGxzIjoiIn0=
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=0#%7C61.14Mb
    vmess://eyJ2IjoiMiIsInBzIjoifDQ0LjkwTWIiLCJhZGQiOiIxNTIuNjkuMTk3LjYwIiwicG9ydCI6IjEwNjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiYWFhIDI2OCIsImFkZCI6InNnMDIueGlhb3FpOTkuY2YiLCJwb3J0IjoiNjM2MzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDkxNjY5MjktMDIwZS00ZWYwLTk3ZTctNzk4OWNlOTJmYzY5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoic2cwMi54aWFvcWk5OS5jZiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@167.88.63.79:3306#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2071
    vmess://eyJ2IjoiMiIsInBzIjoifDE5LjI0TWIiLCJhZGQiOiI4LjIxNC4zMy4xNTgiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2I4MWU2YWItMWQ4My00YWMxLWYwYWQtYWU1YzJhN2MyOWVmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://c60fbf90-4b55-11ed-b935-225401db9d57@de.tjvpn.org:443?allowInsecure=1&sni=adjprog.ir#%F0%9F%87%A9%F0%9F%87%AA%20%E5%BE%B7%E5%9B%BD%20003
    trojan://c60fbf90-4b55-11ed-b935-225401db9d57@de.tjvpn.org:443?allowInsecure=1&sni=de.tjvpn.org#%F0%9F%87%AB%F0%9F%87%B7%20%E6%B3%95%E5%9B%BD%28TG%E9%A2%91%E9%81%93%40kxswa%29%203
    trojan://c60fbf90-4b55-11ed-b935-225401db9d57@de.tjvpn.org:443?allowInsecure=1&sni=adjprog.ir#%F0%9F%87%A9%F0%9F%87%AA%20DE%201%20%E2%86%92%20openitsub.com
    trojan://DigitalOcean@digitalocean.kinhproxy.com:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2043
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg54uu5Z+OMnx0Z+mikemBk0ByaXBhb2ppZWRpYW4gMiIsImFkZCI6IjE2NS4xNTQuMjQ0LjI5IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhMTQ0ZGUzOC1hODgxLTRkNDUtODUyYi01OWViNWMzOGY3YTgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6OVh3WXlac0s4U056UUR0WQ@213.183.53.177:9059#213.183.53.1779059
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cg5be06KW/IDAwMiIsImFkZCI6IjE2OC4xMzguMjAxLjIwOCIsInBvcnQiOiIxMDMyOCIsInR5cGUiOiJub25lIiwiaWQiOiJiZjg0N2JmNy0wYmE1LTQ4ODUtYmQyYi1kYTRkNzdhZmJkYTgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6cnBnYk5uVTlyRERVNGFXWg@213.183.53.177:9094#213.183.53.1779094
    trojan://6248895b-4255-4f07-9479-d198bc1eb8db@103.195.236.24:28443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%BB%F0%9F%87%B3%20%E8%B6%8A%E5%8D%97%20001
    trojan://6248895b-4255-4f07-9479-d198bc1eb8db@103.195.236.24:28443?allowInsecure=1&sni=glc.hruqoaw.cn#VN%201%20%E2%86%92%20openitsub.com
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=0#%7C59.07Mb
    vmess://eyJ2IjoiMiIsInBzIjoiXzAyIiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiXzAzIiwiYWRkIjoiMTI4LjEuMTM0LjEyNiIsInBvcnQiOiI2NjY2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdmYjNiNTcxLWNkYTgtNDBmNi1jOWU2LWRiOTc2NWVhOGZhYSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiYWFhIDciLCJhZGQiOiIxMjguMS4xMzQuMTI2IiwicG9ydCI6IjY2NjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiN2ZiM2I1NzEtY2RhOC00MGY2LWM5ZTYtZGI5NzY1ZWE4ZmFhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206V0N1ejd5cmZaU0NRUVhTTnJ0R1B6MkhU@139.28.218.93:50168#%F0%9F%87%AA%F0%9F%87%BA%20%E6%AC%A7%E6%B4%B2%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%20119
    ss://YWVzLTI1Ni1nY206V0N1ejd5cmZaU0NRUVhTTnJ0R1B6MkhU@91.240.243.9:50168#%F0%9F%87%B7%F0%9F%87%BA%20%5B10-19%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-362-91.240.243.9
    ss://YWVzLTI1Ni1nY206cjlRM2FkYzNydTlzZkJEUEVqNHlwNlU2@176.125.231.5:48794#%F0%9F%87%AA%F0%9F%87%BA%20%E6%AC%A7%E6%B4%B2%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2096
    

</details>

### 所有节点
合并节点总数: `4283`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `233`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `139`
- [freefq/free](https://github.com/freefq/free), 节点数量: `24`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4479`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `9`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `25`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `12`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `151`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `172`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `21`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `29`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `79`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `34`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `259`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `216`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `292`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `25`

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
