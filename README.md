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

    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dauwxncawx.vzwzasc.cn#mianfeifq%20%7C%F0%9F%87%A8%F0%9F%87%B3%2BHK%2B17
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B9%2BTG%3A%40nodpai%2B%28Beta%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDMxNCIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiUmVsYXlfUmVsYXlfIHwgMS43OU1iIiwKICAiYWRkIjogInZhdTEuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZhdTEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#GH
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMSIsCiAgImFkZCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicGF0aCI6ICIvY2hhdCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AD%F0%9F%87%B0%20HK_228%20%7C71.07Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA%20_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65206?allowInsecure=1&sni=dl.hncmhkbgp.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2068%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwKICAiYWRkIjogIjE1Mi42OS4xOTUuMTcxIiwKICAicG9ydCI6IDU1NTU1LAogICJpZCI6ICJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk1LjE3MSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwNiIsCiAgImFkZCI6ICIxNDAuODMuNTcuODAiLAogICJwb3J0IjogNDk4NDAsCiAgImlkIjogIjI5NjlhZDFiLTk3ODctNDkyNy05NGU2LTIyZjU5NzYxOGRlMCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZhdTEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@45.79.141.128:53316?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#US_45.79.141.128_101055b7-214
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@211.99.96.117:65109?allowInsecure=1&sni=dl.bgp7.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%201%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODU5IiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://f1dc4e1e-2095-38e4-bf3d-ffda333686dc@120.241.126.83:65205?allowInsecure=1&sni=gzjpaz.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2047%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E6%81%8B%E7%A5%9E%E5%8A%A0%E9%80%9F_23
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxNDYuNzAuNTMuMjQyOjUwMDAw#%E8%8B%B1%E5%9B%BD%20005
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@120.241.126.83:65208?allowInsecure=1&sni=dl.gdcmhinet3.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2070%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65214?allowInsecure=1&sni=gztwhinetz.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2020%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAxNDciLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%E4%BF%84%E7%BD%97%E6%96%AF%20003
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMjQiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggX1VTX+e+juWbvSIsCiAgImFkZCI6ICIxNTIuNjkuMTk1LjE3MSIsCiAgInBvcnQiOiA1NTU1NSwKICAiaWQiOiAiYjg2ZDk1ZGEtYjg0My00ODA0LTg0NDMtZDg0OWQzMjA3MDc2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@211.99.96.117:65300?allowInsecure=1&sni=dl.bgp4.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%206%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwKICAiYWRkIjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiYTk0ODE2MDAtZWYzNi00MDJhLWEwZTUtNTU0N2JmZDdiODdjIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy1vdmgxLnYyLXJheS5jb20iLAogICJwYXRoIjogIi9mYXN0c3NoL2ZnaGhoLzYzNDE5N2M0Y2RmODEvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@211.99.96.117:65301?allowInsecure=1&sni=dl.bgp3.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%205%20%E2%86%92%20openitsub.com
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@jgwdb3.gaox.ml:443?allowInsecure=1&sni=jgwdb3.gaox.ml#%E4%BA%9A%E6%B4%B2%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@jgwdb3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%E4%BA%9A%E6%B4%B2%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@211.99.96.117:65303?allowInsecure=1&sni=dl.sghgc2.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2012%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMDYiLAogICJhZGQiOiAiMTM5Ljk5LjkxLjk1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MS45NSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0dfMTM5Ljk5LjkxLjk1XzEwMTA1NWI3LTY4IiwKICAiYWRkIjogIjEzOS45OS45MS45NSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsCiAgImFpZCI6IDMyLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzkuOTkuOTEuOTUiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0ZjpOUU5wRnZAMTE2LjEyOS4yNTQuMzU6MTE5Nzk=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2076%20%E2%86%92%20openitsub.com
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@168.138.43.89:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4532?allowInsecure=1&sni=dl.shcuhkbn.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2014%20%E2%86%92%20openitsub.com
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@168.138.43.89:443?allowInsecure=1&sni=eksrda.meijireform.com#%E6%97%A5%E6%9C%AC%20006
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wt5paw5Yqg5Z2hLXNnLW92aDEudjItcmF5LmNvbSIsCiAgImFkZCI6ICJzZy1vdmgxLnYyLXJheS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=dl.shcujpntt2.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2038%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65201?allowInsecure=1&sni=gzhkntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2067%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65203?allowInsecure=1&sni=dl.gdcmjpwea.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2044%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0ZjpOUU5wRnZAMTE2LjEyOS4yNTMuMTM4OjExOTc5#%F0%9F%87%A8%F0%9F%87%B3%20CN%2077%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMDciLAogICJhZGQiOiAiMTcyLjY0LjE1My4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://39f71286-da06-4de4-81ba-5559b9b8b74b@16.163.226.1:2053?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%AD%F0%9F%87%B0%20%5BBGP-GSLB%5D%E9%A6%99%E6%B8%AF%E2%80%A2BGP
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@120.241.126.83:65201?allowInsecure=1&sni=gzhkntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2017%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1NC4zNToyMTA3Mg==#%F0%9F%87%A8%F0%9F%87%B3%20CN%2016%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@shcuac.aag436.ccddn4.icu:65524?allowInsecure=1&sni=dl.shcujpntt3.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2035%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMzQiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://f1dc4e1e-2095-38e4-bf3d-ffda333686dc@120.241.126.83:65211?allowInsecure=1&sni=gghkntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2015%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMzMiLAogICJhZGQiOiAiMTcyLjY0LjE1My4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4989?allowInsecure=1&sni=gzhkhkt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2052%20%E2%86%92%20openitsub.com
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@120.241.126.83:65212?allowInsecure=1&sni=gzhkaz.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2018%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1My4xMzg6MjEwNzI=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2045%20%E2%86%92%20openitsub.com
    trojan://f1dc4e1e-2095-38e4-bf3d-ffda333686dc@120.241.126.83:65210?allowInsecure=1&sni=gztwkbt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2021%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwKICAiYWRkIjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE5NDgxNjAwLWVmMzYtNDAyYS1hMGU1LTU1NDdiZmQ3Yjg3YyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicGF0aCI6ICIvZmFzdHNzaC9mZ2hoaC82MzQxOTdjNGNkZjgxLyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4988?allowInsecure=1&sni=dl.shcujpntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2075%20%E2%86%92%20openitsub.com
    trojan://e27cce7a-617d-48cb-b628-e9717be9c175@113.fastea.top:53313?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%AF%F0%9F%87%B5%20JP%205%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0dfMTM5Ljk5LjkxLjk1XzEwMTA1NWI3LTY4IiwKICAiYWRkIjogIjEzOS45OS45MS45NSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsCiAgImFpZCI6IDMyLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzkuOTkuOTEuOTUiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@120.241.126.83:65204?allowInsecure=1&sni=dl.gdkraws.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2050%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzOCIsCiAgImFkZCI6ICJzZy5wcnByLmxpbmsiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZWE0MjE2MS1iZGRjLTQyMzAtYTliOS1lNDMxODc5NjdmZmEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLnBycHIubGluayIsCiAgInBhdGgiOiAiL1RlbGVncmFtL1NoYXJlQ2VudHJlUHJvL21rbm5peCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%20002
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInVzLmthcG9rLmJ1enoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjQ1NTBhMS1iZDYzLTRmOWMtYjRiNi1mZGQyNGI0NDA3MjgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiY2hhY2hhMjAtcG9seTEzMDUiLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwNTciLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65525?allowInsecure=1&sni=dl.shsgaws.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2078%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:65522?allowInsecure=1&sni=dl.shcuusan.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2011%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://54080134-2cba-4535-8599-95650bd9aa54@jgwhdlb2.gaox.ml:443?allowInsecure=1&sni=jgwhdlb2.gaox.ml#%E7%BE%8E%E5%9B%BD%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%AE%F0%9F%87%B3%20_IN_%E5%8D%B0%E5%BA%A6
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    trojan://54080134-2cba-4535-8599-95650bd9aa54@jgwhdlb2.gaox.ml:443?allowInsecure=1&sni=jgwhdlb2.gaox.ml#%E7%BE%8E%E5%9B%BD%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMDEiLAogICJhZGQiOiAiMTM5Ljk5LjkxLjk1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MS45NSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India/Hyderabad_26
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E6%81%8B%E7%A5%9E%E5%8A%A0%E9%80%9F_23
    trojan://39f71286-da06-4de4-81ba-5559b9b8b74b@16.163.226.1:2053?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20%5BBGP-GSLB%5D%E7%BE%8E%E5%9B%BD1%E2%80%A20.8x
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#PT_%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDA3MSIsCiAgImFkZCI6ICJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJmOTI0N2RmNC0wMmQ1LTRiMzEtYWNjNS00MDIyNjUyYzU5NTMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImVlLmNsb3VkZmxhcmUucXVlc3QiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://39f71286-da06-4de4-81ba-5559b9b8b74b@16.163.226.1:2053?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%B3%F0%9F%87%AC%20%5BBGP-GSLB%5D%E5%B0%BC%E6%97%A5%E5%B0%BC%E4%BA%9A
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMDEiLAogICJhZGQiOiAiMTM5Ljk5LjkxLjk1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MS45NSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiTkwg6I235YWwKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogIjE0MS4xMDEuMTE0LjExMSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImY2NzgzMWMyLTQ2ZmQtNDUzYy1iZTcxLTZkMjdkODcyYWRmYyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZnIyLnpodWppY24yLm9yZyIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%20001
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=jgwcc1.gaox.ml#%E6%AC%A7%E6%B4%B2%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=dg-tj.superyuluo.space#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://f1dc4e1e-2095-38e4-bf3d-ffda333686dc@120.241.126.83:65215?allowInsecure=1&sni=dl.gdhkntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2030%20%E2%86%92%20openitsub.com
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=hiubbxiygcwax.vzwzasc.cn#US_45.79.141.128_10118241-206
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@211.99.96.117:65025?allowInsecure=1&sni=dl.sg7.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%203%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hfVVNf576O5Zu9LT7wn4er8J+Ht19GUl/ms5Xlm70iLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xNTQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==

</details>

### 所有节点
合并节点总数: `2491`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `135`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `150`
- [freefq/free](https://github.com/freefq/free), 节点数量: `35`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `382`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `170`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `12`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `3`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `97`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `136`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `32`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `40`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `201`
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
