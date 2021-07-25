mkdir -p dist
pyinstaller.exe -F -w main.py
cd dist || exit
mv "main.exe" "bleu.exe" || exit
cd ..
rm -rf ../../"bleu" || echo "不存在这个文件夹"
cp -rf "dist" ../../"bleu"