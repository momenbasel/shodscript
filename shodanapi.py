import shodan
import sys
import subprocess

shodan_api_key="API" #enter apikey here
api = shodan.Shodan(shodan_api_key)

if len(sys.argv) <2 :
    print('usage : python3 shodanapi.py <querysearch> <scriptlocation>')
    print('eg: python3 shodan.py "apache" "~/Desktop/cve2003-112-249.py')
    sys.exit(0)

try:
    query= sys.argv[1]
    script = sys.argv[2]
    results=api.search(query)

    for result in results['matches']:
        print(result['ip_str'])
        process = subprocess.Popen(['python3',script],stdout=subprocess.PIPE,universal_newlines=True)
        output = process.stdout.readline()
        print(output.strip())
        return_code = process.poll()
        for output in process.stdout.readlines():
            print(output.strip())
            break

except shodan.APIError as e:
    print(e)
