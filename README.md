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
高速节点数量: `99`
<details>
  <summary>展开复制节点</summary>

    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAxMTIiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MDQiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNjA5IiwKICAiYWRkIjogInVzMDMuZ29nb2dvby5jeW91IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1czAzLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNjA5IiwKICAiYWRkIjogInVzMDMuZ29nb2dvby5jeW91IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1czAzLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#%F0%9F%87%BA%F0%9F%87%B8US_09
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMDY0MzIiLAogICJhZGQiOiAidXMwMy5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDMuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDA0NyIsCiAgImFkZCI6ICJ1cy5rYXBvay5idXp6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWI0NTUwYTEtYmQ2My00ZjljLWI0YjYtZmRkMjRiNDQwNzI4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNjA5IiwKICAiYWRkIjogInVzMDMuZ29nb2dvby5jeW91IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1czAzLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#%F0%9F%87%BA%F0%9F%87%B8US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#US_09
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#%F0%9F%87%BA%F0%9F%87%B8US_09
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#%F0%9F%87%BA%F0%9F%87%B8US_09
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9ANS4xODEuMjM0LjI1NDo4MDg=#%5B10-10%5D-%F0%9F%87%BA%F0%9F%87%A6-%E4%B9%8C%E5%85%8B%E5%85%B0-2450-5.181.234.254
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gg576O5Zu9XzEwMDYwNTQiLAogICJhZGQiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNTUiLAogICJhZGQiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxVU180NS43OS4zMS4yNDZfMTAwOGNjM2YtMzY4IiwKICAiYWRkIjogInZ1czQuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZ1czQuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA1NjIiLAogICJhZGQiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxVU180NS43OS4zMS4yNDZfMTAwOGNjM2YtMzY4IiwKICAiYWRkIjogInZ1czQuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZ1czQuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA1NjIiLAogICJhZGQiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNTUiLAogICJhZGQiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzNC4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3NAMTU2LjE0Ni4zOC4xNjM6NDQz#%F0%9F%87%BA%F0%9F%87%B8US_09
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAxMTIiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggX1VTX+e+juWbvSIsCiAgImFkZCI6ICI2NC4xMTIuNDIuNzIiLAogICJwb3J0IjogMTY5OTksCiAgImlkIjogImI1YTAxZjQ0LWI5ODEtNDIxYS1iZGMwLTZkOWQ1M2RhMDdmZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjY0LjExMi40Mi43MiIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MTIiLAogICJhZGQiOiAiNjQuMTEyLjQyLjcyIiwKICAicG9ydCI6IDE2OTk5LAogICJpZCI6ICJiNWEwMWY0NC1iOTgxLTQyMWEtYmRjMC02ZDlkNTNkYTA3ZmQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICI2NC4xMTIuNDIuNzIiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MDQiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://8c836caa-3d53-4829-bcfb-cbe0aa453a57@23.94.103.146:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%BA%F0%9F%87%B8%20US_1229%20%7C%207.67Mb
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTQ0LjE2OC42MC43MDoyNTI=#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogIjY0LjExMi40Mi43MiIsCiAgInBvcnQiOiAxNjk5OSwKICAiaWQiOiAiYjVhMDFmNDQtYjk4MS00MjFhLWJkYzAtNmQ5ZDUzZGEwN2ZkIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiNjQuMTEyLjQyLjcyIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@129.146.242.130:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    trojan://8c836caa-3d53-4829-bcfb-cbe0aa453a57@23.94.103.146:443?allowInsecure=1&sni=www.sxsy88.tk#%F0%9F%87%BA%F0%9F%87%B8%E7%99%BD%E5%AB%96-0446
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@129.146.242.130:443?allowInsecure=1&sni=sni=hg.jiashumao.net#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxfQXphZE5ldF83IiwKICAiYWRkIjogIjE4OC4xMTQuOTcuNyIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwYXRoIjogIi9nbyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTQ0LjE2OC42MC43MDoyNTI=#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    trojan://8c836caa-3d53-4829-bcfb-cbe0aa453a57@23.94.103.146:443?allowInsecure=1&sni=eksrda.meijireform.com#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMDYwNTUiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTcyLjk2LjE5Mi41ODoyNTQ=#%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD_9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzNSIsCiAgImFkZCI6ICIxNzIuNjQuMTUzLjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTcyLjk2LjE5Mi4xMDA6MjQ2#%E7%BE%8E%E5%9B%BD%20064
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTcyLjk2LjE5Mi41ODoyNTQ=#%E7%BE%8E%E5%9B%BD%20068
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTA3LjE4Mi4xNzcuMTM2OjI1Ng==#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://d4e41ff772c7fd45@23.247.137.70:3389?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%B3%F0%9F%87%B1%2BNL%2B38
    trojan://d4e41ff772c7fd45@23.247.137.70:3389?allowInsecure=1&sni=921tw.tfzhc.top#%E5%B7%B4%E6%9E%97%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwOTMiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MTgiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MDQiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxVU180NS43OS4zMS4yNDZfMTAwOGNjM2YtMzY4IiwKICAiYWRkIjogInZ1czQuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZ1czQuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@129.146.190.42:443?allowInsecure=1&sni=wel-ru.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAxMTgiLAogICJhZGQiOiAiMTI5LjE0Ni4xMzMuMTU3IiwKICAicG9ydCI6IDUxMDA5LAogICJpZCI6ICI4MTcxNGNlZi05YmRlLTRhMDgtYWE1MC1kNmJjMDE3MmQ3OGIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMjkuMTQ2LjEzMy4xNTciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxfQXphZE5ldF83IiwKICAiYWRkIjogIjE4OC4xMTQuOTcuNyIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwYXRoIjogIi9nbyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiUmVsYXlfIHwgOC45OU1iIiwKICAiYWRkIjogImNhLjAxMTIyMzMueHl6IiwKICAicG9ydCI6IDg0NDMsCiAgImlkIjogImMzMDAwZTlkLWJlZTctNGZkYi1iMzEyLWRkMDcwMzBmMzI1ZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiY2EuMDExMjIzMy54eXoiLAogICJwYXRoIjogIi9ob21lIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTA3LjE4Mi4xNzcuMTM2OjI1Ng==#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwOTMiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6X3ZtZXNzX3dzIiwKICAiYWRkIjogInlvdXR1YmUtYmFpLXBpYW8td2FuZy16aGUtdXNhLjk4ODQ4Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImQxNDc4Njg5LTQzOWMtNDU5MC1iN2NlLTM2ZTc4NmEwMmRjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6IiwKICAicGF0aCI6ICIvWW91VHViZUBiYWktcGlhby13YW5nLXpoZV92d3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTcyLjk2LjE5Mi4xMDA6MjQ2#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAxMTIiLAogICJhZGQiOiAidXMua2Fwb2suYnV6eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViNDU1MGExLWJkNjMtNGY5Yy1iNGI2LWZkZDI0YjQ0MDcyOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJjaGFjaGEyMC1wb2x5MTMwNSIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzLmthcG9rLmJ1enoiLAogICJwYXRoIjogIi9TQ1AtOTE0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVEdAaGthYTAgMDA5IiwKICAiYWRkIjogIjE0MS4xMDEuMTE0LjIwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMDdhNjNmZTMtOGE0Ni00Zjg5LWI1NDgtOTE1MWM2MWI5ZGM4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2MnJheTEuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxVU180NS43OS44OC4yMTVfMTAwODhkZjEtMzY1IiwKICAiYWRkIjogInZ1czIuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZ1czIuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNTciLAogICJhZGQiOiAidnVzMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNzg3IiwKICAiYWRkIjogIjE1MC4yMzAuNDEuOSIsCiAgInBvcnQiOiAyMzI5MiwKICAiaWQiOiAiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUwLjIzMC40MS45IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://d4e41ff772c7fd45@23.247.137.70:3389?allowInsecure=1&sni=921tw.tfzhc.top#%E5%B7%B4%E6%9E%97%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAOTcuNjQuMzEuODA6MjQ3#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTA3LjE4Mi4xNzcuMTM2OjI1Ng==#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-107.182.177.136%3A256-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTQ0LjE2OC42MC43MDoyNTI=#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    trojan://d4e41ff772c7fd45@23.247.137.70:3389?allowInsecure=1&sni=eksrda.meijireform.com#%E7%BE%8E%E5%9B%BD%20026
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwNzkiLAogICJhZGQiOiAiMTkwLjkzLjI0Ni4xNDUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20035
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MDYiLAogICJhZGQiOiAiMTcyLjY0LjE1My4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1&sni=eksrda.meijireform.com#%F0%9F%87%BA%F0%9F%87%B8%20US%205%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTcyLjk2LjE5Mi41ODoyNTQ=#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAibWlhbmZlaWZxIHxfQXphZE5ldF83IiwKICAiYWRkIjogIjE4OC4xMTQuOTcuNyIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwYXRoIjogIi9nbyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2MTgiLAogICJhZGQiOiAidXMwMi5nb2dvZ29vLmN5b3UiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIuZ29nb2dvby5jeW91IiwKICAicGF0aCI6ICIvZ28iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNjkiLAogICJhZGQiOiAiczIuNTIwZ3VnZS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZjE4MTljOC1lNTMwLTQ2MjYtYWVjMC04N2FjMDQyMDAzODUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInMyLjUyMGd1Z2UuY29tIiwKICAicGF0aCI6ICIvaGFwcHkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDNAMTcyLjk2LjE5Mi41ODoyNTQ=#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMzAiLAogICJhZGQiOiAidGFvYmFvLmJhYmF6aHVqaS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyYTQ5MThkZS1hZGNlLTRjNGUtYWEwMC04OGE0MjI3Y2Y2ZWEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInRhb2Jhby5iYWJhemh1amkuY29tIiwKICAicGF0aCI6ICIvZGlkaSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMDYxODY3IiwKICAiYWRkIjogInZ1czQuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZ1czQuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTk4LjE4MS41Ni4xNjM6MjM4#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%2037
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogIjE3Mi42NC4xNDQuMTU0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTQ4ODcyNjgtZjNjYi00OGJlLWFkZTMtODdkNDJmYWFlM2U0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJtNS52MnJheWZyZWUxLnh5eiIsCiAgInBhdGgiOiAiL3JheSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hVU18xMyIsCiAgImFkZCI6ICIxNTAuMjMwLjQxLjkiLAogICJwb3J0IjogMjMyOTIsCiAgImlkIjogIjk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsCiAgInBhdGgiOiAiL3dzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://d1478689-439c-4590-b7ce-36e786a02dc3@youtube-bai-piao-wang-zhe-usa.98848.xyz:443?allowInsecure=1&sni=eksrda.meijireform.com#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20041
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDE5IiwKICAiYWRkIjogInRhb2Jhby5iYWJhemh1amkuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMmE0OTE4ZGUtYWRjZS00YzRlLWFhMDAtODhhNDIyN2NmNmVhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ0YW9iYW8uYmFiYXpodWppLmNvbSIsCiAgInBhdGgiOiAiL2RpZGkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6X3ZtZXNzX3dzIiwKICAiYWRkIjogInlvdXR1YmUtYmFpLXBpYW8td2FuZy16aGUtdXNhLjk4ODQ4Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImQxNDc4Njg5LTQzOWMtNDU5MC1iN2NlLTM2ZTc4NmEwMmRjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6IiwKICAicGF0aCI6ICIvWW91VHViZUBiYWktcGlhby13YW5nLXpoZV92d3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAxNjQiLAogICJhZGQiOiAiYzU5czMuamFtamFtczMubmV0IiwKICAicG9ydCI6IDc1MjMsCiAgImlkIjogImNhNDg3ZDcxLTgxYWItNDAzNC04NjkzLWIzZGFkNGQ0NTY0MiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImM1OXMzLmphbWphbXMzLm5ldCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMDMiLAogICJhZGQiOiAiMTQxLjEwMS4xMTQuMjAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwN2E2M2ZlMy04YTQ2LTRmODktYjU0OC05MTUxYzYxYjlkYzgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInYycmF5MS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNjkiLAogICJhZGQiOiAiczIuNTIwZ3VnZS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZjE4MTljOC1lNTMwLTQ2MjYtYWVjMC04N2FjMDQyMDAzODUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInMyLjUyMGd1Z2UuY29tIiwKICAicGF0aCI6ICIvaGFwcHkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNjAiLAogICJhZGQiOiAid2VpeGluLmJhYmF6aHVqaS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyNzg0ODczOS03ZTYyLTQxMzgtOWZkMy0wOThhNjM5NjRiNmIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIndlaXhpbi5iYWJhemh1amkuY29tIiwKICAicGF0aCI6ICIvdGVjaCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA2NDciLAogICJhZGQiOiAiYzU5czMuamFtamFtczMubmV0IiwKICAicG9ydCI6IDc1MjMsCiAgImlkIjogImNhNDg3ZDcxLTgxYWItNDAzNC04NjkzLWIzZGFkNGQ0NTY0MiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImM1OXMzLmphbWphbXMzLm5ldCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTA1NjMiLAogICJhZGQiOiAidnVzMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVzMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwNTgiLAogICJhZGQiOiAiMTQxLjEwMS4xMTQuMjAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwN2E2M2ZlMy04YTQ2LTRmODktYjU0OC05MTUxYzYxYjlkYzgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInYycmF5MS56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9ANzguMTI5LjI1My45OjgwOA==#%5B10-11%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-1002-78.129.253.9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggX1VTX+e+juWbvSIsCiAgImFkZCI6ICI2NC4xMTIuNDIuNzIiLAogICJwb3J0IjogMTY5OTksCiAgImlkIjogImI1YTAxZjQ0LWI5ODEtNDIxYS1iZGMwLTZkOWQ1M2RhMDdmZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjY0LjExMi40Mi43MiIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwNTgiLAogICJhZGQiOiAidGFvYmFvLmJhYmF6aHVqaS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyYTQ5MThkZS1hZGNlLTRjNGUtYWEwMC04OGE0MjI3Y2Y2ZWEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInRhb2Jhby5iYWJhemh1amkuY29tIiwKICAicGF0aCI6ICIvZGlkaSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDVAMTk4LjE4MS41Ni4xNjM6MjM4#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lm1s44CRIiwKICAiYWRkIjogIjE3Mi42NC4xNTMuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDE5IiwKICAiYWRkIjogInRhb2Jhby5iYWJhemh1amkuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMmE0OTE4ZGUtYWRjZS00YzRlLWFhMDAtODhhNDIyN2NmNmVhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ0YW9iYW8uYmFiYXpodWppLmNvbSIsCiAgInBhdGgiOiAiL2RpZGkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrPCfh6cgR0IgNDEiLAogICJhZGQiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://d4e41ff772c7fd45@23.247.137.70:3389?allowInsecure=1&sni=921tw.tfzhc.top#BH%201%20%E2%86%92%20openitsub.com

</details>

### 所有节点
合并节点总数: `2420`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `230`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `145`
- [freefq/free](https://github.com/freefq/free), 节点数量: `45`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `382`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `23`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `12`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `3`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `98`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `136`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `40`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `40`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `40`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `193`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `168`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `270`
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
