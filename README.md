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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYXJtLmZpbmV5b28uY2Y0NDMt6KKr5aKZLeS4rei9rDE1Mi43MC44MS42Ni3op6PplIHml6XmnKzlnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImpwYXJtLmZpbmV5b28uY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImJkNWVlMjQ5LWZlN2ItNDY2OS1hNmQ5LWIzZjVlZWNiOThlNiIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImpwYXJtLmZpbmV5b28uY2YiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYXJtLmZpbmV5b28ubWw0NDMt6KKr5aKZLeS4rei9rDEzOC4yLjMzLjkwLeino+mUgeaXpeacrOWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoianBhcm0uZmluZXlvby5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTBiYTQ3OGUtOWRlMS00YWE5LWMwOWUtNzcwNzAyNTMzNGQzIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhcm0uZmluZXlvby5tbCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYW1kLmZpbmV5b28ubWw0NDMt6KKr5aKZLeS4rei9rDEzOC4yLjMzLjEwMi3op6PplIHml6XmnKzlnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImpwYW1kLmZpbmV5b28ubWwiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM1ZTVlMmVhLTEzNzItNDc0NS1kZmY4LWZiMmJkMTEwMTZjNCIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImpwYW1kLmZpbmV5b28ubWwiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUuZ2E0NDMt6KKr5aKZLeS4rei9rDE1Mi42OS4yMjkuMjIyLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoiYW1ka3IucHR1dS5nYSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTYxMmI2N2YtYTc5Yi00YTcxLWE4MmItYTQ2OTA2NzUyMDIzIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii80MDgiLCJob3N0IjoiYW1ka3IucHR1dS5nYSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUubWw0NDMt6KKr5aKZLeS4rei9rDE0Ni41Ni45Ni43NS3op6PplIHpn6nlm73lnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImFtZGtyLnB0dXUubWwiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImUyY2RjMzA1LWRkYTctNDY1ZS1iNjc1LWJhMDQ2OGQyYThiMyIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvOTg3IiwiaG9zdCI6ImFtZGtyLnB0dXUubWwiLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@185.172.113.102:443#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-04%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-4755-185.172.113.102
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjOWRhYTYxNi0zZDY3LTQwNzgtOWZhNS0yOWVmYTRiMzE4ZTI@xjp.paolujichang.com:81#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-04%5D-%F0%9F%87%B8%F0%9F%87%AC-%E6%96%B0%E5%8A%A0%E5%9D%A1-2065-xjp.paolujichang.com
    ss://YWVzLTI1Ni1nY206Tkh3UVRQTENmYVRNU3FUblUzbWpjU3hl@84.17.58.148:443#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-04%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-3970-84.17.58.148
    ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@141.164.39.146:6697#%F0%9F%87%B0%F0%9F%87%B7%20%5B11-04%5D-%F0%9F%87%B0%F0%9F%87%B7-%E9%9F%A9%E5%9B%BD-300-141.164.39.146
    ssr://MTE5LjIzNy4xOTUuMjMwOjU0MzphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhyZkNmaDdBZ0xlbW1tZWE0cnkweE1Ua3VNak0zTGpFNU5TNHlNekEmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPU5UTTVNalE2YUdwbmFuVjVOblEyTlRWcWFtYw
    ssr://MTY4LjcwLjkyLjEyOjQ0MzphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhyZkNmaDdBZ0xlbW1tZWE0cnkweE5qZ3VOekF1T1RJdU1USSZvYmZzcGFyYW09WkVNMWRGcFRPVEpqUnpWdldWaFImcHJvdG9wYXJhbT1OVEV6TmpFNk5qZHRaa2xVYjB3NE5GQnVXbkV3WkE
    ssr://NDIuOTguMjcuMTgzOjU0MzphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhyZkNmaDdBZ0xlbW1tZWE0cnkwME1pNDVPQzR5Tnk0eE9ETSZvYmZzcGFyYW09JnByb3RvcGFyYW09TlRFek5qRTZOamR0WmtsVWIwdzRORkJ1V25Fd1pB
    trojan://3753719b-eb37-4f34-ab60-ae3a70486b27@kr1.api-aws.com:443?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-04%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-1355-kr1.api-aws.com
    trojan://951ca91e-c27c-4b18-bf27-aecf16239524@tgunivstar.219.76.13.180.sslip.io:443?allowInsecure=0#%F0%9F%87%AD%F0%9F%87%B0%20%5B11-04%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-425-tgunivstar.219.76.13.180.sslip.io
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAzN2EucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzdhLnJ1aTc3LmNvbSIsInBvcnQiOiIxMjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ODA2NWMxNC1mYzgwLTQwYjUtYTQ2Yy0wZTM0ZWZkZjgyZmEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzdhLnJ1aTc3LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNzIuMTA1LjIyNC4xNTEiLCJhZGQiOiIxNzIuMTA1LjIyNC4xNTEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry00Ny4yNDMuOTIuMTEiLCJhZGQiOiI0Ny4yNDMuOTIuMTEiLCJwb3J0IjoiMjA5NSIsInR5cGUiOiJub25lIiwiaWQiOiJlOTRjNzA2YS0yMzVmLTQ2NjMtZTIxNC1lZGZhMDUyZjI1NmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJlbHMyMDAuamtsaXN0LmdhIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00Ny43NC41MS4xMjIiLCJhZGQiOiI0Ny43NC41MS4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkxNjQ2ZjlhLWI0ZTktNGFjYS1iZmUzLTg4OTJiM2U1OGZlNyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImxnMzAuY2ZjZG4zLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry02LmRvdWx1b3MuaWN1IiwiYWRkIjoiNi5kb3VsdW9zLmljdSIsInBvcnQiOiI1NDAwNiIsInR5cGUiOiJub25lIiwiaWQiOiJkNzVhZDY4ZC0zYjQxLTNkYzctOTlkNS04M2RiZGQ4NzMwNTYiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiI2LmRvdWx1b3MuaWN1IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcC1iZWkuYmZ5dW4udG9wIiwiYWRkIjoianAtYmVpLmJmeXVuLnRvcCIsInBvcnQiOiIxMDAyMyIsInR5cGUiOiJub25lIiwiaWQiOiI5ZTA1NWFkNS01YjRjLTRiOGQtYmMzOC0wYWNlNDFhYmUyNjciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJqcC1iZWkuYmZ5dW4udG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDA1LXZtMC5lbnRyeS5zcnRoZHcuYXJ0IiwiYWRkIjoianAwNS12bTAuZW50cnkuc3J0aGR3LmFydCIsInBvcnQiOiI0NDQiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2YxMTM4Y2MtNGJiZS0zYjY0LTlkN2YtN2NjNTQ2MzczMzM1IiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAwNS12bTAuZW50cnkuc3J0aGR3LmFydCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDA2LXZtMC5lbnRyeS5yd2VzZGh5dGp1ZnR5aGRhZnNkZ2ZyaC5jbHViIiwiYWRkIjoianAwNi12bTAuZW50cnkucndlc2RoeXRqdWZ0eWhkYWZzZGdmcmguY2x1YiIsInBvcnQiOiI0NDkiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjc5MDZiMjEtODZiMy0zNjQ0LTgwNmYtYTExYzQ4NTM2ZTc1IiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAwNi12bTAuZW50cnkucndlc2RoeXRqdWZ0eWhkYWZzZGdmcmguY2x1YiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDIuc2FuZmVuMDAxLnBpY3MiLCJhZGQiOiJqcDIuc2FuZmVuMDAxLnBpY3MiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjNhOWE0NTg0LWI3NzgtNDVkMi1iNGI5LWZlODRjNGU5MzI2NiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwMi5zYW5mZW4wMDEucGljcyIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZy1vdmgyLnYyLXJheS5jb20iLCJhZGQiOiJzZy1vdmgyLnYyLXJheS5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGNlNGM0NzItNmYzZi00YzQ1LTgwZTUtY2JmZTVlY2FkN2VlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoic2ctb3ZoMi52Mi1yYXkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1saS5iaWcyMzQuY29tIiwiYWRkIjoibGkuYmlnMjM0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjEzZTc4M2EtMjA3NC00YWVmLWI2ZDktMmFjNmQ0ZDBkYzA0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoibGkuYmlnMjM0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzEtMi5iZnl1bi50b3AiLCJhZGQiOiJzZzEtMi5iZnl1bi50b3AiLCJwb3J0IjoiMTAwMjEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzY2YWRhZWMtY2RkZi00Y2I1LTk4Y2EtYTQ3ZDE3MzkxOGFlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoic2cxLTIuYmZ5dW4udG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry12MjEuaWRjbG91ZGhvc3QuZGUiLCJhZGQiOiJ2MjEuaWRjbG91ZGhvc3QuZGUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjMwMDc5MDMtZjE4Ny00ZjEzLWJlNjctNjYyOTAzYTg2MWI1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjIxLmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAyOGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMjhhLnJ1aTc3LmNvbSIsInBvcnQiOiI1MjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ODA2NWMxNC1mYzgwLTQwYjUtYTQ2Yy0wZTM0ZWZkZjgyZmEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidjIxLmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAzNGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzRhLnJ1aTc3LmNvbSIsInBvcnQiOiIxMjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiJhNzJlNzkwZi1lMThhLTQzYjAtYTdhNy1iY2MzM2YxNDQwOTIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidjIxLmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xMzkuMTYyLjExOS44MSIsImFkZCI6IjEzOS4xNjIuMTE5LjgxIiwicG9ydCI6IjI3NDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY3MmVlNThmLTc4YmYtNGI2MS04NDQyLTdiOWNjYTkxMmIxNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEzOS4xNjIuMTE5LjgxIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00NS43Ny4xODMuMTExIiwiYWRkIjoiNDUuNzcuMTgzLjExMSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiIwMGE3OTUyMC01MzgwLTQwYWMtODdlMS00OTlmNWE2ZWIyMWQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJWaXBtYWhzYSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00Ny43NC40My4xNTgiLCJhZGQiOiI0Ny43NC40My4xNTgiLCJwb3J0IjoiMjA1MyIsInR5cGUiOiJub25lIiwiaWQiOiJiZjY3NDM3ZS02YzkwLTQ1Y2EtYWJjMi1jNzI0MGE1Y2UyYWEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJmb3h1ay5mb3ZpLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1rci5pZGNsb3VkaG9zdC5kZSIsImFkZCI6ImtyLmlkY2xvdWRob3N0LmRlIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjIzMDA3OTAzLWYxODctNGYxMy1iZTY3LTY2MjkwM2E4NjFiNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImtyLmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC12MjYuaWRjbG91ZGhvc3QuZGUiLCJhZGQiOiJ2MjYuaWRjbG91ZGhvc3QuZGUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjMwMDc5MDMtZjE4Ny00ZjEzLWJlNjctNjYyOTAzYTg2MWI1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjI2LmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDAzLXZtMC5lbnRyeS5zcnRoZHcuYXJ0IiwiYWRkIjoianAwMy12bTAuZW50cnkuc3J0aGR3LmFydCIsInBvcnQiOiI0NDQiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2YxMTM4Y2MtNGJiZS0zYjY0LTlkN2YtN2NjNTQ2MzczMzM1IiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAwMy12bTAuZW50cnkuc3J0aGR3LmFydCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0xMjguMTk5LjIwMi44MCIsImFkZCI6IjEyOC4xOTkuMjAyLjgwIiwicG9ydCI6IjE1OTg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjVmN2U4MGQyLTgxMTUtNDU5Ny05MmUwLWY4NWYzYmM5NzJmZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyOC4xOTkuMjAyLjgwIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS01NC4xNzkuOTguMjIyIiwiYWRkIjoiNTQuMTc5Ljk4LjIyMiIsInBvcnQiOiI0NTEyMyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjdlODBkMi04MTE1LTQ1OTctOTJlMC1mODVmM2JjOTcyZmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiI1NC4xNzkuOTguMjIyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZy5pZGNsb3VkaG9zdC5kZSIsImFkZCI6InNnLmlkY2xvdWRob3N0LmRlIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjIzMDA3OTAzLWYxODctNGYxMy1iZTY3LTY2MjkwM2E4NjFiNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InNnLmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzIuc2FuZmVuMDAxLnBpY3MiLCJhZGQiOiJzZzIuc2FuZmVuMDAxLnBpY3MiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjA1MzgzMDIyLTU5NGEtNDRlYS1hMTllLWM5NzJmNGExNTQ5MiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5taWNyb3NvZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS12MzkuaWRjbG91ZGhvc3QuZGUiLCJhZGQiOiJ2MzkuaWRjbG91ZGhvc3QuZGUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjMwMDc5MDMtZjE4Ny00ZjEzLWJlNjctNjYyOTAzYTg2MWI1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjM5LmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vi0yMTEuNzIuMzUuMTE5IiwiYWRkIjoiMjExLjcyLjM1LjExOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmZmZmZmZmYtZmZmZi1mZmZmLWZmZmYtZmZmZmZmZmZmZmZmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiY3J1ZGUtZnJhbmtsaW4tZmF2b3JzLW91dHNvdXJjaW5nLnRyeWNsb3VkZmxhcmUuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi10dzEubXliZXN0amouY29tIiwiYWRkIjoidHcxLm15YmVzdGpqLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI0NTJhODgtMDhhMC00YTZhLWFjODctOTM3YmIwYjI3OTA5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidHcxLm15YmVzdGpqLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWNl+aKleWOvy12aXAyMS13cy10bHMuanNzc2xpbmUudG9wIiwiYWRkIjoidmlwMjEtd3MtdGxzLmpzc3NsaW5lLnRvcCIsInBvcnQiOiI0MzQwMyIsInR5cGUiOiJub25lIiwiaWQiOiI2NzMwM2VmYS1hYmRlLTgwMDQtMzM4ZS0yMGQ4MGIwM2E3NDkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2aXAyMS13cy10bHMuanNzc2xpbmUudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuahg+WbreW4gi10dzAxLmhlbmV0LnRvcCIsImFkZCI6InR3MDEuaGVuZXQudG9wIiwicG9ydCI6IjIwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3YjUzOTJhLTAzYTItNDgzZi05ZDUxLTg5ZmYxYWE2YzE5ZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiU3QiUyMkhvc3QlMjI6JTIyY2N0di5jb20lMjIlN0QiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1nY206ZTRGQ1dyZ3BramkzUVk@38.75.136.102:9101#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-04%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-5245-38.75.136.102
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@38.75.137.9:8080#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-04%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-330-38.75.137.9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYXJtLmZpbmV5b28uY2Y0NDMt6KKr5aKZLeS4rei9rDE1Mi43MC44MS42Ni3op6PplIHml6XmnKzlnLDljLpORumdnuiHquWItuWJpyAyIiwiYWRkIjoianBhcm0uZmluZXlvby5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmQ1ZWUyNDktZmU3Yi00NjY5LWE2ZDktYjNmNWVlY2I5OGU2IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhcm0uZmluZXlvby5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUubWw0NDMt6KKr5aKZLeS4rei9rDE0Ni41Ni45Ni43NS3op6PplIHpn6nlm73lnLDljLpORumdnuiHquWItuWJpyAyIiwiYWRkIjoiYW1ka3IucHR1dS5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTJjZGMzMDUtZGRhNy00NjVlLWI2NzUtYmEwNDY4ZDJhOGIzIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii85ODciLCJob3N0IjoiYW1ka3IucHR1dS5tbCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUuZ2E0NDMt6KKr5aKZLeS4rei9rDE1Mi42OS4yMjkuMjIyLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDIiLCJhZGQiOiJhbWRrci5wdHV1LmdhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhNjEyYjY3Zi1hNzliLTRhNzEtYTgyYi1hNDY5MDY3NTIwMjMiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiLzQwOCIsImhvc3QiOiJhbWRrci5wdHV1LmdhIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.101.159:7002#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-04%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-2005-38.91.101.159
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYW1kLmZpbmV5b28ubWw0NDMt6KKr5aKZLeS4rei9rDEzOC4yLjMzLjEwMi3op6PplIHml6XmnKzlnLDljLpORumdnuiHquWItuWJpyAyIiwiYWRkIjoianBhbWQuZmluZXlvby5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzVlNWUyZWEtMTM3Mi00NzQ1LWRmZjgtZmIyYmQxMTAxNmM0IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhbWQuZmluZXlvby5tbCIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.91.106.51:443#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-04%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-2665-38.91.106.51
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug576O5Zu9LXZtZXNzLWpwYXJtLmZpbmV5b28ubWw0NDMt6KKr5aKZLeS4rei9rDEzOC4yLjMzLjkwLeino+mUgeaXpeacrOWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDIiLCJhZGQiOiJqcGFybS5maW5leW9vLm1sIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIxMGJhNDc4ZS05ZGUxLTRhYTktYzA5ZS03NzA3MDI1MzM0ZDMiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiLzEyMyIsImhvc3QiOiJqcGFybS5maW5leW9vLm1sIiwidGxzIjoidGxzIn0=
    trojan://2b2b1b4f-3372-47f7-9f90-26097c7683f9@sg.liangyuandian.top:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%201
    ssr://MTY1LjE1NC4yMjUuOTQ6NDEwMDI6YXV0aF9hZXMxMjhfc2hhMTpjaGFjaGEyMC1pZXRmOnRsczEuMl90aWNrZXRfYXV0aDplVkJMY21WNFdHRldUVUZZUm1abGVnLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcVBDZmg2WWdMZVdLb09hTHYtV2tweTB4TmpVdU1UVTBMakl5TlM0NU5BJm9iZnNwYXJhbT1NR1ZqTlRReU9EQTROQzVrYjNkdWJHOWhaQzUzYVc1a2IzZHpkWEJrWVhSbExtTnZKU1h2djcwJnByb3RvcGFyYW09TWpnd09EUTZhMlkwTjFobQ
    ss://YWVzLTI1Ni1jZmI6Y2Ruc3NyLnNzcnN1Yi5jb20@cdnssr.ssrsub.com:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-cdnssr.ssrsub.com
    ss://YWVzLTI1Ni1jZmI6Y2Ruc3NyLnNzcnN1Yi5jb20@cdnssr.ssrsub.com:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-cdnssr.ssrsub.com%202
    trojan://41b87c2c-7dce-3a3d-85e7-9c00b5bea867@azhj001.xibai6.top:20714?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-04%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-660-azhj001.xibai6.top
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzIuNjcuMjM2Ljc0IiwiYWRkIjoiMTcyLjY3LjIzNi43NCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2JhYWFkMGYtYjc2NC00ZjRlLWQzODItY2RkMTA0MzkwODM4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmFvb3AxOTk0LmV1Lm9yZyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yNy43MmltZy54eXoiLCJhZGQiOiIyNy43MmltZy54eXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjgxZDkzZjYyLTE1YTItNDk5NC1hZGI5LTBiNWQ5MDZhYWM3ZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjI3LjcyaW1nLnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwOGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDhhLnJ1aTc3LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTcyZTc5MGYtZTE4YS00M2IwLWE3YTctYmNjMzNmMTQ0MDkyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjI3LjcyaW1nLnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA0MGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNDBhLnJ1aTc3LmNvbSIsInBvcnQiOiIxMjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ODA2NWMxNC1mYzgwLTQwYjUtYTQ2Yy0wZTM0ZWZkZjgyZmEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMjcuNzJpbWcueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTguMjguMTkiLCJhZGQiOiIxMDQuMTguMjguMTkiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzU1NTY4NjMtMjJiOS00MGI5LTg3MjItYTE5MmI4NTI2ZWRjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZnIxLmNhY2hleHkuZ2EiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzAuMTg3LjE5Ni4xMjgiLCJhZGQiOiIxNzAuMTg3LjE5Ni4xMjgiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xODUuMTQzLjIzMy4xMjAiLCJhZGQiOiIxODUuMTQzLjIzMy4xMjAiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzVkMjU4OTktZWQyMC00NmQ5LTljN2MtOTljMGQ0MTRkNWU0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMDkuMTQxLjQ3Ljk4IiwiYWRkIjoiMjA5LjE0MS40Ny45OCIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiI1Zjc5ZjNmNC02YzAwLTRkYTctOThkMC03NDNkNWQ3NTE1ZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIyMDkuMTQxLjQ3Ljk4IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMC4yMDUuNTcuMTc0IiwiYWRkIjoiMjAuMjA1LjU3LjE3NCIsInBvcnQiOiI0ODAwNyIsInR5cGUiOiJub25lIiwiaWQiOiI4NjY3YzQzOS0xMmI5LTNhOGYtYjdkOC00ZGQ3OWY0NjkxMjEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMTciLCJhZGQiOiIxMDMuODMuMTU2Ljg5IiwicG9ydCI6Ijg4ODgiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWU3NDg2ZjktZDdiNy00ZjI2LTk3YTAtZGM1YjA5M2RmYTg5IiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTAzLjgzLjE1Ni44OSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMTEiLCJhZGQiOiJiYW40LmZlaWNsb3VkZGQubWUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZkYTQzMWU0LWQ3YjEtNGY2MS1iM2UyLWYzZjhkNmYwM2JiOCIsImFpZCI6IjYwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NkYWZhc2ZzYSIsImhvc3QiOiJiYW40LmZlaWNsb3VkZGQubWUiLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@185.104.184.78:443#%F0%9F%87%A9%F0%9F%87%AA%20%5B11-04%5D-%F0%9F%87%A9%F0%9F%87%AA-%E5%BE%B7%E5%9B%BD-4725-185.104.184.78
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@37.120.147.230:443#%F0%9F%87%B7%F0%9F%87%B4%20%5B11-04%5D-%F0%9F%87%B7%F0%9F%87%B4-%E7%BD%97%E9%A9%AC%E5%B0%BC%E4%BA%9A-3670-37.120.147.230
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMTAiLCJhZGQiOiJ1bml2c3Rhci41MS4xOTUuMTQwLjIwOC5zc2xpcC5pbyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTcyMTI2ZjgtNTMwMS04M2MyLTBhMjYtYzMwY2VkM2RiN2M0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93bXptdndzIiwiaG9zdCI6InVuaXZzdGFyLjUxLjE5NS4xNDAuMjA4LnNzbGlwLmlvIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDkiLCJhZGQiOiJqcDQubWF5YWEuY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjFkM2Q3M2YzLTI0M2MtNGI0OC1iMGI5LWI2OTkzMTRhNTkwYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwNC5tYXlhYS5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDgiLCJhZGQiOiIxMDQuMTkuNDUuMTE3IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIzYjVlMjU4ZS04YzVlLTQ1ZDMtYjdkMi0wMmM4ZjVmYzBiYjIiLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTA0LjE5LjQ1LjExNyIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMTIiLCJhZGQiOiJqcGF3cy5odWFyZW5saWZlLnRvcCIsInBvcnQiOiI4ODg4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImFlNzQ4NmY5LWQ3YjctNGYyNi05N2EwLWRjNWIwOTNkZmE4OSIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwYXdzLmh1YXJlbmxpZmUudG9wIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ@167.88.61.119:443#%F0%9F%87%B8%F0%9F%87%AA%20%5B11-04%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-3565-167.88.61.119
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDYiLCJhZGQiOiI5Ni40My45MS42MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2JmYjQzZTItN2RmZS00NzU3LTg2ZWUtMWNlOWZiOWZkMTNhIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8zMTA5MTAyMTE5MTYiLCJob3N0IjoiOTYuNDMuOTEuNjAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDQiLCJhZGQiOiJtamozMDA2LmhqZG4udGsiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjcxZTg3YWVjLTE1NjktNGYwYS1jMmMyLTc3MTc2YjY2ZjBiYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Im1qajMwMDYuaGpkbi50ayIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDIiLCJhZGQiOiIxNzIuNjcuMTc4LjU1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwMTQ1YmZlZi1hYTUzLTQxNmYtOTBkNC04NjM0Mjk1ZGFiNTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNzIuNjcuMTc4LjU1IiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@85.208.108.18:8090#%F0%9F%87%B8%F0%9F%87%A6%20%5B11-04%5D-%F0%9F%87%A6%F0%9F%87%B6-%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AF-755-85.208.108.18
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAxMDEiLCJhZGQiOiIxMDQuMTkuMzYuMTYwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhZDgwNjQ4Ny0yZDI2LTQ2MzYtOThiNi1hYjg1Y2M4NTIxZjciLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTA0LjE5LjM2LjE2MCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA5OCIsImFkZCI6IjEwNC4xOS4xMTAuMzQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRjZGIwMTZmLWYxNGUtMzBiMy05N2Q2LTQ1M2M3NDFhNWM4MCIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIveTQ3NSIsImhvc3QiOiIxMDQuMTkuMTEwLjM0IiwidGxzIjoidGxzIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpwcnloeXh5YQ@52.58.249.78:57824#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2094
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA5MyIsImFkZCI6IjUxLjc5LjE2NC4xNDYiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmVmNjRkYzgtY2EzYy00NWI4LWFkNWYtMjA4NzE0NTIxNDNiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNTEuNzkuMTY0LjE0NiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpIR0JkT0tkY0llcjU@167.99.192.30:3567#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2092
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpaM1lTMEt4Qjh1NWpncDczNmU4MzR5M0RhWHdTT1l6eGxGREZxcE5DYWFsREE5Q0VJUmNlWk9DQW5SMnlUUw@154.17.1.251:18334#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2090
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA4OSIsImFkZCI6ImNmLjczMTgwOC50ayIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDJiYjZlYzEtODZkZi00M2VmLWE5M2ItNzBhOTgxZjhmZDNmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9tbHltdndzIiwiaG9zdCI6ImNmLjczMTgwOC50ayIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA4OCIsImFkZCI6IjEwNy4xNzUuNDQuMTU0IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIxMTRmNTc4Ni1hOGEwLTQ0NmEtYTMyZi00NDY4OTM0ODA1NjAiLCJhaWQiOiIxMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8yNzM1MzQ4NmYzYTFkNGYvIiwiaG9zdCI6IjEwNy4xNzUuNDQuMTU0IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA4MyIsImFkZCI6IjE3Mi42Ny42NS4xNjYiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM4YmE5N2I4LTNhZDUtNDkxYy1jMzVjLTU4NDUxZDViMDhkMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjE3Mi42Ny42NS4xNjYiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA4MiIsImFkZCI6Ijg1LjExNy4yMzQuMTg0IiwicG9ydCI6IjE5MzAzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMzODA2YWJmLWFmYWYtNGVkMS04ZjdlLTQxYTdlY2RiYjRlMyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIxNzIuNjcuNjUuMTY2IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpaM1lTMEt4Qjh1NWpncDczNmU4MzR5M0RhWHdTT1l6eGxGREZxcE5DYWFsREE5Q0VJUmNlWk9DQW5SMnlUUw@154.17.5.184:18331#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2081
    

</details>

### 所有节点
合并节点总数: `2338`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `104`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `139`
- [freefq/free](https://github.com/freefq/free), 节点数量: `20`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `213`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3206`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `18`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `77`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `21`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `44`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `298`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `74`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `20`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `25`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `33`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `22`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `238`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `230`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `292`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `17`

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
