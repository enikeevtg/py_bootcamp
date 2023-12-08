## Playbook structure:
```yaml
- name: MC
  hosts: all
  become: yes

  tasks:
  - name: install mc webserver
    apt: name=mc state=latest
  - name: test ping servers
    ping:
```

## In Python notation
```python
[
  {
    'name': 'MC',
    'hosts': 'all',
    'become': True,
    'tasks':
            [
              {
                'name': 'install mc webserver',
                'apt': 'name=mc state=latest'
              },
              {
                'name': 'test ping servers',
                'ping': None
              }
            ]
  }
]
```
