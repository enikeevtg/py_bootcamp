import yaml


# with open("deploy.yml", "r") as fp:
with open("../../materials/todo.yml", "r") as fp:
    download_data = yaml.load(fp, Loader=yaml.FullLoader)

# task: Install packages
task_install = [
  {
    "name": "Packages installing",
    "apt": {"name": download_data["server"]["install_packages"]}
  }
]

# task: Copy over files
src_files = [
              "../ex00/" + download_data["server"]["exploit_files"][0],
              "../ex00/script.html",
              "../ex01/" + download_data["server"]["exploit_files"][1],
              "../ex01/common.py"
            ]
task_copy = []
for filepath in src_files:
    task = {
            "name": "Copy " + filepath,
            "copy": {
                      "src": filepath,
                      "dest": "."
                    }
           }
    task_copy.append(task)

# task: Run files on a remote server with a Python interpreter,
# specifying corresponding arguments
interpreter = "python3 "
scripts = download_data["server"]["exploit_files"]
consumer_args = " -e " + ",".join(download_data["bad_guys"])
task_run = [{
              "name": "Run " + scripts[0],
              "command": interpreter + scripts[0]
            },
            {
              "name": "Run " + scripts[1],
              "command": interpreter + scripts[1] + consumer_args
            }]

playbook = [{
              "name": "exercise 02 - deploy",
              "hosts": "localhost",
              "tasks": task_install + task_copy + task_run
            }]
upload_data = yaml.dump(playbook, explicit_start=True, explicit_end=True,
                        sort_keys=False)
with open("deploy.yml", "w") as fp:
    fp.write(upload_data)
