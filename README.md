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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7hfVVNf576O5Zu9XzkiLCJhZGQiOiIxMzguMi44LjIyNyIsInBvcnQiOiI1OTQ0MiIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmQwNDJmYS1lODY0LTRhOTUtODViYy02ZjU5MGEwM2QzNGEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1#%E7%BE%8E%E5%9B%BD%20030%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNTUyIDIiLCJhZGQiOiIxMzguMi44LjIyNyIsInBvcnQiOiI1OTQ0MiIsInR5cGUiOiJub25lIiwiaWQiOiI2ZmQwNDJmYS1lODY0LTRhOTUtODViYy02ZjU5MGEwM2QzNGEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9ieS54Ynlnb29kLnh5eiIsImhvc3QiOiIlN0IlMjJob3N0JTIyOiUyMmEuMTg5LmNuJTIyJTdEIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgMzgwIiwiYWRkIjoiMTUyLjcwLjIzNS4yMDciLCJwb3J0IjoiMzU0MTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjgwLjg1Ljg0LjgyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA2MyIsImFkZCI6IjEzOC4yLjguMjI3IiwicG9ydCI6IjU5NDQyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1#JP_138.2.8.227_1014d2b4-117
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HpvCfh7ogQVUgNyIsImFkZCI6IjEyOS4xNTQuNTcuMTM0IiwicG9ydCI6IjI2MjgyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNhYmJkZjVkLTNjY2EtNDYwNS1iYTFjLWM4OWE3ZDViNGMwNyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJnbGMuaHJ1cW9hdy5jbiIsInRscyI6IiJ9
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1#JP_138.2.8.227_1014d2b4-44
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@download2tw.windowsupdate1.com:28443?allowInsecure=0&sni=glc.hruqoaw.cn#%E5%8F%B0%E6%B9%BEHinet2%20%7C%20%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@download2tw.windowsupdate1.com:28443?allowInsecure=0&sni=glc.hruqoaw.cn#2.49%7C%20%E5%8F%B0%E6%B9%BEHinet2%20%20%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysIDAwMSIsImFkZCI6Im00LjQwMDEwMDEwLnh5eiIsInBvcnQiOiIzNzEyMSIsInR5cGUiOiJub25lIiwiaWQiOiI1NzVlNGQ5Mi0xMDU2LTQ0YzItOGNhYy03NWVmMWM4NTlhZDUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZzZzEuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5r6z5aSn5Yip5LqaIDAwMSIsImFkZCI6IjEyOS4xNTQuNTcuMTM0IiwicG9ydCI6IjI2MjgyIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNhYmJkZjVkLTNjY2EtNDYwNS1iYTFjLWM4OWE3ZDViNGMwNyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@download1tw.windowsupdate1.com:28443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%B9%F0%9F%87%BC%20TW%205%20TG%3A%40airproxies
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1#%E7%BE%8E%E5%9B%BD%20066
    vmess://eyJ2IjoiMiIsInBzIjoiQHZwbl9wcm94eTY2fEtSXzEiLCJhZGQiOiIxNTIuNjcuMjE4LjM4IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJiNWU5NDgwYS1iN2FhLTQwYTQtZjlhNy01Mjk5YjVlMzYzYjQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxNTIuNjcuMjE4LjM4IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIDI2IiwiYWRkIjoiaGFuZ3VvYi55b25neWV2cG4uY29tIiwicG9ydCI6IjQzNjMyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL29vb28iLCJob3N0IjoiYmFpZHUuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIDI1IiwiYWRkIjoiNDMuMjAxLjUwLjIzNiIsInBvcnQiOiI0MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6ImJhaWR1LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7hfVVNf576O5Zu9XzkgMiIsImFkZCI6IjEzOC4yLjguMjI3IiwicG9ydCI6IjU5NDQyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiI0Ny4yNDIuMTA0LjE2MSIsInRscyI6IiJ9
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@download1tw.windowsupdate1.com:28443?allowInsecure=0&sni=glc.hruqoaw.cn#%E5%8F%B0%E6%B9%BEHinet%20%7C%20%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93
    ss://YWVzLTI1Ni1jZmI6YUxwUXRmRVplNDQ1UXlIaw@185.126.116.125:9098#%F0%9F%87%B7%F0%9F%87%B4RO_08
    vmess://eyJ2IjoiMiIsInBzIjoifDI0LjUwTWIiLCJhZGQiOiIxMjkuMTU0LjU3LjEzNCIsInBvcnQiOiIyNjI4MiIsInR5cGUiOiJub25lIiwiaWQiOiJjYWJiZGY1ZC0zY2NhLTQ2MDUtYmExYy1jODlhN2Q1YjRjMDciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiS1JfMTUyLjcwLjI0MS4xOF8xMDE0ZDJiNC0zOCAyIiwiYWRkIjoiMTUyLjcwLjI0MS4xOCIsInBvcnQiOiIyNjY3NiIsInR5cGUiOiJub25lIiwiaWQiOiJlY2QyNzRjMC0xNzVkLTQ1ZjctODI3Ni1hM2RhOTM3ODY2MzIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2xjLmhydXFvYXcuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzEwMTQxMzg4IiwiYWRkIjoiMTMuMTI1LjIwMC4yNiIsInBvcnQiOiI0MzYzMiIsInR5cGUiOiJub25lIiwiaWQiOiIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidjcuZ2l0dnBuLmV1Lm9yZyIsInRscyI6IiJ9
    trojan://de39d941-eaf6-405d-958a-ebebe1315574@46.51.245.44:2053?allowInsecure=1&sni=wel-vn.qchwnd.moe#%F0%9F%87%BB%F0%9F%87%B3%20%5BBGP-GSLB%5D%E8%B6%8A%E5%8D%97%E8%83%A1%E5%BF%97%E6%98%8E
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7hVU18xMCIsImFkZCI6IjEzOC4yLjE1LjIzIiwicG9ydCI6IjQ2MzcwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk5ODE1MWU1LTBiYzUtNDM3Ny1lMzkwLWM0MWJiMjZmZGQwYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@43.200.164.211:28443?allowInsecure=0&sni=glc.hruqoaw.cn#%E9%9F%A9%E5%9B%BD%E4%BA%9A%E9%A9%AC%E9%80%8A-1%E5%8F%B7%20%7C%20%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93%0D
    trojan://de39d941-eaf6-405d-958a-ebebe1315574@46.51.245.44:2053?allowInsecure=1&sni=wel-th.qchwnd.moe#%F0%9F%87%B9%F0%9F%87%AD%20%5BBGP-GSLB%5D%E6%B3%B0%E5%9B%BD%E6%9B%BC%E8%B0%B7
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1#JP_138.2.8.227_1014d2b4-44%202
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAwNyIsImFkZCI6IjE1Mi43MC4yNDEuMTgiLCJwb3J0IjoiMjY2NzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvZ3JhcGhxbCIsImhvc3QiOiJtYWhzYXByb3h5Y2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLCJ0bHMiOiIifQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoifCA2LjY1TWIiLCJhZGQiOiIxNTIuNzAuMjQxLjE4IiwicG9ydCI6IjI2Njc2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVjZDI3NGMwLTE3NWQtNDVmNy04Mjc2LWEzZGE5Mzc4NjYzMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiS1JfMTUyLjcwLjI0MS4xOF8xMDE0ZmNkZC04NSIsImFkZCI6IjE1Mi43MC4yNDEuMTgiLCJwb3J0IjoiMjY2NzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNTk0IiwiYWRkIjoiMTM4LjIuMTUuMjMiLCJwb3J0IjoiNDYzNzAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTk4MTUxZTUtMGJjNS00Mzc3LWUzOTAtYzQxYmIyNmZkZDBjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDIzIDMiLCJhZGQiOiJzZy5wcnByLmxpbmsiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNlYTQyMTYxLWJkZGMtNDIzMC1hOWI5LWU0MzE4Nzk2N2ZmYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwiaG9zdCI6InNnLnBycHIubGluayIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5be06KW/IDAwMSIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3YycmF5IiwiaG9zdCI6ImRiMDEucGFvcGFvY2xvdWQuY3lvdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzEwMTQxMjkiLCJhZGQiOiJlcjIubXliZXN0amouY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5YzQxOWE1My05YTI5LTRjNTktOTZhNy1iMDUyZTc5ZTRjMzciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzE2NTM1MzEiLCJob3N0IjoiZXIxLm15YmVzdGpqLmNvbSIsInRscyI6InRscyJ9
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=0#%7C476.22Mb
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAxNiIsImFkZCI6IjEzOC4yLjE1LjIzIiwicG9ydCI6IjQ2MzcwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk5ODE1MWU1LTBiYzUtNDM3Ny1lMzkwLWM0MWJiMjZmZGQwYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3BhdGgvMTczNDE4MTQxMTIzIiwiaG9zdCI6Ind3dy4xNzA4MDEwMC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQyMzQgMiIsImFkZCI6IjE1Mi42OS4xOTUuMTcxIiwicG9ydCI6IjU1NTU1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzUuemh1amljbjIuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNTc2IDIiLCJhZGQiOiIxNTIuNjkuMTk3LjYwIiwicG9ydCI6IjEwNjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImdsYy5ocnVxb2F3LmNuIiwidGxzIjoiIn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1#SG%2B%E6%96%B0%E5%8A%A0%E5%9D%A1_4%202
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1#SG%2B%E6%96%B0%E5%8A%A0%E5%9D%A1_4
    vmess://eyJ2IjoiMiIsInBzIjoifCA2LjY1TWIgMyIsImFkZCI6IjE1Mi43MC4yNDEuMTgiLCJwb3J0IjoiMjY2NzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5mbGllc3dpbWluZy50ayIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5be06KW/IDAwMyIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnNnMS4wYmFkLmNvbSIsInRscyI6IiJ9
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=0#999%202
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=0#999
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1#mianfeifq%20297
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMEQ@45.77.48.44:8099#45.77.48.44%3A8099
    vmess://eyJ2IjoiMiIsInBzIjoifDIwLjQ1TWIiLCJhZGQiOiIxMzguMi4xNS4yMyIsInBvcnQiOiI0NjM3MCIsInR5cGUiOiJub25lIiwiaWQiOiI5OTgxNTFlNS0wYmM1LTQzNzctZTM5MC1jNDFiYjI2ZmRkMGMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmZsaWVzd2ltaW5nLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqvCfh7og5qyn5rSyKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIDciLCJhZGQiOiIxNjcuMTcyLjY0LjExIiwicG9ydCI6IjEwMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc2YTI3NmEyLTBmYzMtNGJmYi1jYjAwLTZjZDJhNDMwOTY3NyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1#mianfeifq%20248
    vmess://eyJ2IjoiMiIsInBzIjoi5r6z5aSn5Yip5LqaIDAwMyIsImFkZCI6InZhdTEuMGJhZC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2hhdCIsImhvc3QiOiJ2YXUxLjBiYWQuY29tIiwidGxzIjoidGxzIn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1#mianfeifq%20297%202
    vmess://eyJ2IjoiMiIsInBzIjoi5r6z5aSn5Yip5LqaXzEwMTQwNzUiLCJhZGQiOiJ2YXUxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmF1MS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAzMyIsImFkZCI6IjE1Mi43MC4yNDEuMTgiLCJwb3J0IjoiMjY2NzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvY2hhdCIsImhvc3QiOiJ2YXUxLjBiYWQuY29tIiwidGxzIjoiIn0=
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@103.135.102.156:28443?allowInsecure=0&sni=glc.hruqoaw.cn#%E9%A6%99%E6%B8%AFHKIX%0D
    vmess://eyJ2IjoiMiIsInBzIjoi5r6z5aSn5Yip5LqaXzEwMTQwNzQiLCJhZGQiOiJ2YXUxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmF1MS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDIzIDIiLCJhZGQiOiJzZy5wcnByLmxpbmsiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNlYTQyMTYxLWJkZGMtNDIzMC1hOWI5LWU0MzE4Nzk2N2ZmYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwiaG9zdCI6InNnLnBycHIubGluayIsInRscyI6InRscyJ9
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1#mianfeifq%20284
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@162.251.61.221:802#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoifDIwLjY5TWIiLCJhZGQiOiIxNTIuNjkuMTk3LjYwIiwicG9ydCI6IjEwNjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvY2hhdCIsImhvc3QiOiJ2c2cxLjBiYWQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgODYwIDIiLCJhZGQiOiIxMzguMi40NC4yMTEiLCJwb3J0IjoiMjAwODEiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTkzYjg1MjUtMGM0OC00YjBmLWQ5YWYtMmQ3M2E5MTQ4OTczIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImdsYy5ocnVxb2F3LmNuIiwidGxzIjoiIn0=
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1#%E7%BE%8E%E5%9B%BD%20044
    vmess://eyJ2IjoiMiIsInBzIjoifDU2LjI1TWIiLCJhZGQiOiIxNjguMTM4LjIwNy42NiIsInBvcnQiOiIyMTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiI5MDVmOTliMS1lN2JhLTQ1ZTAtYWU0ZC1iMGZmZGYwYWQyNDUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmZsaWVzd2ltaW5nLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5r6z5aSn5Yip5LqaXzEwMTQwMDciLCJhZGQiOiJ2YXUxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmF1MS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAyOCIsImFkZCI6IjE1Mi42OS4xOTUuMTcxIiwicG9ydCI6IjU1NTU1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzUuemh1amljbjIuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQyMTQgMiIsImFkZCI6IjE1Mi42OS4xOTUuMTcxIiwicG9ydCI6IjU1NTU1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ3ZWwtaWQucWNod25kLm1vZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wt5paw5Yqg5Z2hLTE2Ny4xNzIuNjQuMTEiLCJhZGQiOiIxNjcuMTcyLjY0LjExIiwicG9ydCI6IjEwMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc2YTI3NmEyLTBmYzMtNGJmYi1jYjAwLTZjZDJhNDMwOTY3NyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3JhdWMiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQyMjciLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9ieS54Ynlnb29kLnh5eiIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1#mianfeifq%20248%203
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgODYwIiwiYWRkIjoiMTM4LjIuNDQuMjExIiwicG9ydCI6IjIwMDgxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU5M2I4NTI1LTBjNDgtNGIwZi1kOWFmLTJkNzNhOTE0ODk3MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzUuemh1amljbjIuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzEwMTQxMzMiLCJhZGQiOiJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoiZWUuY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikgOCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9yYXkiLCJob3N0IjoiYXJtanAuZmluZXlvby5tbCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoifCA2LjY1TWIgMiIsImFkZCI6IjE1Mi43MC4yNDEuMTgiLCJwb3J0IjoiMjY2NzYiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAxNyIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9wYXRoLzE3MzQxODE0MTEyMyIsImhvc3QiOiJ3d3cuMTcwODAxMDAueHl6IiwidGxzIjoiIn0=
    trojan://de39d941-eaf6-405d-958a-ebebe1315574@16.163.226.1:2053?allowInsecure=0&sni=wel-hkt.qchwnd.moe#TG%E9%A2%91%E9%81%93%3A%40kxswa%20%7C%20%F0%9F%87%AD%F0%9F%87%B0%20%5BBGP-GSLB%5D%E9%A6%99%E6%B8%AF%E2%80%A2HKT%0D
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAzMCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoibGc1LnpodWppY24yLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDIwLjY5TWIgMiIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoibGc1LnpodWppY24yLmNvbSIsInRscyI6IiJ9
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@jgwxn4.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2010%20%E2%86%92%20openitsub.com%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQwNTAiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQwNDMiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoianAwNC12bTAuZW50cnkucndlc2RoeXRqdWZ0eWhkYWZzZGdmcmguY2x1YiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQyMzUiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@140.238.205.173:443?allowInsecure=1#%F0%9F%87%A6%F0%9F%87%BA_AU_%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A_2_7%4027
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQyMzQgMiIsImFkZCI6IjE1Mi42OS4xOTUuMTcxIiwicG9ydCI6IjU1NTU1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzUuemh1amljbjIuY29tIiwidGxzIjoiIn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=0&sni=jgwxn3.gaox.ml#%F0%9F%87%A6%F0%9F%87%BA%20AU%2014
    trojan://41dbac14-48c9-402a-9c30-a63acbae2522@210.0.158.220:28443?allowInsecure=0&sni=glc.hruqoaw.cn#%E9%A6%99%E6%B8%AFHGC%20%7C%20%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93%0D
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@jgwdb3.gaox.ml:443?allowInsecure=1#JP%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91%206
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@jgwdb4.gaox.ml:443?allowInsecure=1#JP%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikgMzcgMiIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2xjLmhydXFvYXcuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDIwLjY5TWIgMyIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmZsaWVzd2ltaW5nLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzEwMTQxNTMiLCJhZGQiOiJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoiZWUuY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8zIDUiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid2VsLWlkLnFjaHduZC5tb2UiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDE3OS41M01iIiwiYWRkIjoiMTM5Ljk5LjkxLjk1IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQxNDggMiAyIiwiYWRkIjoiMTUyLjY5LjE5NS4xNzEiLCJwb3J0IjoiNTU1NTUiLCJ0eXBlIjoibm9uZSIsImlkIjoiYjg2ZDk1ZGEtYjg0My00ODA0LTg0NDMtZDg0OWQzMjA3MDc2IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImxnNC56aHVqaWNuMi5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQyMzUiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9ieS54Ynlnb29kLnh5eiIsImhvc3QiOiJ0ZXh0Mi54Ynl3d2NwLnVzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQxNTgiLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93bmN1dndzIiwiaG9zdCI6Im9za2EuaGVoZWRhZGEudGsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pel5pysXzEwMTQyMjkiLCJhZGQiOiI4LjIwOS4yMjAuMzQiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ3NThmMDYtZjRiOS00ZWYxLWE4NmMtZjBhMGNjODIxMDlmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmllcyIsImhvc3QiOiJsdXguanVzdHUubWwiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQxNTggMiIsImFkZCI6IjE1Mi42OS4xOTUuMTcxIiwicG9ydCI6IjU1NTU1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJnbGMuaHJ1cW9hdy5jbiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMTQyNDciLCJhZGQiOiIxNTIuNjkuMTk1LjE3MSIsInBvcnQiOiI1NTU1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMTQxMTYiLCJhZGQiOiJzaG9waWZ5LmNvbSIsInBvcnQiOiIyMDg2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImRjOGI2NGRiLWViNmQtNGJkZi05OGIyLTMxNjE1MzE5YmVhOCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0Ijoidm4uY2xvdWRmbGFyZS5xdWVzdCIsInRscyI6IiJ9

</details>

### 所有节点
合并节点总数: `6515`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `184`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `152`
- [freefq/free](https://github.com/freefq/free), 节点数量: `41`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `157`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `4162`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `21`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `43`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `50`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `177`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `205`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `38`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `42`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `34`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `24`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `261`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `236`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `275`
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
- [阿伟云](https://awslcn.xyz/#/register?code=8C18uZwl)
  - 最低月付 1¥ 起, 9.99¥100G
  - 无带宽速率限制，有流媒体解锁，香港 BGP 中继线路

## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

## 星标统计
[![Star History Chart](https://api.star-history.com/svg?repos=alanbobs999/TopFreeProxies&type=Date)](https://star-history.com/#alanbobs999/TopFreeProxies&Date)
