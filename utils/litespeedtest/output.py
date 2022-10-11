import json, base64, os, time, argparse

def output(output_file='./Eternity',output_range=99):
    output_list = []
    with open('./config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        output_range = config['output_range']
        if ',' in output_range:
            output_range = {'begin': int(output_range.split(',',1)[0]),'end': int(output_range.split(',',1)[1])}
        else:
            output_range = {'begin': 0, 'end': int(output_range)}
    while os.path.isfile('./out.json')==False:
        print('Awaiting speedtest complete...')
        time.sleep(30)
    with open('./out.json', 'r', encoding='utf-8') as f:
        proxies_all = json.load(f)
    os.remove('./out.json')
    for index in range(output_range['begin'],output_range['end']):
        try:
            proxy = proxies_all[index]['Link']
            output_list.append(proxy)
        except Exception:
            pass
    content = base64.b64encode('\n'.join(output_list).encode('utf-8')).decode('ascii')
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write(content)
        print('Write content to subcription file.')
    return proxies_all

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test nodes, and output base64 subscription file.')
    parser.add_argument('--target', '-t', help='Target file path to output', default='./output.txt')
    parser.add_argument('--range', '-r', help='Target proxies range to output', default=99)
    
    args = parser.parse_args()

    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if os.name == 'posix':
        os.system('./lite --config ./config.json --test \"https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml\"')
    elif os.name == 'nt':
        os.system('lite.exe --config ./config.json --test \"https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml\"')
    output(args.target,args.range)

    os.chdir(work_dir)