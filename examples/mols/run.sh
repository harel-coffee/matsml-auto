for i in 0 1 2 3 4 5 6 7 8 9 ; do
	python mols.py | tee log-$i
done
