# TopFreeProxies
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alanbobs999/topfreeproxies/sub_merge?label=sub_merge)](https://github.com/alanbobs999/TopFreeProxies/actions/workflows/sub_merge.yml) 

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

    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#mianfeifq%2B215
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AD%F0%9F%87%B0%20HK_228%20%7C71.07Mb
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=gbo02.vsvideo.shop#%F0%9F%87%AD%F0%9F%87%B0%20HK%201%20%E2%86%92%20openitsub.com
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20038
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=youtube-bai-piao-wang-zhe-usa.98848.xyz#999
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=112.fastea.top#%7C332.10Mb
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20openitsub.com
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=gbo02.vsvideo.shop#mianfeifq%2B256
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=eksrda.meijireform.com#mianfeifq%2B248
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODU5IiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B9%2BTG%3A%40nodpai%2B%28Beta%29
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dauwxncawx.vzwzasc.cn#mianfeifq%20%7C%F0%9F%87%A8%F0%9F%87%B3%2BHK%2B17
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9QyIsCiAgImFkZCI6ICIzLjM0LjE4Ny4xMDMiLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjMuMzQuMTg3LjEwMyIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=112.fastea.top#mianfeifq%2B256
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDMiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTAwMTYiLAogICJhZGQiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBvcnQiOiAyNjY3NiwKICAiaWQiOiAiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDMiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7BISy0xOC4xNjYuMjI4LjQ4LTAwNiIsCiAgImFkZCI6ICIxOC4xNjYuMjI4LjQ4IiwKICAicG9ydCI6IDQ1MzQyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxOC4xNjYuMjI4LjQ4IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAxNDciLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTUyLjcwLjI0MS4xOF8xMDExODNlNi0xMzEiLAogICJhZGQiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBvcnQiOiAyNjY3NiwKICAiaWQiOiAiZWNkMjc0YzAtMTc1ZC00NWY3LTgyNzYtYTNkYTkzNzg2NjMyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjI0MS4xOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=flowery.meijireform.com#mianfeifq%2B189
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=112.fastea.top#%7C120.90Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMiIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifCAxLjc5TWIiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMyIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTUyLjcwLjIzNS4yMDdfMTAxMTgzZTYtMTE2IiwKICAiYWRkIjogIjE1Mi43MC4yMzUuMjA3IiwKICAicG9ydCI6IDM1NDEyLAogICJpZCI6ICI3MGQ5NTMwOC0yYTYxLTRmOTMtZjEzOS05MTAzZDA1ODdmZDkiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzOCIsCiAgImFkZCI6ICJzZy5wcnByLmxpbmsiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZWE0MjE2MS1iZGRjLTQyMzAtYTliOS1lNDMxODc5NjdmZmEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLnBycHIubGluayIsCiAgInBhdGgiOiAiL1RlbGVncmFtL1NoYXJlQ2VudHJlUHJvL21rbm5peCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMzQiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HpvCfh7ogX0FVX+a+s+Wkp+WIqeS6miIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=kr1.api-aws.com#v2rayfree.eu.org%20-%20%E6%97%A5%E6%9C%ACNTT%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8WebARENA%2021
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMyIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://7a566d21dfcd0f12490275fd3dd3cfc4@trs04.bolab.net:443?allowInsecure=1&sni=112.fastea.top#%E6%97%A5%E6%9C%AC%20012
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=eksrda.meijireform.com#%F0%9F%87%BA%F0%9F%87%B8%20US%205%20%E2%86%92%20openitsub.com
    trojan://39f71286-da06-4de4-81ba-5559b9b8b74b@16.163.226.1:2053?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%AD%F0%9F%87%B0%20%5BBGP-GSLB%5D%E9%A6%99%E6%B8%AF%E2%80%A2BGP
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@140.238.205.173:443?allowInsecure=1&sni=jgwdb3.gaox.ml#AU_140.238.205.173_101183e6-141
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%7C50.15Mb
    trojan://39f71286-da06-4de4-81ba-5559b9b8b74b@16.163.226.1:2053?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20%5BBGP-GSLB%5D%E7%BE%8E%E5%9B%BD1%E2%80%A20.8x
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=dl.sghgc2.cc.tjcct.xyz#GH
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%A6%F0%9F%87%BA%20AU%208
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#PT_%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%E7%99%BD%E5%AB%96-0313
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A6%F0%9F%87%BA%20AU%201%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%20002
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=kr1.api-aws.com#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20003
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMiIsCiAgImFkZCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicGF0aCI6ICIvY2hhdCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDM5IiwKICAiYWRkIjogImNmLm5haXhpaS50b3AiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIzZmFkM2I0Yy04NjkxLTQyZjItYTQ2ZC05ODc1Y2FjYWVlYjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxpbm9kZS5zaGFyZWNlbnRyZS54eXoiLAogICJwYXRoIjogIi9iNDcyZi8iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=dl.sg7.cc.tjcct.xyz#GH
    trojan://54080134-2cba-4535-8599-95650bd9aa54@jgwhdlb2.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AE%F0%9F%87%B3%20_IN_%E5%8D%B0%E5%BA%A6
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#IN_%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.ml%E3%80%91
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%E7%99%BD%E5%AB%96-0313
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODU5IiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6xTRy0xOC4xNDIuMTg1LjEzNy0wMDQiLAogICJhZGQiOiAiMTguMTQyLjE4NS4xMzciLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE4LjE0Mi4xODUuMTM3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMTYiLAogICJhZGQiOiAiMTQxLjEwMS4xMTUuMiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE1YmE4YjJiLThmYzUtNDUyMS1hMzVlLTkyODFiZTYxYzFjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGcxLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=scus3.ddns-pop.cyou#%E5%8D%B0%E5%BA%A6%20001
    trojan://54080134-2cba-4535-8599-95650bd9aa54@152.67.160.174:443?allowInsecure=1&sni=sni=huayun.xyz#%F0%9F%87%AE%F0%9F%87%B3_IN_%E5%8D%B0%E5%BA%A6
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%5B09-26%5D%7Copenrunner%7C%E5%8D%B0%E5%BA%A6%28IN%29India/Hyderabad_26
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@jgwdb3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%7C14.12Mb
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%7C11.28Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwOTEiLAogICJhZGQiOiAiMTM1LjE0OC40Ny4yNDAiLAogICJwb3J0IjogODAsCiAgImlkIjogImZkNGZhMDMwLWI4ZjEtNDI0Yi1hNzgwLTU3OGRiYjU5Zjk1MCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMtdi5zc2htYXgueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://8d2d5953-d649-4034-94f2-72f2df2623da@jgwdb3.gaox.ml:443?allowInsecure=1&sni=jgwdb3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20US%20543
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiQFNTUlNVQi1WMDgt5LuY6LS55o6o6I2QOnN1by55dC9zc3JzdWIiLAogICJhZGQiOiAiMTcyLjY0LjE1My4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNC56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%202%20%E2%86%92%20openitsub.com
    trojan://123456@194.233.88.109:443?allowInsecure=1&sni=jgwdb3.gaox.ml#SG_194.233.88.109_101183e6-73
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVNf44CQ5LuY6LS55o6o6I2Q77yad3hmei5tbOOAkSIsCiAgImFkZCI6ICIxNzIuNjQuMTQ0LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6xTRy0xMy4yMTIuMjEuMjQ1LTAwMiIsCiAgImFkZCI6ICJ4aW5qaWFwb2EueW9uZ3lldnBuLmNvbSIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAieGluamlhcG9hLnlvbmd5ZXZwbi5jb20iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://006baa3f-4bc3-4915-b60d-c8c5dae11a11@jgwhdlb3.gaox.ml:443?allowInsecure=1&sni=scus3.ddns-pop.cyou#%E5%8D%B0%E5%BA%A6%20002
    trojan://123456@trojan-ctb-sg01.globalssh.xyz:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%A9%F0%9F%87%AA%20DE%2032
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#GH
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://e27cce7a-617d-48cb-b628-e9717be9c175@112.fastea.top:53316?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%B8%F0%9F%87%AC%2BSG%2B1%2BTG%3A%40nodpai
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hXzEwMTAwMDEiLAogICJhZGQiOiAiMTM5Ljk5LjkxLjk1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwKICAiYWlkIjogMzIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOS45OS45MS45NSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=112.fastea.top#%7C50.34Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMzQiLAogICJhZGQiOiAiMTcyLjY0LjE1NS4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNC56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=jgwdb3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20018
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiQVUg5r6z5aSn5Yip5LqaKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInZhdTEuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZhdTEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5YyI54mZ5YipXzEwMTAwMDEiLAogICJhZGQiOiAiMTg1LjIyNS42OS4xMzQiLAogICJwb3J0IjogNDUwODEsCiAgImlkIjogIjNjM2JmZDc1LWRjMzAtNGU3Ni04OTQwLTQ3ZTExMzdlMjFmOSIsCiAgImFpZCI6IDY0LAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxODUuMjI1LjY5LjEzNCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggMTYiLAogICJhZGQiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==

</details>

### 所有节点
合并节点总数: `5654`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `135`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `130`
- [freefq/free](https://github.com/freefq/free), 节点数量: `49`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3682`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `37`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `22`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `4`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `99`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `128`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `43`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `175`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `180`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `273`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `50`

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
