if [ -z "$1" ]; then
	echo "Input 00..10"
	exit
fi
if [ ! -d "./python$1" ]; then
	echo "dir no exists"
	exit
fi

rm -rf /tmp/tmppush

cp -r "./python$1"/ /tmp/tmppush
cd /tmp/tmppush || exit
git init
git branch -m master main
rm -rf tester .vogsphere_cleanup.sh en.subject.pdf

REPO=""
read -rp "Iput Repo:" REPO 
if [ -z "$REPO" ]; then
	echo "No repo was given"
	rm -rf /tmp/tmppush
	exit
fi


git remote add origin "$REPO"
git add .
git commit -m "auto delete"
git push -f origin main
git ls-files

rm -rf /tmp/tmppush
