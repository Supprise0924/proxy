# TopFreeProxies
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alanbobs999/topfreeproxies/sub_merge?label=sub_merge)](https://github.com/alanbobs999/TopFreeProxies/actions/workflows/sub_merge.yml) 

![Watchers](https://img.shields.io/github/watchers/alanbobs999/topfreeproxies) ![Stars](https://img.shields.io/github/stars/alanbobs999/topfreeproxies) ![Forks](https://img.shields.io/github/forks/alanbobs999/topfreeproxies) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=alanbobs999.topfreeproxies) ![LICENSE](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)

[仓库介绍](https://github.com/alanbobs999/TopFreeProxies#仓库介绍) | [使用方法](https://github.com/alanbobs999/TopFreeProxies#使用方法) | [节点信息](https://github.com/alanbobs999/TopFreeProxies#节点信息) | [软件推荐](https://github.com/alanbobs999/TopFreeProxies#客户端选择) | [机场推荐](https://github.com/alanbobs999/TopFreeProxies#机场推荐) | [仓库声明](https://github.com/alanbobs999/TopFreeProxies#仓库声明)

## 仓库介绍
本仓库自动化功能全部基于 `GitHub Actions` 实现，如果有需要可以自行 Fork 实现个性化需求。

对网络上各免费节点池及博主分享的节点进行测速筛选出较为稳定高速的节点，再导入到仓库中进行分享记录。所筛选的节点链接在仓库 `./sub/sub_list.json` 文件中，其中大部分为其他 `GitHub` 仓库链接，如果大家有好的订阅链接欢迎提交 PR ，这些链接包含的所有节点会合并在仓库 `./sub/sub_merge.txt` 中。

测速筛选后的节点订阅文件在仓库根目录 `Eterniy`(Base64) 和 `Eternity.yml`(Clash)。同时在仓库的 `./update` 中保留了原始节点链接的的记录。

测速功能使用 [LiteSpeedTest](https://github.com/xxf098/LiteSpeedTest) 在 `GitHub Actions` 环境下实现，所以美国节点较多，不能很好代表国内网络环境下节点可用性，目前正在解决这一问题。

虽然是测速筛选过后的节点，但仍然会出现部分节点不可用的情况，遇到这种情况建议选择`Clash`, `Shadowrocket`之类能自动切换低延迟节点的客户端。

## 使用方法
将以下订阅链接导入相应客户端即可。链接中大部分为 SS 协议节点，少量 Vmess, Trojan ,SSR 协议节点，建议选择协议支持完整的客户端。

- [多协议Base64编码](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity)
- [Clash](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml)

另有国内加速链接：

- [多协议Base64编码](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity)
- [Clash](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity.yml)

>`Clash`链接所使用的配置在仓库`./update/provider/`中，有相应配置文件和以国家分类的`proxy-provider`。
>
>需要其它配置可使用订阅转换工具自行转换。
>自用在线订阅转换网址：[sub-web-modify](https://sub.v1.mk/)

## 节点信息
### 高速节点
高速节点数量: `99`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMiIsImFkZCI6Imlta2NwLmdheSIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjczOTczYTNlLTIwMmEtNDE2MC1kYjI0LWY2ZmM3MzRhYjExYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaW1rY3AuZ2F5IiwiaG9zdCI6Imlta2NwLmdheSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDQxMS45M01iIiwiYWRkIjoiaW1rY3AuZ2F5IiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzM5NzNhM2UtMjAyYS00MTYwLWRiMjQtZjZmYzczNGFiMTFjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9pbWtjcC5nYXkiLCJob3N0IjoiaW1rY3AuZ2F5IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTMiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MSIsImFkZCI6Imlta2NwLmdheSIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjczOTczYTNlLTIwMmEtNDE2MC1kYjI0LWY2ZmM3MzRhYjExYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaW1rY3AuZ2F5IiwiaG9zdCI6Imlta2NwLmdheSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MSIsImFkZCI6Imlta2NwLmdheSIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjczOTczYTNlLTIwMmEtNDE2MC1kYjI0LWY2ZmM3MzRhYjExYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaW1rY3AuZ2F5IiwiaG9zdCI6Imlta2NwLmdheSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73ljY7nm5vpob9Db2dlbnTpgJrkv6Hlhazlj7ggMTkiLCJhZGQiOiJ3d3cueWlhbmR4dS5idXp6IiwicG9ydCI6IjExMzQ4IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc0NjJlNDg5LWMxNTItNDQ3My1lNzI5LTA2NDZhMTkxMzQ0MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvc2RmMjYiLCJob3N0Ijoid3d3LnlpYW5keHUuYnV6eiIsInRscyI6InRscyJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20061
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD_1
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@35.91.237.33:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-35.91.237.33%3A443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-129.146.242.130-63
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@107.182.177.136:256#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNzQ5IiwiYWRkIjoiMjMuMjMwLjE0Ni4yNTQiLCJwb3J0IjoiMTI1OCIsInR5cGUiOiJhdXRvIiwiaWQiOiJlZGViNDFjYy1hNzZhLTQ3ZjItZmE5Ni1iOTE0MWU2NmEyYjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD_7
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20061
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2043%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@107.182.177.136:256#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDE0NCIsImFkZCI6ImdhaW8ubWlhb2dlMTEwLmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0ODkzZWQzZS04YTVmLTQ4ZGMtYWExZS1iYmMyZTY3YTA2NWIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2pjbmYiLCJob3N0IjoiZ2Fpby5taWFvZ2UxMTAuY2YiLCJ0bHMiOiIifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2047
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMiIsImFkZCI6Imlta2NwLmdheSIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjczOTczYTNlLTIwMmEtNDE2MC1kYjI0LWY2ZmM3MzRhYjExYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaW1rY3AuZ2F5IiwiaG9zdCI6Imlta2NwLmdheSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYwNDgiLCJhZGQiOiI2Ny4yMS43Mi40NCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8xMjAyMDgzMDE0MjIiLCJob3N0Ijoid3d3LjQ4ODE2NjI2Lnh5eiIsInRscyI6InRscyJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20077
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEzNiIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvVFMvcmVjaGFyZ2UvdHpVcmwuaHRtbCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjYwMDciLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@129.146.242.130:443?allowInsecure=1#mianfeifq%20108
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgMjIxIiwiYWRkIjoiczIuNTIwZ3VnZS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImNmMTgxOWM4LWU1MzAtNDYyNi1hZWMwLTg3YWMwNDIwMDM4NSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaGFwcHkiLCJob3N0IjoiczIuNTIwZ3VnZS5jb20iLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@107.182.177.136:256#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxNiIsImFkZCI6IjY3LjIxLjcyLjQ0IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wYXRoLzEyMDIwODMwMTQyMiIsImhvc3QiOiJ3d3cuNDg4MTY2MjYueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifDI0LjE0TWIiLCJhZGQiOiI2Ny4yMS43Mi40NCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8xMjAyMDgzMDE0MjIiLCJob3N0Ijoid3d3LjQ4ODE2NjI2Lnh5eiIsInRscyI6InRscyJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTMiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggOue+juWbvS12bWVzcy1nYWlvLm1pYW9nZTExMC5jZjo0NDMt6KKr5aKZLeS4rei9rDoxMDQuMjguMjA1LjExMS3op6PplIHnvo7lm73lnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImdhaW8ubWlhb2dlMTEwLmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0ODkzZWQzZS04YTVmLTQ4ZGMtYWExZS1iYmMyZTY3YTA2NWIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2pjbmYiLCJob3N0IjoiZ2Fpby5taWFvZ2UxMTAuY2YiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXlhazlj7hDRE7oioLngrkgMTQiLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgS1Ig6Z+p5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIDEwIiwiYWRkIjoiMjUuNzJpbWcueHl6IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiI0MjNiNGEyYi05ODdmLTQ2YTctOTIyMi03NzY4MzkxMTdiM2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIyNS43MmltZy54eXoiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgU0cg5paw5Yqg5Z2hKHlvdXR1YmXpmL/kvJ/np5HmioApIDciLCJhZGQiOiIxMi43MmltZy54eXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6IjQyM2I0YTJiLTk4N2YtNDZhNy05MjIyLTc3NjgzOTExN2IzYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLjcyaW1nLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMjMuMjMwLjE0Ni4yNTQtODkiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6ImF1dG8iLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIyMy4yMzAuMTQ2LjI1NCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYwNDciLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjYwMDgiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://a9b56b59-ee82-4331-91f8-955d1fdc4e10@nice-ca02.tiktokcdn.buzz:8443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%A6%20%5B09-30%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-222-nice-ca02.tiktokcdn.buzz
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMDQuMTUuNzUuOTkiLCJhZGQiOiIyMDQuMTUuNzUuOTkiLCJwb3J0IjoiNTgyOTAiLCJ0eXBlIjoidm1lc3MiLCJpZCI6ImQ1Y2MzMTQ4LTJlODgtNDM5YS1jYjE3LWUzNjNlN2RiZTQzYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjIwNC4xNS43NS45OSIsInRscyI6IiJ9
    trojan://a9b56b59-ee82-4331-91f8-955d1fdc4e10@nice-ca02.tiktokcdn.buzz:8443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%A6%20CA%202%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYwNDciLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjYwMDciLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjY1MzUiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57ljaHlroHlurfnibnliKlNdWx0YWNvbeWFrOWPuCA0NiIsImFkZCI6IjIwNC4xNS43NS45OSIsInBvcnQiOiI1ODI5MCIsInR5cGUiOiJhdXRvIiwiaWQiOiJkNWNjMzE0OC0yZTg4LTQzOWEtY2IxNy1lMzYzZTdkYmU0M2MiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIyMDQuMTUuNzUuOTkiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgOue+juWbvS12bWVzcy1qcGFybS5maW5leW9vLm1sOjQ0My3ooqvlopkt5Lit6L2sOjEzOC4yLjMzLjkwLeino+mUgeaXpeacrOWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoianBhcm0uZmluZXlvby5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTBiYTQ3OGUtOWRlMS00YWE5LWMwOWUtNzcwNzAyNTMzNGQzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhcm0uZmluZXlvby5tbCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYwNzYiLCJhZGQiOiJqcGFybS5maW5leW9vLmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJiZDVlZTI0OS1mZTdiLTQ2NjktYTZkOS1iM2Y1ZWVjYjk4ZTYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzEyMyIsImhvc3QiOiJqcGFybS5maW5leW9vLmNmIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgOue+juWbvS12bWVzcy1qcGFybS5maW5leW9vLmNmOjQ0My3ooqvlopkt5Lit6L2sOjE1Mi43MC44MS42Ni3op6PplIHml6XmnKzlnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImpwYXJtLmZpbmV5b28uY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImJkNWVlMjQ5LWZlN2ItNDY2OS1hNmQ5LWIzZjVlZWNiOThlNiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImpwYXJtLmZpbmV5b28uY2YiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgU0cg5paw5Yqg5Z2hKHlvdXR1YmXpmL/kvJ/np5HmioApIDciLCJhZGQiOiIxMi43MmltZy54eXoiLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6IjQyM2I0YTJiLTk4N2YtNDZhNy05MjIyLTc3NjgzOTExN2IzYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEyLjcyaW1nLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDQxMS45M01iIiwiYWRkIjoiaW1rY3AuZ2F5IiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzM5NzNhM2UtMjAyYS00MTYwLWRiMjQtZjZmYzczNGFiMTFjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9pbWtjcC5nYXkiLCJob3N0IjoiaW1rY3AuZ2F5IiwidGxzIjoidGxzIn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%20474
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan%2FTokyo_16
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20044
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2034%20%E2%86%92%20openitsub.com
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=0#%7C52.23Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYxNzg5IiwiYWRkIjoidnVzMi4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czIuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20046
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP%205
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgX0pQX+aXpeacrF8xIiwiYWRkIjoianAyLnR6Y2N3ei5maXQiLCJwb3J0IjoiMjc0ODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjcyZWU1OGYtNzhiZi00YjYxLTg0NDItN2I5Y2NhOTEyYjE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAyLnR6Y2N3ei5maXQiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjYxNDM5IiwiYWRkIjoianBhcm0uZmluZXlvby5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTBiYTQ3OGUtOWRlMS00YWE5LWMwOWUtNzcwNzAyNTMzNGQzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhcm0uZmluZXlvby5tbCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgX0pQX+aXpeacrF8xIiwiYWRkIjoianAyLnR6Y2N3ei5maXQiLCJwb3J0IjoiMjc0ODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjcyZWU1OGYtNzhiZi00YjYxLTg0NDItN2I5Y2NhOTEyYjE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAyLnR6Y2N3ei5maXQiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgX0pQX+aXpeacrF8xIiwiYWRkIjoianAyLnR6Y2N3ei5maXQiLCJwb3J0IjoiMjc0ODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjcyZWU1OGYtNzhiZi00YjYxLTg0NDItN2I5Y2NhOTEyYjE0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoianAyLnR6Y2N3ei5maXQiLCJ0bHMiOiJ0bHMifQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=0#%7C40.43Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDIiLCJhZGQiOiIxNTAuMjMwLjE5OS4xNzciLCJwb3J0IjoiMjE2OTYiLCJ0eXBlIjoiYXV0byIsImlkIjoiNmI3NDVjYWYtZTdmNi00OWYxLTliNjMtZTVjNDE2MzAzYmFjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVPjgJDku5jotLnmjqjojZDvvJpndmlwLmdx44CRXzYiLCJhZGQiOiJnYWlvLm1pYW9nZTExMC5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDg5M2VkM2UtOGE1Zi00OGRjLWFhMWUtYmJjMmU2N2EwNjViIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9qY25mIiwiaG9zdCI6IiU3QiUyMkhvc3QlMjI6JTIyZ2Fpby5taWFvZ2UxMTAuY2YlMjIlN0QiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@107.182.177.136:256#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgSlAg5pel5pysKHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoiMjguNzJpbWcueHl6IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI0MjNiNGEyYi05ODdmLTQ2YTctOTIyMi03NzY4MzkxMTdiM2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIyOC43MmltZy54eXoiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgbWlhbmZlaWZxIHxKUCDml6XmnKwoeW91dHViZeenkeaKgCkgOSIsImFkZCI6IjI3LjcyaW1nLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoiYXV0byIsImlkIjoiNDIzYjRhMmItOTg3Zi00NmE3LTkyMjItNzc2ODM5MTE3YjNhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMjcuNzJpbWcueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi44CQ5LuY6LS55o6o6I2Q77yaZ3ZpcC5nceOAkV8xMSIsImFkZCI6ImNkbi5ib290bG9hZGVyLmNmIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc0NzU4ZjA2LWY0YjktNGVmMS1hODZjLWYwYTBjYzgyMTA5ZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXJpZXMiLCJob3N0IjoibHV4Lmp1c3R1Lm1sIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgSlAg5pel5pysKHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoianBhbWQuZmluZXlvby5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOWJkYWM1NTgtMWQyYi00MjViLWYwZTctNDQ1ZDM4YmUwMjVlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoianBhbWQuZmluZXlvby5jZiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDE3IiwiYWRkIjoiMTk4LjQxLjIxMi4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIwN2E2M2ZlMy04YTQ2LTRmODktYjU0OC05MTUxYzYxYjlkYzgiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJ2MnJheTEuemh1amljbjIuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoibWlhbmZlaWZxIHxVU181MS44MS4yMjMuMjZfMDkyOWFlY2YtMzc2IiwiYWRkIjoiNTEuODEuMjIzLjI2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLCJhaWQiOiIzMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjYwMzciLCJhZGQiOiJjZG4uYm9vdGxvYWRlci5jZiIsInBvcnQiOiI4MCIsInR5cGUiOiJ2bWVzcyIsImlkIjoiNzQ3NThmMDYtZjRiOS00ZWYxLWE4NmMtZjBhMGNjODIxMDlmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmllcyIsImhvc3QiOiJsdXguanVzdHUubWwiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDE0IiwiYWRkIjoiYXJtLnB0dXUuZ3EiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk4MjFiODE3LTVjYjAtNGFmMy1hM2UzLTdjMTM3ODUwOTM1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImFybS5wdHV1LmdxIiwidGxzIjoidGxzIn0=
    trojan://a9b56b59-ee82-4331-91f8-955d1fdc4e10@nice-ca02.tiktokcdn.buzz:8443?allowInsecure=1&sni=nice-ca02.tiktokcdn.buzz#%F0%9F%87%A8%F0%9F%87%A6%20CA%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%28youtube%E9%98%BF%E4%BC%9F%E7%A7%91%E6%8A%80%29%0D
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgbWlhbmZlaWZxIHxISyDpppnmuK8oeW91dHViZeenkeaKgCkgOCIsImFkZCI6IjM4LjcyaW1nLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoiYXV0byIsImlkIjoiNDIzYjRhMmItOTg3Zi00NmE3LTkyMjItNzc2ODM5MTE3YjNhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMzguNzJpbWcueHl6IiwidGxzIjoidGxzIn0=
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91_1
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjY1NTciLCJhZGQiOiJqcGFtZC5maW5leW9vLm1sIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiIzNWU1ZTJlYS0xMzcyLTQ3NDUtZGZmOC1mYjJiZDExMDE2YzQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzEyMyIsImhvc3QiOiJqcGFtZC5maW5leW9vLm1sIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVPjgJDku5jotLnmjqjojZDvvJpndmlwLmdx44CRXzM4IiwiYWRkIjoiMTM4LjIuOC4yMjciLCJwb3J0IjoiNTk0NDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNmZkMDQyZmEtZTg2NC00YTk1LTg1YmMtNmY1OTBhMDNkMzRhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi44CQ5LuY6LS55o6o6I2Q77yaZ3ZpcC5nceOAkSIsImFkZCI6IjE5OC40MS4yMTIuMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDdhNjNmZTMtOGE0Ni00Zjg5LWI1NDgtOTE1MWM2MWI5ZGM4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoidjJyYXkxLnpodWppY24yLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDExLjA5TWIiLCJhZGQiOiI1MS44MS4yMjMuNiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3BhdGgvMTIwMjA4MzAxNDIyIiwiaG9zdCI6Ind3dy40ODgxNjYyNi54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjY1MzkiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://a9b56b59-ee82-4331-91f8-955d1fdc4e10@nice-ca02.tiktokcdn.buzz:8443?allowInsecure=1#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20004
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjY4NzQiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiX1VTX3dtdCg5LjI5KV8xMiIsImFkZCI6IjU1LjcyaW1nLnh5eiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDIzYjRhMmItOTg3Zi00NmE3LTkyMjItNzc2ODM5MTE3YjNhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiNTUuNzJpbWcueHl6IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoifDE2LjAxTWIiLCJhZGQiOiI1MS44MS4yMjMuMjUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmZsaWVzd2ltaW5nLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA5MjYyNzEiLCJhZGQiOiIxMzguMi4xNS4yMyIsInBvcnQiOiI0NjM3MCIsInR5cGUiOiJub25lIiwiaWQiOiI5OTgxNTFlNS0wYmM1LTQzNzctZTM5MC1jNDFiYjI2ZmRkMGMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii91c2VycyIsImhvc3QiOiJzZ3AxLnRpZmEucHJvIiwidGxzIjoiIn0=

</details>

### 所有节点
合并节点总数: `6095`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `116`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `143`
- [freefq/free](https://github.com/freefq/free), 节点数量: `47`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3583`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `256`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `49`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `41`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `47`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `49`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `281`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `268`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `41`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `33`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `42`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `41`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `331`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `222`

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