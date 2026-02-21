git branch -D vogsphere
git checkout -b vogsphere

rm -rf tester .vogsphere_cleanup.sh en.subject.pdf

git add .
git commit -m "auto delete"
git push -f 42 vogsphere:main
git checkout main
