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

Run the tool with a Java-folder or file:
qark --java path/to/parent/java/folder
qark --java path/to/specific/java/file.java

Running with java-folder instead of APK, for 2nd entry in Dimitris' list
(placed on desktop):
qark --java ../../Android-IMSI-Catcher-Detector-0.1.36-alpha-b00

This ran MUCH faster, only taking 15~ seconds, compared to the usual 13~ minutes.
It also did not throw the javalang error, that it throws when decompiling the apk.
One of the contributers also stated here (https://github.com/linkedin/qark/issues/321) that "Overall, we are not too concerned with the performance of decompiling APKs. It is there for convenience". 

After running the tool, the results are stored in:
..\venv\lib\python3.12\site-packages\qark\report\report.html

## APKs for Qark ##
**Based on Dimitris' messages on Discord, these APKs are relevant for Qark (WIP!!)**
Entries in list:
2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 23, 26, 124, 125, 126, 130, 131

For now, I'll focus on the ones that have 'webview' in tags/title:
6, 13, 17?, 20, 23, 26, 130, 131

**Android-IMSI-Catcher-Detector.apk**
2. Vulnerabilities detected by AndroBugs Framework,https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector/issues/650,CellularPrivacy/Android-IMSI-Catcher-Detector,Unsafe addJavascriptInterface Usage,"bug, security_issue" 
(release v0.1.36-alpha-b00 has the bug)

Gives error:
javalang.tokenizer.LexerError: Unterminated character/string literal at "'", line 13: public /* varargs */ akr(int n2, boolean bl2, String[] arrstring, org.benf.cfr.reader.util.ConfusedCFRException: VARARGS method doesn't have an array as last arg!!

Issue raised on Qark github (2019), but never resolved:
https://github.com/linkedin/qark/issues/317

**SkyTube-Oss-2.978.apk**
4. "Find some crashes, and hope they can help you to debug",https://github.com/SkyTubeTeam/SkyTube/issues/956,SkyTubeTeam/SkyTube,Debug Settings Left Enabled in Production | Lifecycle-Related WebView Crash,"bug, incomplete",
(release Version 2.978. Issue from april 9 2021. Release from March 22 2021)

Tried to run Qark, but didnt manage to finish within an hour-ish, so aborted.

**Metrolist.apk**
5. v13.0.0 PLAYBACK/CRASH ISSUES MEGATHREAD,https://github.com/MetrolistGroup/Metrolist/issues/2556,MetrolistGroup/Metrolist,Debug Settings Left Enabled in Production | Lifecycle-Related WebView Crash,"bug, help wanted, SEVERE ISSUE"
(release version 12.12.4. There's a lot of different assets for this release, so I'm just assuming I've picked the right .apk, but not sure.
GOT ERROR: javalang.tokenizer.LexerError: Unterminated character/string literal at "'", line 13: public /* varargs */ akr(int n2, boolean bl2, String[] arrstring, org.benf.cfr.reader.util.ConfusedCFRException: VARARGS method doesn't have an array as last arg!!)

**app-full-release.apk**
6. Android Mobile App Intermittently Slow,https://github.com/home-assistant/android/issues/3396,home-assistant/android,File Access Enabled in WebView,"bug, webview"
(version beta-3232-aaef2549. issue from march 4 2023. TONS of releases, even on the same day. Im just picking the last release from march 3rd 2023. 
**Qark got 'maximum recursion depth exceeded' after running for 2+ hours!!!)

**home-assistant-full-beta-2884.apk**
7. Open iframe content external link correctly on android,https://github.com/home-assistant/android/issues/3044,home-assistant/android,Bridge Callable from Untrusted Content,"bug, webview"
(SAME APP AS 6!! Version beta-2884-8a50f0d0. Latest release from nov 3 2022. issue nov 6 2022)

**openhab-android.apk**
10. Confusing new layout,https://github.com/openhab/openhab-android/issues/3159,openhab/openhab-android,Unsafe WebView Configuration Defaults,bug
(Version 3.0.1. Issue jan 26 2023.
Qark error: javalang.tokenizer.LexerError: Unterminated character/string literal at "'", line 13: public /* varargs */ akr(int n2, boolean bl2, String[] arrstring, org.benf.cfr.reader.util.ConfusedCFRException: VARARGS method doesn't have an array as last arg!!)

**OuterTune-0.6.3-universal-release.apk**
11. Unexpected error 2000 playing songs when logged in,https://github.com/OuterTune/OuterTune/issues/140,OuterTune/OuterTune,Debug Settings Left Enabled in Production,bug
(release 0.6.3. Issue dec 17 2024)

**OuterTune-0.7.7-universal-release.apk**
12. Source Error 2000; Music Failing to Play & Unable to Download Music,https://github.com/OuterTune/OuterTune/issues/464,OuterTune/OuterTune,Debug Settings Left Enabled in Production,bug
(Same app as 11. Release 0.7.7)

**app-full-release-2023103.apk**
13. Device screen timeout has no affect when dashboard is streaming live camera,https://github.com/home-assistant/android/issues/3953,home-assistant/android,Insecure Mixed Content Handling,"bug, webview"
(Version 2023.10.3. Issue oct 19 2023. Release from oct 15 2023)

**X**
14. HomeAssistant access denied after short time.,https://github.com/home-assistant/android/issues/1712,home-assistant/android,Unsafe WebView Configuration Defaults,bug

**X**
15. Can't connect Wear OS,https://github.com/home-assistant/android/issues/3441,home-assistant/android,Unsafe WebView Configuration Defaults,bug

**X**
16. Logging in to social.tchncs.de logs in in the browser frame,https://github.com/pachli/pachli-android/issues/210,pachli/pachli-android,Unsafe WebView Configuration Defaults,bug

**android-youtube-player-12.1.2 folder**
17. ConnectivityManager$TooManyRequestsException when using compose,https://github.com/PierfrancescoSoffritti/android-youtube-player/issues/1239,PierfrancescoSoffritti/android-youtube-player,JavaScript Enabled Unnecessarily,bug
(Issue august 12 2025. Release 12.1.2. This doesn't seem to be an actual application, but rather a library one can add to their app, to play youtube videos. Not sure what to do with this. No APK file.)

**X**
18. No Video Will play (any video),https://github.com/TeamNewPipe/NewPipe/issues/7734,TeamNewPipe/NewPipe,Debug Settings Left Enabled in Production,"bug, ASAP, youtube"

**jellyfin-android-v2.3.0-proprietary-release.apk**
20. Unable to access server running Jellyfin 10.8.0,https://github.com/jellyfin/jellyfin-android/issues/480,jellyfin/jellyfin-android,Attacker-Controlled URL Loaded in WebView,"bug, upstream"
(Issue 4 august 2021. Release 2.3.0, but different kinds of assets. Going with 'proprietary' for now.)

**X**
23. Authentication fails when opened in external browser,https://github.com/home-assistant/android/issues/6375,home-assistant/android,Attacker-Controlled URL Loaded in WebView,bug
(Users complain about a 'bug', some functionality not working anymore, but developer responded that it was never supposed to work. So not an actual bug?)

**X**
26. Connection refused when using WireGuard,https://github.com/duckduckgo/Android/issues/887,duckduckgo/Android,Attacker-Controlled URL Loaded in WebView,"bug, needs triage"
(Issue marked as completed. Seemed the cause was user's own device. So not actually relevant?)

**X**
124. Android 15: ContentResolver.query returns null from hooked app to external ContentProvider,https://github.com/JingMatrix/Vector/issues/253,JingMatrix/Vector,Debug Settings Left Enabled in Production,bug

**X**
125. Some images not loading in incognito mode,https://github.com/Slion/Fulguris/issues/368,Slion/Fulguris,Insecure Mixed Content Handling,"bug, user"

**X**
126. Qi Scans Bug,https://github.com/keiyoushi/extensions-source/issues/12123,keiyoushi/extensions-source,Insecure Mixed Content Handling,Bug

**pairdrop-android-1.12.0 folder**
130. [Pairdrop] use pairdrop native file share preview ,https://github.com/fm-sys/pairdrop-android/issues/274,fm-sys/pairdrop-android,Attacker-Controlled URL Loaded in WebView,"bug, PairDrop speciffic"
(I don't see anything in the issue about loading attacker-controlled URL! Is this relevant?? Issue march 15 2023. Release UI release - 14.02.2023. From february 14 2023. Need to build APK!!)

**X**
131. Mangacrab not loading pages,https://github.com/keiyoushi/extensions-source/issues/9978,keiyoushi/extensions-source,Attacker-Controlled URL Loaded in WebView,Bug
(Issue august 4 2025. This doesn't have releases, and I have no idea how to figure out which files/commit is relevant. XXX)


## APKs for wDroid (MOVE LATER) ##
4, 5, 9, 32, 41, 44, 49, 52, 54, 58, 60, 63, 64, 65, 66, 67, 68, 69, 72, 75, 78, 79, 80, 81, 82, 83, 84, 85, 91, 97, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 129, 138, 142, 143, 144, 149

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