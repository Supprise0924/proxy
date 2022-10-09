import json, base64, os, time, argparse

def output(output_file='./Eternity',num=99):
    output_list = []

    while os.path.isfile('./out.json')==False:
        print('Awaiting speedtest complete...')
        time.sleep(30)

    with open('./out.json', 'r', encoding='utf-8') as f:
        proxies_all = json.load(f)
    os.remove('./out.json')
    for index in range(num):
        proxy = proxies_all[index]['Link']
        output_list.append(proxy)
    content = base64.b64encode('\n'.join(output_list).encode('utf-8')).decode('ascii')
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write(content)
        print('Write content to subcription file.')
    return proxies_all

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test nodes, and output base64 subscription file.')
    parser.add_argument('--target', '-t', help='Target file path to output', default='./output.txt')
    parser.add_argument('--num', '-n', help='Target proxies amount to output', default=99)
    
    args = parser.parse_args()

    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if os.name == 'posix':
        os.system('./lite --config ./config.json --test \"https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml\"')
    elif os.name == 'nt':
        os.system('lite.exe --config ./config.json --test \"https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml\"')
    output(args.target,int(args.num))

    os.chdir(work_dir)