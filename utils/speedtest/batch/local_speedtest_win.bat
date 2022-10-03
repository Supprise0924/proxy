if exist ./lite.exe (
    echo "LiteSpeedTest is ready to run."
) else (
    echo "LiteSpeedTest is not exist, please download from https://github.com/alanbobs999/LiteSpeedTest/releases/download/v0.11.2m/lite-windows-amd64-v0.11.2m.zip. Move .exe file to root and rename it to lite.exe."
)

lite.exe --config ../lite_config.json --test https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity
python ../output.py
python ../../main.py