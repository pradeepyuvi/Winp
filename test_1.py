from paramiko import SSHClient
from scp import SCPClient
import paramiko
from stat import S_ISDIR, S_ISREG
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('159.39.149.26',username='prathmesh.patil',password='Voyage@1918')