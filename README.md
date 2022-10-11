# TopFreeProxies
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alanbobs999/topfreeproxies/sub_merge?label=sub_merge)](https://github.com/alanbobs999/TopFreeProxies/actions/workflows/sub_merge.yml) 

![Watchers](https://img.shields.io/github/watchers/alanbobs999/topfreeproxies) ![Stars](https://img.shields.io/github/stars/alanbobs999/topfreeproxies) ![Forks](https://img.shields.io/github/forks/alanbobs999/topfreeproxies) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=alanbobs999.topfreeproxies) ![LICENSE](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)

[仓库介绍](https://github.com/alanbobs999/TopFreeProxies#仓库介绍) | [使用方法](https://github.com/alanbobs999/TopFreeProxies#使用方法) | [节点信息](https://github.com/alanbobs999/TopFreeProxies#节点信息) | [软件推荐](https://github.com/alanbobs999/TopFreeProxies#客户端选择) | [机场推荐](https://github.com/alanbobs999/TopFreeProxies#机场推荐) | [仓库声明](https://github.com/alanbobs999/TopFreeProxies#仓库声明)

## 仓库介绍
本仓库自动化功能全部基于 `GitHub Actions` 实现，如果有需要可以自行 Fork 实现个性化需求。

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

    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=ru.p1.gay#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B619
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlBfMTM4LjIuOC4yMjdfMTAxMTgyNDEtMTE2IiwKICAiYWRkIjogIjEzOC4yLjguMjI3IiwKICAicG9ydCI6IDU5NDQyLAogICJpZCI6ICI2ZmQwNDJmYS1lODY0LTRhOTUtODViYy02ZjU5MGEwM2QzNGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzguMi44LjIyNyIsCiAgInBhdGgiOiAiL2F0RzM3WU5XLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=hk-01.nodemao.com#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgSlAgMTA1IiwKICAiYWRkIjogIjE0Ni41Ni4xNTUuNzAiLAogICJwb3J0IjogMTgwNTAsCiAgImlkIjogImY5NzcxYzE5LWM5MWMtNDFiNS05MDY0LTg3NjhiNTFjZWM2ZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE0Ni41Ni4xNTUuNzAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTUyLjcwLjI0MS4xOF8xMDExODI0MS0zOTgiLAogICJhZGQiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBvcnQiOiAyNjY3NiwKICAiaWQiOiAiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20029
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxNDYuNzAuNTMuMjQyOjUwMDAw#%E8%8B%B1%E5%9B%BD%20005
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTAwMTYiLAogICJhZGQiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBvcnQiOiAyNjY3NiwKICAiaWQiOiAiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDE0IiwKICAiYWRkIjogIlBMLm5leGl0YWxseS54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI1NGM2YzgyMy00OTU3LTRjNmMtYjEwYy0zNTliYzUxZjdjYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIlBMLm5leGl0YWxseS54eXoiLAogICJwYXRoIjogIi9hNTRlMjg0Y2I2LyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDMxNCIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTkzLjM3LjI1Mi4yMTA6ODEw#%5B10-11%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-660-193.37.252.210
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTQ2LjU2LjE1NS43MF8xMDExODI0MS0xMDMiLAogICJhZGQiOiAiMTQ2LjU2LjE1NS43MCIsCiAgInBvcnQiOiAzMzQ0OSwKICAiaWQiOiAiZTExNWFkYTctOWIxOS00ZGY5LWM1OGEtY2FkZDQ1NDBlYzEzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTQ2LjU2LjE1NS43MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMDkiLAogICJhZGQiOiAiMTcyLjY0LjE1NC4xNTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDI5IiwKICAiYWRkIjogIjE0MS4xMDEuMTE1LjIiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhNWJhOGIyYi04ZmM1LTQ1MjEtYTM1ZS05MjgxYmU2MWMxYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMzIiLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#GH
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B9%2BTG%3A%40nodpai%2B%28Beta%29
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9ANS4xODEuMjM0LjI1NDo4MDg=#%5B10-10%5D-%F0%9F%87%BA%F0%9F%87%A6-%E4%B9%8C%E5%85%8B%E5%85%B0-2450-5.181.234.254
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#Relay_%20%7C50.15Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E6%81%8B%E7%A5%9E%E5%8A%A0%E9%80%9F_23
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%A6%F0%9F%87%BA%2BAU%2B8
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%E4%BF%84%E7%BD%97%E6%96%AF%20003
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MDYiLAogICJhZGQiOiAiMTcyLjY0LjE1My4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=sg4.elknode.top#SG_159.223.89.239_10118241-179
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=112.fastea.top#Relay_Relay_%20%7C301.90Mb
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20031
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA%20_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAxNDciLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hiubbxiygcwax.vzwzasc.cn#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDIzIiwKICAiYWRkIjogInVzLmthcG9rLmJ1enoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjQ1NTBhMS1iZDYzLTRmOWMtYjRiNi1mZGQyNGI0NDA3MjgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiY2hhY2hhMjAtcG9seTEzMDUiLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@168.138.43.89:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=sni=jpa.jiashumao.net#999
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMjQiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=bgroup.node3.t.nodelist-gfwairport.download#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20openitsub.com
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dauwxncawx.vzwzasc.cn#mianfeifq%20%7C%F0%9F%87%A8%F0%9F%87%B3%2BHK%2B17
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInVzLmthcG9rLmJ1enoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjQ1NTBhMS1iZDYzLTRmOWMtYjRiNi1mZGQyNGI0NDA3MjgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiY2hhY2hhMjAtcG9seTEzMDUiLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMS44N3wgaHR0cHNnaXRodWJjb21BbHZpbjk5OTluZXdwYWN3aWtpIGNsYXNoIGlwMiDmtJvmnYnnn7YxMkNETiIsCiAgImFkZCI6ICIxNzIuNjQuMTQ0LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNTg5IiwKICAiYWRkIjogIjE2OC4xMzguMjA3LjY2IiwKICAicG9ydCI6IDIxMzY1LAogICJpZCI6ICI5MDVmOTliMS1lN2JhLTQ1ZTAtYWU0ZC1iMGZmZGYwYWQyNDUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNjguMTM4LjIwNy42NiIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0dfMTM5Ljk5LjkxLjk1XzEwMTA1NWI3LTY4IiwKICAiYWRkIjogIjEzOS45OS45MS45NSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsCiAgImFpZCI6IDMyLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzkuOTkuOTEuOTUiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogIjY0LjExMi40Mi43MiIsCiAgInBvcnQiOiAxNjk5OSwKICAiaWQiOiAiYjVhMDFmNDQtYjk4MS00MjFhLWJkYzAtNmQ5ZDUzZGEwN2ZkIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiNjQuMTEyLjQyLjcyIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVNf44CQ5LuY6LS55o6o6I2Q77yad3hmei5tbOOAkSIsCiAgImFkZCI6ICIxNzIuNjQuMTUzLjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMzQiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=hiubbxiygcwax.vzwzasc.cn#US_45.79.141.128_10118241-206
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMTkiLAogICJhZGQiOiAiMTk4LjQxLjIxMi4zMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjEwNWM2MzVmLTkxOGQtNGIyYS04YzlkLWQ1NDI2ZTk0ZWI0YiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGcyLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDA1MiIsCiAgImFkZCI6ICIxNzIuNjQuMTUzLjE1MCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImJmNDYxOWU0LTAxZGMtNDhjYS1iZTA4LTA5NzZiNTQ5NjhjZSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGc1LnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%20002
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMTMiLAogICJhZGQiOiAiMTM5Ljk5LjkwLjEyMiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsCiAgImFpZCI6IDMyLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzkuOTkuOTAuMTIyIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=youtube-bai-piao-wang-zhe-usa.98848.xyz#%F0%9F%87%AE%F0%9F%87%B3_IN_%E5%8D%B0%E5%BA%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMDEiLAogICJhZGQiOiAiMTM5Ljk5LjkxLjk1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MS45NSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=ru.p1.gay#%F0%9F%87%AE%F0%9F%87%B3%20%E5%8D%B0%E5%BA%A6%20001
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AE%F0%9F%87%B3%20_IN_%E5%8D%B0%E5%BA%A6
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#PT_%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMDQiLAogICJhZGQiOiAiMTQxLjEwMS4xMTUuMTUwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hfVVNf576O5Zu9LT7wn4ep8J+Hql9ERV/lvrflm71fMiIsCiAgImFkZCI6ICIxNzIuNjQuMTU1LjIwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE4MDMwYWZkLTgxMmEtNGFmZS1hNzY2LTljNzZmZjNlZGRkNCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGc0LnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@45.79.141.128:53316?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#US_45.79.141.128_101055b7-214
    trojan://a153fb4e-6d1b-4db0-b03d-acb4012b7198@146.56.176.239:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#KR_%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMDIiLAogICJhZGQiOiAiMTk4LjQxLjIxMi4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiMTcyLjY0LjE1NS4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNC56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20035
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+PgeeZveWrli0wMTMiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://2e4c54a0-a780-4994-97c0-44eb92857d76@kr1.api-aws.com:443?allowInsecure=1&sni=kr1.api-aws.com#%E9%9F%A9%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-138.68.248.130%3A811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-138.68.248.130%3A811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs02.bolab.net:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E6%97%A5%E6%9C%AC%20005
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMS43NXwgaHR0cHNnaXRodWJjb21BbHZpbjk5OTluZXdwYWN3aWtpIGNsYXNoIGlwNSDms5Xlm71DRE4xMSIsCiAgImFkZCI6ICIxOTguNDEuMjEyLjIiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwN2E2M2ZlMy04YTQ2LTRmODktYjU0OC05MTUxYzYxYjlkYzgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInYycmF5MS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs02.bolab.net:443?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%AF%F0%9F%87%B5%20JP%202%20%E2%86%92%20openitsub.com
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@133.18.199.114:443?allowInsecure=1&sni=eksrda.meijireform.com#JP_133.18.199.114_10118241-98
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs02.bolab.net:443?allowInsecure=1&sni=trs02.bolab.net#JP%2B%E6%97%A5%E6%9C%AC%28youtube%E9%98%BF%E4%BC%9F%E7%A7%91%E6%8A%80%29%0D
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMDMiLAogICJhZGQiOiAiMTcyLjY0LjE1My4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs01.bolab.net:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E6%97%A5%E6%9C%AC%20003
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs01.bolab.net:443?allowInsecure=1&sni=sdhawuyfkjuwx.vzwzasc.cn#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%20007
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUA4My4yMjkuNzMuNjA6NTAwMDA=#%E8%8B%B1%E5%9B%BD%20007
    ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklkQDE2Ny44OC42Mi42ODo1MDA0#%5B10-11%5D-%F0%9F%87%B8%F0%9F%87%AA-%E7%91%9E%E5%85%B8-816-167.88.62.68
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0NAMzguNjguMTM0LjQ4Ojg4ODg=#%5B10-11%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-666-38.68.134.48
    ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9TQDM4LjY4LjEzNC44NTo2Njc5#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybUAxNjcuODguNjIuNjg6ODAwMA==#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-167.88.62.68%3A8000-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0QDE2Ny44OC42Mi42ODo4ODgx#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-167.88.62.68%3A8881-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0QDE2Ny44OC42Mi42ODo4ODgx#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-167.88.62.68%3A8881-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybUAzOC42OC4xMzQuODU6ODA4MA==#%5B10-11%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-658-38.68.134.85
    ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3QDM4LjY4LjEzNC4xOTE6ODA5MQ==#%5B10-11%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-868-38.68.134.191
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybUAxNjcuODguNjIuNjg6ODAwMA==#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-167.88.62.68%3A8000-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0NAODUuMjA4LjEwOC42MDo1MDAx#%5B10-11%5D-%F0%9F%87%A6%F0%9F%87%B6-%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AF-1094-85.208.108.60
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0QDM4LjEyMS40My43MTo4ODgy#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQQDEzNC4xOTUuMTk2LjE0OTo3MzA3#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklkQDM4Ljg2LjEzNS4yNzo1MDA0#%5B10-11%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-622-38.86.135.27
    ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9TQDM4LjExNC4xMTQuNjc6NjY5Nw==#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0NAMzguMTIxLjQzLjcxOjMzODk=#%5B10-11%5D-%F0%9F%87%BA%F0%9F%87%B8-%E7%BE%8E%E5%9B%BD-656-38.121.43.71

</details>

### 所有节点
合并节点总数: `2394`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `135`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `150`
- [freefq/free](https://github.com/freefq/free), 节点数量: `25`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `382`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `130`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `12`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `3`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `85`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `136`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `23`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `40`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `175`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `195`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `273`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `33`

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
