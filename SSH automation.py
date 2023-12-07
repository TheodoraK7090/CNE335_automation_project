import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='35.92.45.28',
            username='ubuntu',
            key_filename=r"C:\Users\teddy\Downloads\SSH-assignment-CNE335-teddy-kp-pem.pem")

update_command = 'sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean'


stdin, stdout, stderr = ssh.exec_command(update_command)
line = stdout.readline()
while line:
    print(line)
    line = stdout.readline()


ssh.close()