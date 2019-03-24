
plant() { java -jar plantuml.jar -duration -o "./output" "$1" ; }

for i in *.txt ; do
    echo "Processing $i..."
    plant "$i"
done
