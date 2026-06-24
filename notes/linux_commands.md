# Important Linux Commands

## Navigation Commands

### pwd
**Purpose:** Show current working directory
```bash
pwd
```

### cd
**Purpose:** Change directory
```bash
cd Documents
```

### cd ..
**Purpose:** go back one folder
```bash
cd ..
```

### cd ~
**Purpose:** go home
```bash
cd ~
```

## Listing Commands

### ls
**Purpose:** list files and folders in the current directory
```bash
ls
```

### ls -l 
**Purpose:** detailed view
```bash
ls -l
```

### ls -a
**Purpose:** show hidden files
```bash
la -a
```

### ls -la
**Purpose:** show hidden files with detail
```bash
ls -la
```

## File and Folder Commands

### mkdir
**Purpose:** create folder
```bash
mkdir folder_name
```

### touch
**Purpose:** create file
```bash
touch file1.txt
```

### rm
**Purpose:** remove/delete file
```bash
rm file1.txt
```

### rmdir
**Purpose:** remove empty folder
```bash
rmdir folder1
```

### rm -r
**Purpose:** remove folder and contents
```bash
rm -r folder1 
```

## Copy and Move Commands

### cp
**Purpose:** copy file
```bash
cp file1.txt
```

### cp -r
**Purpose:** copy folder
```bash
cp -r folder1
```

### mv
**Purpose:** rename file
```bash
mv old.txt new.txt
```

### mv
**Purpose:** moving file to a specific folder
```bash
mv file.txt folder1/
```

## File Viewing Commands

### cat
**Purpose:** print file (to view file content)
```bash
cat file.txt
```

### less
**Purpose:** read large files (q  --to quit)
```bash
less file.txt
```

### nano
**Purpose:** nano editor (edit files)
```bash
nano notes.txt	
```

## Search Commands

### find
**Purpose:** find files
```bash
find . -name "*.py"
```

### which
**Purpose:** find program location
```bash
which git
```

### grep
**Purpose:** Search for a word or pattern in a file. 
```bash
grep "hello" file.txt
```

### grep -i
**Purpose:** this ignores uppercase/lowercase
```bash
grep -i"ros2" notes.txt
```

### grep -r
**Purpose:** Search recursively in a folder
```bash
grep -r "piblisher" .
```

## Package Management Commands

### sudo apt update
**Purpose:** update package list
```bash
sudo apt update
```

### sudo apt upgrade
**Purpose:** upgrade packages after updating with sudo apt update
```bash
sudo apt upgrade
```

### sudo apt install software_name
**Purpose:** install software (git - name of software)
```bash
sudo apt install git
```

### sudo apt remove package_name
**Purpose:** remove software
```bash
sudo apt remove package_name
```

## Process Management

### ps aux
**Purpose:** see running processes
```bash
ps aux
```

### top
**Purpose:** system monitor (q  --to quit)
```bash
top
```

### kill PID
**Purpose:** kill process
```bash
kill 1234
```
