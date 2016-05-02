find bootstrap/ -mindepth 1 -maxdepth 1 -not -name "dist" -not -name ".*" > ignore
find bootstrap/dist -mindepth 1 -type f -not -name "*.min.*" >> ignore
find bootstrap/dist -mindepth 1 -type f -name "*.map" >> ignore
sed 's/.*/    - "\/&"/' -i ignore
cat ignore

