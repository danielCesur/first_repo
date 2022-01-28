 Para la ejecución de los test, con abrir una consola y situarla en la carpeta raiz del proyecto ya podremos ejecutar todos los tests y ver sus resultados.
 
Para el test de complejidad, escribiendo la siguiente sentencia obtendremos el resultado del test "flake8 --max-complexity 8 --statistics src/main/scripts/main.py"

Para los demas test unitarios y de calidad podremos ejecutar la siguiente sentencia para ver los tests realizados "coverage run -m pytest -v" y para ver el reporte con los porcentajes ejecutaremos la siguiente sentencia "coverage report -m"