#pip install paramiko --user
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='35.86.136.74',
            username='ubuntu',
            key_filename="C:\Users\teddy\Downloads\CNE335-Teddy-kp-ppk.ppk")

update command = sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean
stdin, stdout, stdout = ssh.exec_command('lbs_release -a')  #stdin, stdout, and stderr are used for
#how you want to get the commands.
for line in stdout.read(),splitlines():
    print(line)

#This might be a better option for the above block...
stdout = "lbs_realease"
line = stdout.readline()
while line:
    line = stdout.readline()  #or can use line = stdout.read().decode()

ssh.close()