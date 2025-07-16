echo "Trigger deployment for image: 0be5d968f9cd0180e66051c75fde96056e23d208" >> README.md
git add README.md
GIT_COMMITTER_DATE="`date`" git commit --allow-empty -m "Deploy scanned image 0be5d968"