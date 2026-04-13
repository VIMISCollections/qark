### Anne's Notes ###
Install python3-venv package (may need sudo):
apt install python3.12-venv

Create virtual environment:
python3 -m venv venv

Activate virtual environment (ubuntu). To do this, call command with relative path to venv folder:
source ../venv/bin/activate
(My venv folder is placed in Desktop folder, which is outside this one)

Install qark:
pip install qark

Also, make sure Java is installed! Might cause trouble with dex2jar otherwise.

My APKs are stored in the myApks-folder.
Run the tool for an APK:
qark --apk myApks/name_of_apk_file.apk

After running the tool, the results are stored in:
..\venv\lib\python3.12\site-packages\qark\report\report.html

## How the tool works - UNFINISHED NOTES ##
In qark/qark.py, they use 'click', a package for creating command line interfaces. The @click.option() lets you set a flag, that saves the passed value. 
So @click.option("--apk", "source",...) saves the passed value after '--apk' in a variable called 'source'.
I believe it then calls the cli() method with those option variables:
- Runs decompiler (qark.decompiler.decompiler - Decompiler)
- Runs scans (qark.scanner.scanner)
- Writes report (qark.report)

**Decompiler**
"This class handles unpacking and decompiling APKs into Java source code."
In qark.py, it inits the Compiler -> In init(), it calls:
        self.dex_path = self._unpack_apk()
        -> "Unpacks an APK and extracts its contents". Using an unzip.

        self.jar_path = self._run_dex2jar()
        -> "Runs dex2jar in the lib on the dex file". Uses the dex_path set by the _unpack_apk(). 

        self.manifest_path = self.run_apktool()
        -> "Runs `APK_TOOL_COMMAND` with the users path to APK to decompile the APK". 
            Attempts to make apktool in lib/apktool/{operating_system}/ executable. (configure apk_tool)
            


Then qark calls .run() on the decompiler -> run():
Uses DECOMPILERS imported from qark.decompiler.external_decompiler (compilers: cfr, procyon, fernflower).
Runs each decompiler (in threads) using _decompiler_function(), waits for them to finish.

Then calls unpack_fernflower_jar():
"Fernflower puts its decompiled code back into a jar so we need to unpack it."
Uses the 'jar xf ...' command I tried in BabelView. 

**Scanner**

**Reporter**