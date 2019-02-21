time=$(date "+%Y-%m-%d %H:%M:%S")
git add .
git commit -m "Auto Push at ${time}"
git push

echo "Done"