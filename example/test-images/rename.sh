a=1
for i in *; do
  if [ "$i" != "rename.sh" ]; then
    new=$(printf "%03d.jpg" "$a") #03 pad to length of 3
    mv -i -- "$i" "$new"
    let a=a+1
  fi
done
