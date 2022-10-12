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

    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVNf44CQ5LuY6LS55o6o6I2Q77yad3hmei5tbOOAkSIsCiAgImFkZCI6ICIxNzIuNjQuMTQ0LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E7%BE%8E%E5%9B%BD%20030
    vmess://ewogICJ2IjogMiwKICAicHMiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6X3ZtZXNzX3dzIiwKICAiYWRkIjogInlvdXR1YmUtYmFpLXBpYW8td2FuZy16aGUtdXNhLjk4ODQ4Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImQxNDc4Njg5LTQzOWMtNDU5MC1iN2NlLTM2ZTc4NmEwMmRjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAieW91dHViZS1iYWktcGlhby13YW5nLXpoZS11c2EuOTg4NDgueHl6IiwKICAicGF0aCI6ICIvWW91VHViZUBiYWktcGlhby13YW5nLXpoZV92d3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://bb5b1337-fa9e-4e00-b8c6-1110e626171d@sg-01.tiktokcdn.top:443?allowInsecure=1&sni=sni=jpa.jiashumao.net#999
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65208?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%A8%F0%9F%87%B3%20_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%B9%F0%9F%87%BC_TW_%E5%8F%B0%E6%B9%BE
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6xTRy0xOC4xNDIuMTg1LjEzNy0wMDQiLAogICJhZGQiOiAiMTguMTQyLjE4NS4xMzciLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE4LjE0Mi4xODUuMTM3IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAidjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXoioLngrkgMTQiLAogICJhZGQiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjU0YzZjODIzLTQ5NTctNGM2Yy1iMTBjLTM1OWJjNTFmN2NjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiUEwubmV4aXRhbGx5Lnh5eiIsCiAgInBhdGgiOiAiL2E1NGUyODRjYjYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMzUiLAogICJhZGQiOiAic2cucHJwci5saW5rIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiY2VhNDIxNjEtYmRkYy00MjMwLWE5YjktZTQzMTg3OTY3ZmZhIiwKICAiYWlkIjogMCwKICAic2N5IjogImNoYWNoYTIwLXBvbHkxMzA1IiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAic2cucHJwci5saW5rIiwKICAicGF0aCI6ICIvVGVsZWdyYW0vU2hhcmVDZW50cmVQcm8vbWtubml4IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65201?allowInsecure=1&sni=gzhkntt.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B40%2BTG%3A%40airproxies
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65210?allowInsecure=1&sni=gztwkbt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2079%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65206?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2026%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxNDYuNzAuNTMuMjQyOjUwMDAw#%F0%9F%87%AC%F0%9F%87%A7%20%40SSRSUB%20-%20%E8%8B%B1%E5%9B%BD%20%207
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxNDYuNzAuNTMuMjQyOjUwMDAw#%E8%8B%B1%E5%9B%BD%20002
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65206?allowInsecure=1&sni=dl.sghgc2.cc.tjcct.xyz#CN_120.241.126.83_101183e6-361
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%E8%8D%B7%E5%85%B0%20002
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65212?allowInsecure=1&sni=dl.shcujpntt5.cc.tjcct.xyz#CN_120.241.126.83_101183e6-284
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65208?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2021%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIDIiLAogICJhZGQiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@211.99.96.117:65303?allowInsecure=1&sni=dl.shcuhkt3.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B16
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5paw5Yqg5Z2hIDAwMyIsCiAgImFkZCI6ICJ1czAyLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDIueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hfVVNf576O5Zu9LT7wn4ep8J+Hql9ERV/lvrflm71fMyIsCiAgImFkZCI6ICIxNzIuNjQuMTQ0LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiU0dfMTM5Ljk5LjkxLjk1XzEwMTA1NWI3LTY4IiwKICAiYWRkIjogIjEzOS45OS45MS45NSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsCiAgImFpZCI6IDMyLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxMzkuOTkuOTEuOTUiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wt5paw5Yqg5Z2hLXNnLW92aDEudjItcmF5LmNvbSIsCiAgImFkZCI6ICJzZy1vdmgxLnYyLXJheS5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65212?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2029%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTkzLjM3LjI1Mi4yMTA6ODEw#%5B10-12%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-690-193.37.252.210
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDExLjQ5TWIiLAogICJhZGQiOiAidXMwMi54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1czAyLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuPCfh6wgX1NHX+aWsOWKoOWdoSIsCiAgImFkZCI6ICJ1czAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInVzMDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@cn-sh.sasg4e.ccddn4.icu:4901?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2027%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTopMU4xRTZ2MFNVX3JHVHBnQDM4LjY0LjEzOC41MzoxMDM1#%F0%9F%87%A8%F0%9F%87%A6%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-38.64.138.53%3A1035-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA0#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A804-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiSlBfMTM4LjIuOC4yMjdfMTAxMTgzZTYtNzciLAogICJhZGQiOiAiMTM4LjIuOC4yMjciLAogICJwb3J0IjogNTk0NDIsCiAgImlkIjogIjZmZDA0MmZhLWU4NjQtNGE5NS04NWJjLTZmNTkwYTAzZDM0YSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEzOC4yLjguMjI3IiwKICAicGF0aCI6ICIvYXRHMzdZTlcvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://3f29ee90-8567-4671-8d99-9875874e472f@116.fastea.top:53316?allowInsecure=1&sni=wel-jp.qchwnd.moe#%F0%9F%87%BA%F0%9F%87%B8%20US%2016%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1NC4zNToyMTA3Mg==#%F0%9F%87%A8%F0%9F%87%B3%20CN%205%20%E2%86%92%20openitsub.com
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@cn-sh.sasg4e.ccddn4.icu:4901?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%BA%F0%9F%87%B8%20_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDI1IiwKICAiYWRkIjogIjE3Mi42NC4xNDQuMTAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiNmU5MjE3ZGUtYWQ3ZS00YTY3LWJkMTctYTZkY2E5NTE3MzNiIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzMuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@cn-sh.sasg4e.ccddn4.icu:4901?allowInsecure=1&sni=dl.shcujpntt6.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%20CN%2042%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDI0IiwKICAiYWRkIjogImVlLm9wcG8ucXVlc3QiLAogICJwb3J0IjogODAsCiAgImlkIjogImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZWUub3Bwby5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65210?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2022%20%E2%86%92%20openitsub.com
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%E4%BF%84%E7%BD%97%E6%96%AF%20003
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA%20_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiUlUg5L+E572X5pavKHlvdXR1YmXpmL/kvJ/np5HmioApIiwKICAiYWRkIjogInNob3BpZnkuY29tIiwKICAicG9ydCI6IDIwODYsCiAgImlkIjogIjczNGIyMWYyLTRhYjAtNDc4ZC1kOTE5LWE0NzhhNTZmMWRjZSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAianVzdGhvc3QuY2xvdWRmbGFyZS5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65207?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%201%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODEy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A812-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDMzIiwKICAiYWRkIjogIjE3Mi42NC4xNTUuMjAwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYTgwMzBhZmQtODEyYS00YWZlLWE3NjYtOWM3NmZmM2VkZGQ0IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzQuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAxODUuMTYyLjEyNi4yMTc6NTAwMDQ=#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-185.162.126.217%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODEy#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A812-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65525?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B68
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=dl.shcujpntt2.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B34%2BTG%3A%40nodpai
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1NC4zNToyMTA3Mg==#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%201
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1NC4zNToyMTA3Mg==#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%201
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65526?allowInsecure=1&sni=gzhkntt.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B44
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTk2LjI0Ny41OS4xNTQ6ODAw#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1My4xMzg6MjEwNzI=#%F0%9F%87%A8%F0%9F%87%B3%20CN%2077%20%E2%86%92%20openitsub.com
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@152.67.162.166:443?allowInsecure=1&sni=flowery.meijireform.com#%F0%9F%87%AE%F0%9F%87%B3_IN_%E5%8D%B0%E5%BA%A6_1_4%4018
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65216?allowInsecure=1&sni=sni=sg.jiashumao.net#%F0%9F%87%BA%F0%9F%87%B8%20_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%E8%8D%B7%E5%85%B0%20002
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODA1#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65525?allowInsecure=1&sni=dl.gdcmhkbgp.cc.tjcct.xyz#%F0%9F%87%A8%F0%9F%87%B3%2BCN%2B68
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%7C11.28Mb
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%5B10-12%5D-%F0%9F%87%B7%F0%9F%87%BA-%E4%BF%84%E7%BD%97%E6%96%AF-1074-ru-ss.superyuluo1.asia
    trojan://e05c749b-7c6b-41b8-9c71-9dcf685edf4a@jgwhdlb1.gaox.ml:443?allowInsecure=1&sni=flowery.meijireform.com#%F0%9F%87%BA%F0%9F%87%B8%2BUS%2B501
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmlrDliqDlnaFPVkggMTEiLAogICJhZGQiOiAic2ctb3ZoMS52Mi1yYXkuY29tIiwKICAicG9ydCI6IDgwLAogICJpZCI6ICJhOTQ4MTYwMC1lZjM2LTQwMmEtYTBlNS01NTQ3YmZkN2I4N2MiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInNnLW92aDEudjItcmF5LmNvbSIsCiAgInBhdGgiOiAiL2Zhc3Rzc2gvZmdoaGgvNjM0MTk3YzRjZGY4MS8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=dl.shcujpntt2.cc.tjcct.xyz#%E4%B8%AD%E8%BD%AC%2B%F0%9F%87%AF%F0%9F%87%B5%2BJP%2B34%2BTG%3A%40nodpai
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9IDAzNCIsCiAgImFkZCI6ICJ1cy5rYXBvay5idXp6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZWI0NTUwYTEtYmQ2My00ZjljLWI0YjYtZmRkMjRiNDQwNzI4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJ1cy5rYXBvay5idXp6IiwKICAicGF0aCI6ICIvU0NQLTkxNCIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA%20_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E6%81%8B%E7%A5%9E%E5%8A%A0%E9%80%9F_23
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiMi4yMHwgaHR0cHNnaXRodWJjb21BbHZpbjk5OTluZXdwYWN3aWtpIGNsYXNoIGlwMiDmtJvmnYnnn7YxM0NETiIsCiAgImFkZCI6ICIxNzIuNjQuMTU1LjEwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjZlOTIxN2RlLWFkN2UtNGE2Ny1iZDE3LWE2ZGNhOTUxNzMzYiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGczLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1My4xMzg6MjEwNzI=#%F0%9F%87%A8%F0%9F%87%B3%20CN%202%20%E2%86%92%20openitsub.com
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9AMTYyLjI1MS42MS4yMjE6ODAw#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-162.251.61.221%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDI0IiwKICAiYWRkIjogImVlLm9wcG8ucXVlc3QiLAogICJwb3J0IjogODAsCiAgImlkIjogImY5MjQ3ZGY0LTAyZDUtNGIzMS1hY2M1LTQwMjI2NTJjNTk1MyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiZWUub3Bwby5xdWVzdCIsCiAgInBhdGgiOiAiL2FyaWVzIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://b473e4c5-0ae7-31e5-98fb-1aac5701f9e7@120.241.126.83:65216?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A8%F0%9F%87%B3%20CN%2030%20%E2%86%92%20openitsub.com
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTAwMjEiLAogICJhZGQiOiAiMTk4LjQxLjIxMi4yMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE1YmE4YjJiLThmYzUtNDUyMS1hMzVlLTkyODFiZTYxYzFjMyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGcxLnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3YjMwZGJlMi01ZmQ5LTRmODctYTczMy1mYWNlZjM3OTYzMmJAcnUtc3Muc3VwZXJ5dWx1bzEuYXNpYToxMDM4#%F0%9F%87%B7%F0%9F%87%BA_RU_%E4%BF%84%E7%BD%97%E6%96%AF%E8%81%94%E9%82%A6
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTAwMzIiLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI2ZTkyMTdkZS1hZDdlLTRhNjctYmQxNy1hNmRjYTk1MTczM2IiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMy56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1nY206NkxzQVFWV3dxalcweEdmSUAxMTYuMTI5LjI1My4xMzg6MjEwNzI=#%F0%9F%87%BA%F0%9F%87%B8%20_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDniLHmspnlsLzkupogIDIxIiwKICAiYWRkIjogIjE3Ni4xMTIuMTQ2LjE5MCIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZjkyNDdkZjQtMDJkNS00YjMxLWFjYzUtNDAyMjY1MmM1OTUzIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNzYuMTEyLjE0Ni4xOTAiLAogICJwYXRoIjogIi9hcmllcyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxOTQuMjYuMjEzLjE1NTo1MDAwMA==#%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%20001
    ss://YWVzLTI1Ni1jZmI6MzEzNTc3MTYxOUAxODUuMTEzLjE0MC4yNDc6NTAwMDA=#%E8%91%A1%E8%90%84%E7%89%99%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiVVNf44CQ5LuY6LS55o6o6I2Q77yad3hmei5tbOOAkSIsCiAgImFkZCI6ICIxNzIuNjQuMTU0LjIwMCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImE4MDMwYWZkLTgxMmEtNGFmZS1hNzY2LTljNzZmZjNlZGRkNCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibGc0LnpodWppY24yLmNvbSIsCiAgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    trojan://e27cce7a-617d-48cb-b628-e9717be9c175@113.fastea.top:53313?allowInsecure=1&sni=n2.gladns.com#github.com/freefq%20-%20%E6%97%A5%E6%9C%AC%E4%B8%9C%E4%BA%ACLinode%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2018
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5YyI54mZ5YipXzEwMTAwMDEiLAogICJhZGQiOiAiMTg1LjIyNS42OS4xMzQiLAogICJwb3J0IjogNDUwODEsCiAgImlkIjogIjNjM2JmZDc1LWRjMzAtNGU3Ni04OTQwLTQ3ZTExMzdlMjFmOSIsCiAgImFpZCI6IDY0LAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxODUuMjI1LjY5LjEzNCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6NDQxNTkzNDI5NUAzMS4xMzMuMTAwLjQ5OjUwMDA0#%F0%9F%87%AE%F0%9F%87%B1%3A%E4%BB%A5%E8%89%B2%E5%88%97-ss-31.133.100.49%3A50004-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E4%BB%A5%E8%89%B2%E5%88%97%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://BXE9notY@nice-jp01.tiktokcdn.buzz:443?allowInsecure=1&sni=dl.bgp4.cc.tjcct.xyz#%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%20003
    ss://YWVzLTI1Ni1jZmI6dWVMWFZrdmg0aGNraEVyUUAyMTMuMTgzLjUzLjIwMDo5MDYw#213.183.53.200%3A9060
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-138.68.248.130%3A811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8%3A%E7%BE%8E%E5%9B%BD-ss-138.68.248.130%3A811-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVbHRyQHIwMHRfMjAxN0AxMzguNjguMjQ4LjEzMDo4MTE=#%F0%9F%87%BA%F0%9F%87%B8_%E6%B2%B9%E7%AE%A1%EF%BC%9A%E5%85%A8%E7%BD%91%E6%9C%80%E5%BC%BA%E7%99%BD%E5%AB%96

</details>

### 所有节点
合并节点总数: `2406`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `135`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `130`
- [freefq/free](https://github.com/freefq/free), 节点数量: `44`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `198`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `382`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `50`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `26`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `4`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `7`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `119`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `132`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `40`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `34`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `36`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `194`
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
