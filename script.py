import subprocess, os, time, sys, shutil

FTP_DIRECTORY = "/home/ASO/Builds"
ABSOL_PATH = "/home/podar/ASO"

def pullAndBuild(creds):
	ABS_PATH = "/home/podar/ASO"
	REPO_PATH = "~/ASO"
	BUILD_PATH = "~/ASO/Builds"
	
	print("Git tracking build scripts")

	os.chdir(os.path.expanduser(os.path.join(REPO_PATH, creds[0])))
	# print(os.path.join(REPO_PATH, creds[0]))

	p = subprocess.check_output(["git", "pull", "origin", "master"])
	x = p.decode(sys.stdout.encoding)
	# print(x)

	if (x == 'Already up to date.\n'):
		print("The repository " + creds[0] + " is up to date");
	else:
		print("Build...")
		# o = subprocess.call("runuser " + "-l " + creds[0] + " -c" + " '" + creds[1] + "'", shell = True)
		# o = subprocess.call("sudo " + "-u " + creds[0] + " '" + creds[1] + "'", shell = True)
		o = subprocess.call("su " + "-l " + creds[0] + " -c " + "'make -f MakeFile'", shell = True)
		if (o == 0):
			d = subprocess.check_output("ls", shell = True)
			dec = d.decode(sys.stdout.encoding)
			lis = dec.split("\n")
			if(creds[2] in lis):
				print("The build was succesfull!\n")
				os.chdir(os.path.expanduser(BUILD_PATH))
				d = subprocess.check_output("ls", shell = True)
				dec = d.decode(sys.stdout.encoding)
				lis = dec.split("\n")
				if(creds[0] not in lis):
					 subprocess.call(["mkdir", creds[0]])
				os.chdir(os.path.expanduser(os.path.join(os.path.join(BUILD_PATH, creds[0]))))
				n = subprocess.check_output("ls | wc -l", shell =True)
				m = n.decode(sys.stdout.encoding)
				i = int(m)
				print(i)
				i = i + 1
				z = "mkdir" + " build_" + str(i)
				z1 = "build_" + str(i)
				u = subprocess.call(z, shell = True)
				y = subprocess.call(["mv", os.path.join(ABS_PATH, creds[0], creds[3]), os.path.join(ABS_PATH, "Builds", creds[0], z1)])
		else:
			print("Build failed")


def check(creds):
	while True:
		for p in creds:
			pullAndBuild(p)			
		time.sleep(10)

def createUsers(creds):
	for cred in creds:
		q = subprocess.call(["id", "-u", cred[0]])
		print(q)
		if (q == 1):
			subprocess.call(["sudo", "useradd", cred[0]])
			p = subprocess.call("sudo chown -R " + cred[0] + ":" + cred[0] + " " + ABSOL_PATH + "/" + cred[0] + "/", shell = True)
			o = subprocess.call("sudo chmod 704 " + ABSOL_PATH + "/" + cred[0] + "/", shell = True)

if (len(sys.argv) != 2):
	print("Scriptul trebuie sa contina doar un fisier de configurare ca parametru")
	sys.exit()
	
script_conf = sys.argv[1]
projects_builds = []

f = open(script_conf, "r")
projects_builds = f.read().splitlines()

print(projects_builds)

# every build's info from their configuration files
creds = []

for i in projects_builds:
	# info for build i
	g = open(i, "r")
	lines = g.read().splitlines()
	creds.append(lines)

print(creds)	

createUsers(creds)

check(creds)








