rm -rf ./problems
python3 gen_imos.py > imos.txt
python3 gen_problems.py < imos.txt