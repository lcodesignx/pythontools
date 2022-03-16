import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def conn_netbox():
    token = ''
    url = 'https://netboxdev.jhuapl.edu/api/virtualization/virtual-machines/'
    headers = {
        'Authorization' : 'Token ' + token,
        'Accept' : 'application/json'
    }
    return requests.get(url, headers=headers, verify=False).json()

def get_vms():
    names = []
    response = conn_netbox()
    results = response['results']

    for result in results:
        names.append(result['name'])

    return names

def get_clusters():
    clusters = []
    groups = { "_meta": { "hostvars": {} }, "all": { "children": [] } }
    results = conn_netbox()['results']
    
    for result in results:
        cluster = result['cluster']['name']
        if cluster not in clusters:
            clusters.append(cluster)

    for cluster in clusters:
        groups[cluster] = {}
        groups[cluster]['hosts'] = []

        for result in results:
            if result['cluster']['name'] == cluster:
                groups[cluster]['hosts'].append(result['name'])

    return groups

print(json.dumps(get_clusters(), indent=4))
