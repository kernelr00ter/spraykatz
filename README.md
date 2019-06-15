# [```SPRAYKATZ```](https://github.com/aas-n/spraykatz/blob/master/README.md)
A tool to spray love around the world by [@lydericlefebvre](https://twitter.com/lydericlefebvre).

### Index

| Title        | Description   |
| ------------- |:-------------|
| [About](#about)  | Brief Description about the tool. |
| [Installation](#installation)  | Installation and Requirements. |
| [Usage](#using-spraykatz)  | How to use Spraykatz. |
| [Todo](#todo)  | Things planned to improve this tool. |
| [Acknowlegments](#acknowlegments)  | Acknowlegments. |

### About  
Spraykatz is a tool without any pretention able to **retrieve credentials** on large Active Directory networks.

It tries to __filelessly procdump__ machines and __parse dumps locally__ in order to **avoid detections** by antivirus softwares as much as possible.

### Installation
This tool is written for **`>= python3.6`**. You have to use python3.6 and pip3.6.
#### Ubuntu
On a fresh updated Ubuntu.
```bash
apt update
apt install -y python3.6 python3-pip git nmap
git clone --recurse-submodules https://github.com/aas-n/spraykatz.git
cd spraykatz
pip3 install -r requirements.txt
```

### Using Spraykatz
A quick start could be:
```bash
./spraykatz.py -d company.local -u H4x0r -p L0c4L4dm1n -t 192.168.1.0/24
```

#### Mandatory arguments
| Switches | Description |
| -------|:--------|
| -d, --domain | User's domain. If he is **not** member of a domain, simply use `-d .` instead. |
| -u, --username | User to spray with. He must have admin rights on targeted systems in order to gain remote code execution. |
| -p, --password | User's password or NTLM hash in the `LM:NT` format. |
| -t, --targets | IP addresses and/or IP address ranges. You can submit them via a file of targets (one target per line), or inline (separated by commas). |

#### Optional arguments
| Switches | Description |
| -------|:--------|
| -m, --methods | Execution method to use. If omitted, wmiexec is tried first, then atexec, and  then smbexec. |
| -s, --share | SMB Share to use for command execution. By default: `C$`. |
| -w, --wait | Timeout for each procdump thread to finish. Default: 10 seconds. |
| -q, --quiet | Quiet mode. Default is verbose. |

### TODO
v1.0.0
- [x] Targets file as input
- [x] Use Impacket as git submodules
- [x] Threading
- [x] Logging
- [x] Refactoring code
- [x] Require domain argument
- [x] Refactoring Utils
- [x] Imports review
- [x] suicide thread inside exec if too long
- [x] Use nmap python
- [ ] README (Logo, Gif, Release Version)
- [ ] License

v1.1.0
- [ ] Bypass AVs (lsass dump)

v1.2.0
- [ ] isDomAdmin feature

v1.3.0
- [ ] SQLite Support

### Acknowlegments  
Spraykatz uses slighlty modified parts of the following projects:
* [Impacket](https://github.com/SecureAuthCorp/impacket)
* [Pypykatz](https://github.com/skelsec/pypykatz)
* [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec)
* [Pywerview](https://github.com/the-useless-one/pywerview)
* [Sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/)

# 
*Created by [Lydéric Lefebvre](https://www.linkedin.com/in/lydericlefebvre/)*
