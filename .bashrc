python ~/main.pyclear

# صوت ترحيب
termux-tts-speak "Welcome... Al Hack Asad Al Amri"

# تأثير ماتريكس
cmatrix -b -C green -n & sleep 1; killall cmatrix

clear

# الاسم
figlet "ASAD" | lolcat
figlet "AL-AMRI" | lolcat

echo ""
toilet -f mono12 -F border "الهاك اسد العامري" | lolcat
echo ""

# معلومات النظام
neofetch

echo ""
echo "🔥 ACCESS GRANTED"
echo "💀 WELCOME HACKER"
echo "=========================="nano ~/.bashrc
clear
echo "==============================="
echo "     مرحبًا بك في Termux"
echo "==============================="
figlet "Asad Al-Amri"
echo ""
toilet -f mono12 -F border "الهاك اسد العامري"
echo ""
echo "🔥 System Ready..."sleep 0.8 && termux-tts-speak -l ar -r 0.9 -p 0.8 "النظام... مُتصل... أهلاً بعودتك أيها الهكر... أسد" && termux-toast "مرحباً بعودتك يا أسد"
clear && echo -e "\033[1;95m" && figlet -f smslant "ASSAD" | sed "1,3s/^/\x1b[1;95m/; 4,\$s/^/\x1b[1;91m/" && echo -e "\033[0m\033[1;90m───────────────────────────────────\033[0m" && echo -e "\033[1;95m  🥷 \033[1;97mSILENT BREACH INITIATED\033[1;91m 🥷\033[0m" && echo -e "\033[1;90m  >> \033[1;95mAGENT: \033[1;91mASSAD\033[1;90m <<\033[0m" && echo -e "\033[1;90m  >> \033[1;95mMODE: \033[1;97mSTEALTH\033[1;90m <<\033[0m" && echo -e "\033[1;90m───────────────────────────────────\033[0m" && echo
PS1='\[\033[1;95m\]ASSAD \[\033[1;91m\]@\[\033[1;95m\]TERMUX \[\033[1;94m\]\w \[\033[1;91m\]❯\[\033[1;95m\]❯\[\033[1;91m\]❯\[\033[0m\] '
