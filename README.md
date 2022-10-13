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

    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hVU18xMCIsCiAgImFkZCI6ICIxMzguMi4xNS4yMyIsCiAgInBvcnQiOiA0NjM3MCwKICAiaWQiOiAiOTk4MTUxZTUtMGJjNS00Mzc3LWUzOTAtYzQxYmIyNmZkZDBjIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuMTUuMjMiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://c09eb137-bf68-4658-84e0-102d94b74168@150.230.217.213:443?allowInsecure=1&sni=flowery.meijireform.com#%E7%BE%8E%E5%9B%BD%20040
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C47.18Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@jgwdj3.gaox.ml:443?allowInsecure=1&sni=dl.sg7.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B380
    trojan://fbb2cc06-b018-4ad0-bb27-baa4a834807f@jp-az.uuuglass.co:29999?allowInsecure=1&sni=jp-ln.uuuglass.co#%5B%E6%97%A5%E6%9C%AC9%5DNTT%2B%E6%9D%AD%E5%B7%9EBGP%E5%85%A5%E5%8F%A3%2BTV
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5be06KW/IDAwMSIsCiAgImFkZCI6ICIxNjguMTM4LjIwNy42NiIsCiAgInBvcnQiOiAyMTM2NSwKICAiaWQiOiAiOTA1Zjk5YjEtZTdiYS00NWUwLWFlNGQtYjBmZmRmMGFkMjQ1IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTY4LjEzOC4yMDcuNjYiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://da777aae-defb-41d0-a183-2c27da2b4677@150.230.96.103:443?allowInsecure=1&sni=dl.shcujpntt6.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20031
    trojan://zFyLKH62WN@138.2.8.227:44150?allowInsecure=1&sni=dl.bgp8.cc.tjcct.xyz#JP_138.2.8.227_1012a0e8-91
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7h8VEfpopHpgZNAYmFpcGlhb2V2ZXJ5dGhpbmd8MTMiLAogICJhZGQiOiAiMTM4LjIuOC4yMjciLAogICJwb3J0IjogNTk0NDIsCiAgImlkIjogIjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOC4yLjguMjI3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMzA2IiwKICAiYWRkIjogIlBMLm5leGl0YWxseS54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI1NGM2YzgyMy00OTU3LTRjNmMtYjEwYy0zNTliYzUxZjdjYzMiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIlBMLm5leGl0YWxseS54eXoiLAogICJwYXRoIjogIi9hNTRlMjg0Y2I2LyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwNjEiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=flowery.meijireform.com#%E7%BE%8E%E5%9B%BD%20038
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7jnvo7lm70o5qyi6L+O6K6i6ZiFWW91dHViZeWFg+S6qOWIqei0nilfMTEiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy5wcnByLmxpbmsiLAogICJwYXRoIjogIi9UZWxlZ3JhbS9TaGFyZUNlbnRyZVByby9ta25uaXgiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDMyIiwKICAiYWRkIjogInNnLnBycHIubGluayIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImNlYTQyMTYxLWJkZGMtNDIzMC1hOWI5LWU0MzE4Nzk2N2ZmYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVPjgJDku5jotLnmjqjojZDvvJp3eGZ6Lmdx44CRIiwKICAiYWRkIjogImFncm91cC5ub2RlMi52Lm5vZGVsaXN0LWdmd2FpcnBvcnQuZG93bmxvYWQiLAogICJwb3J0IjogNTAwMDEsCiAgImlkIjogImRkZWE0ZDZiLTUyZjktNDkwMS04ZGQ2LTQ5YmQyZTA5ZjJhYyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImFncm91cC5ub2RlMi52Lm5vZGVsaXN0LWdmd2FpcnBvcnQuZG93bmxvYWQiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiW+WPsOa5vjFd5paw5YyXIOWuieW+vUJHUOWFpeWPoyBUViIsCiAgImFkZCI6ICJ0dy1zYy51dXVnbGFzcy5jbyIsCiAgInBvcnQiOiA1MjIyMiwKICAiaWQiOiAiZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidHctc2MudXV1Z2xhc3MuY28iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI3NDQiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy5wcnByLmxpbmsiLAogICJwYXRoIjogIi9UZWxlZ3JhbS9TaGFyZUNlbnRyZVByby9ta25uaXgiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxMTYiLAogICJhZGQiOiAiaGFuZ3VvYi55b25neWV2cG4uY29tIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJoYW5ndW9iLnlvbmd5ZXZwbi5jb20iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIwMjUiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://aa12A45bbutassOAm96ahzNlGY@45.11.92.100:8848?allowInsecure=1&sni=921tw.tfzhc.top#%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiKFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAic2hvcGlmeS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogIjI1MDhjYjFkLWJkNTQtNDdjMC1hZWFkLTFiOGY1NTA5MDQyNyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2N3LmNsb3VkZmxhcmUucXVlc3QiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlDjgJDku5jotLnmjqjojZDvvJp3eGZ6Lmdx44CRIiwKICAiYWRkIjogIjguMjA5LjIyMC4zNCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiNzQ3NThmMDYtZjRiOS00ZWYxLWE4NmMtZjBhMGNjODIxMDlmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsdXguanVzdHUubWwiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwMTAiLAogICJhZGQiOiAiMy4zOS4yMjIuMzYiLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjMuMzkuMjIyLjM2IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxMTUiLAogICJhZGQiOiAiMy4zOS4yMjIuMzYiLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjMuMzkuMjIyLjM2IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIwNDQiLAogICJhZGQiOiAiYmdwLmhrLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImJncC5oay5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSVLjgJDku5jotLnmjqjojZDvvJp3eGZ6Lmdx44CRIiwKICAiYWRkIjogIk1haHNhUHJveHlUZWxlZ3JhbUNoYW5uZWwud2F5LW9mLWZyZWVkb20uY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJiODMxMzgxZC02MzI0LTRkNTMtYWQ0Zi04Y2RhNDhiMzA4MTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiY2hhY2hhMjAtcG9seTEzMDUiLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJNYWhzYVByb3h5VGVsZWdyYW1DaGFubmVsLndheS1vZi1mcmVlZG9tLmNvbSIsCiAgInBhdGgiOiAiL2dyYXBocWwiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://aa12A45bbutassOAm96ahzNlGY@45.11.92.100:8848?allowInsecure=1&sni=45.11.92.100#US-trojan
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDE5MCIsCiAgImFkZCI6ICIxOTguNDEuMjEyLjIwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTViYThiMmItOGZjNS00NTIxLWEzNWUtOTI4MWJlNjFjMWMzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzEuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTIwMTIiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIwNDQiLAogICJhZGQiOiAiYmdwLmhrLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImJncC5oay5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXKFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5LyK5pyXXzEwMTIwMTMiLAogICJhZGQiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwb3J0IjogODAsCiAgImlkIjogImI4MzEzODFkLTYzMjQtNGQ1My1hZDRmLThjZGE0OGIzMDgxMSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiTWFoc2FQcm94eVRlbGVncmFtQ2hhbm5lbC53YXktb2YtZnJlZWRvbS5jb20iLAogICJwYXRoIjogIi9ncmFwaHFsIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://fbb2cc06-b018-4ad0-bb27-baa4a834807f@hk-satellite.iqyun.zone:12225?allowInsecure=1&sni=hk-wtt.uuuglass.co#%5B%E9%A6%99%E6%B8%AF%E4%BC%81%E5%AE%BD2%5D%E9%A6%99%E6%B8%AFBGP%2BTV
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dl.bgp3.cc.tjcct.xyz#mianfeifq%2B253
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDEiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiYmdwLmhrLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImJncC5oay5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=dl.shcujpntt6.cc.tjcct.xyz#mianfeifq%2B248
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxMzAiLAogICJhZGQiOiAiY24taS5wYW5ub2RlLnRvcCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiYmFlODZkOTctMzFlMi00NzM2LWJhMjMtMjE5YWE3YmIzMmViIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ0bXMuZGluZ3RhbGsuY29tIiwKICAicGF0aCI6ICIvd3Jvb3Q/ZWQ9MjA0OCIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxOTgiLAogICJhZGQiOiAic2cucGFubm9kZS50b3AiLAogICJwb3J0IjogODAsCiAgImlkIjogImJhZTg2ZDk3LTMxZTItNDczNi1iYTIzLTIxOWFhN2JiMzJlYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidG1zLmRpbmd0YWxrLmNvbSIsCiAgInBhdGgiOiAiL3dyb290LXNnP2VkPTIwNDgiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B10
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDEiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1nY206ZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmQGhrLW1zNC5pcWRuc2lvLmNvOjYwNTY=#github.com/freefq%20-%20%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%207
    vmess://ewogICJ2IjogMiwKICAicHMiOiAidjJyYXlmcmVlLmV1Lm9yZyAtIOa+s+Wkp+WIqeS6muaWsOWNl+WogeWwlOWjq+W3nuaCieWwvExpbm9kZeaVsOaNruS4reW/gyAyOCIsCiAgImFkZCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicGF0aCI6ICIvY2hhdCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HsPCfh7dLUi01Mi43OS4xMjYuMTY1LTAwNyIsCiAgImFkZCI6ICJoYW5ndW9hLnlvbmd5ZXZwbi5jb20iLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImhhbmd1b2EueW9uZ3lldnBuLmNvbSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B10
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivKFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAic2cucGFubm9kZS50b3AiLAogICJwb3J0IjogODAsCiAgImlkIjogImJhZTg2ZDk3LTMxZTItNDczNi1iYTIzLTIxOWFhN2JiMzJlYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidG1zLmRpbmd0YWxrLmNvbSIsCiAgInBhdGgiOiAiL3dyb290LXNnP2VkPTIwNDgiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDMiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxNDkiLAogICJhZGQiOiAiYXouaGsyLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF6LmhrMi5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxNDkiLAogICJhZGQiOiAiYXouaGsyLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF6LmhrMi5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTI3NDQiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy5wcnByLmxpbmsiLAogICJwYXRoIjogIi9UZWxlZ3JhbS9TaGFyZUNlbnRyZVByby9ta25uaXgiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDMiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7jnvo7lm70o5qyi6L+O6K6i6ZiFWW91dHViZeWFg+S6qOWIqei0nilfMTEiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJzZy5wcnByLmxpbmsiLAogICJwYXRoIjogIi9UZWxlZ3JhbS9TaGFyZUNlbnRyZVByby9ta25uaXgiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71NaWNyb3NvZnTmlbDmja7kuK3lv4MgNCIsCiAgImFkZCI6ICJjbi1paS5wYW5ub2RlLnRvcCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiYmFlODZkOTctMzFlMi00NzM2LWJhMjMtMjE5YWE3YmIzMmViIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ0bXMuZGluZ3RhbGsuY29tIiwKICAicGF0aCI6ICIvd3Jvb3Q/ZWQ9MjA0OCIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmvrPlpKfliKnkuprmlrDljZflqIHlsJTlo6vlt57mgonlsLxMaW5vZGXmlbDmja7kuK3lv4MgMzMiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7At6aaZ5rivLWF6LmhrMi5lY3lkbnMuY29tIiwKICAiYWRkIjogImF6LmhrMi5lY3lkbnMuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWIyMTRhYzUtZmY5OS0zMGIwLThmNDYtYzQ5NTgwNzRjMWY2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhei5oazIuZWN5ZG5zLmNvbSIsCiAgInBhdGgiOiAiL2VjeSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxMzEiLAogICJhZGQiOiAiZG1pdC5oay5lY3lkbnMuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWIyMTRhYzUtZmY5OS0zMGIwLThmNDYtYzQ5NTgwNzRjMWY2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJkbWl0LmhrLmVjeWRucy5jb20iLAogICJwYXRoIjogIi9lY3kiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDQiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDI2OCIsCiAgImFkZCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicGF0aCI6ICIvY2hhdCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwNzEiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=sni=hnyd.52147.top#%F0%9F%87%A8%F0%9F%87%B3_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%A7%F0%9F%87%AD_BH_%E5%B7%B4%E6%9E%97
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwNzIiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxMzQiLAogICJhZGQiOiAiYXouaGsyLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF6LmhrMi5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDQiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@152.67.98.30:443?allowInsecure=1&sni=924hk02.tfzhc.top#%F0%9F%87%A6%F0%9F%87%BA_AU_%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A_2
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiW+mmmea4r01TMV3lub/muK9BR0HliqDpgJ8gVFYiLAogICJhZGQiOiAiaGstbXMxLmlxZG5zaW8uY28iLAogICJwb3J0IjogMzExMTEsCiAgImlkIjogImZiYjJjYzA2LWIwMTgtNGFkMC1iYjI3LWJhYTRhODM0ODA3ZiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImhrLW1zMS5pcWRuc2lvLmNvIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxMzEiLAogICJhZGQiOiAiZG1pdC5oay5lY3lkbnMuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWIyMTRhYzUtZmY5OS0zMGIwLThmNDYtYzQ5NTgwNzRjMWY2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJkbWl0LmhrLmVjeWRucy5jb20iLAogICJwYXRoIjogIi9lY3kiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxMzQiLAogICJhZGQiOiAiYXouaGsyLmVjeWRucy5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlYjIxNGFjNS1mZjk5LTMwYjAtOGY0Ni1jNDk1ODA3NGMxZjYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF6LmhrMi5lY3lkbnMuY29tIiwKICAicGF0aCI6ICIvZWN5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjMxIiwKICAiYWRkIjogIjE3Mi42NC4xNTQuMjAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTgwMzBhZmQtODEyYS00YWZlLWE3NjYtOWM3NmZmM2VkZGQ0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzQuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://6222266fcd4ed224@116.129.253.134:3381?allowInsecure=1&sni=ctldl.windowsupdate.com#CN%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.gq%E3%80%91
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C234.03Mb
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@jgwxn4.gaox.ml:443?allowInsecure=1&sni=content-provider5.cdn-delivery.akamaicd.com#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20004
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxNDQiLAogICJhZGQiOiAiYXouaGsuZWN5ZG5zLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViMjE0YWM1LWZmOTktMzBiMC04ZjQ2LWM0OTU4MDc0YzFmNiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYXouaGsuZWN5ZG5zLmNvbSIsCiAgInBhdGgiOiAiL2VjeSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HrfCfh7BISy0xMDQuMjA4LjExNi4xODctMTAxIiwKICAiYWRkIjogImNuLWkucGFubm9kZS50b3AiLAogICJwb3J0IjogODAsCiAgImlkIjogImJhZTg2ZDk3LTMxZTItNDczNi1iYTIzLTIxOWFhN2JiMzJlYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidG1zLmRpbmd0YWxrLmNvbSIsCiAgInBhdGgiOiAiL3dyb290P2VkPTIwNDgiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6aaZ5rivXzEwMTIxNDQiLAogICJhZGQiOiAiYXouaGsuZWN5ZG5zLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImViMjE0YWM1LWZmOTktMzBiMC04ZjQ2LWM0OTU4MDc0YzFmNiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYXouaGsuZWN5ZG5zLmNvbSIsCiAgInBhdGgiOiAiL2VjeSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=sni=huayun.xyz#999
    ss://YWVzLTI1Ni1nY206ZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmQGhrLW1zNC5pcWRuc2lvLmNvOjYwNTY=#github.com/freefq%20-%20%E9%A6%99%E6%B8%AF%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%207
    trojan://e8c1ab3c-89b3-4933-92df-682e6dce7819@152.67.98.30:443?allowInsecure=1&sni=112.fastea.top#AU%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.gq%E3%80%91
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=ctldl.windowsupdate.com#HK%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Awxfz.gq%E3%80%91
    ss://YWVzLTI1Ni1nY206ZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmQGhrLW1zNC5pcWRuc2lvLmNvOjYwNTY=#%5B10-13%5D-%F0%9F%87%AD%F0%9F%87%B0-%E9%A6%99%E6%B8%AF-034-hk-ms4.iqdnsio.co
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=dl.sg6.cc.tjcct.xyz#mianfeifq%2B279
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-ph.qchwnd.moe#SG_159.223.89.239_1012b7e8-72
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20Relay_Relay_Relay_Relay_Relay_Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_1207%F0%9F%87%BA%F0%9F%87%B8US%20%7C234.03Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiW+mmmea4r01TMV3lub/muK9BR0HliqDpgJ8gVFYiLAogICJhZGQiOiAiaGstbXMxLmlxZG5zaW8uY28iLAogICJwb3J0IjogMzExMTEsCiAgImlkIjogImZiYjJjYzA2LWIwMTgtNGFkMC1iYjI3LWJhYTRhODM0ODA3ZiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImhrLW1zMS5pcWRuc2lvLmNvIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNDUiLAogICJhZGQiOiAiOC4yMDkuMjIwLjM0IiwKICAicG9ydCI6IDgwLAogICJpZCI6ICI3NDc1OGYwNi1mNGI5LTRlZjEtYTg2Yy1mMGEwY2M4MjEwOWYiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImx1eC5qdXN0dS5tbCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIxMjA1IiwKICAiYWRkIjogInVzNmIzMS1ub2RlLmFpcWljaGUxMjMuY29tIiwKICAicG9ydCI6IDgxOTAsCiAgImlkIjogImE5MDU5N2MxLWJhYjMtNDIxNy1hZDZmLTA4Mzg2NzVjODY1MyIsCiAgImFpZCI6IDEwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ3d3cuZmxpZXN3aW1pbmcudGsiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1nY206ZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmQGhrLW1zNC5pcWRuc2lvLmNvOjYwNTY=#%5B%E9%A6%99%E6%B8%AF7-2%5DMS%2B%E4%B8%89%E7%BD%91CN2GIA%E5%85%A5%E5%8F%A3%2BTV%2B%E8%B6%85%E5%A4%A7%E5%B8%A6%E5%AE%BD%E4%BD%8E%E5%BB%B6%E8%BF%9F%E8%8A%82%E7%82%B9
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=linus.sbs#SG_159.223.89.239_1012b7e8-72
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C234.03Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-ph.qchwnd.moe#SG_159.223.89.239_1012b7e8-72
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71NaWNyb3NvZnTmlbDmja7kuK3lv4MgNSIsCiAgImFkZCI6ICJoay1tczEuaXFkbnNpby5jbyIsCiAgInBvcnQiOiAzMTExMSwKICAiaWQiOiAiZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiaGstbXMxLmlxZG5zaW8uY28iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1nY206ZmJiMmNjMDYtYjAxOC00YWQwLWJiMjctYmFhNGE4MzQ4MDdmQGhrLW1zNC5pcWRuc2lvLmNvOjYwNTY=#%5B%E9%A6%99%E6%B8%AF7-2%5DMS%2B%E4%B8%89%E7%BD%91CN2GIA%E5%85%A5%E5%8F%A3%2BTV%2B%E8%B6%85%E5%A4%A7%E5%B8%A6%E5%AE%BD%E4%BD%8E%E5%BB%B6%E8%BF%9F%E8%8A%82%E7%82%B9

</details>

### 所有节点
合并节点总数: `5290`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `193`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `149`
- [freefq/free](https://github.com/freefq/free), 节点数量: `38`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3166`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `91`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `22`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `4`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `3`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `114`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `147`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `36`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `39`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `26`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `200`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `174`
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
