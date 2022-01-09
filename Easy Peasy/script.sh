encrypted_flag="645b565a7a66704c4a575f53694257504054464c3c"

S=""
K=""

MODULAR_LEN=50000
FLAG_LEN=$(( ${#encrypted_flag} / 2 )) # encrypted flag length 
FINAL_LEN=$(( $MODULAR_LEN - $FLAG_LEN ))

for i in $(seq 1 $FINAL_LEN)
do
	S+="a"
done
echo $i

for i in $(seq 1 $MODULAR_LEN)
do
		K+="$((1 + $RANDOM % 9))"
done

echo $S > filler_input.txt
echo $K > key
#echo $S | nc mercury.picoctf.net 41934 > output.txt

