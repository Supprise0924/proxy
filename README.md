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

    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDI0IiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZTQ4NTk2Yy1mMTU5LTQ5OGItYTMzMy1hMGI4NjgzY2JhN2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQwMjIiLAogICJhZGQiOiAidmpwMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmpwMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LXN0cmVhbS5hemFkcmFoMjIuY29tIiwKICAiYWRkIjogInN0cmVhbS5hemFkcmFoMjIuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI3NmUxNTFhNy05OTgwLTQwNzctYmQ1Mi0wN2VmNGU5Y2I0OTYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInN0cmVhbS5hemFkcmFoMjIuY29tIiwKICAicGF0aCI6ICIvdXNlciIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQyMTQiLAogICJhZGQiOiAiMTguMTgxLjE1Mi4xMCIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTguMTgxLjE1Mi4xMCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=n2.gladns.com#%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan/Tokyo_16
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiRlIg5rOV5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogIm1haHNhcHJveHljaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiYjgzMTM4MWQtNjMyNC00ZDUzLWFkNGYtOGNkYTQ4YjMwODExIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJtYWhzYXByb3h5Y2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjAyM2UzOTU4LTk1NjUtNDA4Ni1jNzY1LTVlOTc3ZWY2ZjE2NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBhdGgiOiAiL3JheSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXKFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTQxMjQ3IiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZTQ4NTk2Yy1mMTU5LTQ5OGItYTMzMy1hMGI4NjgzY2JhN2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTQxMjY0IiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwMjNlMzk1OC05NTY1LTQwODYtYzc2NS01ZTk3N2VmNmYxNjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDI1IiwKICAiYWRkIjogIjE3Mi42NC4xNDQuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://Sp3eDVp@content-provider6.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%AB%F0%9F%87%B7%2BFR%2B3
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=content-provider26.cdn-delivery.akamaicd.com#%E7%BE%8E%E5%9B%BD%20026
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C51.45Mb
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=jgwdj3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B379
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgSlAgMTA1IiwKICAiYWRkIjogIjE0Ni41Ni4xNTUuNzAiLAogICJwb3J0IjogMTgwNTAsCiAgImlkIjogImY5NzcxYzE5LWM5MWMtNDFiNS05MDY0LTg3NjhiNTFjZWM2ZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE0Ni41Ni4xNTUuNzAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=n2.gladns.com#%5B09-26%5D%7Copenrunner%7C%E6%97%A5%E6%9C%AC%28JP%29Japan/Tokyo_16
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgX0pQX+aXpeacrCIsCiAgImFkZCI6ICIxNzIuMTA1LjIzOS4yNDEiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIzNzA2MTYxZi0zZWUzLTQ4ZTUtYmZjZi0wZDg1NmNjNmYwYWIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImpzLmFkYnNlLnh5eiIsCiAgInBhdGgiOiAiL2Rvd24iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20openitsub.com
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#Relay_Relay_%20%7C51.45Mb%202
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=content-provider26.cdn-delivery.akamaicd.com#%E7%BE%8E%E5%9B%BD%20034
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTQxMzc0IiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJjZTQ4NTk2Yy1mMTU5LTQ5OGItYTMzMy1hMGI4NjgzY2JhN2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28ubWwiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTQ4NjgiLAogICJhZGQiOiAiYXJtanAuZmluZXlvby5jZiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjEzNGU2YTM3LTIxMzktNDNlYy1mMzY3LTQ3MDQ0ZGJhMjIwYyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYXJtanAuZmluZXlvby5jZiIsCiAgInBhdGgiOiAiL3JheSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7VKUC0xOC4xODEuMTUyLjEwLTA3MiIsCiAgImFkZCI6ICIxOC4xODEuMTUyLjEwIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxOC4xODEuMTUyLjEwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hVU18xMCIsCiAgImFkZCI6ICIxMzguMi4xNS4yMyIsCiAgInBvcnQiOiA0NjM3MCwKICAiaWQiOiAiOTk4MTUxZTUtMGJjNS00Mzc3LWUzOTAtYzQxYmIyNmZkZDBjIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuMTUuMjMiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTQwMTkiLAogICJhZGQiOiAic3RyZWFtLmF6YWRyYWgyMi5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogIjc2ZTE1MWE3LTk5ODAtNDA3Ny1iZDUyLTA3ZWY0ZTljYjQ5NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic3RyZWFtLmF6YWRyYWgyMi5jb20iLAogICJwYXRoIjogIi91c2VyIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%207%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTIwMDEiLAogICJhZGQiOiAibWFoc2Fwcm94eWNoYW5uZWwud2F5LW9mLWZyZWVkb20uY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm1haHNhcHJveHljaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsCiAgInBhdGgiOiAiL2dyYXBocWwiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTIwMTIiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNzU1IiwKICAiYWRkIjogIjEzOC4yLjE1LjIzIiwKICAicG9ydCI6IDQ2MzcwLAogICJpZCI6ICI5OTgxNTFlNS0wYmM1LTQzNzctZTM5MC1jNDFiYjI2ZmRkMGMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzguMi4xNS4yMyIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9Mnx0Z+mikemBkzpAcmlwYW9qaWVkaWFuIiwKICAiYWRkIjogIjU0LjE4MC4xNTcuMjU0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjBhMWUzZDEtOWZiMC00ZjA5LThiYzktYjc1ZWMzMWExODU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiNTQuMTgwLjE1Ny4yNTQiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQyMzQiLAogICJhZGQiOiAiMTguMTgxLjE1Mi4xMCIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTguMTgxLjE1Mi4xMCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5be06KW/IDAwMiIsCiAgImFkZCI6ICIxNjguMTM4LjIwNy42NiIsCiAgInBvcnQiOiAyMTM2NSwKICAiaWQiOiAiOTA1Zjk5YjEtZTdiYS00NWUwLWFlNGQtYjBmZmRmMGFkMjQ1IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTI3LjAuMC4xIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=content-provider26.cdn-delivery.akamaicd.com#%E7%BE%8E%E5%9B%BD%20035
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTUyLjcwLjI0MS4xOF8xMDEzYTAzMy0zNCIsCiAgImFkZCI6ICIxNTIuNzAuMjQxLjE4IiwKICAicG9ydCI6IDI2Njc2LAogICJpZCI6ICJlY2QyNzRjMC0xNzVkLTQ1ZjctODI3Ni1hM2RhOTM3ODY2MzIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNzAuMjQxLjE4IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD_1_6%4027
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQwNTkiLAogICJhZGQiOiAicmliZW5iLnlvbmd5ZXZwbi5jb20iLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInJpYmVuYi55b25neWV2cG4uY29tIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9Mnx0Z+mikemBkzpAcmlwYW9qaWVkaWFuIiwKICAiYWRkIjogIjU0LjE4MC4xNTcuMjU0IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjBhMWUzZDEtOWZiMC00ZjA5LThiYzktYjc1ZWMzMWExODU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiNTQuMTgwLjE1Ny4yNTQiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysMXx0Z+mikemBkzpAcmlwYW9qaWVkaWFuIiwKICAiYWRkIjogIjMuMTEyLjQxLjQ3IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiMjBhMWUzZDEtOWZiMC00ZjA5LThiYzktYjc1ZWMzMWExODU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMy4xMTIuNDEuNDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgSlAgMTUyIiwKICAiYWRkIjogInZqcDEuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZqcDEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=jgwdj3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B379
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1&sni=jgwdj4.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B366
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=jgwdj3.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B619
    trojan://origin@content-provider12.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=content-provider12.cdn-delivery.akamaicd.com#%F0%9F%87%AB%F0%9F%87%B7%20FR%205%20%E2%86%92%20openitsub.com
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=jgwdj4.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD_3_8%407
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDIwNCIsCiAgImFkZCI6ICJyaWJlbmIueW9uZ3lldnBuLmNvbSIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAicmliZW5iLnlvbmd5ZXZwbi5jb20iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20openitsub.com
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1&sni=sg3-xhsa-45as-92js-ht8s.paolu.pics#JP_138.2.8.227_101320a6-41
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTQxMjUwIiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwMjNlMzk1OC05NTY1LTQwODYtYzc2NS01ZTk3N2VmNmYxNjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7h8VEfpopHpgZNAYmFpcGlhb2V2ZXJ5dGhpbmd8MTYiLAogICJhZGQiOiAiMTM4LjIuOC4yMjciLAogICJwb3J0IjogNTk0NDIsCiAgImlkIjogIjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOC4yLjguMjI3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://Sp3eDVp@content-provider13.cdn-delivery.akamaicd.com:443?allowInsecure=1&sni=content-provider13.cdn-delivery.akamaicd.com#%F0%9F%87%B3%F0%9F%87%B1%20NL%202%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQwMDgiLAogICJhZGQiOiAidmpwMS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmpwMS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1&sni=jgwdj4.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B366
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjAyM2UzOTU4LTk1NjUtNDA4Ni1jNzY1LTVlOTc3ZWY2ZjE2NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBhdGgiOiAiL3JheSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#Relay_Relay_%20%7C54.54Mb
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%2011%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgSlAgMTA1IiwKICAiYWRkIjogIjE0Ni41Ni4xNTUuNzAiLAogICJwb3J0IjogMTgwNTAsCiAgImlkIjogImY5NzcxYzE5LWM5MWMtNDFiNS05MDY0LTg3NjhiNTFjZWM2ZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE0Ni41Ni4xNTUuNzAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD_1_6%4027
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDQwIiwKICAiYWRkIjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIwMjNlMzk1OC05NTY1LTQwODYtYzc2NS01ZTk3N2VmNmYxNjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFtZGpwLmZpbmV5b28uY2YiLAogICJwYXRoIjogIi9yYXkiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTQwMTMiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@jgwdj4.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#Relay_Relay_%20%7C%209.18Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTQxNTgiLAogICJhZGQiOiAiNTQuMTgwLjE1Ny4yNTQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIyMGExZTNkMS05ZmIwLTRmMDktOGJjOS1iNzVlYzMxYTE4NTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICI1NC4xODAuMTU3LjI1NCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTUyLjcwLjI0MS4xOF8xMDEzYTAzMy0zNCIsCiAgImFkZCI6ICIxNTIuNzAuMjQxLjE4IiwKICAicG9ydCI6IDI2Njc2LAogICJpZCI6ICJlY2QyNzRjMC0xNzVkLTQ1ZjctODI3Ni1hM2RhOTM3ODY2MzIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNzAuMjQxLjE4IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%203%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysIDAwMSIsCiAgImFkZCI6ICJtNC40MDAxMDAxMC54eXoiLAogICJwb3J0IjogMzcxMjEsCiAgImlkIjogIjU3NWU0ZDkyLTEwNTYtNDRjMi04Y2FjLTc1ZWYxYzg1OWFkNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm00LjQwMDEwMDEwLnh5eiIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjAyM2UzOTU4LTk1NjUtNDA4Ni1jNzY1LTVlOTc3ZWY2ZjE2NiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYW1kanAuZmluZXlvby5jZiIsCiAgInBhdGgiOiAiL3JheSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7h8VEfpopHpgZNAYmFpcGlhb2V2ZXJ5dGhpbmd8MTYiLAogICJhZGQiOiAiMTM4LjIuOC4yMjciLAogICJwb3J0IjogNTk0NDIsCiAgImlkIjogIjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOC4yLjguMjI3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=jgwdj4.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD_3_8%407
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzMyIsCiAgImFkZCI6ICJ0ZXh0Ny54Ynl3d2NwLnVzIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI5OWUyZjUzOS03MDBmLTM5NDctYjMxYS00YzlkOTEyZmY1ZmEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIiU3QiUyMkhvc3QlMjI6JTIyYS4xODkuY24lMjIlN0QiLAogICJwYXRoIjogIi9ieS54Ynlnb29kLnh5eiIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTQxMjMiLAogICJhZGQiOiAiZWUuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZjkyNDdkZjQtMDJkNS00YjMxLWFjYzUtNDAyMjY1MmM1OTUzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJlZS5jbG91ZGZsYXJlLnF1ZXN0IiwKICAicGF0aCI6ICIvYXJpZXMiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTQwMTQiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMi4xOXwgaHR0cHNnaXRodWJjb21BbHZpbjk5OTluZXdwYWN3aWtpIGNsYXNoIGlwMiDmtJvmnYnnn7YxM0NETiIsCiAgImFkZCI6ICIxNzIuNjQuMTU1LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMi4zMnwgaHR0cHNnaXRodWJjb21BbHZpbjk5OTluZXdwYWN3aWtpIGNsYXNoIGlwMiDmtJvmnYnnn7YxQ0ROIiwKICAiYWRkIjogIjE3Mi42NC4xNTMuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTQwMDIiLAogICJhZGQiOiAibWFoc2Fwcm94eWNoYW5uZWwud2F5LW9mLWZyZWVkb20uY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm1haHNhcHJveHljaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsCiAgInBhdGgiOiAiL2dyYXBocWwiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTQxODUiLAogICJhZGQiOiAiMy4zNS4xMzguMjA1IiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJlbi5taWFvZ2UxMTAuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTQxNDgiLAogICJhZGQiOiAiMy4zNS4xMzguMjA1IiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIzLjM1LjEzOC4yMDUiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTQxMzUiLAogICJhZGQiOiAiMy4zNi4xMTMuOTIiLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjMuMzYuMTEzLjkyIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZTaGFya1RlY2jmlbDmja7kuK3lv4MgNSIsCiAgImFkZCI6ICI2Ny4yMS43Mi40NCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsCiAgImFpZCI6IDY0LAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInd3dy40ODgxNjYyNi54eXoiLAogICJwYXRoIjogIi9wYXRoLzEyMDIwODMwMTQyMiIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1Ig6Z+p5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogIjMuMzUuMTM4LjIwNSIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZW4ubWlhb2dlMTEwLmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1Ig6Z+p5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogIjMuMzUuMTM4LjIwNSIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZW4ubWlhb2dlMTEwLmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAxNCIsCiAgImFkZCI6ICI2Ny4yMS43Mi40NCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsCiAgImFpZCI6IDY0LAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInd3dy40ODgxNjYyNi54eXoiLAogICJwYXRoIjogIi9wYXRoLzEyMDIwODMwMTQyMiIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTQwMDMiLAogICJhZGQiOiAibWFoc2Fwcm94eWNoYW5uZWwud2F5LW9mLWZyZWVkb20uY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm1haHNhcHJveHljaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsCiAgInBhdGgiOiAiL2dyYXBocWwiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=jd101.8faka.tk#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20038
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTQxODYiLAogICJhZGQiOiAiMy4zNi4xMTMuOTIiLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjMuMzYuMTEzLjkyIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTQxNTEiLAogICJhZGQiOiAiOC4yMDkuMjIwLjM0IiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI3NDc1OGYwNi1mNGI5LTRlZjEtYTg2Yy1mMGEwY2M4MjEwOWYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImx1eC5qdXN0dS5tbCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI2OTciLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNTk2IiwKICAiYWRkIjogIjEzOC4yLjQ0LjIxMSIsCiAgInBvcnQiOiAyMDA4MSwKICAiaWQiOiAiNTkzYjg1MjUtMGM0OC00YjBmLWQ5YWYtMmQ3M2E5MTQ4OTczIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNTk2IiwKICAiYWRkIjogIjEzOC4yLjQ0LjIxMSIsCiAgInBvcnQiOiAyMDA4MSwKICAiaWQiOiAiNTkzYjg1MjUtMGM0OC00YjBmLWQ5YWYtMmQ3M2E5MTQ4OTczIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi44CQ5LuY6LS55o6o6I2Q77yad3hmei5tbOOAkSIsCiAgImFkZCI6ICIxNDEuMTAxLjExNC4yMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjA3YTYzZmUzLThhNDYtNGY4OS1iNTQ4LTkxNTFjNjFiOWRjOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidjJyYXkxLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=jd101.8faka.tk#mianfeifq%2B215
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=content-provider26.cdn-delivery.akamaicd.com#%E7%BE%8E%E5%9B%BD%20032
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=jgwhdlb3.gaox.ml#SG_159.223.89.239_101320a6-82
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=do-sg-01.vvsoga.net#%F0%9F%87%BA%F0%9F%87%B8%20US%2013%20%E2%86%92%20openitsub.com

</details>

### 所有节点
合并节点总数: `6115`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `195`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `136`
- [freefq/free](https://github.com/freefq/free), 节点数量: `42`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `183`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3995`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `110`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `1`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `1`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `3`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `122`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `125`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `40`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `29`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `200`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `24`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `178`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `124`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `270`
- [ClashNode](https://clashnode.com/f/freenode), 节点数量: `14`

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
