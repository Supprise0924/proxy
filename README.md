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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjYxNTUiLCJhZGQiOiIxNDYuNTYuMTQ5LjIwNSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOWRjMGM2YWEtMzlhMS00NmJlLTk5MzgtODU5OTllM2MzNDk4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9mYXN0c3NoLzE3MzEzOTAwOTMvNjM1N2NlZGQ3YTE5OS8iLCJob3N0Ijoic2cxLjMxdnBuLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjYyNTIiLCJhZGQiOiJ2c2cxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnNnMS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgU0fmlrDliqDlnaEoeW91dHViZeenkeaKgClfMSIsImFkZCI6IjEyOS4xNTAuNDcuMTQyIiwicG9ydCI6IjIyNjI0IiwidHlwZSI6Im5vbmUiLCJpZCI6ImU5YjMzNjI3LWM3YjctNGJiZi1hNmY2LTJmYTUwYzBkN2JmMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjYyNTYiLCJhZGQiOiIxMjkuMTUwLjQ3LjE0MiIsInBvcnQiOiIyMjYyNCIsInR5cGUiOiJub25lIiwiaWQiOiJlOWIzMzYyNy1jN2I3LTRiYmYtYTZmNi0yZmE1MGMwZDdiZjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMjkuMTUwLjQ3LjE0MiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg6Z+p5Zu9XzEwMjYxNTcgMiIsImFkZCI6IjE0Ni41Ni4xNjYuMTUzIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5ZGMwYzZhYS0zOWExLTQ2YmUtOTkzOC04NTk5OWUzYzM0OTgiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Zhc3Rzc2gvMTczMTM5MDA5My82MzU3Y2VkZDdhMTk5LyIsImhvc3QiOiJzZzEuMzF2cG4uY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hIDAwNCIsImFkZCI6IjEzOS45OS45MC4xMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii9mYXN0c3NoLzE3MzEzOTAwOTMvNjM1N2NlZGQ3YTE5OS8iLCJob3N0Ijoic2cxLjMxdnBuLmNvbSIsInRscyI6IiJ9
    trojan://7118b5f4-0ea4-4c11-be7f-11471cb91e4a@144.24.72.126:443?allowInsecure=1#KR_144.24.72.126_10250983-38%202
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:811#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176811-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:807#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176807-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@45.66.134.176:806#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC-ss-45.66.134.176806-%E8%A2%AB%E5%A2%99-%E4%B8%AD%E8%BD%AC185.168.20.250-%E8%A7%A3%E9%94%81%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://f2117e99-9b6e-47fd-b0a9-634a0b15b998@146.56.189.146:443?allowInsecure=1#KR_146.56.189.146_1026af28-166%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMjYyNjUgMiIsImFkZCI6IjEzOS4xNjIuMTE5LjE1OSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmMDg1ZTlhMS02YWY0LTQ4MDYtOTkyZS0xNjEwNTdjMDM4M2UiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3ZtZXNzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzEwMjYyNjUiLCJhZGQiOiIxMzkuMTYyLjExOS4xNTkiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjA4NWU5YTEtNmFmNC00ODA2LTk5MmUtMTYxMDU3YzAzODNlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92bWVzcyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjYwMDIiLCJhZGQiOiJhei5oazAxLnBhb3Bhb2Nsb3VkLmN5b3UiLCJwb3J0IjoiMTAwMTAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZDhjNWI0ODYtODRiYi0zODg3LWExZDktMDc0NTVlYTYwOGYyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92MnJheSIsImhvc3QiOiJwYW9wYW8udjIuYXowMS5wYW9wYW9jbG91ZC5jeW91IiwidGxzIjoidGxzIn0=
    trojan://7118b5f4-0ea4-4c11-be7f-11471cb91e4a@144.24.72.126:443?allowInsecure=1#KR_144.24.72.126_10250983-38%203
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjYzOTkiLCJhZGQiOiIxNjUuMTU0LjUuMjM1IiwicG9ydCI6IjE0NDQ0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlYjlkMmZhLTE3ZDEtNDI3Ni1hZjgwLTE1MzIzZGMxZGNhNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://7118b5f4-0ea4-4c11-be7f-11471cb91e4a@144.24.72.126:443?allowInsecure=1#KR_144.24.72.126_10250983-38
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjY0MzciLCJhZGQiOiIxNjUuMTU0LjUuMjM1IiwicG9ydCI6IjE0NDQ0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBlYjlkMmZhLTE3ZDEtNDI3Ni1hZjgwLTE1MzIzZGMxZGNhNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7Ag6aaZ5rivXzEwMjY0MzcgMiIsImFkZCI6IjE2NS4xNTQuNS4yMzUiLCJwb3J0IjoiMTQ0NDQiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGViOWQyZmEtMTdkMS00Mjc2LWFmODAtMTUzMjNkYzFkY2E1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjYxNjciLCJhZGQiOiJzZ292aDEudjJyYXlzZXJ2LmNvbSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI3OGY5MzZkMS04YTcyLTRiN2MtYWFmYS1jODI4NGUxNWNjYWEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3NzaG9jZWFuIiwiaG9zdCI6InNnb3ZoMS52MnJheXNlcnYuY29tIiwidGxzIjoiIn0=
    trojan://Z3YS0KxB8u5jgp736e834y3DaXwSOYzxlFDFqpNCaalDA9CEIRceZOCAnR2yTS@45.64.22.55:443?allowInsecure=1&sni=reooec.freetrade.link#%F0%9F%87%AF%F0%9F%87%B5%20JP%206%20TG%40airproxies%202
    trojan://01e80e00-2f18-47ea-8c2f-7dbc5b57b71f@1024tw02.tfzhc.top:443?allowInsecure=1&sni=1024tw02.tfzhc.top#%F0%9F%87%AD%F0%9F%87%B0%20HK%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Ahttps%2F%2Fgoo.gs%2Fvip%E3%80%91
    trojan://Z3YS0KxB8u5jgp736e834y3DaXwSOYzxlFDFqpNCaalDA9CEIRceZOCAnR2yTS@45.64.22.55:443?allowInsecure=1&sni=reooec.freetrade.link#%F0%9F%87%AF%F0%9F%87%B5%20JP%206%20TG%40airproxies
    trojan://01e80e00-2f18-47ea-8c2f-7dbc5b57b71f@1024tw02.tfzhc.top:443?allowInsecure=0&sni=1024tw02.tfzhc.top#%F0%9F%87%A8%F0%9F%87%B3%20%E5%8F%B0%E6%B9%BEB%7Ctg%E9%A2%91%E9%81%93%40ripaojiedian
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjM1IDIiLCJhZGQiOiIyMy45MS4xMDAuMjQzIiwicG9ydCI6IjMwODYyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjNiMGY0NGU0LWRkMTEtNDI5ZC1jODBmLTYxNWIxMDU5NWRiOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIxMDI0dHcwMi50ZnpoYy50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMTI4LjEuMTM0LjEyNl8xMDIwY2JkNi01MyIsImFkZCI6IjEyOC4xLjEzNC4xMjYiLCJwb3J0IjoiNjY2NiIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmIzYjU3MS1jZGE4LTQwZjYtYzllNi1kYjk3NjVlYThmYWEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTAyNHR3MDIudGZ6aGMudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjM1IiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTAyNHR3MDIudGZ6aGMudG9wIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiSEtfMjI0IiwiYWRkIjoiMTI4LjEuMTM0LjEyNiIsInBvcnQiOiI2NjY2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdmYjNiNTcxLWNkYTgtNDBmNi1jOWU2LWRiOTc2NWVhOGZhYSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIxMDI0dHcwMi50ZnpoYy50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjYxNDAiLCJhZGQiOiIyMjAuMTMwLjgwLjE3OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjZkN2IwNzItZGUwMC00NWRjLTllMjQtNDlmOGNmNDM1MzBkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5vZCIsImhvc3QiOiJsaW5kby5jbmFiYy5ldS5vcmciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKzkuJzkuqzpg73lk4Hlt53ljLpMaW5vZGXmlbDmja7kuK3lv4MgMTMiLCJhZGQiOiIxMzkuMTYyLjExOS4xNTkiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjA4NWU5YTEtNmFmNC00ODA2LTk5MmUtMTYxMDU3YzAzODNlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92bWVzcyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgZ2l0aHViLmNvbS9mcmVlZnEgLSDlj7Dmub7nnIHlvbDljJbljr/kuK3ljY7nlLXkv6EgMTUiLCJhZGQiOiIyMjAuMTMwLjgwLjE3OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjZkN2IwNzItZGUwMC00NWRjLTllMjQtNDlmOGNmNDM1MzBkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5vZCIsImhvc3QiOiJsaW5kby5jbmFiYy5ldS5vcmciLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7Mg5Y+w5rm+XzEwMjYxMDYiLCJhZGQiOiIyMjAuMTMwLjgwLjE3OSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2ViOGE3ZjQtYTQ1Yi00OGE3LThmOGUtY2E3MTI0YTVlYmVlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ob3dkeSIsImhvc3QiOiJ2MnJheTIudWRwZ3cuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg5paw5Yqg5Z2hXzEwMjYxMDMiLCJhZGQiOiI1MS43OS4xNjQuMTQ2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLCJob3N0IjoiNTEuNzkuMTY0LjE0NiIsInRscyI6InRscyJ9
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
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#US_1234_1%202
    trojan://01e80e00-2f18-47ea-8c2f-7dbc5b57b71f@1024tw02.tfzhc.top:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%202
    trojan://b291d129-ee55-4801-a9b8-b5316e5c37b7@138.2.113.84:443?allowInsecure=1#US_1234_1
    trojan://01e80e00-2f18-47ea-8c2f-7dbc5b57b71f@1024tw03.tfzhc.top:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%201
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@107.181.161.163:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20031
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20035
    trojan://01e80e00-2f18-47ea-8c2f-7dbc5b57b71f@1024tw03.tfzhc.top:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%203
    trojan://e44e1be6-552f-4098-aedd-ff1ed59837e3@1002hk1326.tfzhc.top:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20002
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MSIsImFkZCI6IjE1LjIzNS4xNDcuMTg2IiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjZmZWExNjQ5LTQyNWItNDA5Mi1iZjUzLTI5NzkyMTUyYzkyNSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc3Noa2l0L0VydHVzZzg2LzYzNTAxNDYzOGMyNjQvIiwiaG9zdCI6IjE1LjIzNS4xNDcuMTg2IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjY3NjMiLCJhZGQiOiI2NC4xMTIuMTI2LjQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg1NjBjMGI0LTZmNGItNDVlNi05OTA2LTc3NzY1MGRjYzMxMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3NzaGtpdC9FcnR1c2c4Ni82MzUwMTQ2MzhjMjY0LyIsImhvc3QiOiIxNS4yMzUuMTQ3LjE4NiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjY3NjciLCJhZGQiOiI2NC4xMTIuMTI2LjQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg1NjBjMGI0LTZmNGItNDVlNi05OTA2LTc3NzY1MGRjYzMxMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3NzaGtpdC9FcnR1c2c4Ni82MzUwMTQ2MzhjMjY0LyIsImhvc3QiOiIxNS4yMzUuMTQ3LjE4NiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjYwMzQiLCJhZGQiOiJwaW5nLnBlIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIzYTNlMjYzZC0yMjNmLTQ5Y2MtYmJkYi1mN2UwN2E1NWU2ZmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzExMTExMS5vbmxpbmUiLCJob3N0IjoicGluZy5wZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6Yg5Yqg5ou/5aSnIDAwMiAyIiwiYWRkIjoiY2EyLnYycmF5c2Vydi5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTNlYmEzYWMtNWJlYS00MDlmLWFjNWMtNmM5NjRlMDRkMGM0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zc2hvY2VhbiIsImhvc3QiOiJjYTIudjJyYXlzZXJ2LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjYxNjUiLCJhZGQiOiIyMy4yMjQuMTAxLjEwMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTQ2YmE1ZGYtNTc3MS00ODczLWEzY2ItODkyMzc4NTI2MTQ3IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZm9vdGVycyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjYxNjUgMiIsImFkZCI6IjIzLjIyNC4xMDEuMTAyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5NDZiYTVkZi01NzcxLTQ4NzMtYTNjYi04OTIzNzg1MjYxNDciLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii9mb290ZXJzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDE2IiwiYWRkIjoidjE0OWEuYWFnb2dvLmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MGJkN2YxOC04ZDlkLTM2NTgtOTIxYi0zYWQ2YTNkOWQ2NDYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3YxNDktM0ZqeTY1IiwiaG9zdCI6InYxNDlhLmFhZ29nby5jZiIsInRscyI6InRscyJ9
    trojan://ea48cdda-6db7-4f34-9d42-7bd9d41b4740@1002hk1326.tfzhc.top:443?allowInsecure=0#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2023
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjY3NTkiLCJhZGQiOiIxNzIuNjQuMTU0LjIyMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmNmYWVjOTEtNjA5Ni00NGQ4LTk1NmMtNzg2OGQ5ZTg3NGIxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9yYXkiLCJob3N0IjoibGcxLmNmY2RuMS54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDEiLCJhZGQiOiJtZzEueGJ5d3djcC51cyIsInBvcnQiOiIyNTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiI5OWUyZjUzOS03MDBmLTM5NDctYjMxYS00YzlkOTEyZmY1ZmEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJtZzEueGJ5d3djcC51cyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjYxNTUiLCJhZGQiOiJtZzEueGJ5d3djcC51cyIsInBvcnQiOiIyNTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiJkOTJiNjdkYy04ZWQyLTM4ZWQtOGFjOC1kZjY5NTg0NmM2MDEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJtZzEueGJ5d3djcC51cyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjY3NzEiLCJhZGQiOiJtZzEueGJ5d3djcC51cyIsInBvcnQiOiIyNTM2NSIsInR5cGUiOiJub25lIiwiaWQiOiI3Yzk4MmUxZC02NDdmLTNhMTUtYThhNC0xMDJkNzNkMTkxM2QiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2J5LnhieWdvb2QueHl6IiwiaG9zdCI6Im1nMS54Ynl3d2NwLnVzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73mlrDms73opb/lt55MaW5vZGXlhazlj7ggNCIsImFkZCI6InZ1czQuMGJhZC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InZ1czQuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMjYxNTciLCJhZGQiOiJ2dXM0LjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi55m95auWLTAzNSIsImFkZCI6IjEyOS4xNDYuMTMzLjE1NyIsInBvcnQiOiI1MTAwOSIsInR5cGUiOiJub25lIiwiaWQiOiI4MTcxNGNlZi05YmRlLTRhMDgtYWE1MC1kNmJjMDE3MmQ3OGIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czQuMGJhZC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoifDI1LjcyTWIgMiIsImFkZCI6IjE2OC4xMzguMjA3LjY2IiwicG9ydCI6IjIxMzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkwNWY5OWIxLWU3YmEtNDVlMC1hZTRkLWIwZmZkZjBhZDI0NSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6IiJ9
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1#%F0%9F%87%AE%F0%9F%87%B3%20%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India%2FHyderabad_26
    trojan://vvip-periantara@38.9.140.66:443?allowInsecure=1#ID_38.9.140.66_1026af28-140
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@38.75.136.21:5001#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2091
    trojan://vvip-periantara@38.9.140.66:443?allowInsecure=1#mianfeifq%20346
    trojan://vvip-periantara@38.9.140.66:443?allowInsecure=1#ID_38.9.140.66_1026af28-140%202
    trojan://vvip-periantara@id3tr.jagoan.vip:443?allowInsecure=1#ID_38.9.140.66_1026af28-274%203
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSAzOCIsImFkZCI6IjE1Mi42OS4xOTcuNjAiLCJwb3J0IjoiMTA2OSIsInR5cGUiOiJub25lIiwiaWQiOiJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HpvCfh7og5r6z5aSn5Yip5LqaIDAwMyIsImFkZCI6IjQzLjE1NC4zNC40OSIsInBvcnQiOiIyMzE4MyIsInR5cGUiOiJub25lIiwiaWQiOiJiNDAyYTRhZi0yODVhLTQ2M2UtYzNhNy01M2Y5MWVmZGVjNzgiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMjYxOTYiLCJhZGQiOiIxNDEuMTAxLjExNC4zMyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTVhODhjZTItZmMxYi00NWQxLTljNWYtNTUzNzIxZDI4MDA0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoidjJyYXkxLnpodWppY24yLm9yZyIsInRscyI6InRscyJ9
    trojan://origin@176.31.83.90:443?allowInsecure=1#FR_176.31.83.90_102583f5-61
    trojan://f2117e99-9b6e-47fd-b0a9-634a0b15b998@146.56.189.146:443?allowInsecure=1#mianfeifq%20301
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpzaHdvekVqV2V5@176.97.67.103:444#%F0%9F%87%AC%F0%9F%87%A7%20%5B10-27%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-2814-176.97.67.103
    trojan://Z3YS0KxB8u5jgp736e834y3DaXwSOYzxlFDFqpNCaalDA9CEIRceZOCAnR2yTS@45.64.22.55:443?allowInsecure=1&sni=reooec.freetrade.link#MO%201%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@109.169.72.249:809#%F0%9F%87%AC%F0%9F%87%A7%20%5B10-27%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-2340-109.169.72.249
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=0&sni=youtube-bai-piao-wang-zhe-usa.98848.xyz#%F0%9F%87%BA%F0%9F%87%B8%20youtube-bai-piao-wang-zhe-usa.98848.xyz_trojan_tcp_Trojan
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=0&sni=youtube-bai-piao-wang-zhe-usa.98848.xyz#%F0%9F%87%BA%F0%9F%87%B8%20youtube-bai-piao-wang-zhe-usa.98848.xyz_trojan_gRPC
    vmess://eyJ2IjoiMiIsInBzIjoiXzAyIiwiYWRkIjoiMjMuOTEuMTAwLjI0MyIsInBvcnQiOiIzMDg2MiIsInR5cGUiOiJub25lIiwiaWQiOiIzYjBmNDRlNC1kZDExLTQyOWQtYzgwZi02MTViMTA1OTVkYjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiXzAzIiwiYWRkIjoiMTI4LjEuMTM0LjEyNiIsInBvcnQiOiI2NjY2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjdmYjNiNTcxLWNkYTgtNDBmNi1jOWU2LWRiOTc2NWVhOGZhYSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ5b3V0dWJlLWJhaS1waWFvLXdhbmctemhlLXVzYS45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMjYwMTgiLCJhZGQiOiIxNDEuMTAxLjExNC4xMjAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjMzYWE1N2RmLTFjOTMtNDMxOC05ZmNlLWU4NTA0MzdlZTc4MSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImxnMS5jZmNkbjMueHl6IiwidGxzIjoiIn0=
    trojan://dd04c158-1bac-47cd-99c1-5c4f64796dd5@supersouth.xn--mesv7f5toqlp.club:12004?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2083
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoKSA3NyIsImFkZCI6ImJhbjQuZmVpY2xvdWRkZC5tZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNmRhNDMxZTQtZDdiMS00ZjYxLWIzZTItZjNmOGQ2ZjAzYmI4IiwiYWlkIjoiNjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc2RhZmFzZnNhIiwiaG9zdCI6ImJhbjQuZmVpY2xvdWRkZC5tZSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1nY206OG42cHdBY3JydjJwajZ0RlkycDNUYlE2@82.102.26.117:33992#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2085
    

</details>

### 所有节点
合并节点总数: `2010`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `108`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `120`
- [freefq/free](https://github.com/freefq/free), 节点数量: `16`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `33`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `35`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `2780`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `10`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `29`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `7`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `41`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `161`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `45`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `13`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `9`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `29`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `26`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `217`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `186`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `282`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `36`

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
