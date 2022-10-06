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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIxMjgzIiwiYWRkIjoiMTM3LjE4NC42Ny4yMzIiLCJwb3J0IjoiNDM2MzIiLCJ0eXBlIjoidm1lc3MiLCJpZCI6IjA2NGY2OGM3LTkyNDUtNGYyNy05ZDJmLTQ3YTYzMGFhMzEwMyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2FyaWVzIiwiaG9zdCI6Imx1eC5qdXN0dS5tbCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIxNjM3IiwiYWRkIjoiMTM3LjE4NC42Ny4yMzIiLCJwb3J0IjoiNDM2MzIiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDY0ZjY4YzctOTI0NS00ZjI3LTlkMmYtNDdhNjMwYWEzMTAzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvNDA4IiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwiYWRkIjoidGV4dDMueGJ5d3djcC51cyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiI4M2RlYzk4OS1mZWEwLTMyNTMtOTVmYS03OWM4MGJjNWRhMGQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2EuMTg5LmNuIiwiaG9zdCI6ImJhaWR1LmNvbSIsInRscyI6IiJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20061
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@188.241.176.18:50000#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD_7
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@188.241.176.18:50000#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDI3NTQiLCJhZGQiOiJ2dXM0LjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDI3NTQiLCJhZGQiOiJ2dXM0LjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDI3NTQiLCJhZGQiOiJ2dXM0LjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20061
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDIwMTMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDgiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDYiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoiaHR0cCIsInBhdGgiOiIvIiwiaG9zdCI6IjE1OC4xMDEuMTkuMTcyIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@82.102.30.211:50000#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDgiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20024
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDYiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoiaHR0cCIsInBhdGgiOiIvIiwiaG9zdCI6IjE1OC4xMDEuMTkuMTcyIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20038
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDIwMTMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@129.146.242.130:443?allowInsecure=1#mianfeifq%20%7C%F0%9F%87%BA%F0%9F%87%B8_US_wmt%2810.4%29_24
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#%7C23.09Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDciLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDM3IiwiYWRkIjoiMTk4LjQxLjIxMi4zMCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTA1YzYzNWYtOTE4ZC00YjJhLThjOWQtZDU0MjZlOTRlYjRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoibGcyLnpodWppY24yLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDciLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDIwMDgiLCJhZGQiOiIxNDEuMTAxLjExNS4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiJhNWJhOGIyYi04ZmM1LTQ1MjEtYTM1ZS05MjgxYmU2MWMxYzMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzEuemh1amljbjIuY29tIiwidGxzIjoidGxzIn0=
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20037
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNTciLCJhZGQiOiJ2dXMyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoifDIzLjUyTWIiLCJhZGQiOiIxMDcuMTczLjgzLjIxNCIsInBvcnQiOiIzNzU0MSIsInR5cGUiOiJub25lIiwiaWQiOiJlZjU5YTU4Ni0wNTMyLTQ3NjMtZjM1My05NDhlYjQxM2YwMGQiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoiMTkyLjIxMC4yMDcuMjEzIiwicG9ydCI6IjU4MDYiLCJ0eXBlIjoiaHR0cCIsImlkIjoiMTNiNzMxMTQtZjNhNC00YTFhLWYwODMtYjQ2MjFjZjczMjc1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjE5Mi4yMTAuMjA3LjIxMyIsInRscyI6IiJ9
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.194:443#GB_07
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwNSIsImFkZCI6IjEwNy4xNzMuODMuMjE0IiwicG9ydCI6IjM3NTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImVmNTlhNTg2LTA1MzItNDc2My1mMzUzLTk0OGViNDEzZjAwZCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.197:443#GB_06
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.78:443#GB_07
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxNSIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvdjJyYXkiLCJob3N0IjoiYXVzMDEucGFvcGFvY2xvdWQuY3lvdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDI2ODMiLCJhZGQiOiJjYS4wMTEyMjMzLnh5eiIsInBvcnQiOiI4NDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMzMDAwZTlkLWJlZTctNGZkYi1iMzEyLWRkMDcwMzBmMzI1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvaG9tZSIsImhvc3QiOiJjYS4wMTEyMjMzLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwMiIsImFkZCI6IjEwNy4xNzMuODMuMjE0IiwicG9ydCI6IjM3NTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImVmNTlhNTg2LTA1MzItNDc2My1mMzUzLTk0OGViNDEzZjAwZCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ4aWFvLm1pYW9nZS5nYXkiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.197:443#%F0%9F%87%AC%F0%9F%87%A7%20%E8%8B%B1%E5%9B%BD%20007
    ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@212.102.53.78:443#%F0%9F%87%AC%F0%9F%87%A7%20%E8%8B%B1%E5%9B%BD%20008
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMyIsImFkZCI6IjEwNy4xNzMuODMuMjE0IiwicG9ydCI6IjM3NTQxIiwidHlwZSI6ImF1dG8iLCJpZCI6ImVmNTlhNTg2LTA1MzItNDc2My1mMzUzLTk0OGViNDEzZjAwZCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNDkiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    trojan://012fc57b-69e5-3924-9da4-d6ac132c5fc9@98.126.214.30:19234?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20029
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@3.99.152.11:50000#%F0%9F%87%A8%F0%9F%87%A6%20Quark%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvMTIzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiR0JfNjQuMjI3LjQzLjE2OF8xMDA1N2VlOS03NDMiLCJhZGQiOiI2NC4yMjcuNDMuMTY4IiwicG9ydCI6IjgwIiwidHlwZSI6ImF1dG8iLCJpZCI6IjA3ZDNjMTMyLWU4YjYtNDY4NS1iNDM2LWZmYTNhOGUyZTgyYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cg6Iux5Zu9XzEwMDIwNDIiLCJhZGQiOiJ2dWsyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVrMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71JbnRlcmxhbmQgOSIsImFkZCI6IjY0LjIyNy40My4xNjgiLCJwb3J0IjoiODAiLCJ0eXBlIjoiYXV0byIsImlkIjoiMDdkM2MxMzItZThiNi00Njg1LWI0MzYtZmZhM2E4ZTJlODJiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20036
    trojan://null@34.221.34.74:443?allowInsecure=1#US_34.221.34.74_10057ee9-165
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgNzI4IiwiYWRkIjoiMjMuMjMwLjE0Ni4yNTQiLCJwb3J0IjoiMTI1OCIsInR5cGUiOiJhdXRvIiwiaWQiOiJlZGViNDFjYy1hNzZhLTQ3ZjItZmE5Ni1iOTE0MWU2NmEyYjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@97.64.122.63:253#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNTciLCJhZGQiOiJ2dXMyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwMyIsImFkZCI6IjEwNy4xNzMuODMuMjE0IiwicG9ydCI6IjM3NTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6ImVmNTlhNTg2LTA1MzItNDc2My1mMzUzLTk0OGViNDEzZjAwZCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3BhdGgvMDUxMTExMjMwOTEwIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@78.129.253.9:809#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNTciLCJhZGQiOiJ2dXMyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    trojan://null@nice-us01.tiktokcdn.buzz:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20038
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNTciLCJhZGQiOiJ2dXMyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIxMTgyIiwiYWRkIjoidnVzMi4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czIuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%207%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDE0IiwiYWRkIjoicWlxaXMuY2YiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRlNmQxNTNjLWU1YjItNDkxMS1iYzcyLWUxMWM2NGYzY2U5MyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYjM1NmE0LyIsImhvc3QiOiIxZGNlbGlzLnFpcWlzLm1sIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoiMTk4LjQxLjIxMi4yMCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTViYThiMmItOGZjNS00NTIxLWEzNWUtOTI4MWJlNjFjMWMzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9kb25ndGFpd2FuZy5jb20iLCJob3N0IjoibGcxLnpodWppY24yLmNvbSIsInRscyI6InRscyJ9
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20021
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDI3NTciLCJhZGQiOiJ2ZGUyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmRlMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMTMiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMSIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii92MnJheSIsImhvc3QiOiJhdXMwMS5wYW9wYW9jbG91ZC5jeW91IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwMSIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoiYXV0byIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDIwMDgiLCJhZGQiOiIxNDEuMTAxLjExNS4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJhdXRvIiwiaWQiOiJhNWJhOGIyYi04ZmM1LTQ1MjEtYTM1ZS05MjgxYmU2MWMxYzMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Rvbmd0YWl3YW5nLmNvbSIsImhvc3QiOiJsZzEuemh1amljbjIuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzEwMDIwMzYiLCJhZGQiOiJxaXFpcy5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGU2ZDE1M2MtZTViMi00OTExLWJjNzItZTExYzY0ZjNjZTkzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9iMzU2YTQvIiwiaG9zdCI6IjFkY2VsaXMucWlxaXMubWwiLCJ0bHMiOiJ0bHMifQ==
    trojan://9ccc0c60-9df8-45a3-9886-c2765a52ba2e@ge-03.tiktokcdn.sbs:443?allowInsecure=1#%F0%9F%87%A9%F0%9F%87%AA%20DE%202%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoiMTkyLjIxMC4yMDcuMjEzIiwicG9ydCI6IjU4MDYiLCJ0eXBlIjoiaHR0cCIsImlkIjoiMTNiNzMxMTQtZjNhNC00YTFhLWYwODMtYjQ2MjFjZjczMjc1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjE5Mi4yMTAuMjA3LjIxMyIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@3.99.152.11:50000#%F0%9F%87%A8%F0%9F%87%A6%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOQ@193.108.118.202:50000#%F0%9F%87%A9%F0%9F%87%AA%20%E5%BE%B7%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cgR0IgMyB8IFRHOkBBaXJwcm94aWVzIiwiYWRkIjoic2hvcGlmeS5jb20iLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzZiZDk5NjktYmI5Ni00YmRkLWE2ZGYtOTYwYmJkOGU0NDM5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hcmllcyIsImhvc3QiOiJ0Z3VrLmNsb3VkZmxhcmUucXVlc3QiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDE3IiwiYWRkIjoiMTcyLjY0LjE1NS4yMDAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImE4MDMwYWZkLTgxMmEtNGFmZS1hNzY2LTljNzZmZjNlZGRkNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImxnNC56aHVqaWNuMi5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDI3NTQiLCJhZGQiOiJ2dXM0LjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzNC4wYmFkLmNvbSIsInRscyI6InRscyJ9
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%203%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwMjkiLCJhZGQiOiJ4aWV4aS50ayIsInBvcnQiOiIyMDk2IiwidHlwZSI6ImF1dG8iLCJpZCI6IjM3NTUxY2EwLThjYzMtNDMyZi1jYTFmLTgyYWJhMWRiM2VmOSIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ4aWV4aS50ayIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwNTEiLCJhZGQiOiI2NC4xMTIuNDIuNzIiLCJwb3J0IjoiMTY5OTkiLCJ0eXBlIjoiYXV0byIsImlkIjoiYjVhMDFmNDQtYjk4MS00MjFhLWJkYzAtNmQ5ZDUzZGEwN2ZkIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDE3IiwiYWRkIjoiMTcyLjY0LjE1NS4yMDAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImE4MDMwYWZkLTgxMmEtNGFmZS1hNzY2LTljNzZmZjNlZGRkNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZG9uZ3RhaXdhbmcuY29tIiwiaG9zdCI6ImxnNC56aHVqaWNuMi5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzEwMDIwMjkiLCJhZGQiOiJ4aWV4aS50ayIsInBvcnQiOiIyMDk2IiwidHlwZSI6ImF1dG8iLCJpZCI6IjM3NTUxY2EwLThjYzMtNDMyZi1jYTFmLTgyYWJhMWRiM2VmOSIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ4aWV4aS50ayIsInRscyI6InRscyJ9

</details>

### 所有节点
合并节点总数: `5622`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `183`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `164`
- [freefq/free](https://github.com/freefq/free), 节点数量: `33`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `1`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3450`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `36`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `35`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `44`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `48`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `189`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `93`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `29`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `31`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `43`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `44`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `292`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `234`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `293`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `24`

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