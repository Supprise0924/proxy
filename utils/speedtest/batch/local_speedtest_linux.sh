#准备好所需文件
test -e lite && echo "Listespeedtest is ready to run." || { echo "LiteSpeedTest is not exist, downloading from GitHub release."; wget -O lite.gz https://github.com/alanbobs999/LiteSpeedTest/releases/download/v0.11.2m/lite-linux-amd64-v0.11.2m.gz; gunzip lite.gz;}
#运行 LiteSpeedTest 开始测速
chmod +x ./lite
sudo nohup ./lite --config ../lite_config.json --test https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml >speedtest.log 2>&1 &
#导出筛选结果(仓库根目录的两个 Eternity 文件)
python ../output.py
python ../../main.py