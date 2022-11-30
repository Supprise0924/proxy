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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUuZ2E0NDMt6KKr5aKZLeS4rei9rDE1Mi42OS4yMjkuMjIyLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIiwiYWRkIjoiYW1ka3IucHR1dS5nYSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYTYxMmI2N2YtYTc5Yi00YTcxLWE4MmItYTQ2OTA2NzUyMDIzIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii80MDgiLCJob3N0IjoiYW1ka3IucHR1dS5nYSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUubWw0NDMt6KKr5aKZLeS4rei9rDE0Ni41Ni45Ni43NS3op6PplIHpn6nlm73lnLDljLpORumdnuiHquWItuWJpyIsImFkZCI6ImFtZGtyLnB0dXUubWwiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImUyY2RjMzA1LWRkYTctNDY1ZS1iNjc1LWJhMDQ2OGQyYThiMyIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvOTg3IiwiaG9zdCI6ImFtZGtyLnB0dXUubWwiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wg576O5Zu9LXZtZXNzLWNhLjAxMTIyMzMueHl6ODQ0My3ooqvlopkt5Lit6L2sMTk5Ljg3LjIxMC4xODYt6Kej6ZSB5paw5Yqg5Z2h5Zyw5Yy6TkbpnZ7oh6rliLbliacgMiIsImFkZCI6ImNhLjAxMTIyMzMueHl6IiwicG9ydCI6Ijg0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzMwMDBlOWQtYmVlNy00ZmRiLWIzMTItZGQwNzAzMGYzMjVkIiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii9ob21lIiwiaG9zdCI6ImNhLjAxMTIyMzMueHl6IiwidGxzIjoidGxzIn0=
    ssr://MTE5LjIzNy4xOTUuMjMwOjU0MzphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhyZkNmaDdBZ0xlbW1tZWE0cnkweE1Ua3VNak0zTGpFNU5TNHlNekEmb2Jmc3BhcmFtPSZwcm90b3BhcmFtPQ
    ssr://NDIuOTguMjcuMTgzOjU0MzphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhyZkNmaDdBZ0xlbW1tZWE0cnkwME1pNDVPQzR5Tnk0eE9ETSZvYmZzcGFyYW09JnByb3RvcGFyYW09TlRFek5qRTZOamR0WmtsVWIwdzRORkJ1V25Fd1pB
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0xMC5kb3VsdW9zLmljdSIsImFkZCI6IjEwLmRvdWx1b3MuaWN1IiwicG9ydCI6IjUzMDEwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU1ZjlhZjFiLTNhOGQtMzhmZC1hZDgzLWIwYTUwZTIyMWIxZiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2hvbWUiLCJob3N0IjoiY2EuMDExMjIzMy54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0yMTkuNzYuMTMuMTgwIiwiYWRkIjoiMjE5Ljc2LjEzLjE4MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiODFkOTNmNjItMTVhMi00OTk0LWFkYjktMGI1ZDkwNmFhYzdlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidGd1bml2c3Rhci4xNjgtMTM4LTk0LTE5NC5zc2xpcC5pbyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry00Ny4yNDIuMzAuNzMiLCJhZGQiOiI0Ny4yNDIuMzAuNzMiLCJwb3J0IjoiNTcxOTQiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTkwZjlmNzItMDE0NC00MGMyLTg2MmItOGM3ZmJlN2ZjMzRhIiwiYWlkIjoiMCIsIm5ldCI6Imh0dHAiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1mcmVlLnNnMi5zZnNhLmNmIiwiYWRkIjoiZnJlZS5zZzIuc2ZzYS5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTVmNGVjMzItMzczNS00NTIxLWFjZjItZjU5YWU3ODYyNjMzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiY2RpbWFnZS5kZWJpYW4ub3JnIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oazExLnNhbmZlbjAwMS5waWNzIiwiYWRkIjoiaGsxMS5zYW5mZW4wMDEucGljcyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTdlNzNlMWQtMjQxOC00NzY2LTg4MzEtZDFiM2I4M2NjODc3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3Lm1pY3Jvc29mdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcDAzLXZtMC5lbnRyeS5zcnRoZHcuYXJ0IiwiYWRkIjoianAwMy12bTAuZW50cnkuc3J0aGR3LmFydCIsInBvcnQiOiI0NDciLCJ0eXBlIjoibm9uZSIsImlkIjoiY2Y4NDRjOTQtNDBjZC0zNzc0LThjZDMtZjFmNzU1ODBhNGJiIiwiYWlkIjoiMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoieW91dHViZS1hd2Vpa2VqaSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzAzLjE3MDIwMy54eXoiLCJhZGQiOiJzZzAzLjE3MDIwMy54eXoiLCJwb3J0IjoiNDM1NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDc1NzhmMjYtMTAwOS00YzMxLThjNGQtZmM0NmYxZWVmNTVmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoic2cwMy4xNzAyMDMueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzIudnBuamFudGl0LmNvbSIsImFkZCI6InNnMi52cG5qYW50aXQuY29tIiwicG9ydCI6IjEwMDAwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFmYzMyMTNhLTU5ZGUtMTFlZC1hMDU3LTgzMmU5NDNjYTE2ZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InNnMi52cG5qYW50aXQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZ2F3cy4zMzMyMTAueHl6IiwiYWRkIjoic2dhd3MuMzMzMjEwLnh5eiIsInBvcnQiOiI1MDM4MSIsInR5cGUiOiJub25lIiwiaWQiOiI2OWNkZjFlMi1mYjE0LTQ2ZjQtYjc5MS0yNTc3NWI0MmMxMjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoic2cyLnZwbmphbnRpdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC10Z3VuaXZzdGFyLTE4NS0xNjAtMjYtMTE0LnNzbGlwLmlvIiwiYWRkIjoidGd1bml2c3Rhci0xODUtMTYwLTI2LTExNC5zc2xpcC5pbyIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJkN2YyYjU5Mi0yZTU2LTRhMTItOGYyNC0yMGY1NWI0MjJlZjIiLCJhaWQiOiI2NCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoidm4zLnRoYW5oaGFpdnBuLm5hbWUudm4iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvemmluWwlC0xOTMuMTIyLjExNS41MSIsImFkZCI6IjE5My4xMjIuMTE1LjUxIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjOWQ1ZjlmMS0xYmZkLTRiMTItOTdiZS0wZmEzYjA1YWI4NDUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuamltZW5nc3JvLmNmIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNmEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDZhLnJ1aTc3LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTVkY2IxMTgtODhmNi00NGU4LTg5NWEtMTc3MDQ3OWFiOGRjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5qaW1lbmdzcm8uY2YiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0xMzguMi44My4yMTciLCJhZGQiOiIxMzguMi44My4yMTciLCJwb3J0IjoiNDM4NjMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2E5ODQ0NTctYjAxNy00NmU1LWQ5NzMtNDJhM2MzZmRjMjkyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5qaW1lbmdzcm8uY2YiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0xMzkuMTYyLjE2LjIyOCIsImFkZCI6IjEzOS4xNjIuMTYuMjI4IiwicG9ydCI6IjQwNzcxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjYxMTk0ODEwLTUxOTMtNDhiYy1lYjBhLTc5NzhhMDU5ZDY4MSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuamltZW5nc3JvLmNmIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS0xMy4yNTAuMzEuNTAiLCJhZGQiOiIxMy4yNTAuMzEuNTAiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTdlNzNlMWQtMjQxOC00NzY2LTg4MzEtZDFiM2I4M2NjODc3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS01NC4yNTEuMTI5Ljc2IiwiYWRkIjoiNTQuMjUxLjEyOS43NiIsInBvcnQiOiIxODA4MiIsInR5cGUiOiJub25lIiwiaWQiOiI3NDk2OTY0Zi1iNTM1LTQyNjYtOTAzZS04NWM5ODZhMTU4NGEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1mcmVlLnNnMS5zZnNhLmNmIiwiYWRkIjoiZnJlZS5zZzEuc2ZzYS5jZiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2YwYjNiNmItZWFhMy00MjFmLWI0YjktYTFmMGIyMmVjMDAxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiY2RpbWFnZS5kZWJpYW4ub3JnIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzgwLTIuc2FuZmVuMDAxLnBpY3MiLCJhZGQiOiJzZzgwLTIuc2FuZmVuMDAxLnBpY3MiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTdlNzNlMWQtMjQxOC00NzY2LTg4MzEtZDFiM2I4M2NjODc3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiYS4xODkuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgLeaWsOWKoOWdoS1zZzExLmNsb3VkZmFzdC52biIsImFkZCI6InNnMTEuY2xvdWRmYXN0LnZuIiwicG9ydCI6IjgwIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdhYTkwYzM3LTg5MjgtNGIyNy1hZGJlLThlNzE1N2ZmZjdhMiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InNnMTEuY2xvdWRmYXN0LnZuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry0yMC4xODcuNzAuNDYiLCJhZGQiOiIyMC4xODcuNzAuNDYiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDk0ZTk5YmMtMDllZS00YTU5LWJlNmItOTFhZjgxYmNmYWQ5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry02MS45Mi4xODkuOTgiLCJhZGQiOiI2MS45Mi4xODkuOTgiLCJwb3J0IjoiMzk5OTkiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjdjNTBmNmEtODE2ZC0zNTU1LTg5YjQtMTlkZDI5NjA4ZjhiIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1oazQuY3pzMTAwMC5jb20iLCJhZGQiOiJoazQuY3pzMTAwMC5jb20iLCJwb3J0IjoiMjI4NSIsInR5cGUiOiJub25lIiwiaWQiOiJjNjlhNTJjMi00NjczLTQ2MzctODdlNC1hMDYwM2M5MjBmNTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiaGs0LmN6czEwMDAuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgLemmmea4ry1zYy5kemR2LmNuIiwiYWRkIjoic2MuZHpkdi5jbiIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiIxY2JhMjJkYy1jOTQyLTQ1ZGMtYWI1My01Y2ZjMDRlZjg1MjAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAzNGEucnVpNzcuY29tIiwiYWRkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMzRhLnJ1aTc3LmNvbSIsInBvcnQiOiIxMjM1NiIsInR5cGUiOiJub25lIiwiaWQiOiIxNWRjYjExOC04OGY2LTQ0ZTgtODk1YS0xNzcwNDc5YWI4ZGMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiYS4xODkuY24iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNzIuMTA0LjExMi4xNTkiLCJhZGQiOiIxNzIuMTA0LjExMi4xNTkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY3ZmQwM2U1LTU0NDYtNDVjOS1hYzU3LTVhNWY0NjVmNDI1MSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC0xNzIuMTA0LjExMi4xNzkiLCJhZGQiOiIxNzIuMTA0LjExMi4xNzkiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY3ZmQwM2U1LTU0NDYtNDVjOS1hYzU3LTVhNWY0NjVmNDI1MSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJhLjE4OS5jbiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1mMWYzMjI3LnY1LmdsYWRvcy1jb25maWcubmV0IiwiYWRkIjoiZjFmMzIyNy52NS5nbGFkb3MtY29uZmlnLm5ldCIsInBvcnQiOiIzMzMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU3ZTBjYjRkLWVhZTUtNDhlYy04MDkxLTE0OWRjMmIzMDllMCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6InN0bXAuMTYzLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgLeaXpeacrC1qcC4zMzMyMTAueHl6IiwiYWRkIjoianAuMzMzMjEwLnh5eiIsInBvcnQiOiI0NTAwNSIsInR5cGUiOiJub25lIiwiaWQiOiI2OWNkZjFlMi1mYjE0LTQ2ZjQtYjc5MS0yNTc3NWI0MmMxMjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoic3RtcC4xNjMuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cgLemfqeWbvS1rci4zMzMyMTAueHl6IiwiYWRkIjoia3IuMzMzMjEwLnh5eiIsInBvcnQiOiI0NTAwNCIsInR5cGUiOiJub25lIiwiaWQiOiI2OWNkZjFlMi1mYjE0LTQ2ZjQtYjc5MS0yNTc3NWI0MmMxMjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoic3RtcC4xNjMuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh7MgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbveWPsOa5vihUVylUYWl3YW4vQ2l0eU9mZmljZV8yIiwiYWRkIjoiNjEuMjIyLjIwMi4xNDAiLCJwb3J0IjoiMzM3OTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTU1Y2QxODItMDFiMC00ZmI3LWE1MTAtMzYzNzAxYTQ5MWM1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbvemmmea4ry/kuK3lm73lj7Dmub4oQ04pQ2hpbmEvU2hlbnpoZW4vKOWPr+iDveaYr+S4rei9rOiKgueCuSlfMyIsImFkZCI6IlYxMDQuYmdwbmV0LnRvcCIsInBvcnQiOiIyNjEwNCIsInR5cGUiOiJub25lIiwiaWQiOiJlZjM2MWM4My04Yjg5LTM5NTAtOWM5Yi02Y2NjMTc3ZTYyODUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2FkbWluIiwiaG9zdCI6IlYxMDQuYmdwbmV0LnRvcCIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1nY206ZTB1eWFrZW5kZzc@x.gotout.work:30031#%F0%9F%87%AD%F0%9F%87%B0%20%5B09-26%5D%7Copenrunner%7C%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF%2F%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%28CN%29China%2FShenzhen%2F%28%E5%8F%AF%E8%83%BD%E6%98%AF%E4%B8%AD%E8%BD%AC%E8%8A%82%E7%82%B9%29_4
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuPCfh6wgWzA5LTI2XXxvcGVucnVubmVyfOaWsOWKoOWdoShTRylTaW5nYXBvcmUvU2luZ2Fwb3JlXzciLCJhZGQiOiJ2Mi0yLmdvZGxpZ2h0Lnh5eiIsInBvcnQiOiIzMDUyNiIsInR5cGUiOiJub25lIiwiaWQiOiI0MzMwOGQyNy05NGVjLTQwOGUtYThmNi1kNjgyY2ZiOTljYTkiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLzU0ZjYzNGZzIiwiaG9zdCI6InYyLTIuZ29kbGlnaHQueHl6IiwidGxzIjoidGxzIn0=
    trojan://7Z29DRr1ts@cp-asus.ml:50275?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20%5B09-26%5D%7Copenrunner%7C%E6%96%B0%E5%8A%A0%E5%9D%A1%28SG%29Singapore%2FSingapore_8
    trojan://c19d1432-8b3e-4818-8837-3d160cf65908@jgwdb2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan%2FOsaka_9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrfCfh7AgWzA5LTI2XXxvcGVucnVubmVyfOS4reWbvemmmea4ry/kuK3lm73lj7Dmub4oQ04pQ2hpbmEvQmVpamluZy8o5Y+v6IO95piv5Lit6L2s6IqC54K5KV8xMCIsImFkZCI6InNoY3UuZm9yZ2VidWtraXQuY29tIiwicG9ydCI6IjQ3Mzg5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImY2ODBkZmQ4LTNiNTktNDhhZi1hZWE4LTFkNGJjMDlhMTcwNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJzaGN1LmZvcmdlYnVra2l0LmNvbSIsInRscyI6IiJ9
    trojan://cfbabf31-2cf6-40ca-9688-abbb682370aa@cn.speedabc.xyz:32002?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%F0%9F%87%AD%F0%9F%87%B0%20%5B09-26%5D%7Copenrunner%7C%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF%2F%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%28CN%29China%2FShenzhen%2F%28%E5%8F%AF%E8%83%BD%E6%98%AF%E4%B8%AD%E8%BD%AC%E8%8A%82%E7%82%B9%29_25
    trojan://e5d46365e25e31d94279c2bcf93390a2@sg-sr-116.mitoption.com:443?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20%5B09-26%5D%7Copenrunner%7C%E6%96%B0%E5%8A%A0%E5%9D%A1%28SG%29Singapore%2FSingapore_28
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7UgWzA5LTI2XXxvcGVucnVubmVyfOaXpeacrChKUClKYXBhbi9Ub2t5b18yOSIsImFkZCI6IjE0MC4yMzguNDguMTk0IiwicG9ydCI6Ijg4ODgiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjRmMWRmYWQtMTI2Ny00Mjk3LThlODgtMGU5YjhlZjQ3ZTQ3IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNjcuMjM1LjE5Mi4wIiwiYWRkIjoiMTY3LjIzNS4xOTIuMCIsInBvcnQiOiIyNTA1MiIsInR5cGUiOiJub25lIiwiaWQiOiJjYmVmZjRjZS1hZGNiLTRlMjUtYTQyYi1iNGU1NDYzYjBkOTMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsPCfh7cg576O5Zu9LXZtZXNzLWFtZGtyLnB0dXUuZ2E0NDMt6KKr5aKZLeS4rei9rDE1Mi42OS4yMjkuMjIyLeino+mUgemfqeWbveWcsOWMuk5G6Z2e6Ieq5Yi25YmnIDIiLCJhZGQiOiJhbWRrci5wdHV1LmdhIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhNjEyYjY3Zi1hNzliLTRhNzEtYTgyYi1hNDY5MDY3NTIwMjMiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiLzQwOCIsImhvc3QiOiJhbWRrci5wdHV1LmdhIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6OWQ2Y2NlYWEzNzNiZjJjOGFjYjIyZTYwYjZhNThiZTY@45.33.88.190:443#%F0%9F%87%BA%F0%9F%87%B8%20-%E7%BE%8E%E5%9B%BD-45.33.88.190
    ssr://dXMuaGUuMDYubmVrb2Nsb3VkLmNuOjE5MDM1OmF1dGhfYWVzMTI4X21kNTphZXMtMTI4LWNmYjpwbGFpbjphV3gxZFd4eWVuWnBhV3MvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUh1dkNmaDdnZ0xlZS1qdVdidlMxMWN5NW9aUzR3Tmk1dVpXdHZZMnh2ZFdRdVkyNCZvYmZzcGFyYW09TW1NME5tSTBNall4TXk1M2JuTXVkMmx1Wkc5M2N5NWpiMjAmcHJvdG9wYXJhbT1OREkyTVRNNk5HZDJjWGhZ
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xMS5kb3VsdW9zLmljdSIsImFkZCI6IjExLmRvdWx1b3MuaWN1IiwicG9ydCI6IjUxMDExIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ1NjFiZGEzLWE3NDUtMzcyYi04YTUzLWE1NzdiYmRiZTlkMiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLzQwOCIsImhvc3QiOiJhbWRrci5wdHV1LmdhIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNi5kb3VsdW9zLmljdSIsImFkZCI6IjE2LmRvdWx1b3MuaWN1IiwicG9ydCI6IjUzMDE2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRmMDQ5ZjZjLWQ0MmItMzQ5Mi1iZDM4LWYzZmYxMTdhOTRiYyIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLzQwOCIsImhvc3QiOiJhbWRrci5wdHV1LmdhIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNjIuMTU5LjE2MC4yMjQiLCJhZGQiOiIxNjIuMTU5LjE2MC4yMjQiLCJwb3J0IjoiMjA4NiIsInR5cGUiOiJub25lIiwiaWQiOiI5MDRkNzZmZi0yNDFiLTQxOGUtYjQyMC1iODE1MGVhZmJmNzAiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIwNDllNDI4ZC0yZjdmLTRhNzUtODNjOS00MjQxZGU4MjQxYTEuNjU3NzYxNy54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzIuNjcuMi4xMzkiLCJhZGQiOiIxNzIuNjcuMi4xMzkiLCJwb3J0IjoiMjA1MyIsInR5cGUiOiJub25lIiwiaWQiOiJmZjgzOWFjMy1iZmVhLTRjOGEtYTc2MS1mYmJiNThjNTFjODMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNzIuNjcuMjEyLjY4IiwiYWRkIjoiMTcyLjY3LjIxMi42OCIsInBvcnQiOiIyMDUzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjU5MTIyZDM1LTg2MjItNDZiNi05MzhjLWFkZmFiOTJkNDZiYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImpwLTE4ODc4YTI0LTQ5ZDgtNGZiMi1hMWUzLWYzN2RjZTdjZjJhOC51cDIyLnRrIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMC4yMDUuMTIuOTgiLCJhZGQiOiIyMC4yMDUuMTIuOTgiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ5Njk2NGYtYjUzNS00MjY2LTkwM2UtODVjOTg2YTE1ODRhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMTYuNzMuMTU4LjIzIiwiYWRkIjoiMjE2LjczLjE1OC4yMyIsInBvcnQiOiI2MDA4OSIsInR5cGUiOiJub25lIiwiaWQiOiI2N2ZkMDNlNS01NDQ2LTQ1YzktYWM1Ny01YTVmNDY1ZjQyNTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yMi5kb3VsdW9zLmljdSIsImFkZCI6IjIyLmRvdWx1b3MuaWN1IiwicG9ydCI6IjMzMDIyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ3ZDI4ZGI2LTI0MWUtMzQwMS1hNDE0LTBjMzc2ZmRiYWE2MiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIyMi5kb3VsdW9zLmljdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0yOS5kb3VsdW9zLmljdSIsImFkZCI6IjI5LmRvdWx1b3MuaWN1IiwicG9ydCI6IjU2MTI5IiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ1NjFiZGEzLWE3NDUtMzcyYi04YTUzLWE1NzdiYmRiZTlkMiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIyOS5kb3VsdW9zLmljdSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0zLjc2Ljc1LjYxIiwiYWRkIjoiMy43Ni43NS42MSIsInBvcnQiOiI4MDgxIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijc5NDg5ODBkLTk4ZDYtNDRlZi04YjM2LWI0NGVkMTEzNTk0MCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS05Lm14eXVuMS50b3AiLCJhZGQiOiI5Lm14eXVuMS50b3AiLCJwb3J0IjoiNDExMDkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZDUxZDRjMDItMmU4OS0zODdkLTk2MzUtMDdmYjhiMWQ1NjcxIiwiYWlkIjoiMiIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjkubXh5dW4xLnRvcCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1jYW4wMS5jZi5zc3J1Ny5jYXNhIiwiYWRkIjoiY2FuMDEuY2Yuc3NydTcuY2FzYSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTY3MjNkZmEtNmFlNC0zOGM3LWFjODMtZTNiZDY3YjllMTJkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiY2FuMDEucGFvcGFvY2xvdWQuY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1haC55ZDAxLnNzcnU3LmNhc2EiLCJhZGQiOiJhaC55ZDAxLnNzcnU3LmNhc2EiLCJwb3J0IjoiMTAwMDciLCJ0eXBlIjoibm9uZSIsImlkIjoiMzNlMWM3MmQtM2NmYi0zN2VlLTliYzgtYjU0YzdkMjM1Yjg2IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0Ijoic3NydS52Mi5qcDAxLjJ5dW4ud2luIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1hdXMwMS5jZi5zc3J1Ny5jYXNhIiwiYWRkIjoiYXVzMDEuY2Yuc3NydTcuY2FzYSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNTE3OTc4ODItYzhlZi0zZjNjLTgzYjUtOTA5ZTliZjEwODM0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiYXVzMDEucGFvcGFvY2xvdWQuY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1hemhrMDIuYWpka2phbGpkai54eXoiLCJhZGQiOiJhemhrMDIuYWpka2phbGpkai54eXoiLCJwb3J0IjoiMzY0MDIiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2FkMjNjYTAtMzM2YS0zNDYzLWE0YjQtNDRjMWVjZTk2YjMwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoibGl2ZS5iaWxpYmlsaS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1nZXIwMS5jZi5wYW9wYW9jbG91ZC5jeW91IiwiYWRkIjoiZ2VyMDEuY2YucGFvcGFvY2xvdWQuY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGZlYjRlYTktYmNhYS0zMmMyLWJiZGQtYjNkMTNkZGRiNjEyIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2VyMDEuc3NydTQuZnVuIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1rcjEuY3pzMTAwMC5jb20iLCJhZGQiOiJrcjEuY3pzMTAwMC5jb20iLCJwb3J0IjoiODg4NyIsInR5cGUiOiJub25lIiwiaWQiOiI4MmI0MzhiYS05YzA4LTQ2OWUtYmRiNy1iMTE5NzBkYTNmZTIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2VyMDEuc3NydTQuZnVuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1rcjIuY3pzMTAwMC5jb20iLCJhZGQiOiJrcjIuY3pzMTAwMC5jb20iLCJwb3J0IjoiNjY4OCIsInR5cGUiOiJub25lIiwiaWQiOiIzOGYwMWFhZS1lZGI5LTQzZDMtOTYwOS00OWJmNmFkY2ZiZjkiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2VyMDEuc3NydTQuZnVuIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1oazEuY3pzMTAwMC5jb20iLCJhZGQiOiJoazEuY3pzMTAwMC5jb20iLCJwb3J0IjoiNDQ2NiIsInR5cGUiOiJub25lIiwiaWQiOiI4ODIxN2Y1OS1kOTZlLTQ3OGEtODJjOS00MmM0MmMyNzJiZTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiZ2VyMDEuc3NydTQuZnVuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS1tZWkubW9vb29vYmFpLnRvcCIsImFkZCI6Im1laS5tb29vb29iYWkudG9wIiwicG9ydCI6IjUxMjIiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzAwMGY2OGYtY2JjYi0zMWUxLTljYjQtODk3ODAzZjJlZGMzIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoibWVpLm1vb29vb2JhaS50b3AiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMTAt5LuY6LS55o6o6I2Qc3VvLnl0L3NzcnN1YiIsImFkZCI6IjE3Mi42NC4xNTQuMjIyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJmY2ZhZWM5MS02MDk2LTQ0ZDgtOTU2Yy03ODY4ZDllODc0YjEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzEuY2ZjZG4xLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMDEt5LuY6LS55o6o6I2Qc3VvLnl0L3NzcnN1YiIsImFkZCI6IjEwNi43NS4yMTguMTEyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MTY0NmY5YS1iNGU5LTRhY2EtYmZlMy04ODkyYjNlNThmZTciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJsZzMwLmNmY2RuMy54eXoiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTI1Ni1nY206RjViS2tiOWdna0x4NEpiUXJiTG43TGpa@198.8.92.84:44945#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%29%2048
    ssr://MTE2LjE2Mi4xMjAuNDM6NTY1OmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNDBNdyZvYmZzcGFyYW09ZEM1dFpTOTJjRzVvWVhRJnByb3RvcGFyYW09TWpjME5EVTZhbWRxWjJwbmFtZHFaMnBu
    ssr://MTE2LjE2Mi4xMjAuNDc6NTYxOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNDBOdyZvYmZzcGFyYW09WkVNMWRGcFRPVEpqUnpWdldWaFImcHJvdG9wYXJhbT1NVEV6TVRRNllXNTBhV2h2Y3pj
    ssr://MTE2LjE2Mi4xMjAuNDk6NTYwOmF1dGhfYWVzMTI4X21kNTpjaGFjaGEyMC1pZXRmOnBsYWluOmJXSnNZVzVyTVhCdmNuUS8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9TGVhNWx1V05sLWVjZ1MweE1UWXVNVFl5TGpFeU1DNDBPUSZvYmZzcGFyYW09JnByb3RvcGFyYW09
    ssr://MTE2LjEyOS4yNTMuNjozOTQzOTphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6cGxhaW46UjJoUmNrUlQvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhxUENmaDdNZ0xlV01sLVM2ck9XNGdpMHhNVFl1TVRJNUxqSTFNeTQyJm9iZnNwYXJhbT1kQzV0WlM5MmNHNW9ZWFEmcHJvdG9wYXJhbT1OekV3TURJNmIySXhTMmcy
    ssr://NDIuMTU3LjE5NS4yMzE6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNak14Jm9iZnNwYXJhbT1WRlZrV21Rd09WVmhla3BPVWtWRmVsUnVjR3BrVjFKeFUxaHdZV0Z0VWpGV1JsSkMmcHJvdG9wYXJhbT0
    ssr://NDIuMTU3LjE5NS4yMzk6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNak01Jm9iZnNwYXJhbT1NR1l3T1RrMk1EQTNOemN1ZGpJelpqZHVUVEEmcHJvdG9wYXJhbT1OakF3TnpjM09qRTFORlE0WWc
    ssr://NDIuMTU3LjE5NS4yNDQ6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNalEwJm9iZnNwYXJhbT1UVWRaZDA5VWF6Sk5SRUV6VG5wamRXUnFTWHBhYW1SMVZGUkJKU1h2djcwJnByb3RvcGFyYW09TmpBd056YzNPakUxTkZRNEpTWHZ2NzA
    ssr://NDIuMTU3LjE5NS4yNDU6MTIxMjc6YXV0aF9hZXMxMjhfc2hhMTphZXMtMjU2LWNmYjpodHRwX3NpbXBsZTpOamg0WkdkMU9XVjVhV1kvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVMaWM2STZlNWJpQ0xUUXlMakUxTnk0eE9UVXVNalExJm9iZnNwYXJhbT0mcHJvdG9wYXJhbT1OakF3TnpjM09qRTFORlE0WWc
    ssr://ODguMjEwLjM3LjEyNDo0MTAwODphdXRoX2FlczEyOF9zaGExOmNoYWNoYTIwLWlldGY6dGxzMS4yX3RpY2tldF9hdXRoOmVWQkxjbVY0V0dGV1RVRllSbVpsZWcvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUh0X0NmaDdvZ0xlU19oT2U5bC1hV3J5MDRPQzR5TVRBdU16Y3VNVEkwJm9iZnNwYXJhbT1NR1ZqTlRReU9EQTROQzVrYjNkdWJHOWhaQzUzYVc1a2IzZHpkWEJrWVhSbExtTnZiUSZwcm90b3BhcmFtPU1qZ3dPRFE2YTJZME4xaG0
    ssr://Y25nZGNtLmRlYnVnZXgueHl6OjU2MDphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjAtaWV0ZjpwbGFpbjpiV0pzWVc1ck1YQnZjblEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPUxlYTVsdVdObC1lY2dTMWpibWRrWTIwdVpHVmlkV2RsZUM1NGVYbyZvYmZzcGFyYW09JnByb3RvcGFyYW09TlRJNE56VTZRV0V4TVRJeU1URQ
    ssr://ZWR1YWxsLmJ1enpsaW5lLm9yZzo2MTI6YXV0aF9hZXMxMjhfbWQ1OmNoYWNoYTIwLWlldGY6cGxhaW46YldKc1lXNXJNWEJ2Y25RLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz1MZWE1bHVXTmwtZWNnUzFsWkhWaGJHd3VZblY2ZW14cGJtVXViM0puJm9iZnNwYXJhbT1WRmR3VDJKV2NIUlZWRTVPVmtWV01WbHNaSE5oYlU1MFQxaHdhVTFzYjNkVVJ6RlBaRzFLVWcmcHJvdG9wYXJhbT0
    ssr://aG4tMDEuY2N0ZWxlc2NvcGUueHl6OjExODUzOmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6YUVkclVUWTVNVFYwUkEvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVyVzM1WTJYNTV5QjVyVzM1WS1qNWJpQ0xXaHVMVEF4TG1OamRHVnNaWE5qYjNCbExuaDVlZyZvYmZzcGFyYW09WVdwaGVDNXRhV055YjNOdlpuUXVZMjl0JnByb3RvcGFyYW09TVRVeU1qY3hPa0Z4VTFBek9HNHhURmc
    ssr://aWQtMS5naXRvLmNjOjMzMjg6YXV0aF9hZXMxMjhfbWQ1OmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpPV2xtWVhOMC8_Z3JvdXA9VTFOU1VISnZkbWxrWlhJJnJlbWFya3M9NWJtXzVMaWM1NXlCNW8tdDZaaXo1YmlDTFdsa0xURXVaMmwwYnk1all3Jm9iZnNwYXJhbT0mcHJvdG9wYXJhbT0
    ssr://aWVwbDEubm5vb2RkZWUueHl6OjIwMzE6YXV0aF9hZXMxMjhfbWQ1OmNoYWNoYTIwLWlldGY6aHR0cF9zaW1wbGU6WTNoemMzSTVNVEUvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVyS3o1WTJYNTV5QjZhbTc2YW1zNWJxWDViaUNMV2xsY0d3eExtNXViMjlrWkdWbExuaDVlZyZvYmZzcGFyYW09Wm1VNU9UTTJOakF6TG0xcFkzSnZjMjltZEM1amIyMCZwcm90b3BhcmFtPU5qWXdNenBtYkVweGJFMA
    ssr://c2ctMS5naXRvLmNjOjgzMTphdXRoX2FlczEyOF9tZDU6YWVzLTI1Ni1jZmI6dGxzMS4yX3RpY2tldF9hdXRoOk9XbG1ZWE4wLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IdVBDZmg2d2dMZWF4bi1pTGotZWNnUzF6WnkweExtZHBkRzh1WTJNJm9iZnNwYXJhbT03Ny05YS0tX3ZlLV92VGMxNzctOTc3LTlNTy1fdldydnY3MTNibXh2Wi0tX3ZYZHBibXJ2djcxM2VlLV92WEx2djcxMjc3LTk3Ny05YjIwJnByb3RvcGFyYW09NzctOTI3bnZ2NzN2djcxNjc3LTlYSGd4WWUtX3ZlLV92ZS1fdlE
    ssr://c2hjdXp4aGsuZXVjZHVybC5tZTo1NjI6YXV0aF9hZXMxMjhfbWQ1OmNoYWNoYTIwLWlldGY6cGxhaW46YldKc1lXNXJNWEJ2Y25RLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IcVBDZmg3TWdMZVM0aXVhMXQtVzRnaTF6YUdOMWVuaG9heTVsZFdOa2RYSnNMbTFsJm9iZnNwYXJhbT1WRmR3VDJKV2NIUlZWRTVPVmtWV01WbHNaSE5oYlU1MFQxaHdhVTFzYjNkVVJ6RlBaRzFLVWcmcHJvdG9wYXJhbT1Oak00TURrNlUxWkpVRlJKV2pn
    ssr://cnMtMi5naXRvLmNjOjMzNDExOmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6T1dsbVlYTjAvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhxUENmaDdNZ0xlV01sLVM2ck9XNGdpMXljeTB5TG1kcGRHOHVZMk0mb2Jmc3BhcmFtPU9UUXdZekl6TURnMU5TNWtiM2R1Ykc5aFpDNTNhVzVrYjNkemRYQmtZWFJsTG1OdmJRJnByb3RvcGFyYW09TXpBNE5UVTZNRVoyV2xKNQ
    ssr://dHctMi5naXRvLmNjOjMzNDA1OmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6T1dsbVlYTjAvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPThKLUhxUENmaDdNZzVibV81TGljNTV5QjVibV81YmVlNWJpQ0xYUjNMVEl1WjJsMGJ5NWpZdyZvYmZzcGFyYW09NzctOWEtLV92ZS1fdlRjMTc3LTk3Ny05TU8tX3ZXcnZ2NzEzYm14dlotLV92WGRwYm1ydnY3MTNlZS1fdlhMdnY3MTI3Ny05NzctOWIyMCZwcm90b3BhcmFtPTc3LTkyN252djczdnY3MTY3Ny05WEhneFllLV92ZS1fdmUtX3ZR
    ssr://dXMtNS5naXRvLmNjOjY1MTphdXRoX2FlczEyOF9tZDU6YWVzLTI1Ni1jZmI6dGxzMS4yX3RpY2tldF9hdXRoOk9XbG1ZWE4wLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz04Si1IdXZDZmg3Z2dMZVc1di1TNG5PZWNnUzExY3kwMUxtZHBkRzh1WTJNJm9iZnNwYXJhbT03Ny05YS0tX3ZlLV92VGMxNzctOTc3LTlNTy1fdldydnY3MTNibXh2Wi0tX3ZYZHBibXJ2djcxM2VlLV92WEx2djcxMjc3LTk3Ny05YjIwJnByb3RvcGFyYW09NzctOTI3bnZ2NzN2djcxNjc3LTlYSGd4WWUtX3ZlLV92ZS1fdlE
    ssr://dnBoay04LmdpdG8uY2M6NzYxOmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6T1dsbVlYTjAvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVvLXQ2Wml6NWJpQ0xYWndhR3N0T0M1bmFYUnZMbU5qJm9iZnNwYXJhbT03Ny05YS0tX3ZlLV92VGMxNzctOTc3LTlNTy1fdldydnY3MTNibXh2Wi0tX3ZYZHBibXJ2djcxM2VlLV92WEx2djcxMjc3LTk3Ny05YjIwJnByb3RvcGFyYW09NzctOTI3bnZ2NzN2djcxNjc3LTlHdS1fdmUtX3ZlLV92UQ
    ssr://dnBoay04LmdpdG8uY2M6NzYxOmF1dGhfYWVzMTI4X21kNTphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6T1dsbVlYTjAvP2dyb3VwPVUxTlNVSEp2ZG1sa1pYSSZyZW1hcmtzPTVibV81TGljNTV5QjVvLXQ2Wml6NWJpQ0xYWndhR3N0T0M1bmFYUnZMbU5qSURJJm9iZnNwYXJhbT03Ny05YS0tX3ZlLV92VGMxNzctOTc3LTlNTy1fdldydnY3MTNibXh2Wi0tX3ZYZHBibXJ2djcxM2VlLV92WEx2djcxMjc3LTk3Ny05YjIwJnByb3RvcGFyYW09NzctOTI3bnZ2NzN2djcxNjc3LTlYSGd4WWUtX3ZlLV92ZS1fdlE
    

</details>

### 所有节点
合并节点总数: `2412`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge_base64.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `60`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `143`
- [freefq/free](https://github.com/freefq/free), 节点数量: `36`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `334`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `5398`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `102`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `34`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `50`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `51`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `112`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `110`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `121`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `1`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `16`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `1`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `349`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `218`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `286`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `29`

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
