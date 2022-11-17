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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzExMTcwNjQiLCJhZGQiOiIxNDAuODMuNTcuODAiLCJwb3J0IjoiNDk4NDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjk2OWFkMWItOTc4Ny00OTI3LTk0ZTYtMjJmNTk3NjE4ZGUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTcwNDQiLCJhZGQiOiJsaS5iaWcyMzQuY29tIiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjEzZTc4M2EtMjA3NC00YWVmLWI2ZDktMmFjNmQ0ZDBkYzA0IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImxpLmJpZzIzNC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTcwNjYiLCJhZGQiOiIxOC4xNDMuMTIzLjM1IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY4ZGY0ODM4LTQ2ZDAtNGI1Yi1jM2YwLWE0MGVjNzA2MzI0NSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTc1MzgiLCJhZGQiOiI4LjIxOS4xNzUuMjQiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzY3NDdkYTQtZmIyZS00YTJhLWJkYjctODYxNGJkZDZiMGIzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zc2hraXQvMTczNjk2MDExMS82MzVjYjZkZDQyMDZjLyIsImhvc3QiOiJzZzMtdjJyYXkuc3Noa2l0Lm9yZyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTc1MzYiLCJhZGQiOiI4LjIxOS4xNzEuMTE0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM2NzQ3ZGE0LWZiMmUtNGEyYS1iZGI3LTg2MTRiZGQ2YjBiMyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Noa2l0LzE3MzY5NjAxMTEvNjM1Y2I2ZGQ0MjA2Yy8iLCJob3N0Ijoic2czLXYycmF5LnNzaGtpdC5vcmciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTc1MzciLCJhZGQiOiI4LjIxOS4yMjguMTIxIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM2NzQ3ZGE0LWZiMmUtNGEyYS1iZGI3LTg2MTRiZGQ2YjBiMyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Noa2l0LzE3MzY5NjAxMTEvNjM1Y2I2ZGQ0MjA2Yy8iLCJob3N0Ijoic2czLXYycmF5LnNzaGtpdC5vcmciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTc1NDAiLCJhZGQiOiI4LjIxOS41Ni4xMiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJjNjc0N2RhNC1mYjJlLTRhMmEtYmRiNy04NjE0YmRkNmIwYjMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaGtpdC8xNzM2OTYwMTExLzYzNWNiNmRkNDIwNmMvIiwiaG9zdCI6InNnMy12MnJheS5zc2hraXQub3JnIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMTc1NTYiLCJhZGQiOiI4LjIxOS4xMTcuMjYiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzY3NDdkYTQtZmIyZS00YTJhLWJkYjctODYxNGJkZDZiMGIzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zc2hraXQvMTczNjk2MDExMS82MzVjYjZkZDQyMDZjLyIsImhvc3QiOiJzZzMtdjJyYXkuc3Noa2l0Lm9yZyIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@5.183.176.84:803#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-17%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-372-5.183.176.84
    trojan://2ce84336-46b2-4c8c-ad29-239aacca8343@jp.838501.xyz:15001?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-17%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-1986-jp.838501.xyz
    trojan://4bacb8f1a089763b@211.72.35.157:3306?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%B3%20%5B11-17%5D-%F0%9F%87%B9%F0%9F%87%BC-%E5%8F%B0%E6%B9%BE-11052-211.72.35.157
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi10dzk5LWhpbmV0Lm15bjFkZXMuY29tIiwiYWRkIjoidHc5OS1oaW5ldC5teW4xZGVzLmNvbSIsInBvcnQiOiIyMDk2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjUzMWU2YzRiLTJmNWYtMzYzZi04NTU2LTM1MzFiODU0MjJkNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InR3OTktaGluZXQubXluMWRlcy5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM2EucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDNhLnJ1aTc3LmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmM2ZkYTBjNi00MDI1LTRkYTctODJiNC04ODQyM2Q5ZWM0ODkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidHc5OS1oaW5ldC5teW4xZGVzLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xMDQuMjA4LjEwMy4xMjYiLCJhZGQiOiIxMDQuMjA4LjEwMy4xMjYiLCJwb3J0IjoiNDUwMDciLCJ0eXBlIjoibm9uZSIsImlkIjoiNjljZGYxZTItZmIxNC00NmY0LWI3OTEtMjU3NzViNDJjMTIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InR3OTktaGluZXQubXluMWRlcy5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xMS5kb3VsdW9zLmljdSIsImFkZCI6IjExLmRvdWx1b3MuaWN1IiwicG9ydCI6IjUxMDExIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ3NmZjZmEyLTM2MzItMzlkZC1iZTE0LThhYjViN2QzY2EyYiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ0dzk5LWhpbmV0Lm15bjFkZXMuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOWMl+W4gi0xMTEuMjQxLjEyNy4xOTgiLCJhZGQiOiIxMTEuMjQxLjEyNy4xOTgiLCJwb3J0IjoiMzk5OTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjdjNTBmNmEtODE2ZC0zNTU1LTg5YjQtMTlkZDI5NjA4ZjhiIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InR3OTktaGluZXQubXluMWRlcy5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xMzkuMTYyLjEyMS4xMjciLCJhZGQiOiIxMzkuMTYyLjEyMS4xMjciLCJwb3J0IjoiMjA1MyIsInR5cGUiOiJub25lIiwiaWQiOiIzMjc1NjhmNC1jZTIwLTRhM2UtOWI2MS1kZjNiNTEyNGE5OTYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidHc5OS1oaW5ldC5teW4xZGVzLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNzIuMTA0LjkxLjEwMyIsImFkZCI6IjE3Mi4xMDQuOTEuMTAzIiwicG9ydCI6IjIwNTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTNkMDc1ZjctOTA5Zi00Yzk3LTkwZTMtYTgzNzI0YTc1NTFlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InR3OTktaGluZXQubXluMWRlcy5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuiKseiOsuWOvy0zNi4yMjcuMjIyLjE3NSIsImFkZCI6IjM2LjIyNy4yMjIuMTc1IiwicG9ydCI6IjM5OTk5IiwidHlwZSI6Im5vbmUiLCJpZCI6IjY3YzUwZjZhLTgxNmQtMzU1NS04OWI0LTE5ZGQyOTYwOGY4YiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ0dzk5LWhpbmV0Lm15bjFkZXMuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry02ZjBlY2Q5Yi03YzBmLWNiYjktZDFiNC02MGIwZDBmYjNhM2UuY25uaWMucmlwIiwiYWRkIjoiNmYwZWNkOWItN2MwZi1jYmI5LWQxYjQtNjBiMGQwZmIzYTNlLmNubmljLnJpcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmOTQxNTE0NS1lODAwLTRjNjMtYTYyZS03NjIzODQ4NDk2YzkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiI2ZjBlY2Q5Yi03YzBmLWNiYjktZDFiNC02MGIwZDBmYjNhM2UuY25uaWMucmlwIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry04LmRvdWx1b3MuaWN1IiwiYWRkIjoiOC5kb3VsdW9zLmljdSIsInBvcnQiOiI0MzAwOCIsInR5cGUiOiJub25lIiwiaWQiOiI1MWIwNWFhZS05Y2Y2LTM4OTktYTgxOC0zYjJmYTdkZjNkNjEiLCJhaWQiOiIyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiNmYwZWNkOWItN2MwZi1jYmI5LWQxYjQtNjBiMGQwZmIzYTNlLmNubmljLnJpcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOWMl+W4gi1jYS54bGtqanMudG9wIiwiYWRkIjoiY2EueGxrampzLnRvcCIsInBvcnQiOiIxNTI2OCIsInR5cGUiOiJub25lIiwiaWQiOiIwYTZiNzIyNi0yZjljLTM5M2MtYmM5NC01YTM0ODU5MjUwYzAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJjYS54bGtqanMudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDIuY3pzMTAwMC5jb20iLCJhZGQiOiJqcDIuY3pzMTAwMC5jb20iLCJwb3J0IjoiNTU4OSIsInR5cGUiOiJub25lIiwiaWQiOiJmMGYzOThiYy1lODE4LTQyMzYtYjI3MS03OGE4Y2Q4OTczYjQiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiY2EueGxrampzLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzMuY3pzMTAwMC5jb20iLCJhZGQiOiJzZzMuY3pzMTAwMC5jb20iLCJwb3J0IjoiODg4MyIsInR5cGUiOiJub25lIiwiaWQiOiJmMGYzOThiYy1lODE4LTQyMzYtYjI3MS03OGE4Y2Q4OTczYjQiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiY2EueGxrampzLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1wYW9wYW8udjIuanAwNS5wYW9wYW9jbG91ZC5jeW91IiwiYWRkIjoicGFvcGFvLnYyLmpwMDUucGFvcGFvY2xvdWQuY3lvdSIsInBvcnQiOiIzMzA3IiwidHlwZSI6Im5vbmUiLCJpZCI6IjE1YzFhYTQwLTYzODItMzkzZS05NWI0LTc1NDlkNzVhMjI0NiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwMDUuc3NydTQuZnVuIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuW9sOWMluWOvy10dy54bGtqanMudG9wIiwiYWRkIjoidHcueGxrampzLnRvcCIsInBvcnQiOiIxMTEyNCIsInR5cGUiOiJub25lIiwiaWQiOiIwYTZiNzIyNi0yZjljLTM5M2MtYmM5NC01YTM0ODU5MjUwYzAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ0dy54bGtqanMudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1rcjYuZWxrbm9kZS50b3AiLCJhZGQiOiJrcjYuZWxrbm9kZS50b3AiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMWVkZWQ2ZmMtOGIyOC0zM2RmLWE5M2YtNjQ5MWRlNWY3YTEyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoia3I2LmVsa25vZGUudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1rci1kaXJlY3Qubm9kZTAwMi54eXoiLCJhZGQiOiJrci1kaXJlY3Qubm9kZTAwMi54eXoiLCJwb3J0IjoiNTQzMiIsInR5cGUiOiJub25lIiwiaWQiOiI1MzFlNmM0Yi0yZjVmLTM2M2YtODU1Ni0zNTMxYjg1NDIyZDUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoia3I2LmVsa25vZGUudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOWMl+W4gi0yMTEtMjAtMjU1LTEwNS5uaG9zdC4wMGNkbi5jb20iLCJhZGQiOiIyMTEtMjAtMjU1LTEwNS5uaG9zdC4wMGNkbi5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk2OTgzZWI0LWM4ZjEtMzE2ZS1hYjAwLTUwMDAxNGVkM2Q4YiIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imtic2VydmljZS5jbHViIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOWMl+W4gi0yMTEtMjAtMjU1LTEwNi5uaG9zdC4wMGNkbi5jb20iLCJhZGQiOiIyMTEtMjAtMjU1LTEwNi5uaG9zdC4wMGNkbi5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk2OTgzZWI0LWM4ZjEtMzE2ZS1hYjAwLTUwMDAxNGVkM2Q4YiIsImFpZCI6IjEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imtic2VydmljZS5jbHViIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xLmV6eWRmZGQuY29tIiwiYWRkIjoiMS5lenlkZmRkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGVlNDhhZDgtMTc4Yy00MGEyLTljNTItYTE0ZTkwYTA2ZTQ5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMS5lenlkZmRkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xMDQuMjA4LjExNS4yNTIiLCJhZGQiOiIxMDQuMjA4LjExNS4yNTIiLCJwb3J0IjoiMzEwMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZDAyYzU3OTAtMDRlNS00MzdlLThiNTUtMmNmYWQ0ZGFiYTE4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xMy43NS41Mi43NCIsImFkZCI6IjEzLjc1LjUyLjc0IiwicG9ydCI6IjI0MzI1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjU5OWE1MGY1LWUzMGQtNDkzZS1iZTFmLTBmOGZmYjJiNTEyMyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oay5tYXlpeXVuLnNob3AiLCJhZGQiOiJoay5tYXlpeXVuLnNob3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImUwOTNiMmEyLWE4ZjMtNGZjYS1iZmU5LTAwNTgzMzg3ZTc2NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImEuMTg5LmNuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oazAzLndic3RzLnRvcCIsImFkZCI6ImhrMDMud2JzdHMudG9wIiwicG9ydCI6Ijk2ODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWY1ZGNmZGEtYTNkOS00YTJiLWJkZmUtMzIyYWUyZjY5NmYxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiaGswMy53YnN0cy50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oazA2Lndic3RzLnRvcCIsImFkZCI6ImhrMDYud2JzdHMudG9wIiwicG9ydCI6Ijk2ODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWY1ZGNmZGEtYTNkOS00YTJiLWJkZmUtMzIyYWUyZjY5NmYxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiaGswNi53YnN0cy50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNDYuNTYuMTY2LjE1MyIsImFkZCI6IjE0Ni41Ni4xNjYuMTUzIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJjbGFzaDYuc3NyLWZyZWUueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0zLjExMi4yMS4xMDIiLCJhZGQiOiIzLjExMi4yMS4xMDIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmZmZmZmZmLWZmZmYtZmZmZi1mZmZmLWZmZmZmZmZmZmZmZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNydWRlLWZyYW5rbGluLWZhdm9ycy1vdXRzb3VyY2luZy50cnljbG91ZGZsYXJlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00Ny43NC41MS4zMCIsImFkZCI6IjQ3Ljc0LjUxLjMwIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU3ZTBjYjRkLWVhZTUtNDhlYy04MDkxLTE0OWRjMmIzMDllMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImludHJlcGlkLm1vc3MubmV0d29yayIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDQuZWxrbm9kZS50b3AiLCJhZGQiOiJqcDQuZWxrbm9kZS50b3AiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMWVkZWQ2ZmMtOGIyOC0zM2RmLWE5M2YtNjQ5MWRlNWY3YTEyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZGF0YS52aWRlby5xaXlpLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcC5tYXlpeXVuLnNob3AiLCJhZGQiOiJqcC5tYXlpeXVuLnNob3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImUwOTNiMmEyLWE4ZjMtNGZjYS1iZmU5LTAwNTgzMzg3ZTc2NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImEuMTg5LmNuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrOS4nOS6rC0xNDEuMTQ3LjE4MS4yMTkiLCJhZGQiOiIxNDEuMTQ3LjE4MS4yMTkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjBiODczY2ZmLTExYWItNDcxNi1jNDFhLTA0Zjg4NjEzNTA5MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS1odWNsb3Vkcy5tbCIsImFkZCI6Imh1Y2xvdWRzLm1sIiwicG9ydCI6IjU1MDUiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjk4MDE1MzQtMzg3MC00ZDE0LTlkMDctNmY2NWRhNTkzZGE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiaHVjbG91ZHMubWwiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbveWPsOa5vihUVylUYWl3YW4vQ2l0eU9mZmljZV8yIiwiYWRkIjoiNjEuMjIyLjIwMi4xNDAiLCJwb3J0IjoiMzM3OTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTU1Y2QxODItMDFiMC00ZmI3LWE1MTAtMzYzNzAxYTQ5MWM1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1nY206Q1VuZFNabllzUEtjdTZLajhUSFZNQkhE@64.44.42.196:39772#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2029
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-8796-199.115.228.30
    ss://YWVzLTI1Ni1nY206d3JDYUd0clViemVScVFMZGM4S21rM05k@156.146.33.66:49126#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2026
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIDI1IiwiYWRkIjoiMTQzLjE5OC4yMzcuMjE0IiwicG9ydCI6IjI3NDg5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ3M2YwMjdiLTlhMzctNGU3OS1kZDI5LTNhMGQxZTFkYTEyOCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIDIzIiwiYWRkIjoiMTk4LjQxLjIxMi4yMzQiLCJwb3J0IjoiMjA1MiIsInR5cGUiOiJub25lIiwiaWQiOiIwMDAwMDAwMC0xMTExLTIyMjItMzMzMy00NDQ0NDQ0NDQ0NDQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL1RlbGVncmFtL0BMb3NzXzBfVm1lc3MiLCJob3N0IjoiZnJlZS5qaWFuZ3VveXVuLmNvbSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206NGVqSjhuNWRkTHVZRFVIR1hKcmUydWZK@172.93.153.148:48938#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2021
    ss://YWVzLTI1Ni1nY206cjZoRHJrUDRFdDZFRU5UUzhReTdUY21n@198.8.92.84:44539#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2020
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIDE5IiwiYWRkIjoiMTA0LjI2LjkuNzQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY2YzFiYWJlLTQxNmUtNDdkMS04NzI2LTA0OTY3OGUyNWM3YSIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaG9jZWFuIiwiaG9zdCI6InVzMi52MnJheXNlcnYuY29tIiwidGxzIjoidGxzIn0=
    ssr://MTY1LjE1NC4yMjUuOTQ6NDEwMDI6YXV0aF9hZXMxMjhfc2hhMTpjaGFjaGEyMC1pZXRmOnRsczEuMl90aWNrZXRfYXV0aDplVkJMY21WNFdHRldUVUZZUm1abGVnLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcVBDZmg2WWdMZVdLb09hTHYtV2tweTB4TmpVdU1UVTBMakl5TlM0NU5BJm9iZnNwYXJhbT1NR1ZqTlRReU9EQTROQzVrYjNkdWJHOWhaQzUzYVc1a2IzZHpkWEJrWVhSbExtTnZKU1h2djcwJnByb3RvcGFyYW09TWpnd09EUTZhMlkwTjFobQ
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.33.88.190:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.33.88.190
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.79.111.214:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.79.111.214
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.79.79.37:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.79.79.37
    ssr://eWMuc2FmZXRlbGVzY29wZS5jYzoyMTA3ODphdXRoX2FlczEyOF9tZDU6YWVzLTI1Ni1jZmI6dGxzMS4yX3RpY2tldF9hdXRoOmFFZHJVVFk1TVRWMFJBLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IdXZDZmg3Z2dMZWUtanVXYnZTMTVZeTV6WVdabGRHVnNaWE5qYjNCbExtTmomb2Jmc3BhcmFtPVlXcGhlQzV0YVdOeWIzTnZablF1WTI5dCZwcm90b3BhcmFtPQ
    trojan://28d98ac5a3ef0-b4ab-11ea3fa58b581353bb375d2ddad0f327938@ned-server-01.selfupay.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-474-ned-server-01.selfupay.com
    trojan://2ce84336-46b2-4c8c-ad29-239aacca8343@usa.838501.xyz:15001?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-066-usa.838501.xyz
    trojan://5c640e3ef0-9c44-49a8-98f6-0895b11eecd6@t03.ssrsub.comusa-server-02.selfupay.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-8118-t03.ssrsub.comusa-server-02.selfupay.com
    trojan://821f5e02-729b-4644-a80a-3aaeaf07938d@sg.838501.xyz:15001?allowInsecure=0#%F0%9F%87%B8%F0%9F%87%AC%20%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-2070-sg.838501.xyz
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLeWMl+e+juWcsOWMui0xMDQuMTY2LjEyNC44MiIsImFkZCI6IjEwNC4xNjYuMTI0LjgyIiwicG9ydCI6IjQwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjMyNzU2OGY0LWNlMjAtNGEzZS05YjYxLWRmM2I1MTI0YTk5NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjkuNjQuMzAiLCJhZGQiOiIxMDQuMjkuNjQuMzAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImEyYzViYTY4LWU4NmEtNDk1OS1iN2YzLThmODgwMWQ2MzcwZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImRlMS5rdWFpbmlhby5idXp6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMC5kb3VsdW9zLmljdSIsImFkZCI6IjEwLmRvdWx1b3MuaWN1IiwicG9ydCI6IjUzMDEwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjlmMmUxNDJlLTBjN2EtM2E2Ny1iMmE1LTg0NzAyNjdkZmIxNiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJkZTEua3VhaW5pYW8uYnV6eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMTUud2dvbmcxLnRvcCIsImFkZCI6IjExNS53Z29uZzEudG9wIiwicG9ydCI6IjUyMjE1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdhZDFlMGFmLTg4MGQtMzkxZS05MmNhLTQxNjk3ZjgyYjBlZCIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJkZTEua3VhaW5pYW8uYnV6eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMTYud2dvbmcxLnRvcCIsImFkZCI6IjExNi53Z29uZzEudG9wIiwicG9ydCI6IjUyMjE2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdhZDFlMGFmLTg4MGQtMzkxZS05MmNhLTQxNjk3ZjgyYjBlZCIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJkZTEua3VhaW5pYW8uYnV6eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMTcud2dvbmcxLnRvcCIsImFkZCI6IjExNy53Z29uZzEudG9wIiwicG9ydCI6IjUyMjE3IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdhZDFlMGFmLTg4MGQtMzkxZS05MmNhLTQxNjk3ZjgyYjBlZCIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJkZTEua3VhaW5pYW8uYnV6eiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@5.181.234.254:808#%5B11-17%5D-%F0%9F%87%BA%F0%9F%87%A6-%E4%B9%8C%E5%85%8B%E5%85%B0-618-5.181.234.254
    ss://YWVzLTI1Ni1jZmI6Rkc1ZGRMc01QYlY1Q3V0RQ@213.183.53.179:9050#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-738-213.183.53.179
    ss://YWVzLTI1Ni1jZmI6SmRtUks5Z01FcUZnczhuUA@213.183.53.207:9003#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-942-213.183.53.207
    ss://YWVzLTI1Ni1jZmI6TTN0MlpFUWNNR1JXQmpSYQ@103.172.116.6:9011#%5B11-17%5D-%F0%9F%87%A6%F0%9F%87%B6-%E4%BA%9A%E5%A4%AA%E5%9C%B0%E5%8C%BA-9840-103.172.116.6
    ss://YWVzLTI1Ni1jZmI6TnZTOE40VmY4cUFHUFNDTA@213.183.59.177:9046#%F0%9F%87%B3%F0%9F%87%B1%20%5B11-17%5D-%F0%9F%87%B3%F0%9F%87%B1-%E8%8D%B7%E5%85%B0-8472-213.183.59.177
    ss://YWVzLTI1Ni1jZmI6U241QjdqVHFyNzZhQ0pUOA@213.183.59.191:9097#%F0%9F%87%B3%F0%9F%87%B1%20%5B11-17%5D-%F0%9F%87%B3%F0%9F%87%B1-%E8%8D%B7%E5%85%B0-10332-213.183.59.191
    ss://YWVzLTI1Ni1jZmI6UVdERHZWRTlucE51clFmQQ@213.183.53.214:9026#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-780-213.183.53.214
    ss://YWVzLTI1Ni1jZmI6VE4yWXFnaHhlRkRLWmZMVQ@213.183.53.177:9037#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-8952-213.183.53.177
    ss://YWVzLTI1Ni1jZmI6VlA4WlB4UXBKdFpSQ2pmWg@213.183.53.198:9080#%F0%9F%87%B7%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-8736-213.183.53.198
    ss://YWVzLTI1Ni1nY206TGtGQXprelhrU0NSWWEyQ3NSZEw4Y0di@45.248.79.69:34815#%F0%9F%87%AA%F0%9F%87%BA%20%E6%AC%A7%E6%B4%B2%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2049
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMEQ@45.77.48.44:8099#%F0%9F%87%A6%F0%9F%87%BA%20%5B11-17%5D-%F0%9F%87%A6%F0%9F%87%BA-%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A-408-45.77.48.44
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqvCfh7og5qyn5rSyKOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIDQ3IiwiYWRkIjoic3cub3JhY2xldXNhLm1sIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJkMTI3MGQxMi03NmI3LTRjNGQtOTdmZi02ZDZmNDFhMDEzYjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzRZM2czRW5TVSIsImhvc3QiOiJzdy5vcmFjbGV1c2EubWwiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@145.239.1.137:2376#%F0%9F%87%AA%F0%9F%87%BA%20%E6%AC%A7%E6%B4%B2%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2043
    ss://YWVzLTI1Ni1jZmI6ZkcyYXJ0VW1IZk5UMmNYNw@103.172.116.5:9018#%5B11-17%5D-%F0%9F%87%A6%F0%9F%87%B6-%E4%BA%9A%E5%A4%AA%E5%9C%B0%E5%8C%BA-8616-103.172.116.5
    ss://YWVzLTI1Ni1jZmI6ck5CZk51dUFORkNBazdLQg@213.183.59.190:9056#%F0%9F%87%B3%F0%9F%87%B1%20%5B11-17%5D-%F0%9F%87%B3%F0%9F%87%B1-%E8%8D%B7%E5%85%B0-870-213.183.59.190
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqvCfh7og5qyn5rSyKOasoui/juiuoumYhVlvdXR1YmXnoLTop6PotYTmupDlkJspIDQxIiwiYWRkIjoidjguc3Nyc3ViLmNvbSIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyYTk1ZTZkLWNmODktNDJlZS04MTEwLTY2ZmFiNjg3MWUyZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Nyc3ViIiwiaG9zdCI6InY4LnNzcnN1Yi5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e54a480c-77e3-41ca-8f8b-17ffb50dbd08@t1.ssrsub.com:1033?allowInsecure=0&sni=t1.ssrsub.com#%F0%9F%87%AA%F0%9F%87%BA%20%E6%AC%A7%E6%B4%B2%28%E6%AC%A2%E8%BF%8E%E8%AE%A2%E9%98%85Youtube%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B%29%2039
    ssr://MTE2LjE2Mi4xMjAuMzQ6NTYwOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNHpOQSZvYmZzcGFyYW09JnByb3RvcGFyYW09
    ssr://MTE2LjE2Mi4xMjAuNDk6NTYwOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNDBPUSZvYmZzcGFyYW09WkVNMWRGcFRPVEpqUnpWdldWaFImcHJvdG9wYXJhbT1OVEk0TnpVNlFXRXhNVEl5TVRF
    ssr://MTE2LjE2Mi4xMjAuNTA6NTYwOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNDFNQSZvYmZzcGFyYW09JnByb3RvcGFyYW09
    ssr://MTE2LjEyOS4yNTMuNjozOTQzOTphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46UjJoUmNrUlQvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhxUENmaDdNZ0xlV01sLVM2ck9XNGdpMHhNVFl1TVRJNUxqSTFNeTQyJm9iZnNwYXJhbT1kQzV0WlM5MmNHNW9ZWFEmcHJvdG9wYXJhbT1OekV3TURJNmIySXhTMmcy
    ssr://MTI1Ljk0LjIxNS4yMDA6NTYxOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9OEotSHFQQ2ZoN01nNWJtXzVMaWM1NXlCNWJtXzViZWU1YmlDTFRFeU5TNDVOQzR5TVRVdU1qQXcmb2Jmc3BhcmFtPWRDNXRaUzkyY0c1b1lYUSZwcm90b3BhcmFtPU16ZzNNelU2VEV4TVRHaG5kV3BvYW1nMk56YzRObWRv
    ssr://MTQ2LjE5LjE5Ni4xNDY6NDEwMDU6YXV0aF9hZXMxMjhfc2hhMTpjaGFjaGEyMC1pZXRmOnRsczEuMl90aWNrZXRfYXV0aDplVkJMY21WNFdHRldUVUZZUm1abGVnLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcV9DZmg3Y2dMZWF6bGVXYnZTMHhORFl1TVRrdU1UazJMakUwTmcmb2Jmc3BhcmFtPU1HVmpOVFF5T0RBNE5DNWtiM2R1Ykc5aFpDNTNhVzVrYjNkemRYQmtZWFJsTG1OdmJRJnByb3RvcGFyYW09TWpnd09EUTZhMlkwTjFobQ
    ssr://MTQuMTUyLjkyLjc3OjEyMTI3OmF1dGhfYWVzMTI4X3NoYTE6YWVzLTI1Ni1jZmI6aHR0cF9zaW1wbGU6TmpoNFpHZDFPV1Y1YVdZLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz01Ym1fNUxpYzU1eUI1TGljNkk2ZTViaUNMVEUwTGpFMU1pNDVNaTQzTncmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPU5qQXdOemMzT2pFMU5GUTRZZw
    

</details>

### 所有节点
合并节点总数: `2520`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `90`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `137`
- [freefq/free](https://github.com/freefq/free), 节点数量: `18`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `594`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4513`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `119`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `39`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `33`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `46`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `145`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `26`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `15`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `19`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `110`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `33`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `323`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `139`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `293`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `4`

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
