read -p "Are you sure you want to reset your rating? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
echo "800" > ./rating/A.txt
echo "800" > ./rating/C.txt
echo "800" > ./rating/G.txt
echo "800" > ./rating/N.txt
echo "Rating reset."
