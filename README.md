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

    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan%2FOsaka_9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDgwMTAiLCJhZGQiOiJsaS5iaWcyMzQuY29tIiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjEzZTc4M2EtMjA3NC00YWVmLWI2ZDktMmFjNmQ0ZDBkYzA0IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImxpLmJpZzIzNC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzExMDg0NzgiLCJhZGQiOiI1MS43OS4xNDAuMjQ5IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyMzhmYzdmLWNlNWEtNDY1Zi1lZmY1LTY2ZDk2ZGY4ZDZlZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvQG1haW50ZW5hbmNlei9AbXRjc3RvcmVzL0BqdWFsYmVsaXZwcyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzExMDgyMDEiLCJhZGQiOiI0Ny45MS4yMy4xODIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU3MjEyNmY4LTUzMDEtODNjMi0wYTI2LWMzMGNlZDNkYjdjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd216bXZ3cyIsImhvc3QiOiJnb29kZmFtaWx5MTkuc2l0ZSIsInRscyI6InRscyJ9
    trojan://cf1815f4-fe98-4acf-94b2-853f35fc4bf7@kr.838501.xyz:15001?allowInsecure=0#%F0%9F%87%AF%F0%9F%87%B5%20%5B11-09%5D-%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC-3405-kr.838501.xyz
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry00Ny4yNDIuNjEuMTI1IiwiYWRkIjoiNDcuMjQyLjYxLjEyNSIsInBvcnQiOiI1MTc4NCIsInR5cGUiOiJub25lIiwiaWQiOiI0MzFjNGMwMS1iNTk2LTRkMTItYTllNi00ZjdmMjFmZTgyYmEiLCJhaWQiOiIwIiwibmV0IjoiaHR0cCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00Ny43NC4xLjE1NSIsImFkZCI6IjQ3Ljc0LjEuMTU1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwNDc5ZWI5ZC05OTlkLTRiZmYtYWUzZi00ZjdjYzQ0MGNlNDYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2MnJheTIuc3NyLWZyZWUyLnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry04LjIxMC4yMDMuMTg5IiwiYWRkIjoiOC4yMTAuMjAzLjE4OSIsInBvcnQiOiIzNzMwOSIsInR5cGUiOiJub25lIiwiaWQiOiI3NGNkY2MyOC1hMGJjLTQyMWYtYmQxNS1jNmE2ZTQwMWI1MjMiLCJhaWQiOiIwIiwibmV0IjoiaHR0cCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry04LjIxMC4yMzQuMTg5IiwiYWRkIjoiOC4yMTAuMjM0LjE4OSIsInBvcnQiOiI0NjY0NCIsInR5cGUiOiJub25lIiwiaWQiOiJjMjVhMWM5YS0xYzcxLTRjNTgtYWZiYS02NmVlZDczOGIyMmIiLCJhaWQiOiIwIiwibmV0IjoiaHR0cCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1hZWFkanBhZXMwMS54bi0tejRxNDhsY3ZwLmNvbSIsImFkZCI6ImFlYWRqcGFlczAxLnhuLS16NHE0OGxjdnAuY29tIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk0NjczZTE5LTExZmEtNDM3MC04NTgzLTk4OWU5ZWIxYTcxMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImFlYWRqcGFlczAxLnhuLS16NHE0OGxjdnAuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1mMDguaG90bGFuZC5zaXRlIiwiYWRkIjoiZjA4LmhvdGxhbmQuc2l0ZSIsInBvcnQiOiIxMDAwOCIsInR5cGUiOiJub25lIiwiaWQiOiIxMTRkYjg3Yy0yMjQ1LTQ4NDItYjZkMS1iYmQ3ZWMxYjk2YjkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJmMDguaG90bGFuZC5zaXRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi1oaW5ldC0yLmFraWpwLm5ldCIsImFkZCI6ImhpbmV0LTIuYWtpanAubmV0IiwicG9ydCI6IjMwMDE1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImUyOWM5NzFmLWM4OWUtNGMwNy1hYmE4LWNlYTNlZTg4NTEzNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InYucXEuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oa2JncC5sYW55dW5zaGkuY2MiLCJhZGQiOiJoa2JncC5sYW55dW5zaGkuY2MiLCJwb3J0IjoiMTAwMSIsInR5cGUiOiJub25lIiwiaWQiOiI3ZjY3ZmIxMS04MzJkLTM0OTItYWRmZS02M2UwY2NlYWZiZTAiLCJhaWQiOiIyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoidi5xcS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry10Y2hrNC56aGFuZ3h1YW4uYmVzdCIsImFkZCI6InRjaGs0LnpoYW5neHVhbi5iZXN0IiwicG9ydCI6IjIiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWI0MmVhMWYtOGUyZi0zZmZmLThhMTEtZDEyNGQ2MmI4NDllIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InYucXEuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi10dzk5LWhpbmV0Lm15bjFkZXMuY29tIiwiYWRkIjoidHc5OS1oaW5ldC5teW4xZGVzLmNvbSIsInBvcnQiOiIyMDg3IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ3OGMwYmYzLWI1YmItMzk0OC1iNWFmLTgzMzc5ZDhjOTE3ZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InR3OTktaGluZXQubXluMWRlcy5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi10dzIucm92b2QudG9wIiwiYWRkIjoidHcyLnJvdm9kLnRvcCIsInBvcnQiOiIxMDAwMCIsInR5cGUiOiJub25lIiwiaWQiOiJhYjQyZWExZi04ZTJmLTNmZmYtOGExMS1kMTI0ZDYyYjg0OWUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidHc5OS1oaW5ldC5teW4xZGVzLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry11czEubmV0ZmxpeDYuY29tIiwiYWRkIjoidXMxLm5ldGZsaXg2LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzEyMTk1NjctNTEyNS0zZWI0LTkyMDItZjA2ODM2ODdjY2E3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMxLm5ldGZsaXg2LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1jcy5oZ2Riay5nYSIsImFkZCI6ImNzLmhnZGJrLmdhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIzZjcyNDExNS04Y2EyLTRhYTQtYjhjYy1lYjcyZDliNmIxZWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJZb3VUdWJlLWF3ZWlrZWppIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLeaWsOWKoOWdoS1oay12LnNvbW5vZGUudG9wIiwiYWRkIjoiaGstdi5zb21ub2RlLnRvcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmMTM5ODU3OS1lZWQxLTMzMzUtOWZmYi01ZGFjNDY3ZTIzYWMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2YWxpLWRucy5jcDMxLm90dC5jaWJudHYubmV0IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS12MzYuaWRjbG91ZGhvc3QuZGUiLCJhZGQiOiJ2MzYuaWRjbG91ZGhvc3QuZGUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDA5NzRkNzEtMDMyZi00ZjVjLTk0MWItNjEyZmI0MjYyNTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidjM2LmlkY2xvdWRob3N0LmRlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xMTdqcDEuYmZ5dW4udG9wIiwiYWRkIjoiMTE3anAxLmJmeXVuLnRvcCIsInBvcnQiOiIxMzU2OCIsInR5cGUiOiJub25lIiwiaWQiOiI1NzBkNmIyMi0yMDk0LTQ4YTAtODkzMy1jYTAyN2UzMmYwMTAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMTdqcDEuYmZ5dW4udG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNjAuMTYuNjkuMTAyIiwiYWRkIjoiMTYwLjE2LjY5LjEwMiIsInBvcnQiOiIxMDExMSIsInR5cGUiOiJub25lIiwiaWQiOiJhYjQyZWExZi04ZTJmLTNmZmYtOGExMS1kMTI0ZDYyYjg0OWUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTE3anAxLmJmeXVuLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNmEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDZhLnJ1aTc3LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzgwNjVjMTQtZmM4MC00MGI1LWE0NmMtMGUzNGVmZGY4MmZhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjExN2pwMS5iZnl1bi50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1hZ3JvdXAubm9kZTMudi5ub2RlbGlzdC1nZndhaXJwb3J0LmRvd25sb2FkIiwiYWRkIjoiYWdyb3VwLm5vZGUzLnYubm9kZWxpc3QtZ2Z3YWlycG9ydC5kb3dubG9hZCIsInBvcnQiOiI1MDAwMSIsInR5cGUiOiJub25lIiwiaWQiOiI4ZDE4MzRjOS00ZTIzLTQ3ZTMtODM0ZS0zNjNjYjgxYjFmZjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTE3anAxLmJmeXVuLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLeaWsOWKoOWdoS1oay1iLnNvbW5vZGUudG9wIiwiYWRkIjoiaGstYi5zb21ub2RlLnRvcCIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmMTM5ODU3OS1lZWQxLTMzMzUtOWZmYi01ZGFjNDY3ZTIzYWMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2YWxpLWRucy5jcDMxLm90dC5jaWJudHYubmV0IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuWPsOS4reW4gi10dzEucm92b2QudG9wIiwiYWRkIjoidHcxLnJvdm9kLnRvcCIsInBvcnQiOiIxMDAxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiNDJlYTFmLThlMmYtM2ZmZi04YTExLWQxMjRkNjJiODQ5ZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ2YWxpLWRucy5jcDMxLm90dC5jaWJudHYubmV0IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgLeWPsOa5vuaWsOWMl+W4gi1oaW5ldC5uYnNkLndpbiIsImFkZCI6ImhpbmV0Lm5ic2Qud2luIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5ZWM5NzU3MC02YTk1LTMwNTYtODg1ZC0yZWQ3ZWRiYWVjNDUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJoaW5ldC5uYnNkLndpbiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAzMmEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzJhLnJ1aTc3LmNvbSIsInBvcnQiOiIxMjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiIxNjE3ZmYxYi00ZTg1LTRhOGEtODFjMy01MTFiM2MyZWZhZDgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiaGluZXQubmJzZC53aW4iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1hZ3JvdXAubm9kZTQudi5ub2RlbGlzdC1nZndhaXJwb3J0LmRvd25sb2FkIiwiYWRkIjoiYWdyb3VwLm5vZGU0LnYubm9kZWxpc3QtZ2Z3YWlycG9ydC5kb3dubG9hZCIsInBvcnQiOiI1MDAwMSIsInR5cGUiOiJub25lIiwiaWQiOiI4ZDE4MzRjOS00ZTIzLTQ3ZTMtODM0ZS0zNjNjYjgxYjFmZjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiaGluZXQubmJzZC53aW4iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry12MjEuaWRjbG91ZGhvc3QuZGUiLCJhZGQiOiJ2MjEuaWRjbG91ZGhvc3QuZGUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDA5NzRkNzEtMDMyZi00ZjVjLTk0MWItNjEyZmI0MjYyNTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiJTdCJTIySG9zdCUyMjolMjJ2MjEuaWRjbG91ZGhvc3QuZGUlMjIlN0QiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNDYuNTYuMTg0LjEiLCJhZGQiOiIxNDYuNTYuMTg0LjEiLCJwb3J0IjoiNTUyMTQiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTc3NzU1ODgtZmM2NS0zM2MzLTkyYzYtMTI3MzM5MTg4YmZkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00My4xOTguMTIuMjIyIiwiYWRkIjoiNDMuMTk4LjEyLjIyMiIsInBvcnQiOiIxMDUxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiNDJlYTFmLThlMmYtM2ZmZi04YTExLWQxMjRkNjJiODQ5ZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC00NS43Ni4yMjMuMTM2IiwiYWRkIjoiNDUuNzYuMjIzLjEzNiIsInBvcnQiOiIxMDAxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiNDJlYTFmLThlMmYtM2ZmZi04YTExLWQxMjRkNjJiODQ5ZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1hZ3JvdXAubm9kZTEudi5ub2RlbGlzdC1nZndhaXJwb3J0LmRvd25sb2FkIiwiYWRkIjoiYWdyb3VwLm5vZGUxLnYubm9kZWxpc3QtZ2Z3YWlycG9ydC5kb3dubG9hZCIsInBvcnQiOiI1MDAwMSIsInR5cGUiOiJub25lIiwiaWQiOiI4ZDE4MzRjOS00ZTIzLTQ3ZTMtODM0ZS0zNjNjYjgxYjFmZjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYWdyb3VwLm5vZGUxLnYubm9kZWxpc3QtZ2Z3YWlycG9ydC5kb3dubG9hZCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDAyLXZtMC5lbnRyeS5yd2VzZGh5dGp1ZnR5aGRhZnNkZ2ZyaC5jbHViIiwiYWRkIjoianAwMi12bTAuZW50cnkucndlc2RoeXRqdWZ0eWhkYWZzZGdmcmguY2x1YiIsInBvcnQiOiI0NDkiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjM0NzZmYjMtOWZhOS0zZmFiLTk5ODktNGY5YzQ0M2FlOTJiIiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAwMi12bTAuZW50cnkucndlc2RoeXRqdWZ0eWhkYWZzZGdmcmguY2x1YiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC11cmdqcC5ob3RmdW4uYnV6eiIsImFkZCI6InVyZ2pwLmhvdGZ1bi5idXp6IiwicG9ydCI6IjE0NDE0IiwidHlwZSI6Im5vbmUiLCJpZCI6ImUxZjgwNDE2LTUzOTQtNGZjZC1hZjgwLTEyZWY5Nzk5YTkyYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InVyZ2pwLmhvdGZ1bi5idXp6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAyN2EucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMjdhLnJ1aTc3LmNvbSIsInBvcnQiOiI1MjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ODA2NWMxNC1mYzgwLTQwYjUtYTQ2Yy0wZTM0ZWZkZjgyZmEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXJnanAuaG90ZnVuLmJ1enoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS1vcmFjbGUuMTcwNTI1Lnh5eiIsImFkZCI6Im9yYWNsZS4xNzA1MjUueHl6IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJlZGIzNTUyNS03MDNkLTRmYjAtYzYyZi02MmVkMzZjNWRlZjYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXJnanAuaG90ZnVuLmJ1enoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKwgIDEiLCJhZGQiOiJ2OC41ODMxODEueHl6IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRhYzY4MTc5LTQ0OWEtNGY0Ny04NTRjLTMwZjBjZTQ4OGZiYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InB1bGwuZnJlZS52aWRlby4xMDAxMC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbveWPsOa5vihUVylUYWl3YW4vQ2l0eU9mZmljZV8yIiwiYWRkIjoiNjEuMjIyLjIwMi4xNDAiLCJwb3J0IjoiMzM3OTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTU1Y2QxODItMDFiMC00ZmI3LWE1MTAtMzYzNzAxYTQ5MWM1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbvemmmea4ry/kuK3lm73lj7Dmub4oQ04pQ2hpbmEvU2hlbnpoZW4vKOWPr+iDveaYr+S4rei9rOiKgueCuSlfMyIsImFkZCI6IlYxMDQuYmdwbmV0LnRvcCIsInBvcnQiOiIyNjEwNCIsInR5cGUiOiJub25lIiwiaWQiOiJlZjM2MWM4My04Yjg5LTM5NTAtOWM5Yi02Y2NjMTc3ZTYyODUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2FkbWluIiwiaG9zdCI6IlYxMDQuYmdwbmV0LnRvcCIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206ZTB1eWFrZW5kZzc@x.gotout.work:30031#%F0%9F%87%AD%F0%9F%87%B0%20%5B09-26%5D%7Copenrunner%7C%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF%2F%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%28CN%29China%2FShenzhen%2F%28%E5%8F%AF%E8%83%BD%E6%98%AF%E4%B8%AD%E8%BD%AC%E8%8A%82%E7%82%B9%29_4
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgWzA5LTI2XXxvcGVucnVubmVyfOaWsOWKoOWdoShTRylTaW5nYXBvcmUvU2luZ2Fwb3JlXzciLCJhZGQiOiJ2Mi0yLmdvZGxpZ2h0Lnh5eiIsInBvcnQiOiIzMDUyNiIsInR5cGUiOiJub25lIiwiaWQiOiI0MzMwOGQyNy05NGVjLTQwOGUtYThmNi1kNjgyY2ZiOTljYTkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzU0ZjYzNGZzIiwiaG9zdCI6InYyLTIuZ29kbGlnaHQueHl6IiwidGxzIjoidGxzIn0=
    trojan://7Z29DRr1ts@cp-asus.ml:50275?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20%5B09-26%5D%7Copenrunner%7C%E6%96%B0%E5%8A%A0%E5%9D%A1%28SG%29Singapore%2FSingapore_8
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAyNmEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMjZhLnJ1aTc3LmNvbSIsInBvcnQiOiI1MjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiJlZGM5ZThhOC01MThlLTQyNWEtODE4NC1lNTVkMTZkODQ0YjIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMjZhLnJ1aTc3LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAzMGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzBhLnJ1aTc3LmNvbSIsInBvcnQiOiI1MjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ODA2NWMxNC1mYzgwLTQwYjUtYTQ2Yy0wZTM0ZWZkZjgyZmEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzBhLnJ1aTc3LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTYuMTQ4LjQ4IiwiYWRkIjoiMTA0LjE2LjE0OC40OCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMWE1NGU3NTYtZDQ1NC00NWEwLWFlZmEtZTk1MTRlMWRhMWYxIiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidmluY2VudC1qYWNrc29uMjAyMS5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTcuMTg4LjkxIiwiYWRkIjoiMTA0LjE3LjE4OC45MSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWY0YjJlNDItZmYyYi00MzQyLTg2ZmMtYjdiYTFiNTM2MWU4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidmluY2VudC1qYWNrc29uMjAyMS5nYSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTcuMzYuMTc4IiwiYWRkIjoiMTA0LjE3LjM2LjE3OCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2I1ZTI1OGUtOGM1ZS00NWQzLWI3ZDItMDJjOGY1ZmMwYmIyIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNkbmRlLmlydGV5ei50b2RheSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTkuMjQuMTkyIiwiYWRkIjoiMTA0LjE5LjI0LjE5MiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJkNDZlMzBhYS1kYjJmLTRlNTgtYWYwMS03NTg4NzRiMWIzNDEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMTkuMjM4LjU5IiwiYWRkIjoiMTA0LjE5LjIzOC41OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2I1ZTI1OGUtOGM1ZS00NWQzLWI3ZDItMDJjOGY1ZmMwYmIyIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNkbmRlLmlydGV5ei50b2RheSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjQuMjI2LjUzIiwiYWRkIjoiMTA0LjI0LjIyNi41MyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJkNDZlMzBhYS1kYjJmLTRlNTgtYWYwMS03NTg4NzRiMWIzNDEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJjZi5haWZ1cWlhbmcudGsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjQuNDIuMTQ4IiwiYWRkIjoiMTA0LjI0LjQyLjE0OCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2I1ZTI1OGUtOGM1ZS00NWQzLWI3ZDItMDJjOGY1ZmMwYmIyIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNkbmRlLmlydGV5ei50b2RheSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjUuMTc1LjY5IiwiYWRkIjoiMTA0LjI1LjE3NS42OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGU4YjUwOTctMWQ3NS00N2M0LWZmMjgtZWVmNjYwOTkxNmMxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidmluY2VudC1qYWNrc29uMjAyMS5jZiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjUuMTA0LjI0MCIsImFkZCI6IjEwNC4yNS4xMDQuMjQwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjRiMmU0Mi1mZjJiLTQzNDItODZmYy1iN2JhMWI1MzYxZTgiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ2aW5jZW50LWphY2tzb24yMDIxLmdhIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjUuMjUxLjQ5IiwiYWRkIjoiMTA0LjI1LjI1MS40OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2I1ZTI1OGUtOGM1ZS00NWQzLWI3ZDItMDJjOGY1ZmMwYmIyIiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjEuMTcuODciLCJhZGQiOiIxMDQuMjEuMTcuODciLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU3MjEyNmY4LTUzMDEtODNjMi0wYTI2LWMzMGNlZDNkYjdjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMDQuMjIuMy4zIiwiYWRkIjoiMTA0LjIyLjMuMyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGU4YjUwOTctMWQ3NS00N2M0LWZmMjgtZWVmNjYwOTkxNmMxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidmluY2VudC1qYWNrc29uMjAyMS5jZiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLeWMl+e+juWcsOWMui0xMDcuMTczLjE1Ny4xNjgiLCJhZGQiOiIxMDcuMTczLjE1Ny4xNjgiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRmNmFhMGMzLTdiZTEtNGVhYS1hNjRjLWEyMzQxODA3MDQyMiIsImFpZCI6IjYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5zaHVueGluLm1sIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMS5teHl1bjEudG9wIiwiYWRkIjoiMTEubXh5dW4xLnRvcCIsInBvcnQiOiI0MTExMSIsInR5cGUiOiJub25lIiwiaWQiOiJjNTU1NmZhMi0xNDNiLTNjNDktYThmYS0zMGUxZGFhYTc3MjgiLCJhaWQiOiIyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LnNodW54aW4ubWwiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMTEud2dvbmcxLnRvcCIsImFkZCI6IjExMS53Z29uZzEudG9wIiwicG9ydCI6IjUyMjExIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRkMDI5NWRkLTk4YzktMzE4MC1hYTkxLTg5NTVhNzdkZTM1NCIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuc2h1bnhpbi5tbCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMTIud2dvbmcxLnRvcCIsImFkZCI6IjExMi53Z29uZzEudG9wIiwicG9ydCI6IjUyMjEyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImIzZTcyYjRjLWQzYTgtM2NkZi1iMzZjLWViZmZlNGRhOTJkMSIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuc2h1bnhpbi5tbCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMy4yMTUuMjE4LjEwMSIsImFkZCI6IjEzLjIxNS4yMTguMTAxIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI2MzgyYjRlLTAwZjAtNGY0Zi05MGE4LTNkZTM1MmUyYTA2ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDEuMTAxLjExNC4xNyIsImFkZCI6IjE0MS4xMDEuMTE0LjE3IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJjbGFzaDYuc3NyLWZyZWUueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDEuMTAxLjExNC4xOTkiLCJhZGQiOiIxNDEuMTAxLjExNC4xOTkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc1MGEyOWJmLTBhNDAtNDM3Zi1iMTIwLTM4ZGU3NGFlN2VhZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImhpbmV0Lm1laXpoaXl1YW55YS54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDEuMTAxLjExNS4xNTUiLCJhZGQiOiIxNDEuMTAxLjExNS4xNTUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjVmNjRmYTY1LTdiMTQtNDljNS05NTRkLWFhMTVjNmJmY2FjZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImNsYXNoNi5zc3ItZnJlZS54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDEuMTAxLjEyMC4xOTAiLCJhZGQiOiIxNDEuMTAxLjEyMC4xOTAiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNmIwZGMyYTUtMGI3MC00ZGVmLWJhNjUtOTNkOWMxMjM3YTBlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTQxLjEwMS4xMjAuMTkwIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNDIuNC4xMjcuNjciLCJhZGQiOiIxNDIuNC4xMjcuNjciLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuNDc3Mjc0NTAueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMDYt5LuY6LS55o6o6I2Qc3VvLnl0L3NzcnN1YiIsImFkZCI6IjEwNi43NS4yMTguMTEyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MTY0NmY5YS1iNGU5LTRhY2EtYmZlMy04ODkyYjNlNThmZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzMwLmNmY2RuMy54eXoiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsvCfh70g5aKo6KW/5ZOlXzExMDgwMDEiLCJhZGQiOiIxMzEuMTk2LjI1My4xNDAiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZDU0MjI2ZjktNDQyNy00NDY2LTk1N2YtMTczYjBhNWIxY2JjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zc2hvY2VhbiIsImhvc3QiOiIxMzEuMTk2LjI1My4xNDAiLCJ0bHMiOiIifQ==
    ssr://dnBoay02LmdpdG8uY2M6NzgxOmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6T1dsbVlYTjAvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhxUENmaDdNZ0xlYXhuLWlMai1lY2dTMTJjR2hyTFRZdVoybDBieTVqWXcmb2Jmc3BhcmFtPU9UUXdZekl6TURnMU5TNWtiM2R1Ykc5aFpDNTNhVzVrYjNkemRYQmtZWFJsTG1OdmJRJnByb3RvcGFyYW09TXpBNE5UVTZNRVoyV2xKNQ
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh6wgLeWQieWwlOWQieaWr+aWr+Wdpi0zNy4xNDMuMTI5LjIzOCIsImFkZCI6IjM3LjE0My4xMjkuMjM4IiwicG9ydCI6IjY2MTYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjhkMTliYTUtODY4NC00NWYyLTg1MjMtNzdkYmVhNTg4OTU1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cgLeiLseWbvS05NS4xNzkuMjMwLjc4IiwiYWRkIjoiOTUuMTc5LjIzMC43OCIsInBvcnQiOiIxMTkxMSIsInR5cGUiOiJub25lIiwiaWQiOiJhYjQyZWExZi04ZTJmLTNmZmYtOGExMS1kMTI0ZDYyYjg0OWUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh7cgLeW4jOiFii1hb3Auc3NmcmVlLnJ1IiwiYWRkIjoiYW9wLnNzZnJlZS5ydSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiODMxODU2YjAtNGFhYi0xMWVkLThhMTYtMDAwMDE3MDIyMDA4IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImFvcC5zc2ZyZWUucnUiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7EgLeiNt+WFsC1ubC52Mi1yYXkuY29tIiwiYWRkIjoibmwudjItcmF5LmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJiYjk3ZWUwYS02ZDU3LTQwYzAtYTQ0Ni00NWI3OGMzMDM2MDMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJubC52Mi1yYXkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HtfCfh60gLeiPsuW+i+Wuvi1wcmVtaXBoLnZwbmphbnRpdC5jb20iLCJhZGQiOiJwcmVtaXBoLnZwbmphbnRpdC5jb20iLCJwb3J0IjoiMTAwMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiYmFhNTY0M2MtNDUxYi0xMWVkLTg5M2EtZTNkODhiOWY5ZjdmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoicHJlbWlwaC52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiLeS5jOWFi+WFsC11c2E0LnZwbmphbnRpdC5jb20iLCJhZGQiOiJ1c2E0LnZwbmphbnRpdC5jb20iLCJwb3J0IjoiMTAwMDAiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzZhNDQzOTQtNGY4My0xMWVkLWFmOWYtYmIyNjFlZWRjNzAyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXNhNC52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Ht/Cfh7ogLeS/hOe9l+aWr+iOq+aWr+enkS1lbHMudGR6amluZy54eXoiLCJhZGQiOiJlbHMudGR6amluZy54eXoiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDAwMDAwMDAtMTExMS0xMTExLTExMTEtMjIyMjIyMjIyMjIyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InVzYTQudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA3MCIsImFkZCI6IjU3LjEyOC40NS4xNjEiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzVkMjU4OTktZWQyMC00NmQ5LTljN2MtOTljMGQ0MTRkNWU0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNTcuMTI4LjQ1LjE2MSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA2OSIsImFkZCI6InVuaXZzdGFyLjE4OC4xNjYuMTg2LjI0OS5zc2xpcC5pbyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTcyMTI2ZjgtNTMwMS04M2MyLTBhMjYtYzMwY2VkM2RiN2M0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93bXptdndzIiwiaG9zdCI6InVuaXZzdGFyLjE4OC4xNjYuMTg2LjI0OS5zc2xpcC5pbyIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cgLeW3tOilv+Wco+S/nee9ly0xODguMTE0Ljk3LjciLCJhZGQiOiIxODguMTE0Ljk3LjciLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjJkZjhjYjMzLWRlNDAtNDM4Yy04NDBhLTVmMWQwNWZlNzUxOCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InY1LnRnZmFrYS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsfCfh7ogLeWNouajruWgoS1sdTAxLnBhb3Bhb2Nsb3VkLmN5b3UiLCJhZGQiOiJsdTAxLnBhb3Bhb2Nsb3VkLmN5b3UiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg5Yjc2ZmU2LTgzM2UtM2FiMC1hYjk2LTUzYmRiMDY2MjU5OCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Imx1MDEuc3NydTMuY2FzYSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh7cgLeW3tOilv+Wco+S/nee9ly0xODguMTE0Ljk2LjMiLCJhZGQiOiIxODguMTE0Ljk2LjMiLCJwb3J0IjoiODg4MCIsInR5cGUiOiJub25lIiwiaWQiOiIyYjk4NGIyMS0yZDM1LTQ3OWQtZmRjMC1kNzJjN2ZhNzYyYWYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh7cgLeW4jOiFii0xNDQuMjQuODkuMTU2IiwiYWRkIjoiMTQ0LjI0Ljg5LjE1NiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI1NGIzZWY4Ny0wMDg0LTQzNjItYWY1Ny0yZmI0OTRkOGNhMTUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiLeacrOacuuWcsOWdgC1qdXN0bGJ5Lnh5eiIsImFkZCI6Imp1c3RsYnkueHl6IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIzMjhmNjg2Yy02YjJiLTNjNDAtYjY3Ny1lZDc2OTcyOGRjYzAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoianVzdGxieS54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HtfCfh60gLeiPsuW+i+Wuvi1waDQudnBuamFudGl0LmNvbSIsImFkZCI6InBoNC52cG5qYW50aXQuY29tIiwicG9ydCI6IjEwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQyMDNiNzA2LTQ1MWUtMTFlZC04Yzc5LTJiNGMwZGMxOGQ0OSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InBoNC52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6VWtYUnNYdlI2YnVETUcyWQ@213.183.63.221:9001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2066
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HpvCfh7ogLea+s+Wkp+WIqeS6mi1kZG5zLWtyMDIuYXlhbmFtaS5iZXN0IiwiYWRkIjoiZGRucy1rcjAyLmF5YW5hbWkuYmVzdCIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZmMGM0Y2JkLWJjZmItNDBhZi05NTM4LWYzMWU5MWZlYjJkNyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJwaDQudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hq/Cfh7cgLeazleWbvS0xNDYuMTkuMTk2LjEyNSIsImFkZCI6IjE0Ni4xOS4xOTYuMTI1IiwicG9ydCI6IjMxMjQ0IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4YWFhNmUxLWYwYjMtYjllYy0zZGZjLWJiMjI2YzE2N2IzMyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJwaDQudnBuamFudGl0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hq/Cfh7cgLeazleWbvS1mcjAxLnBhb3Bhb2Nsb3VkLmN5b3UiLCJhZGQiOiJmcjAxLnBhb3Bhb2Nsb3VkLmN5b3UiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg5Yjc2ZmU2LTgzM2UtM2FiMC1hYjk2LTUzYmRiMDY2MjU5OCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImZyMDEuMnl1bi53aW4iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hq/Cfh7cgLeazleWbvS1wYW9wYW8udjIuaGwwMS5wYW9wYW9jbG91ZC5jeW91IiwiYWRkIjoicGFvcGFvLnYyLmhsMDEucGFvcGFvY2xvdWQuY3lvdSIsInBvcnQiOiIzMzA2IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg5Yjc2ZmU2LTgzM2UtM2FiMC1hYjk2LTUzYmRiMDY2MjU5OCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImhsMDEuc3NydTMuY2FzYSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cgLeiLseWbvS0xODUuMTI2LjEzNi4yMTYiLCJhZGQiOiIxODUuMTI2LjEzNi4yMTYiLCJwb3J0IjoiMTAwMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWI0MmVhMWYtOGUyZi0zZmZmLThhMTEtZDEyNGQ2MmI4NDllIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImhsMDEuc3NydTMuY2FzYSIsInRscyI6IiJ9
    

</details>

### 所有节点
合并节点总数: `2410`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `66`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `149`
- [freefq/free](https://github.com/freefq/free), 节点数量: `33`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `325`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4050`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `31`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `68`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `34`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `44`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `264`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `43`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `30`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `33`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `17`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `49`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `229`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `188`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `287`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `49`

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
