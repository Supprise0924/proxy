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

    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=eksrda.meijireform.com#%E7%BE%8E%E5%9B%BD%20018
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiS1JfMTQ2LjU2LjE1NS43MF8xMDExODNlNi0xOTkiLAogICJhZGQiOiAiMTQ2LjU2LjE1NS43MCIsCiAgInBvcnQiOiAxODA1MCwKICAiaWQiOiAiZjk3NzFjMTktYzkxYy00MWI1LTkwNjQtODc2OGI1MWNlYzZkIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTQ2LjU2LjE1NS43MCIsCiAgInBhdGgiOiAiL2xpdmUiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4989?allowInsecure=1&sni=gzhkhkt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%20105%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hr/Cfh7UgSlAgMTA1IiwKICAiYWRkIjogIjE0Ni41Ni4xNTUuNzAiLAogICJwb3J0IjogMTgwNTAsCiAgImlkIjogImY5NzcxYzE5LWM5MWMtNDFiNS05MDY0LTg3NjhiNTFjZWM2ZCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE0Ni41Ni4xNTUuNzAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgNTg5IiwKICAiYWRkIjogIjE2OC4xMzguMjA3LjY2IiwKICAicG9ydCI6IDIxMzY1LAogICJpZCI6ICI5MDVmOTliMS1lN2JhLTQ1ZTAtYWU0ZC1iMGZmZGYwYWQyNDUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNjguMTM4LjIwNy42NiIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4989?allowInsecure=1&sni=flowery.meijireform.com#CN_139.227.50.179_101183e6-345
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=eksrda.meijireform.com#%E7%BE%8E%E5%9B%BD%20026
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlAg5pel5pysKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogIjE3Mi42NC4xNDQuMTkyIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTIxYjI2NjUtMGU3ZC00ZGFjLWRmZGItODkxYWIzOTJiZGVjIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJqcDIubW9jaGVuMTMxNC5nYSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=dl.shcujpntt2.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B34%2BTG%3A%40nodpai
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlBfMTM4LjIuOC4yMjdfMTAxMTgzZTYtNzciLAogICJhZGQiOiAiMTM4LjIuOC4yMjciLAogICJwb3J0IjogNTk0NDIsCiAgImlkIjogIjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOC4yLjguMjI3IiwKICAicGF0aCI6ICIvYXRHMzdZTlcvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@shcuac.aag436.ccddn4.icu:65524?allowInsecure=1&sni=flowery.meijireform.com#CN_139.227.50.179_101183e6-334
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDMxNCIsCiAgImFkZCI6ICIxNTIuNzAuMjM1LjIwNyIsCiAgInBvcnQiOiAzNTQxMiwKICAiaWQiOiAiNzBkOTUzMDgtMmE2MS00ZjkzLWYxMzktOTEwM2QwNTg3ZmQ5IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjcwLjIzNS4yMDciLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@cn-sh.sasg4e.ccddn4.icu:65525?allowInsecure=1&sni=dl.shcuhkt4.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2014%20%E2%86%92%20openitsub.com
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=112.fastea.top#%7C50.34Mb
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%202%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@cn-sh.sasg4e.ccddn4.icu:4901?allowInsecure=1&sni=dl.shcujpntt6.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2042%20%E2%86%92%20openitsub.com
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@cn-sh.sasg4e.ccddn4.icu:65520?allowInsecure=1&sni=dl.shcujpntt4.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B30%2BTG%3A%40airproxies
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65525?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B68
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=zj.ecvvvw.cn#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B60
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4532?allowInsecure=1&sni=dl.shcuhkbn.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2022%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HsPCfh7dLUi0zLjM1LjEzNi4xNTMtMDEwIiwKICAiYWRkIjogIjMuMzUuMTM2LjE1MyIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMy4zNS4xMzYuMTUzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@cn-sh.sasg4e.ccddn4.icu:65523?allowInsecure=1&sni=dl.shcujpntt5.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2044%20%E2%86%92%20openitsub.com
    trojan://c58b5a1f-af92-3108-997e-ca513b1c9747@zj.ecvvvw.cn:48002?allowInsecure=1&sni=zj.ecvvvw.cn#%F0%9F%87%B8%F0%9F%87%AC%2BTG%E9%A2%91%E9%81%93%3A%40kxswa%2B%7C%2B%E6%96%B0%E5%8A%A0%E5%9D%A1%2B02
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiUlUg5L+E572X5pavKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInNob3BpZnkuY29tIiwKICAicG9ydCI6IDIwODYsCiAgImlkIjogIjczNGIyMWYyLTRhYjAtNDc4ZC1kOTE5LWE0NzhhNTZmMWRjZSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAianVzdGhvc3QuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4988?allowInsecure=1&sni=dl.shcujpntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2046%20%E2%86%92%20openitsub.com
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@cn-sh.sasg4e.ccddn4.icu:65521?allowInsecure=1&sni=dl.shcuhkt2.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2048%20%E2%86%92%20openitsub.com
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@cn-sh.sasg4e.ccddn4.icu:65523?allowInsecure=1&sni=dl.shcujpntt5.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B32%2BTG%3A%40airproxies
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@cn-sh.sasg4e.ccddn4.icu:4901?allowInsecure=1&sni=dl.shcujpntt6.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B36%2BTG%3A%40airproxies
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:65526?allowInsecure=1&sni=dl.shcuhkt3.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B84%2BTG%3A%40airproxies
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:4988?allowInsecure=1&sni=jp-bgp.speedaccelerate.com#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B75
    trojan://xxoo@146.19.230.241:443?allowInsecure=1&sni=112.fastea.top#_null_null
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=ru.p1.gay#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B619
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA%20_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDI1IiwKICAiYWRkIjogIjE3Mi42NC4xNDQuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20029
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dauwxncawx.vzwzasc.cn#mianfeifq%20%7C%F0%9F%87%A8%F0%9F%87%B3%2BHK%2B17
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@211.99.96.117:65025?allowInsecure=1&sni=wel-jp.qchwnd.moe#CN_211.99.96.117_101183e6-319
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%AD%F0%9F%87%B0%20_HK_%E9%A6%99%E6%B8%AF
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%E8%8D%B7%E5%85%B0%20002
    trojan://d02058f4f819dced@116.129.253.134:3381?allowInsecure=1&sni=ctldl.windowsupdate.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2072%20%E2%86%92%20openitsub.com
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=112.fastea.top#%7C71.07Mb
    trojan://6222266fcd4ed224@116.129.253.134:3381?allowInsecure=1&sni=ctldl.windowsupdate.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2071%20%E2%86%92%20openitsub.com
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@159.223.89.239:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20openitsub.com
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=sni=jpa.jiashumao.net#999
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=eksrda.meijireform.com#%E7%BE%8E%E5%9B%BD%20021
    ss://Y2hhY2hhMjAtaWV0ZjpOUU5wRnZAMTE2LjEyOS4yNTQuNDU6MTE5Nzk=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2032%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMzUiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@116.129.254.7:4570?allowInsecure=1&sni=hnjpntt2.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2051%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiQVUg5r6z5aSn5Yip5LqaKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInZhdTEuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZhdTEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDMiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://c58b5a1f-af92-3108-997e-ca513b1c9747@zj.ecvvvw.cn:46001?allowInsecure=1&sni=zj.ecvvvw.cn#%F0%9F%87%AF%F0%9F%87%B5%2BTG%E9%A2%91%E9%81%93%3A%40kxswa%2B%7C%2B%E6%97%A5%E6%9C%AC%2B02
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifCAxLjc5TWIiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1My4xMzg6MjEwNzI=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2077%20%E2%86%92%20openitsub.com
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=112.fastea.top#%7C301.90Mb
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://c58b5a1f-af92-3108-997e-ca513b1c9747@zj.ecvvvw.cn:46000?allowInsecure=1&sni=zj.ecvvvw.cn#%F0%9F%87%AF%F0%9F%87%B5%2BTG%E9%A2%91%E9%81%93%3A%40kxswa%2B%7C%2B%E6%97%A5%E6%9C%AC%2B01
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=flowery.meijireform.com#mianfeifq%2B189
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=gbo02.vsvideo.shop#mianfeifq%2B256
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMSIsCiAgImFkZCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwKICAicGF0aCI6ICIvY2hhdCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0ZjpOUU5wRnZAMTE2LjEyOS4yNTQuMzU6MTE5Nzk=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2031%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMjQiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1NC43OjIxMDcy#%F0%9F%87%A8%F0%9F%87%B3%20CN%2078%20%E2%86%92%20openitsub.com
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B9%2BTG%3A%40nodpai%2B%28Beta%29
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@120.241.126.83:65211?allowInsecure=1&sni=gghkntt.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B44%2BTG%3A%40nodpai
    trojan://zFyLKH62WN@www.sxsy88.tk:44150?allowInsecure=1&sni=hk-01.nodemao.com#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTEyOC1jdHI6VGFlc3NpY2ExMDI2QDExNi4xMjkuMjU0LjM1OjEyMTQ0#%F0%9F%87%A8%F0%9F%87%B3%20CN%2086%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzNCIsCiAgImFkZCI6ICJ1cy5rYXBvay5idXp6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWI0NTUwYTEtYmQ2My00ZjljLWI0YjYtZmRkMjRiNDQwNzI4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTEyOC1jdHI6VGFlc3NpY2ExMDI2QDExNi4xMjkuMjUzLjEzODoxMjE0NA==#%F0%9F%87%A8%F0%9F%87%B3%20CN%2049%20%E2%86%92%20openitsub.com
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=112.fastea.top#Relay_Relay_%20%7C301.90Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#Relay_%20%7C50.15Mb
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%A6%F0%9F%87%BA%2BAU%2B8
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=sdhawuyfkjuwx.vzwzasc.cn#GH
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwNTciLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%E7%99%BD%E5%AB%96-0313
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65210?allowInsecure=1&sni=gztwkbt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2079%20%E2%86%92%20openitsub.com
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@211.99.96.117:65022?allowInsecure=1&sni=dl.shcujpntt2.cc.tjcct.xyz#CN_211.99.96.117_101183e6-343
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDI0IiwKICAiYWRkIjogImVlLm9wcG8ucXVlc3QiLAogICJwb3J0IjogODAsCiAgImlkIjogImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZWUub3Bwby5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@211.99.96.117:65022?allowInsecure=1&sni=dl.sg6.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2074%20%E2%86%92%20openitsub.com
    trojan://289xWT@14.29.147.58:10246?allowInsecure=1&sni=ctldl.windowsupdate.com#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B11%2BTG%3A%40airproxies
    trojan://PGp7fn@14.29.147.58:10246?allowInsecure=1&sni=ctldl.windowsupdate.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%208%20%E2%86%92%20openitsub.com
    trojan://5bc96fd6-8432-31b2-9524-9910eabaa4aa@shcuac.aag436.ccddn4.icu:65522?allowInsecure=1&sni=dl.gdcmhinet3.cc.tjcct.xyz#CN_139.227.50.179_101183e6-346
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@120.241.126.83:65208?allowInsecure=1&sni=dl.gdcmhinet3.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2034%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65212?allowInsecure=1&sni=dl.shcujpntt5.cc.tjcct.xyz#CN_120.241.126.83_101183e6-284

</details>

### 所有节点
合并节点总数: `2421`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `135`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `130`
- [freefq/free](https://github.com/freefq/free), 节点数量: `36`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `382`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `113`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `12`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `3`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `97`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `132`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `30`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `40`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `196`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `195`
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
