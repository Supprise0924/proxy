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

    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDI2IiwKICAiYWRkIjogIjE3Mi42NC4xNTMuMTUwIiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwMzQiLAogICJhZGQiOiAiMTUyLjY3LjIxOC4zOCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImI1ZTk0ODBhLWI3YWEtNDBhNC1mOWE3LTUyOTliNWUzNjNiNCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY3LjIxOC4zOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HsPCfh7dLUi0zLjM1LjEzNi4xNTMtMDEwIiwKICAiYWRkIjogIjMuMzUuMTM2LjE1MyIsCiAgInBvcnQiOiA0MzYzMiwKICAiaWQiOiAiMWQyOTc4YmEtMzBiYS00YjY0LTg2OTktOWJhNmJhM2NkNGU4IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMy4zNS4xMzYuMTUzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxNTkiLAogICJhZGQiOiAibTQuNDAwMTAwMTAueHl6IiwKICAicG9ydCI6IDM3MTIxLAogICJpZCI6ICI1NzVlNGQ5Mi0xMDU2LTQ0YzItOGNhYy03NWVmMWM4NTlhZDUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJtNC40MDAxMDAxMC54eXoiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwNDciLAogICJhZGQiOiAiMy4zNS4xMzYuMTUzIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIzLjM1LjEzNi4xNTMiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwNDQiLAogICJhZGQiOiAiMTUyLjY3LjIxOC4zOCIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImI1ZTk0ODBhLWI3YWEtNDBhNC1mOWE3LTUyOTliNWUzNjNiNCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY3LjIxOC4zOCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxNTYiLAogICJhZGQiOiAiaGFuZ3VvYS55b25neWV2cG4uY29tIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJoYW5ndW9hLnlvbmd5ZXZwbi5jb20iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwNjMiLAogICJhZGQiOiAiMy4zNC4xODcuMTAzIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIzLjM0LjE4Ny4xMDMiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HsPCfh7dLUi00My4yMDEuNTAuMjM2LTAwNyIsCiAgImFkZCI6ICJoYW5ndW9iLnlvbmd5ZXZwbi5jb20iLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImhhbmd1b2IueW9uZ3lldnBuLmNvbSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiQFNTUlNVQi1WMDgt5LuY6LS55o6o6I2QOnN1by55dC9zc3JzdWIiLAogICJhZGQiOiAiMTcyLjY0LjE1My4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNC56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxNTIiLAogICJhZGQiOiAiMy4zNS4xMzYuMTUzIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIzLjM1LjEzNi4xNTMiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HsPCfh7dLUi01Mi43OS4xMjYuMTY1LTAwNyIsCiAgImFkZCI6ICJoYW5ndW9hLnlvbmd5ZXZwbi5jb20iLAogICJwb3J0IjogNDM2MzIsCiAgImlkIjogIjFkMjk3OGJhLTMwYmEtNGI2NC04Njk5LTliYTZiYTNjZDRlOCIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImhhbmd1b2EueW9uZ3lldnBuLmNvbSIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxNTgiLAogICJhZGQiOiAiaGFuZ3VvYi55b25neWV2cG4uY29tIiwKICAicG9ydCI6IDQzNjMyLAogICJpZCI6ICIxZDI5NzhiYS0zMGJhLTRiNjQtODY5OS05YmE2YmEzY2Q0ZTgiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJoYW5ndW9iLnlvbmd5ZXZwbi5jb20iLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIxNDgiLAogICJhZGQiOiAibTQuNDAwMTAwMTAueHl6IiwKICAicG9ydCI6IDM3MTIxLAogICJpZCI6ICI1NzVlNGQ5Mi0xMDU2LTQ0YzItOGNhYy03NWVmMWM4NTlhZDUiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJqcDAzLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7hfVVNf576O5Zu9LT7wn4er8J+Ht19GUl/ms5Xlm70iLAogICJhZGQiOiAiMTcyLjY0LjE0NC4xNTQiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://f818af82-bd17-35ea-8272-5088e3a5cd76@shcuac.aag436.ccddn4.icu:65521?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%BA%F0%9F%87%B8%20_CN_%E4%B8%AD%E5%9B%BD-%3E%F0%9F%87%BA%F0%9F%87%B8_US_%E7%BE%8E%E5%9B%BD
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMiIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HpvCfh7ogX0FVX+a+s+Wkp+WIqeS6miIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMyIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMyIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDI0MyIsCiAgImFkZCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImU1YjY5ZGUxLTFkMmItNDNkZC04MjM3LTUwYzgxMWZkYzllMiIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwYXRoIjogIi92bWVzcyIsCiAgInRscyI6IHRydWUsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLAogICJhZGQiOiAiMTcyLjY0LjE1NS4yMDAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJhODAzMGFmZC04MTJhLTRhZmUtYTc2Ni05Yzc2ZmYzZWRkZDQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnNC56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaIDAwMiIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HpvCfh7ogX0FVX+a+s+Wkp+WIqeS6miIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAifDI1LjQ4TWIiLAogICJhZGQiOiAiYXUwMS54aWFvcWk5OS5jZiIsCiAgInBvcnQiOiA2MzYzMiwKICAiaWQiOiAiOTJjMGNmZDAtYmI5Zi00MjU4LWJkMGMtODAwMGFhMWExZDYyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiYWFhIDIwOSIsCiAgImFkZCI6ICJhdTAxLnhpYW9xaTk5LmNmIiwKICAicG9ydCI6IDYzNjMyLAogICJpZCI6ICI5MmMwY2ZkMC1iYjlmLTQyNTgtYmQwYy04MDAwYWExYTFkNjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1MDEueGlhb3FpOTkuY2YiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDMiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTAwMDMiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDgiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7gt576O5Zu9LWF1LnZtZXNzMS54c2VydnMueHl6IiwKICAiYWRkIjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiZTViNjlkZTEtMWQyYi00M2RkLTgyMzctNTBjODExZmRjOWUyIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJhdS52bWVzczEueHNlcnZzLnh5eiIsCiAgInBhdGgiOiAiL3ZtZXNzIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwNzkiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9ANzguMTI5LjI1My45OjgwOQ==#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW9ANzguMTI5LjI1My45OjgwOA==#%5B10-12%5D-%F0%9F%87%AC%F0%9F%87%A7-%E8%8B%B1%E5%9B%BD-582-78.129.253.9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDQiLAogICJhZGQiOiAiYXUudm1lc3MxLnhzZXJ2cy54eXoiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICJlNWI2OWRlMS0xZDJiLTQzZGQtODIzNy01MGM4MTFmZGM5ZTIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImF1LnZtZXNzMS54c2VydnMueHl6IiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSDmvrPlpKfliKnkuprmlrDljZflqIHlsJTlo6vlt57mgonlsLxMaW5vZGXmlbDmja7kuK3lv4MgMjkiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERANDUuNzcuNDguNDQ6ODA5OQ==#45.77.48.44%3A8099
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Z+p5Zu9XzEwMTIwMDMiLAogICJhZGQiOiAiMTI5LjE1NC41Ny4xMzQiLAogICJwb3J0IjogMjYyODIsCiAgImlkIjogImNhYmJkZjVkLTNjY2EtNDYwNS1iYTFjLWM4OWE3ZDViNGMwNyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjEyOS4xNTQuNTcuMTM0IiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@140.238.205.173:443?allowInsecure=1&sni=wel-ph.qchwnd.moe#AU_140.238.205.173_1012b7e8-88
    trojan://036ba5aa-fcb7-4e6f-95b5-a857cb354aa8@kr1.api-aws.com:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%B0%F0%9F%87%B7%E7%99%BD%E5%AB%96-093
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%7C50.15Mb
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20003
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pyq55+lXzEwMTIwNzYiLAogICJhZGQiOiAiMTkwLjkzLjI0Ni4xNDUiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5NDg4NzI2OC1mM2NiLTQ4YmUtYWRlMy04N2Q0MmZhYWUzZTQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIm01LnYycmF5ZnJlZTEueHl6IiwKICAicGF0aCI6ICIvcmF5IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5qyn5rSyKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIDI1IiwKICAiYWRkIjogIjE5OC40MS4yMTIuMzAiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIxMDVjNjM1Zi05MThkLTRiMmEtOGM5ZC1kNTQyNmU5NGViNGIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogImxnMi56aHVqaWNuMi5jb20iLAogICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODU5IiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIyMDE4IiwKICAiYWRkIjogImNmLm5haXhpaS50b3AiLAogICJwb3J0IjogNDQzLAogICJpZCI6ICIzZmFkM2I0Yy04NjkxLTQyZjItYTQ2ZC05ODc1Y2FjYWVlYjIiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYWVzLTEyOC1nY20iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsaW5vZGUuc2hhcmVjZW50cmUueHl6IiwKICAicGF0aCI6ICIvYjQ3MmYvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Iux5Zu9XzEwMTIxMDIiLAogICJhZGQiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://5d1b3b0a-de2a-4731-938d-4c7e15f034c1@43.229.153.148:50418?allowInsecure=1&sni=sni=hg.jiashumao.net#%F0%9F%87%AD%F0%9F%87%B0%20_HK_%E9%A6%99%E6%B8%AF
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDUiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=glc.hruqoaw.cn#%F0%9F%87%A6%F0%9F%87%BA%7CTG%E9%A2%91%E9%81%93%40baipiaoeverything%7C1
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=kr1.api-aws.com#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%20003
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5r6z5aSn5Yip5LqaXzEwMTIwMDYiLAogICJhZGQiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmF1MS4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=dauwxncawx.vzwzasc.cn#mianfeifq%20%7C%F0%9F%87%A8%F0%9F%87%B3%2BHK%2B17
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@140.238.205.173:443?allowInsecure=1&sni=jgwdb3.gaox.ml#AU_140.238.205.173_101183e6-141
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODU5IiwKICAiYWRkIjogIjE1Mi42OS4xOTcuNjAiLAogICJwb3J0IjogMTA2OSwKICAiaWQiOiAiYWM4ZTI2ZmUtODE1MC00YjYwLWFlNjQtODJmYzc3ZWJhMmNmIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBhdGgiOiAiLyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=hk1.kp1a-ls9a-426a-x45g.paolu.pics#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B9%2BTG%3A%40nodpai%2B%28Beta%29
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=112.fastea.top#mianfeifq%2B256
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=flowery.meijireform.com#mianfeifq%2B189
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTI0NzUiLAogICJhZGQiOiAiMTM4LjIuNDQuMjExIiwKICAicG9ydCI6IDIwMDgxLAogICJpZCI6ICI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLAogICJhaWQiOiA2NCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=linus.sbs#%F0%9F%87%AD%F0%9F%87%B0%2BHK%2B10
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIwODIiLAogICJhZGQiOiAiMTM4LjIuNDQuMjExIiwKICAicG9ydCI6IDIwMDgxLAogICJpZCI6ICI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLAogICJhaWQiOiA2NCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTI0ODEiLAogICJhZGQiOiAiMTM4LjIuNDQuMjExIiwKICAicG9ydCI6IDIwMDgxLAogICJpZCI6ICI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLAogICJhaWQiOiA2NCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAid3d3LmZsaWVzd2ltaW5nLnRrIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6Iux5Zu9XzEwMTIwMjMiLAogICJhZGQiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidnVrMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIyMDEwIiwKICAiYWRkIjogIjE3Mi42NC4xNTQuMTU1IiwKICAicG9ydCI6IDQ0MywKICAiaWQiOiAiYmY0NjE5ZTQtMDFkYy00OGNhLWJlMDgtMDk3NmI1NDk2OGNlIiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICJsZzUuemh1amljbjIuY29tIiwKICAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=jgwdb3.gaox.ml#GH
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTIyMzUiLAogICJhZGQiOiAiNjQuMTEyLjQyLjcyIiwKICAicG9ydCI6IDE2OTk5LAogICJpZCI6ICJiNWEwMWY0NC1iOTgxLTQyMWEtYmRjMC02ZDlkNTNkYTA3ZmQiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICI2NC4xMTIuNDIuNzIiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=eksrda.meijireform.com#mianfeifq%2B248
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI2ODAiLAogICJhZGQiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=112.fastea.top#%F0%9F%87%A6%F0%9F%87%BA%20AU%208
    trojan://7rfcbuZdkU@realhk-1.tiktokcdn.sbs:12425?allowInsecure=1&sni=1009jp.tfzhc.top#mianfeifq%2B248
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=gbo02.vsvideo.shop#mianfeifq%2B256
    trojan://7rfcbuZdkU@103.177.248.160:12425?allowInsecure=1&sni=linus.sbs#mianfeifq%2B253
    trojan://cb43b7c2-b744-41c5-bcc2-fd7467b332cf@jgwxn3.gaox.ml:443?allowInsecure=1&sni=d76bb35696.wns.windows.com#%F0%9F%87%A6%F0%9F%87%BA%20AU%201%20%E2%86%92%20openitsub.com
    trojan://666888@118.140.206.169:443?allowInsecure=1&sni=wel-jp.qchwnd.moe#GH
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMTIiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi576O5Zu9XzEwMTI2NjgiLAogICJhZGQiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAibHUxLmdvZ29nb28uY3lvdSIsCiAgInBhdGgiOiAiL2dvIiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIyMDgiLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInd3dy4xNzA4MDEwMC54eXoiLAogICJwYXRoIjogIi9wYXRoLzE3MzQxODE0MTEyMyIsCiAgInRscyI6IGZhbHNlLAogICJzbmkiOiAiIgp9
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@jgwdb4.gaox.ml:443?allowInsecure=1&sni=hk.vc2.hyperlinkvpn.xyz#%7C21.67Mb
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAwMzQiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIwODAiLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIyNzAiLAogICJhZGQiOiAiMTM4LjIuNDQuMjExIiwKICAicG9ydCI6IDIwMDgxLAogICJpZCI6ICI1OTNiODUyNS0wYzQ4LTRiMGYtZDlhZi0yZDczYTkxNDg5NzMiLAogICJhaWQiOiA2NCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAidGNwIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAiMTM4LjIuNDQuMjExIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIyNjgiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+Hq/Cfh7dfVEfpopHpgZNAYmFpcGlhb2V2ZXJ5dGhpbmdfMjAiLAogICJhZGQiOiAiNTEuNjguMTI2LjE5MyIsCiAgInBvcnQiOiA4MCwKICAiaWQiOiAiZDRhNzk1MDUtZGQ3Zi00N2U0LTk4YjctMzBjOWZhNzdmYTY2IiwKICAiYWlkIjogMCwKICAic2N5IjogImF1dG8iLAogICJuZXQiOiAid3MiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICI1MS42OC4xMjYuMTkzIiwKICAicGF0aCI6ICIvdm1lc3MiLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTAxNDciLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HuvCfh7ggVVMgODM3IiwKICAiYWRkIjogInZkZTEuMGJhZC5jb20iLAogICJwb3J0IjogNDQzLAogICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogInZkZTEuMGJhZC5jb20iLAogICJwYXRoIjogIi9jaGF0IiwKICAidGxzIjogdHJ1ZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNDUiLAogICJhZGQiOiAiMTQwLjgzLjU3LjgwIiwKICAicG9ydCI6IDQ5ODQwLAogICJpZCI6ICIyOTY5YWQxYi05Nzg3LTQ5MjctOTRlNi0yMmY1OTc2MThkZTAiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNDAuODMuNTcuODAiLAogICJwYXRoIjogIi8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIyNjkiLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLAogICJhZGQiOiAiMTUyLjY5LjE5Ny42MCIsCiAgInBvcnQiOiAxMDY5LAogICJpZCI6ICJhYzhlMjZmZS04MTUwLTRiNjAtYWU2NC04MmZjNzdlYmEyY2YiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ0Y3AiLAogICJ0eXBlIjogbnVsbCwKICAiaG9zdCI6ICIxNTIuNjkuMTk3LjYwIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTIxNzkiLAogICJhZGQiOiAiMTUyLjY5LjIwNC4xOTMiLAogICJwb3J0IjogMzMyMjYsCiAgImlkIjogImNmZWU2YTY0LTY2YzQtNGEyMC1iMTkzLTMzMjZhZDdiNGNjNSIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogInRjcCIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE1Mi42OS4yMDQuMTkzIiwKICAicGF0aCI6ICIvIiwKICAidGxzIjogZmFsc2UsCiAgInNuaSI6ICIiCn0=
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi5pel5pysXzEwMTI0ODQiLAogICJhZGQiOiAiMTk0LjE1Ni4yMzEuMjMiLAogICJwb3J0IjogOTk5LAogICJpZCI6ICI5MDg4NjEyYS02NjgxLTQyNTMtYzViNy02MDI4Yzk5ZDMwNTEiLAogICJhaWQiOiAwLAogICJzY3kiOiAiYXV0byIsCiAgIm5ldCI6ICJ3cyIsCiAgInR5cGUiOiBudWxsLAogICJob3N0IjogIjE5NC4xNTYuMjMxLjIzIiwKICAicGF0aCI6ICIvbm9yaW8iLAogICJ0bHMiOiBmYWxzZSwKICAic25pIjogIiIKfQ==
    vmess://ewogICJ2IjogMiwKICAicHMiOiAi8J+HqfCfh6pfREVf5b635Zu9XzBAMTEiLAogICJhZGQiOiAidmRlMi4wYmFkLmNvbSIsCiAgInBvcnQiOiA0NDMsCiAgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsCiAgImFpZCI6IDAsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6IG51bGwsCiAgImhvc3QiOiAidmRlMi4wYmFkLmNvbSIsCiAgInBhdGgiOiAiL2NoYXQiLAogICJ0bHMiOiB0cnVlLAogICJzbmkiOiAiIgp9

</details>

### 所有节点
合并节点总数: `5161`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `120`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `130`
- [freefq/free](https://github.com/freefq/free), 节点数量: `39`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `90`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `200`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `19`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `28`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3166`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `1`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `22`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `4`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `3`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `93`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `203`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `31`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `39`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `13`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `48`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `176`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `180`
- [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls), 节点数量: `284`
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
