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

    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDIwIiwKICAiYWRkIjogInNnLnBycHIubGluayIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImNlYTQyMTYxLWJkZGMtNDIzMC1hOWI5LWU0MzE4Nzk2N2ZmYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://xxoo@146.19.230.241:443?allowInsecure=1&sni=youtube-bai-piao-wang-zhe-usa.98848.xyz#_null_null
    trojan://Sp3eDVp@content-provider6.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=sg-01.tiktokcdn.top#mianfeifq%2B128
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7Xnmb3lq5YtMDYxIiwKICAiYWRkIjogIjEzOC4yLjQ0LjIxMSIsCiAgInBvcnQiOiAyMDA4MSwKICAiaWQiOiAiNTkzYjg1MjUtMGM0OC00YjBmLWQ5YWYtMmQ3M2E5MTQ4OTczIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=glc.hruqoaw.cn#mianfeifq%2B279
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1&sni=jp.iamnotagoodman.com#JP_138.2.8.227_1012a0e8-91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIwMTMiLAogICJhZGQiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwb3J0IjogNTU1NTUsCiAgImlkIjogImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4xOTUuMTcxIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7Xnmb3lq5YtMDUzIiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIwMjkiLAogICJhZGQiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwb3J0IjogNTU1NTUsCiAgImlkIjogImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4xOTUuMTcxIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://xxoo@146.19.230.241:443?allowInsecure=1&sni=linus.sbs#1.51%7Cnullwmt101090
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMi4yNnxKUOaXpeacrHlvdXR1YmXpmL/kvJ/np5HmioA2IiwKICAiYWRkIjogIjE1Mi42OS4xOTUuMTcxIiwKICAicG9ydCI6IDU1NTU1LAogICJpZCI6ICJiODZkOTVkYS1iODQzLTQ4MDQtODQ0My1kODQ5ZDMyMDcwNzYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk1LjE3MSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://Sp3eDVp@content-provider23.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=glc.hruqoaw.cn#TG%40hkaa0%7C%E8%8D%B7%E5%85%B0%2B001
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggOCIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNTUiLAogICJhZGQiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwb3J0IjogNTU1NTUsCiAgImlkIjogImI4NmQ5NWRhLWI4NDMtNDgwNC04NDQzLWQ4NDlkMzIwNzA3NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInd3dy40ODgxNjYyNi54eXoiLAogICJwYXRoIjogIi9wYXRoLzEyMDIwODMwMTQyMiIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggX1VTX+e+juWbvSIsCiAgImFkZCI6ICIxNTIuNjkuMTk1LjE3MSIsCiAgInBvcnQiOiA1NTU1NSwKICAiaWQiOiAiYjg2ZDk1ZGEtYjg0My00ODA0LTg0NDMtZDg0OWQzMjA3MDc2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5NS4xNzEiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5be06KW/IDAwMSIsCiAgImFkZCI6ICIxNjguMTM4LjIwNy42NiIsCiAgInBvcnQiOiAyMTM2NSwKICAiaWQiOiAiOTA1Zjk5YjEtZTdiYS00NWUwLWFlNGQtYjBmZmRmMGFkMjQ1IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTY4LjEzOC4yMDcuNjYiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-ph.qchwnd.moe#SG_159.223.89.239_1012b7e8-72
    trojan://xxoo@146.19.230.241:443?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%AB%F0%9F%87%B7%20FR%201%20%E2%86%92%20openitsub.com
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@jgwdb4.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C21.67Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwMDIiLAogICJhZGQiOiAiMTQxLjEwMS4xMTUuMiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE1YmE4YjJiLThmYzUtNDUyMS1hMzVlLTkyODFiZTYxYzFjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGcxLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://aa12A45bbutassOAm96ahzNlGY@45.11.92.100:8848?allowInsecure=1&sni=45.11.92.100#%F0%9F%87%B7%F0%9F%87%BA%20RU%203%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hIDAwMiIsCiAgImFkZCI6ICIxMzkuOTkuOTEuOTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjMDE1NjQ1MS00ZWZiLTQ1ZTItODRmYy04ZDMxNWM0NjUwZGIiLAogICJhaWQiOiAzMiwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM5Ljk5LjkxLjk1IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C44.01Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIxMDIiLAogICJhZGQiOiAic2hvcGlmeS5jb20iLAogICJwb3J0IjogMjA4NiwKICAiaWQiOiAiZGM4YjY0ZGItZWI2ZC00YmRmLTk4YjItMzE2MTUzMTliZWE4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2bi5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicGF0aCI6ICIvYXJpZXMiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=flowery.meijireform.com#%E7%BE%8E%E5%9B%BD%20038
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://xxoo@146.19.230.241:443?allowInsecure=1&sni=content-provider5.cdn-delivery.akamaicd.com#%E6%B3%95%E5%9B%BD%20002
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-ph.qchwnd.moe#SG_159.223.89.239_1012b7e8-72
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6xTRy0xMjIuMjQ4LjIyNy4yMjctMDAzIiwKICAiYWRkIjogInhpbmppYXBvYi55b25neWV2cG4uY29tIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ4aW5qaWFwb2IueW9uZ3lldnBuLmNvbSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://0Y9gOHSdRt@150.230.249.42:443?allowInsecure=1&sni=content-provider5.cdn-delivery.akamaicd.com#%E7%BE%8E%E5%9B%BD%20032
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjQ2IiwKICAiYWRkIjogIjE3Mi42NC4xNTQuMjAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTgwMzBhZmQtODEyYS00YWZlLWE3NjYtOWM3NmZmM2VkZGQ0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzQuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lmdx44CRIiwKICAiYWRkIjogIjE3Mi42NC4xNTMuMTUwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI1NTYiLAogICJhZGQiOiAic3R1ZHluZXcuY24iLAogICJwb3J0IjogNDgwMDgsCiAgImlkIjogImI4ODYzYjQyLTI3YjgtNDg1Mi1iNmRkLWIwYmRlYTQ1MzQ5NSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic3R1ZHluZXcuY24iLAogICJwYXRoIjogIi95YW5ncnVpIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAwNSIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7At6aaZ5rivLWZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAiYWRkIjogImZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjc0ZjExYzYtZjY5Yi00MGI5LTg5NjYtZjM5ZTA2ZTk3YmU3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJmdWxsYWNjZXNzdG9ob25na29uZ25ldC5henVyZXdlYnNpdGVzLm5ldCIsCiAgInBhdGgiOiAiL3dzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIwNDEiLAogICJhZGQiOiAiZnVsbGFjY2Vzc3RvaG9uZ2tvbmduZXQuYXp1cmV3ZWJzaXRlcy5uZXQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyNzRmMTFjNi1mNjliLTQwYjktODk2Ni1mMzllMDZlOTdiZTciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImZ1bGxhY2Nlc3N0b2hvbmdrb25nbmV0LmF6dXJld2Vic2l0ZXMubmV0IiwKICAicGF0aCI6ICIvd3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LTE0MS4xMDEuMTE1LjIwMCIsCiAgImFkZCI6ICIxNDEuMTAxLjExNS4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%202%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODEy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A812-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI3MDUiLAogICJhZGQiOiAiMTcyLjY0LjE1NC4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C97.96Mb
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=45.11.92.100#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20openitsub.com
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%A8%F0%9F%87%B3_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%A7%F0%9F%87%AD_BH_%E5%B7%B4%E6%9E%97
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=sni=huayun.xyz#%E5%8D%B0%E5%BA%A6%20002
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwOTkiLAogICJhZGQiOiAiMTQxLjEwMS4xMTQuMTUwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgU0cgNzQiLAogICJhZGQiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnNnMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDE5NSIsCiAgImFkZCI6ICJzaG9waWZ5LmNvbSIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiMzUzYmJmNWYtYTI2NC00NzMxLWU3MzUtOTg0ZTYxMWMyZTAxIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ0Z3VzLmNsb3VkZmxhcmUucXVlc3QiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjQ1IiwKICAiYWRkIjogIjE3Mi42NC4xNTUuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwMTEiLAogICJhZGQiOiAiMTk4LjQxLjIxMi4zMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjEwNWM2MzVmLTkxOGQtNGIyYS04YzlkLWQ1NDI2ZTk0ZWI0YiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGcyLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi44CQ5LuY6LS55o6o6I2Q77yad3hmei5nceOAkSIsCiAgImFkZCI6ICJzaG9waWZ5LmNvbSIsCiAgInBvcnQiOiAyMDg2LAogICJpZCI6ICJkYzhiNjRkYi1lYjZkLTRiZGYtOThiMi0zMTYxNTMxOWJlYTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZuLmNsb3VkZmxhcmUucXVlc3QiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India/Hyderabad_26
    trojan://Sp3eDVp@content-provider6.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=sg-01.tiktokcdn.top#FR%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.gq%E3%80%91
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=jgwhdlb3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B220
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDIxIiwKICAiYWRkIjogIjE3Ni4xMTIuMTQ2LjE5MCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZjkyNDdkZjQtMDJkNS00YjMxLWFjYzUtNDAyMjY1MmM1OTUzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNzYuMTEyLjE0Ni4xOTAiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI3MzIiLAogICJhZGQiOiAiZWUuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZjkyNDdkZjQtMDJkNS00YjMxLWFjYzUtNDAyMjY1MmM1OTUzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicGF0aCI6ICIvYXJpZXMiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNjEiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lmdx44CRIiwKICAiYWRkIjogIjE3Mi42NC4xNTUuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAwNSIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0dfMTM5Ljk5LjkwLjEyMl8xMDExODI0MS05NSIsCiAgImFkZCI6ICIxMzkuOTkuOTAuMTIyIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MC4xMjIiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1&sni=jp.iamnotagoodman.com#JP_138.2.8.227_1012a0e8-91
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs06.bolab.net:443?allowInsecure=1&sni=ukt1.sshocean.net#%F0%9F%87%AF%F0%9F%87%B5%20_JP_%E6%97%A5%E6%9C%AC
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7rnmb3lq5YtMTg0IiwKICAiYWRkIjogIjE4NS4yMjUuNjkuMTM0IiwKICAicG9ydCI6IDQ1MDgxLAogICJpZCI6ICIzYzNiZmQ3NS1kYzMwLTRlNzYtODk0MC00N2UxMTM3ZTIxZjkiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxODUuMjI1LjY5LjEzNCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B619
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=trs02.bolab.net#%F0%9F%87%AF%F0%9F%87%B5%20JP%203%20%E2%86%92%20openitsub.com
    trojan://aa12A45bbutassOAm96ahzNlGY@45.11.92.100:8848?allowInsecure=1&sni=n2.gladns.com#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%88%A9%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6iaclouds.com%204
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDml6XmnKzkuJzkuqxBbWF6b27mlbDmja7kuK3lv4MgMjciLAogICJhZGQiOiAianAtMDQudGlrdG9rY2RuLnNicyIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImJjZDUzOTNhLTNiZWQtNDIwMC05NTdmLTU4MzJiNGU4NDcyYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAianAtMDQudGlrdG9rY2RuLnNicyIsCiAgInBhdGgiOiAiL3RucGp2d3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=jgwld1.gaox.ml#mianfeifq%2B253
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=sni=huayun.xyz#%F0%9F%87%A8%F0%9F%87%B3_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%A7%F0%9F%87%AD_BH_%E5%B7%B4%E6%9E%97
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDIyIiwKICAiYWRkIjogImVlLmNsb3VkZmxhcmUucXVlc3QiLAogICJwb3J0IjogODAsCiAgImlkIjogImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZWUuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI2NzciLAogICJhZGQiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI2NzYiLAogICJhZGQiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNTciLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xNTQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI3MDUiLAogICJhZGQiOiAiMTcyLjY0LjE1NC4xNTAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiZWUuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZjkyNDdkZjQtMDJkNS00YjMxLWFjYzUtNDAyMjY1MmM1OTUzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicGF0aCI6ICIvYXJpZXMiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNS45MTo1MDAwNA==#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.125.91%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-138.68.248.130%3A811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8_%E6%B2%B9%E7%AE%A1%EF%BC%9A%E5%85%A8%E7%BD%91%E6%9C%80%E5%BC%BA%E7%99%BD%E5%AB%96
    trojan://Sp3eDVp@content-provider6.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=sg-01.tiktokcdn.top#mianfeifq%2B128
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAzMS4xMzMuMTAwLjQ5OjUwMDA0#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-31.133.100.49%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@133.18.200.127:443?allowInsecure=1&sni=jgwhdlb3.gaox.ml#JP_133.18.200.127_1012b7e8-43
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs01.bolab.net:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%20004
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=ukt1.sshocean.net#_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%A7%F0%9F%87%AD_BH_%E5%B7%B4%E6%9E%97
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs02.bolab.net:443?allowInsecure=1&sni=sg-01.tiktokcdn.top#%F0%9F%87%AF%F0%9F%87%B5_JP_%E6%97%A5%E6%9C%AC_3_2%4019
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDE4IiwKICAiYWRkIjogIjE0MS4xMDEuMTE0LjIwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMDdhNjNmZTMtOGE0Ni00Zjg5LWI1NDgtOTE1MWM2MWI5ZGM4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2MnJheTEuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://6222266fcd4ed224@116.129.253.134:3381?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%201%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVEdAaGthYTAgMDA5IiwKICAiYWRkIjogIjE0MS4xMDEuMTE0LjIwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMDdhNjNmZTMtOGE0Ni00Zjg5LWI1NDgtOTE1MWM2MWI5ZGM4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2MnJheTEuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDEzIiwKICAiYWRkIjogIjE3Mi42NC4xNTUuMjAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTgwMzBhZmQtODEyYS00YWZlLWE3NjYtOWM3NmZmM2VkZGQ0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzQuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@133.18.199.114:443?allowInsecure=1&sni=trs09.bolab.net#JP_133.18.199.114_1012b7e8-45
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6LaK5Y2XXzEwMTIwMTYiLAogICJhZGQiOiAiMTAzLjE4Ni4xNDguMTEzIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI2NzQ2OGQ4OS1jZjg3LTQ0M2MtYmFjYS00OWYxZTczYjU5OTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEwMy4xODYuMTQ4LjExMyIsCiAgInBhdGgiOiAiL3Nob3B2cG4ubmV0IiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs02.bolab.net:443?allowInsecure=1&sni=content-provider5.cdn-delivery.akamaicd.com#%E6%97%A5%E6%9C%AC%20008
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI3MDYiLAogICJhZGQiOiAiMTcyLjY0LjE1NC4xNTUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJiZjQ2MTllNC0wMWRjLTQ4Y2EtYmUwOC0wOTc2YjU0OTY4Y2UiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9

</details>

### 所有节点
合并节点总数: `5267`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `193`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `149`
- [freefq/free](https://github.com/freefq/free), 节点数量: `37`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3166`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `53`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `22`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `27`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `3`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `168`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `147`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `35`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `39`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `26`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `30`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `203`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `130`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `284`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `32`

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
